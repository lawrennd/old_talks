import numpy as np
import GPy

def initialize(self, noise_factor=0.01, linear_factor=1):
    """Helper function for deep model initialization."""
    self.obslayer.likelihood.variance = self.Y.var()*noise_factor
    for layer in self.layers:
        if type(layer.X) is GPy.core.parameterization.variational.NormalPosterior:
            if layer.kern.ARD:
                var = layer.X.mean.var(0)
            else:
                var = layer.X.mean.var()
        else:
            if layer.kern.ARD:
                var = layer.X.var(0)
            else:
                var = layer.X.var()

        # Average 0.5 upcrossings in four standard deviations. 
        layer.kern.lengthscale = linear_factor*np.sqrt(layer.kern.input_dim)*2*4*np.sqrt(var)/(2*np.pi)

def staged_optimize(self, iters=(1000,1000,10000), messages=(False, False, True)):
    """Optimize with parameters constrained and then with parameters released"""
    for layer in self.layers:
        # Fix the scale of each of the covariance functions.
        layer.kern.variance.fix(warning=False)
        layer.kern.lengthscale.fix(warning=False)

        # Fix the variance of the noise in each layer.
        layer.likelihood.variance.fix(warning=False)

    self.optimize(messages=messages[0],max_iters=iters[0])
    
    for layer in self.layers:
        layer.kern.lengthscale.constrain_positive(warning=False)
    self.obslayer.kern.variance.constrain_positive(warning=False)


    self.optimize(messages=messages[1],max_iters=iters[1])

    for layer in self.layers:
        layer.kern.variance.constrain_positive(warning=False)
        layer.likelihood.variance.constrain_positive(warning=False)
    self.optimize(messages=messages[2],max_iters=iters[2])

def posterior_sample(self, X, **kwargs):
    """Give a sample from the posterior of the deep GP."""
    Z = X
    for i, layer in enumerate(reversed(self.layers)):
        Z = layer.posterior_samples(Z, size=1, **kwargs)[:, :, 0]
 
    return Z

def visualize(self, scale=1.0, offset=0.0, xlabel='input', ylabel='output', 
              xlim=None, ylim=None, fontsize=20, portion=0.2,dataset=None, 
              diagrams='../diagrams'):
    """Visualize the layers in a deep GP with one-d input and output."""
    import os
    from gp_tutorial import gpplot
    depth = len(self.layers)
    if dataset is None:
        fname = 'deep-gp-layer'
    else:
        fname = dataset + '-deep-gp-layer'
    filename = os.path.join(diagrams, fname)
    last_name = xlabel
    last_x = self.X
    for i, layer in enumerate(reversed(self.layers)):
        if i>0:
            plt.plot(last_x, layer.X.mean, 'r.',markersize=10)
            last_x=layer.X.mean
            ax=plt.gca()
            name = 'layer ' + str(i)
            plt.xlabel(last_name, fontsize=fontsize)
            plt.ylabel(name, fontsize=fontsize)
            last_name=name
            mlai.write_figure(filename=filename + '-' + str(i-1) + '.svg', 
                              transparent=True, frameon=True)
            
        if i==0 and xlim is not None:
            xt = plot.pred_range(np.array(xlim), portion=0.0)
        elif i>0:
            xt = plot.pred_range(np.array(next_lim), portion=0.0)
        else:
            xt = plot.pred_range(last_x, portion=portion)
        yt_mean, yt_var = layer.predict(xt)
        if layer==self.obslayer:
            yt_mean = yt_mean*scale + offset
            yt_var *= scale*scale
        yt_sd = np.sqrt(yt_var)
        gpplot(xt,yt_mean,yt_mean-2*yt_sd,yt_mean+2*yt_sd)
        ax = plt.gca()
        if i>0:
            ax.set_xlim(next_lim)
        elif xlim is not None:
            ax.set_xlim(xlim)
        next_lim = plt.gca().get_ylim()
        
    plt.plot(last_x, self.Y*scale + offset, 'r.',markersize=10)
    plt.xlabel(last_name, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    mlai.write_figure(filename=filename + '-' + str(i) + '.svg', 
                      transparent=True, frameon=True)

    if ylim is not None:
        ax=plt.gca()
        ax.set_ylim(ylim)


def visualize_pinball(self, ax=None, scale=1.0, offset=0.0, xlabel='input', ylabel='output', 
                  xlim=None, ylim=None, fontsize=20, portion=0.2, points=50, vertical=True):
    """Visualize the layers in a deep GP with one-d input and output."""
    import teaching_plots as plot
    def scale_data(x, portion):     
        scale = (x.max()-x.min())/(1-2*portion)
        offset = x.min() - portion*scale
        return (x-offset)/scale, scale, offset

    if ax is None:
        fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

    depth = len(self.layers)

    last_name = xlabel
    last_x = self.X

    # Recover input and output scales from output plot
    plot.model_output(self, scale=scale, offset=offset, ax=ax, 
                      xlabel=xlabel, ylabel=ylabel, 
                      fontsize=fontsize, portion=portion)
    xlim=ax.get_xlim()
    xticks=ax.get_xticks()
    xtick_labels=ax.get_xticklabels().copy()
    ylim=ax.get_ylim()
    yticks=ax.get_yticks()
    ytick_labels=ax.get_yticklabels().copy()

    # Clear axes and start again
    ax.cla()
    if vertical:
        ax.set_xlim((0, 1))
        ax.invert_yaxis()

        ax.set_ylim((depth, 0))
    else:
        ax.set_ylim((0, 1))
        ax.set_xlim((0, depth))
        
    ax.set_axis_off()#frame_on(False)


    def pinball(x, y, y_std, color_scale=None, 
                layer=0, depth=1, ax=None, 
                alpha=1.0, portion=0.0, vertical=True):  

        
        scaledx, xscale, xoffset = scale_data(x, portion=portion)
        scaledy, yscale, yoffset = scale_data(y, portion=portion)
        y_std /= yscale

        # Check whether data is anti-correlated on output
        if np.dot((scaledx-0.5).T, (scaledy-0.5))<0:
            scaledy=1-scaledy
            flip=-1
        else:
            flip=1

        if color_scale is not None:
            color_scale, _, _=scale_data(color_scale, portion=0)
        scaledy = (1-alpha)*scaledx + alpha*scaledy

        def color_value(x, cmap=None, width=None, centers=None):
            """Return color as a function of position along x axis"""
            if cmap is None:
                cmap = np.asarray([[1, 0, 0], [1, 1, 0], [0, 1, 0]])
            ncenters = cmap.shape[0]
            if centers is None:
                centers = np.linspace(0+0.5/ncenters, 1-0.5/ncenters, ncenters)
            if width is None:
                width = 0.25/ncenters
            
            r = (x-centers)/width
            weights = np.exp(-0.5*r*r).flatten()
            weights /=weights.sum()
            weights = weights[:, np.newaxis]
            return np.dot(cmap.T, weights).flatten()


        for i in range(x.shape[0]):
            if color_scale is not None:
                color = color_value(color_scale[i])
            else:
                color=(1, 0, 0)
            x_plot = np.asarray((scaledx[i], scaledy[i])).flatten()
            y_plot = np.asarray((layer, layer+alpha)).flatten()
            if vertical:
                ax.plot(x_plot, y_plot, color=color, alpha=0.5, linewidth=3)
                ax.plot(x_plot, y_plot, color='k', alpha=0.5, linewidth=0.5)
            else:
                ax.plot(y_plot, x_plot, color=color, alpha=0.5, linewidth=3)
                ax.plot(y_plot, x_plot, color='k', alpha=0.5, linewidth=0.5)

            # Plot error bars that increase as sqrt of distance from start.
            std_points = 50
            stdy = np.linspace(0, alpha,std_points)
            stdx = np.sqrt(stdy)*y_std[i]
            stdy += layer
            mean_vals = np.linspace(scaledx[i], scaledy[i], std_points)
            upper = mean_vals+stdx 
            lower = mean_vals-stdx 
            fillcolor=color
            x_errorbars=np.hstack((upper,lower[::-1]))
            y_errorbars=np.hstack((stdy,stdy[::-1]))
            if vertical:
                ax.fill(x_errorbars,y_errorbars,
                        color=fillcolor, alpha=0.1)
                ax.plot(scaledy[i], layer+alpha, '.',markersize=10, color=color, alpha=0.5)
            else:
                ax.fill(y_errorbars,x_errorbars,
                        color=fillcolor, alpha=0.1)
                ax.plot(layer+alpha, scaledy[i], '.',markersize=10, color=color, alpha=0.5)
            # Marker to show end point
        return flip


    # Whether final axis is flipped
    flip = 1
    first_x=last_x
    for i, layer in enumerate(reversed(self.layers)):     
        if i==0:
            xt = plot.pred_range(last_x, portion=portion, points=points)
            color_scale=xt
        yt_mean, yt_var = layer.predict(xt)
        if layer==self.obslayer:
            yt_mean = yt_mean*scale + offset
            yt_var *= scale*scale
        yt_sd = np.sqrt(yt_var)
        flip = flip*pinball(xt,yt_mean,yt_sd,color_scale,portion=portion, 
                            layer=i, ax=ax, depth=depth,vertical=vertical)#yt_mean-2*yt_sd,yt_mean+2*yt_sd)
        xt = yt_mean
    # Make room for axis labels
    if vertical:
        ax.set_ylim((2.1, -0.1))
        ax.set_xlim((-0.02, 1.02))
        ax.set_yticks(range(depth,0,-1))
    else:
        ax.set_xlim((-0.1, 2.1))
        ax.set_ylim((-0.02, 1.02))
        ax.set_xticks(range(0, depth))
        
    def draw_axis(ax, scale=1.0, offset=0.0, level=0.0, flip=1, 
                  label=None,up=False, nticks=10, ticklength=0.05,
                  vertical=True,
                 fontsize=20):
        def clean_gap(gap):
            nsf = np.log10(gap)
            if nsf>0:
                nsf = np.ceil(nsf)
            else:
                nsf = np.floor(nsf)
            lower_gaps = np.asarray([0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 
                                     0.1, 0.25, 0.5, 
                                     1, 1.5, 2, 2.5, 3, 4, 5, 10, 25, 50, 100])
            upper_gaps = np.asarray([1, 2, 3, 4, 5, 10])
            if nsf >2 or nsf<-2:
                d = np.abs(gap-upper_gaps*10**nsf)
                ind = np.argmin(d)
                return upper_gaps[ind]*10**nsf
            else:
                d = np.abs(gap-lower_gaps)
                ind = np.argmin(d)
                return lower_gaps[ind]
            
        tickgap = clean_gap(scale/(nticks-1))
        nticks = int(scale/tickgap) + 1
        tickstart = np.round(offset/tickgap)*tickgap
        ticklabels = np.asarray(range(0, nticks))*tickgap + tickstart
        ticks = (ticklabels-offset)/scale
        axargs = {'color':'k', 'linewidth':1}
        
        if not up:
            ticklength=-ticklength
        tickspot = np.linspace(0, 1, nticks)
        if flip < 0:
            ticks = 1-ticks
        for tick, ticklabel in zip(ticks, ticklabels):
            if vertical:
                ax.plot([tick, tick], [level, level-ticklength], **axargs)
                ax.text(tick, level-ticklength*2, ticklabel, horizontalalignment='center', 
                        fontsize=fontsize/2)
                ax.text(0.5, level-5*ticklength, label, horizontalalignment='center', fontsize=fontsize)
            else:
                ax.plot([level, level-ticklength], [tick, tick],  **axargs)
                ax.text(level-ticklength*2, tick, ticklabel, horizontalalignment='center', 
                        fontsize=fontsize/2)
                ax.text(level-5*ticklength, 0.5, label, horizontalalignment='center', fontsize=fontsize)
        
        if vertical:
            xlim = list(ax.get_xlim())
            if ticks.min()<xlim[0]:
                xlim[0] = ticks.min()
            if ticks.max()>xlim[1]:
                xlim[1] = ticks.max()
            ax.set_xlim(xlim)
            
            ax.plot([ticks.min(), ticks.max()], [level, level], **axargs)
        else:
            ylim = list(ax.get_ylim())
            if ticks.min()<ylim[0]:
                ylim[0] = ticks.min()
            if ticks.max()>ylim[1]:
                ylim[1] = ticks.max()
            ax.set_ylim(ylim)
            ax.plot([level, level], [ticks.min(), ticks.max()], **axargs)


    _, xscale, xoffset = scale_data(first_x, portion=portion)
    _, yscale, yoffset = scale_data(yt_mean, portion=portion)
    draw_axis(ax=ax, scale=xscale, offset=xoffset, level=0.0, label=xlabel, 
              up=True, vertical=vertical)
    draw_axis(ax=ax, scale=yscale, offset=yoffset, 
              flip=flip, level=depth, label=ylabel, up=False, vertical=vertical)
    
