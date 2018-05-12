---
title: "Towards Machine Learning Systems Design"
abstract: 
published: 2018-05-02
venue: Sheffield ML Research Network Launch
reveal: 2018-05-02-towards-ml-systems-design.slides.html
ipynb: 2018-05-02-towards-ml-systems-design.ipynb
layout: talk
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
published: 2018-05-02
---

### What is Machine Learning?



What is machine learning? At its most basic level machine learning is a combination of

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. That experience can be other data, it can come
from transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our
inductive biases. The *prediction* is an action to be taken or a
categorization or a quality score. The reason that machine learning
has become a mainstay of artificial intelligence is the importance of
predictions in artificial intelligence. The data and the model are combined through computation.




In practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and the objectie function leads to a *learning algorithm*. The class of prediction functions and objective functions we can make use of is restricted by the algorithms they lead to. If the prediction function or the objective function are too complex, then it can be difficult to find an appropriate learning algorithm. Much of the acdemic field of machine learning is the quest for new learning algorithms that allow us to bring different types of models and data together.

A useful reference for state of the art in machine learning is the UK Royal Society Report, [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on ["What is Machine Learning?"](http://inverseprobability.com/2017/07/17/what-is-machine-learning)


Machine learning technologies have been the driver of two related, but distinct disciplines. The first is *data science*. Data science is an emerging field that arises from the fact that we now collect so much data by happenstance, rather than by *experimental design*. Classical statistics is the science of drawing conclusions from data, and to do so statistical experiments are carefully designed. In the modern era we collect so much data that there's a desire to draw inferences directly from the data.

As well as machine learning, the field of data science draws from statistics, cloud computing, data storage (e.g. streaming data), visualization and data mining.

In contrast, artificial intelligence technologies typically focus on emulating some form of human behaviour, such as understanding an image, or some speech, or translating text from one form to another. The recent advances in artifcial intelligence have come from machine learning providing the automation. But in contrast to data science, in artifcial intelligence the data is normally collected with the specific task in mind. In this sense it has relations to classical statistics. 

Classically artificial intelligence worried more about *logic* and *planning* and focussed less on data driven decision making. Modern machine learning owes more to the field of *Cybernetics* than artificial intelligence. Related fields include *robotics*, *speech recognition*, *language understanding* and *computer vision*. 

There are strong overlaps between the fields, the wide availability of data by happenstance makes it easier to collect data for designing AI systems. These relations are coming through wide availability of sensing technologies that are interconnected by celluar networks, WiFi and the internet. This phenomenon is sometimes known as the *Internet of Things*, but this feels like a dangerous misnomer. We must never forget that we are interconnecting people, not things. 




### What does Machine Learning do? 

* ML Automates through Data
    * *Strongly* related to statistics.
    * Field underpins revolution in *data science* and *AI*
* With AI: 
    * *logic*, *robotics*, *computer vision*, *speech*
* With Data Science: 
    * *databases*, *data mining*, *statistics*, *visualization*

### "Embodiment Factors"

<table>
 <tr>
  <td></td>
  <td align="center"><img class="" src="./slides/diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="40%" align="center" style="background:none; border:none; box-shadow:none;"></td>
  <td align="center"><img class="" src="./slides/diagrams/ClaudeShannon_MFO3807.jpg" width="25%" align="center" style="background:none; border:none; box-shadow:none;"></td>
 </tr>
 <tr>
  <td>compute</td>
  <td align="center">$$\approx 10 \text{ gigaflops}$$</td><td align="center">$$\approx 14 \text{ teraflops}$$</td>
 </tr>
 <tr>
  <td>communicate</td>
  <td align="center">$$\approx 1 \text{ gigbit/s}$$</td>
  <td align="center">$$\approx 100 \text{ bit/s}$$</td>
 </tr>
 <tr>
  <td>(compute/communicate)</td>
  <td align="center">$$10$$</td>
  <td align="center">$$\approx 10^{13}$$</td>
 </tr>
</table>



There is a fundamental limit placed on our intelligence based on our ability to communicate. Claude Shannon founded the field of information theory. The clever part of this theory is it allows us to separate our measurement of information from what the information pertains to[^knowledge-representation].

[^knowledge-representation]: the challenge of understanding what it pertains to is known as knowledge representation). 

Shannon measured information in bits. One bit of information is the amount of information I pass to you when I give you the result of a coin toss. Shannon was also interested in the amount of information in the English language. He estimated that on average a word in the English language contains 12 bits of information. 

Given typical speaking rates, that gives us an estimate of our ability to communicate of around 100 bits per second. Computers on the other hand can communicate much more rapidly. Current wired network speeds are around a billion bits per second, ten million times faster. 

When it comes to compute though, our best estimates indicate our computers are slower. A typical modern computer can process make around 2 billion floating point operations per second, each floating point operation involves a 64 bit number. So the computer is processing around 120 billion bits per second. 

It's difficult to get similar estimates for humans, but by some estimates the amount of compute we would require to *simulate* a human brain is equivalent to that in the UK's fastest computer, the MET office machine in Exeter, which in 2018 ranks as the 11th fastest computer in the world. That machine simulates the world's weather each morning, and then simulates the world's climate. It is a 16 petaflop machine. 

So when it comes to our ability to compute we are extraordinary, not compute in our conscious mind, but the underlying neuron firings that underpin both our consciousness, our sbuconsciousness as well as our motor control etc. By analogy I sometimes like to think of us as a Formula One engine. But in terms of our ability to deploy that computation in actual use, to share the results of what we have inferred, we are very limited. So when you imagine the F1 car that represents a psyche, think of an F1 car with bicycle wheels.

In contrast, our computers have less computational power, but they can communicate fare more fluidly. They are more like a go-kart, less well powered, but with tires that allow them to deploy that power.

For humans, that means much of our computation should be dedicated to considering *what* we should compute. To do that efficiently we need to model the world around us. The most complex thing in the world around us is other humans. So it is no surprise that we model them. We second guess what their intentions are, and our communication is only necessary when they are departing from how we model them. Naturally, for this to work well, we need to understand those we work closely with. So it is no surprise that social communication, social bonding, forms so much of a part of our use of our limited bandwidth. 

There is a second effect here, our need to anthropomorphise objects around us. Our tendency to model our fellow humans extends to when we interact with other entities in our environment. To our pets as well as inanimate objects around us, such as computers or even our cars. This tendency to overinterpret could be a consequence of our limited ability to communicate. 

For more details see this paper ["Living Together: Mind and Machine Intelligence"](https://arxiv.org/abs/1705.07996), and this [TEDx talk](http://inverseprobability.com/talks/lawrence-tedx17/living-together.html).

### Evolved Relationship 

<object class="svgplot" align="" data="./slides/diagrams/data-science/information-flow003.svg"></object>

The high bandwidth of computers has resulted in a close relationship between the computer and data. Larege amounts of information can flow between the two. The degree to which the computer is mediating our relationship with data means that we should consider it an intermediary. 

Origininally our low bandwith relationship with data was affected by two characteristics. Firstly, our tendency to over-interpret driven by our need to extract as much knowledge from our low bandwidth information channel as possible. Secondly, by our improved understanding of the domain of *mathematical* statistics and how our cognitive biases can mislead us. 

With this new set up there is a potential for assimilating far more information via the computer, but the computer can present this to us in various ways. If it's motives are not aligned with ours then it can misrepresent the information. This needn't be nefarious it can be simply as a result of the computer pursuing a different objective from us. For example, if the computer is aiming to maximize our interaction time that may be a different objective from ours which may be to summarize information in a representative manner in the *shortest* possible lenght of time. 

For example, for me it was  a common experience to pick up my telephone with the intention of checking when my next appointme was, but to soon find myself  distracted by another application on the phone, and end up reading something on the internet. By the time I'd finished reading, I would often have forgotten the reason I picked up my phone in the first place. 

We can benefit enormously from the very large amount of information we can now obtain through this evolved relationship between us and data. Biology has already benefited from large scale data sharing and the improved inferences that can be drawn through summarizing data by computer. That has underpinned the revolution in computational biology. But in our daily lives this phenomenon is affecting us in ways which we haven't envisaged.

Better mediation of this flow actually requires a better understanding of human-computer interaction. This in turn involves understanding our own intelligence better, what its cognitive biases are and how these might mislead us.

For further thoughts see [this Guardian article](https://www.theguardian.com/media-network/2015/jul/23/data-driven-economy-marketing) on marketing in the internet era and [this blog post](http://inverseprobability.com/2015/12/04/what-kind-of-ai) on System Zero. 





### What does Machine Learning do?


Any process of automation allows us to scale what we do by codifying a process in some way that makes it efficient and repeatable. Machine learning automates by emulating human (or other actions) found in data. Machine learning codifies in the form of a mathematical function that is learnt by a computer. If we can create these mathematical functions in ways in which they can interconnect, then we can also build systems.

### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ \text{odds} = \frac{\text{bought}}{\text{not bought}} $$
$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$


### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ p(\text{bought}) =  \mappingFunction\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}\right)$$


### Codify Through Mathematical Functions

* How does machine learning work?
* Jumper (jersey/sweater) purchase with logistic regression
$$ p(\text{bought}) =  \mappingFunction\left(\boldsymbol{\beta}^\top \inputVector\right)$$

We call $\mappingFunction(\cdot)$ the *prediction function*

### Fit to Data

* Use an objective function
$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix)$$

* E.g. least squares
$$\errorFunction(\boldsymbol{\beta}) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i)\right)^2$$

### Two Components

* Prediction function, $\mappingFunction(\cdot)$
* Objective function, $\errorFunction(\cdot)$


### Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

<small>Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.</small>

<img class="" src="./slides/diagrams/deepface_neg.png" width="100%" align="" style="background:none; border:none; box-shadow:none;">

<p align="right">
<small>Source: DeepFace</small></p>


<img class="" src="./slides/diagrams/576px-Early_Pinball.jpg" width="50%" align="" style="background:none; border:none; box-shadow:none;">

We can think of what these models are doing as being similar to early pin ball machines. In a neural network, we input a number (or numbers), whereas in pinball, we input a ball. The location of the ball on the left-right axis can be thought of as the number. As the ball falls through the machine, each layer of pins can be thought of as a different layer of neurons. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it's like playing pinball in a *hyper-space*.




At initialization, the pins aren't in the right place to bring the ball to the correct decision.


Learning involves moving all the pins to be in the right position, so that the ball falls in the right place. But moving all these pins in hyperspace can be difficult. In a hyper space you have to put a lot of data through the machine for to explore the positions of all the pins. Adversarial learning reflects the fact that a ball can be moved a small distance and lead to a very different result.

Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine.

```{.python}
import numpy as np
import teaching_plots as plot
```

```{.python}
%load -s compute_kernel mlai.py
```

```{.python}
%load -s eq_cov mlai.py
```

```{.python}
np.random.seed(10)
plot.rejection_samples(compute_kernel, kernel=eq_cov, 
                       lengthscale=0.25, diagrams='./slides/diagrams/gp')
```





```{.python}
import pods
import matplotlib.pyplot as plt
```


### Olympic Marathon Data

The first thing we will do is load a standard data set for regression modelling. The data consists of the pace of Olympic Gold Medal Marathon winners for the Olympics from 1896 to present. First we load in the data and plot.



```{.python}
data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())

xlim = (1875,2030)
ylim = (2.5, 6.5)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(figure=fig, filename='./slides/diagrams/datasets/olympic-marathon.svg', transparent=True, frameon=True)

```

### Olympic Marathon Data

<table><tr><td width="70%">
-   Gold medal times for Olympic Marathon since 1896.

-   Marathons before 1924 didn’t have a standardised distance.

-   Present results using pace per km.

-   In 1904 Marathon was badly organised leading to very slow times.
</td><td width="30%">
![image](./slides/diagrams/Stephen_Kiprotich.jpg)
<small>Image from Wikimedia Commons <http://bit.ly/16kMKHQ></small>
</td></tr></table>


<object class="svgplot" align="" data="./slides/diagrams/ml/olympic_marathon.svg"></object>


Things to notice about the data include the outlier in 1904, in this year, the olympics was in St Louis, USA. Organizational problems and challenges with dust kicked up by the cars following the race meant that participants got lost, and only very few participants completed. 

More recent years see more consistently quick marathons.




Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).

```{.python}
m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function
```

The first command sets up the model, then 
```
m_full.optimize()
```
optimizes the parameters of the covariance function and the noise level of the model. Once the fit is complete, we'll try creating some test points, and computing the output of the GP model in terms of the mean and standard deviation of the posterior functions between 1870 and 2030. We plot the mean function and the standard deviation at 200 locations. We can obtain the predictions using
```
y_mean, y_var = m_full.predict(xt)
```


```{.python}
xt = np.linspace(1870,2030,200)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)
```

Now we plot the results using the helper function in ```teaching_plots```.

```{.python}
import teaching_plots as plot
```

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='./slides/diagrams/gp/olympic-marathon-gp.svg', 
                  transparent=True, frameon=True)
```


<object class="svgplot" align="" data="./slides/diagrams/gp/olympic-marathon-gp.svg"></object>


### Fit Quality

In the fit we see that the error bars (coming mainly from the noise variance) are quite large. This is likely due to the outlier point in 1904, ignoring that point we can see that a tighter fit is obtained. To see this making a version of the model, ```m_clean```, where that point is removed. 

```
x_clean=np.vstack((x[0:2, :], x[3:, :]))
y_clean=np.vstack((y[0:2, :], y[3:, :]))

m_clean = GPy.models.GPRegression(x_clean,y_clean)
_ = m_clean.optimize()
```


### 

Data is fine for answering very specific questions, like "Who won the Olympic Marathon in 2012?", because we have that answer stored, however, we are not given the answer to many other questions. For example, Alan Turing was a formidable marathon runner, in 1946 he ran a time 2 hours 46 minutes (just under four minutes per kilometer, faster than I and most of the other [Endcliffe Park Run](http://www.parkrun.org.uk/sheffieldhallam/) runners can do 5 km). What is the probability he would have won an Olympics if one had been held in 1946?

<table><tr><td width=""></td><td width=""></td></tr></table>{<img class="" src="./slides/diagrams/turing_run.jpg" width="40%" align="" style="background:none; border:none; box-shadow:none;">}{<img class="50%" src="./slides/diagrams/turing-times.gif" width="50%" align="" style="background:none; border:none; box-shadow:none;">

*Alan Turing, in 1946 he was only 11 minutes slower than the winner of the 1948 games. Would he have won a hypothetical games held in 1946? Source: [Alan Turing Internet Scrapbook](http://www.turing.org.uk/scrapbook/run.html).*


### Deep GP Fit




Let's see if a deep Gaussian process can help here. We will construct a deep Gaussian process with one hidden layer (i.e. one Gaussian process feeding into another). 

Build a Deep GP with an additional hidden layer (one dimensional) to fit the model.


```{.python}
hidden = 1
m = deepgp.DeepGP([y.shape[1],hidden,x.shape[1]],Y=yhat, X=x, inits=['PCA','PCA'], 
                  kernels=[GPy.kern.RBF(hidden,ARD=True),
                           GPy.kern.RBF(x.shape[1],ARD=True)], # the kernels for each layer
                  num_inducing=50, back_constraint=False)
```
				  

Deep Gaussian process models also can require some thought in initialization. Here we choose to start by setting the noise variance to be one percent of the data variance.

Optimization requires moving variational parameters in the hidden layer representing the mean and variance of the expected values in that layer. Since all those values can be scaled up, and this only results in a downscaling in the output of the first GP, and a downscaling of the input length scale to the second GP. It makes sense to first of all fix the scales of the covariance function in each of the GPs.

Sometimes, deep Gaussian processes can find a local minima which involves increasing the noise level of one or more of the GPs. This often occurs because it allows a minimum in the KL divergence term in the lower bound on the likelihood. To avoid this minimum we habitually train with the likelihood variance (the noise on the output of the GP) fixed to some lower value for some iterations.

Let's create a helper function to initialize the models we use in the notebook.


```{.python}
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
# Bind the new method to the Deep GP object.
deepgp.DeepGP.initialize=initialize
```

```{.python}
# Call the initalization
m.initialize()
```

Now optimize the model. The first stage of optimization is working on variational parameters and lengthscales only. 
```
m.optimize(messages=False,max_iters=100)
```

Now we remove the constraints on the scale of the covariance functions associated with each GP and optimize again.
```
for layer in m.layers:
    pass #layer.kern.variance.constrain_positive(warning=False)
m.obslayer.kern.variance.constrain_positive(warning=False)
m.optimize(messages=False,max_iters=100)
```

Finally, we allow the noise variance to change and optimize for a large number of iterations.
```
for layer in m.layers:
    layer.likelihood.variance.constrain_positive(warning=False)
m.optimize(messages=True,max_iters=10000)
```

For our optimization process we define a new function.

```{.python}
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
	
# Bind the new method to the Deep GP object.
deepgp.DeepGP.staged_optimize=staged_optimize
```

```{.python}
m.staged_optimize(messages=(True,True,True))
```


### Plot the prediction

The prediction of the deep GP can be extracted in a similar way to the normal GP. Although, in this case, it is an approximation to the true distribution, because the true distribution is not Gaussian. 


```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', 
          fontsize=20, portion=0.2)
ax.set_xlim(xlim)

ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='./slides/diagrams/deepgp/olympic-marathon-deep-gp.svg', 
                transparent=True, frameon=True)
```


### Olympic Marathon Data Deep GP

<object class="svgplot" align="" data="./slides/diagrams/deepgp/olympic-marathon-deep-gp.svg"></object>


```{.python}
def posterior_sample(self, X, **kwargs):
    """Give a sample from the posterior of the deep GP."""
    Z = X
    for i, layer in enumerate(reversed(self.layers)):
        Z = layer.posterior_samples(Z, size=1, **kwargs)[:, :, 0]
 
    return Z
deepgp.DeepGP.posterior_sample = posterior_sample
```

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_sample(m, scale=scale, offset=offset, samps=10, ax=ax, 
                  xlabel='year', ylabel='pace min/km', portion = 0.225)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig, filename='./slides/diagrams/deepgp/olympic-marathon-deep-gp-samples.svg', 
                  transparent=True, frameon=True)
```


### Olympic Marathon Data Deep GP {data-transition="None"}

<object class="svgplot" align="" data="./slides/diagrams/deepgp/olympic-marathon-deep-gp-samples.svg"></object>



### Fitted GP for each layer

Now we explore the GPs the model has used to fit each layer. First of all, we look at the hidden layer.


```{.python}
def visualize(self, scale=1.0, offset=0.0, xlabel='input', ylabel='output', 
              xlim=None, ylim=None, fontsize=20, portion=0.2,dataset=None, 
              diagrams='./diagrams'):
    """Visualize the layers in a deep GP with one-d input and output."""
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

# Bind the new method to the Deep GP object.
deepgp.DeepGP.visualize=visualize
```

```{.python}
m.visualize(scale=scale, offset=offset, xlabel='year',
            ylabel='pace min/km',xlim=xlim, ylim=ylim,
            dataset='olympic-marathon',
            diagrams='./slides/diagrams/deepgp')
```





```{.python}
def scale_data(x, portion):     
    scale = (x.max()-x.min())/(1-2*portion)
    offset = x.min() - portion*scale
    return (x-offset)/scale, scale, offset

def visualize_pinball(self, ax=None, scale=1.0, offset=0.0, xlabel='input', ylabel='output', 
                  xlim=None, ylim=None, fontsize=20, portion=0.2, points=50, vertical=True):
    """Visualize the layers in a deep GP with one-d input and output."""

    if ax is None:
        fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

    depth = len(self.layers)

    last_name = xlabel
    last_x = self.X

    # Recover input and output scales from output plot
    plot_model_output(self, scale=scale, offset=offset, ax=ax, 
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
    
    #for txt in xticklabels:
    #    txt.set
# Bind the new method to the Deep GP object.
deepgp.DeepGP.visualize_pinball=visualize_pinball
```


```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
m.visualize_pinball(ax=ax, scale=scale, offset=offset, points=30, portion=0.1,
                    xlabel='year', ylabel='pace km/min', vertical=True)
mlai.write_figure(figure=fig, filename='./slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball.svg', 
                  transparent=True, frameon=True)
```

### Olympic Marathon Pinball Plot

<object class="svgplot" align="" data="./slides/diagrams/deepgp/olympic-marathon-deep-gp-pinball.svg"></object>

The pinball plot shows the flow of any input ball through the deep Gaussian process. In a pinball plot a series of vertical parallel lines would indicate a purely linear function. For the olypmic marathon data we can see the first layer begins to shift from input towards the right. Note it also does so with some uncertainty (indicated by the shaded backgrounds). The second layer has less uncertainty, but bunches the inputs more strongly to the right. This input layer of uncertainty, followed by a layer that pushes inputs to the right is what gives the heteroschedastic noise.


<!-- ### Data Science

* Industrial Revolution 4.0?
* *Industrial Revolution* (1760-1840) term coined by Arnold Toynbee,
late 19th century.
* Maybe: But this one is dominated by *data* not *capital*
* That presents *challenges* and *opportunities* 

compare [digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data) vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)

* Apple vs Nokia: How you handle disruption.


Disruptive technologies take time to assimilate, and best practices, as well as the pitfalls of new technologies take time to share. Historically, new technologies led to new professions. [Isambard Kingdom Brunel](https://en.wikipedia.org/wiki/Isambard_Kingdom_Brunel) (born 1806) was a leading innovator in civil, mechanical and naval engineering. Each of these has its own professional institutions founded in 1818, 1847, and 1860 respectively.

[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla) developed the modern approach to electrical distribution, he was born in 1856 and the American Instiute for Electrical Engineers was founded in 1884, the UK equivalent was founded in 1871. 

[William Schockley Jr](https://en.wikipedia.org/wiki/William_Shockley), born 1910, led the group that developed the transistor, referred to as "the man who brought silicon to Silicon Valley", in 1963 the American Institute for Electical Engineers merged with the Institute of Radio Engineers to form the Institute of Electrical and Electronic Engineers. 

[Watts S. Humphrey](https://en.wikipedia.org/wiki/Watts_Humphrey), born 1927, was known as the "father of software quality", in the 1980s he founded a program aimed at understanding and managing the software process. The British Computer Society was founded in 1956.







Why the need for these professions? Much of it is about codification of best practice and developing trust between the public and practitioners. These fundamental characteristics of the professions are shared with the oldest professions (Medicine, Law) as well as the newest (Information Technology).





So where are we today? My best guess is we are somewhere equivalent to the 1980s for Software Engineering. In terms of professional deployment we have a basic understanding of the equivalent of "programming" but much less understanding of *machine learning systems design* and *data infrastructure*. How the components we ahve developed interoperate together in a reliable and accountable manner. Best practice is still evolving, but perhaps isn't being shared widely enough. 

One problem is that the art of data science is superficially similar to regularl software engineering. Although in practice it is rather different. Modern software engineering practice operates to generate code which is well tested as it is written, agile programming techniques provide the appropriate degree of flexibility for the individual programmers alongside sufficient formalization and testing. These techniques have evolved from an overly restrictive formalization that was proposed in the early days of software engineering.

While data science involves programming, it is different in the following way. Most of the work in data science involves understanding the data and the appropriate manipulations to apply to extract knowledge from the data. The eventual number of lines of code that are required to extract that knowledge are often very few, but the amount of thought and attention that needs to be applied to each line is much more than a traditional line of software code. Testing of those lines is also of a different nature, provisions have to be made for evolving data environments. Any development work is often done on a static snapshot of data, but deployment is made in a live environment where the nature of data changes. Quality control involves checking for degradation in performance arising form unanticipated changes in data quality. It may also need to check for regulatory conformity. For example, in the UK the General Data Protection Regulation stipulates standards of explainability and fairness that may need to be monitored. These concerns do not affect traditional software deployments.

Others are also pointing out these challenges, [this post](https://medium.com/@karpathy/software-2-0-a64152b37c35) from Andrej Karpathy (now head of AI at Tesla) covers the notion of "Software 2.0". Google researchers have highlighted the challenges of "Technical Debt" in machine learning [@Sculley:debt15]. Researchers at Berkeley have characterized the systems challenges associated with machine learning [@Stoica:systemsml17].


 -->
<!-- Data science is not only about technical expertise and analysis of data, we need to also generate a culture of decision making that acknowledges the true challenges in data-driven automated decision making. In particular, a focus on algorithms has neglected the importance of data in driving decisions. The quality of data is paramount in that poor quality data will inevitably lead to poor quality decisions. Anecdotally most data scientists will suggest that 80% of their time is spent on data clean up, and only 20% on actually modelling. 

### The Software Crisis

>The major cause of the software crisis is that the machines have
>become several orders of magnitude more powerful! To put it quite
>bluntly: as long as there were no machines, programming was no problem
>at all; when we had a few weak computers, programming became a mild
>problem, and now we have gigantic computers, programming has become an
>equally gigantic problem.
>
> Edsger Dijkstra (1930-2002), The Humble Programmer

In the late sixties early software programmers made note of the increasing costs of software development and termed the challenges associated with it as the "[Software Crisis](https://en.wikipedia.org/wiki/Software_crisis)". Edsger Dijkstra referred to the crisis in his 1972 Turing Award winner's address.

### The Data Crisis

>The major cause of the data crisis is that machines have become more
>interconnected than ever before. Data access is therefore cheap, but
>data quality is often poor. What we need is cheap high quality
>data. That implies that we develop processes for improving and
>verifying data quality that are efficient.
>
>There would seem to be two ways for improving efficiency. Firstly, we
>should not duplicate work. Secondly, where possible we should automate
>work. 


What I term "The Data Crisis" is the modern equivalent of this problem. The quantity of modern data, and the lack of attention paid to data as it is initially "laid down" and the costs of data cleaning are bringing about a crisis in data-driven decision making. Just as with software, the crisis is most correctly addressed by 'scaling' the manner in which we process our data. Duplication of work occurs because the value of data cleaning is not correctly recognised in management decision making processes. Automation of work is increasingly possible through techniques in "artificial intelligence", but this will also require better management of the data science pipeline so that data about data science (meta-data science) can be correctly assimilated and processed. The Alan Turing institute has a program focussed on this area, [AI for Data Analytics](https://www.turing.ac.uk/research_projects/artificial-intelligence-data-analytics/).
 -->

<!-- ### Rest of this Talk: Two Areas of Focus  -->

<!-- * Reusability of Data -->

<!-- * Deployment of Machine Learning Systems -->

<!-- ### Rest of this Talk: Two Areas of Focus  -->

<!-- * <s>Reusability of Data</s> -->

<!-- * Deployment of Machine Learning Systems -->

<!--### Data Readiness Levels

[<img class="" src="./slides/diagrams/data-science/data-readiness-levels.png" width="" align="" style="background:none; border:none; box-shadow:none;">](https://arxiv.org/pdf/1705.02245.pdf)

[Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels)

Data readiness levels are an attempt to develop a language around data quality that can bridge the gap between technical solutions and decision makers such as managers and project planners. The are inspired by Technology Readiness Levels which attempt to quantify the readiness of technologies for deployment.

### Three Grades of Data Readiness:

Data-readiness describes, at its coarsest level,  three separate stages of data graduation.

* Grade C - accessibility

* Grade B - validity

* Grade A - usability

### Accessibility: Grade C

The first grade refers to the accessibility of data. Most data science practitioners will be used to working with data-providers who, perhaps having had little experience of data-science before, state that they "have the data". More often than not, they have not verified this. A convenient term for this is "Hearsay Data", someone has *heard* that they have the data so they *say* they have it. This is the lowest grade of data readiness. 

Progressing through Grade C involves ensuring that this data is accessible. Not just in terms of digital accessiblity, but also for regulatory, ethical and intellectual property reasons.



### Validity: Grade B

Data transits from Grade C to Grade B once we can begin digital analysis on the computer. Once the challenges of access to the data have been resolved, we can make the data available either via API, or for direct loading into analysis software (such as Python, R, Matlab, Mathematica or SPSS). Once this has occured the data is at B4 level. Grade B involves the *validity* of the data. Does the data really represent what it purports to? There are challenges such as missing values, outliers, record duplication. Each of these needs to be investigated. 

Grade B and C are important as if the work done in these grades is documented well, it can be reused in other projects. Reuse of this labour is key to reducing the costs of data-driven automated decision making. There is a strong overlap between the work required in this grade and the statistical field of [*exploratory data analysis*](https://en.wikipedia.org/wiki/Exploratory_data_analysis) [@Tukey:exploratory77]. 


### Usability: Grade A

Once the validity of the data is determined, the data set can be considered for use in a particular task. This stage of data readiness is more akin to what machine learning scientists are used to doing in Universities. Bringing an algorithm to bear on a well understood data set. 

In Grade A we are concerned about the utility of the data given a particular task. Grade A may involve additional data collection (experimental design in statistics) to ensure that the task is fulfilled.

This is the stage where the data and the model are brought together, so expertise in learning algorithms and their application is key. Further ethical considerations, such as the fairness of the resulting predictions are required at this stage. At the end of this stage a prototype model is ready for deployment.

Deployment and maintenance of machine learning models in production is another important issue which Data Readiness Levels are only a part of the solution for.



To find out more, or to contribute ideas go to <http://data-readiness.org>



Throughout the data preparation pipeline, it is important to have close interaction between data scientists and application domain experts. Decisions on data preparation taken outside the context of application have dangerous downstream consequences. This provides an additional burden on the data scientist as they are required for each project, but it should also be seen as a learning and familiarization exercise for the domain expert. Long term, just as biologists have found it necessary to assimilate the skills of the bioinformatician to be effective in their science, most domains will also require a familiarity with the nature of data driven decision making and its application. Working closely with data-scientists on data preparation is one way to begin this sharing of best practice.

The processes involved in Grade C and B are often badly taught in courses on data science. Perhaps not due to a lack of interest in the areas, but maybe more due to a lack of access to real world examples where data quality is poor. 

These stages of data science are also ridden with ambiguity. In the long term they could do with more formalization, and automation, but best practice needs to be understood by a wider community before that can happen.

-->

### Artificial Intelligence

* Challenges in deploying AI.

* Currently this is in the form of "machine learning systems"

### Internet of People

* Fog computing: barrier between cloud and device blurring.
    * Computing on the Edge

* Complex feedback between algorithm and implementation
  
### Deploying ML in Real World: Machine Learning Systems Design

* Major new challenge for systems designers.

* Internet of Intelligence but currently:
	* AI systems are *fragile*

### Fragility of AI Systems



### Pigeonholing

<img class="" src="./slides/diagrams/TooManyPigeons.jpg" width="60%" align="" style="background:none; border:none; box-shadow:none;">


The way we are deploying artificial intelligence systems in practice is to build up systems of machine learning components. To build a machine learning system, we decompose the task into parts which we can emulate with ML methods. Each of these parts can be, typically, independently constructed and verified. For example, in a driverless car we can decompose the tasks into components such as "pedestrian detection" and "road line detection". Each of these components can be constructed with, for example, an independent classifier. We can then superimpose a logic on top. For example, "Follow the road line unless you detect a pedestrian in the road". 

This allows for verification of car performance, as long as we can verify the individual components. However, it also implies that the AI systems we deploy are *fragile*.

### Rapid Reimplementation



### Early AI

<img class="rotateimg90" src="./slides/diagrams/2017-10-12 16.47.34.jpg" width="40%" align="" style="background:none; border:none; box-shadow:none;">

### Machine Learning Systems Design

<img class="" src="./slides/diagrams/SteamEngine_Boulton&Watt_1784_neg.png" width="50%" align="" style="background:none; border:none; box-shadow:none;">

### Adversaries

* Stuxnet
* Mischevious-Adversarial

### Turnaround And Update

* There is a massive need for turn around and update
* A redeploy of the entire system.
    * This involves changing the way we design and deploy.
* Interface between security engineering and machine learning.

### Peppercorns

* A new name for system failures which aren't bugs.
* Difference between finding a fly in your soup vs a peppercorn in
  your soup. 


### Uncertainty Quantification

* Deep nets are powerful approach to images, speech, language.

* Proposal: Deep GPs may also be a great approach, but better to deploy according to natural strengths.

### Uncertainty Quantification

* Probabilistic numerics, surrogate modelling, emulation, and UQ.

* Not a fan of AI as a term.

* But we are faced with increasing amounts of *algorithmic decision making*.

### ML and Decision Making

* When trading off decisions: compute or acquire data?

* There is a critical need for uncertainty.


### Uncertainty Quantification

> Uncertainty quantification (UQ) is the science of quantitative characterization and reduction of uncertainties in both computational and real world applications. It tries to determine how likely certain outcomes are if some aspects of the system are not exactly known.

* Interaction between physical and virtual worlds of major interest for Amazon.

We will to illustrate different concepts of [Uncertainty Quantification](https://en.wikipedia.org/wiki/Uncertainty_quantification) (UQ) and the role that Gaussian processes play in this field. Based on a simple simulator of a car moving between a valley and a mountain, we are going to illustrate the following concepts:

- **Systems emulation**. Many real world decisions are based on simulations that can be computationally very demanding. We will show how simulators can be replaced by *emulators*: Gaussian process models fitted on a few simulations that can be used to replace the *simulator*. Emulators are cheap to compute, fast to run, and always provide ways to quantify the uncertainty of how precise they are compared the original simulator.

- **Emulators in optimization problems**. We will show how emulators can be used to optimize black-box functions that are expensive to evaluate. This field is also called Bayesian Optimization and has gained an increasing relevance in machine learning as emulators can be used to optimize computer simulations (and machine learning algorithms) quite efficiently.

- **Multi-fidelity emulation methods**. In many scenarios we have simulators of different quality about the same measure of interest. In these cases the goal is to merge all sources of information under the same model so the final emulator is cheaper and more accurate than an emulator fitted only using data from the most accurate and expensive simulator.


### Example: Formula One Racing

* Designing an F1 Car requires CFD, Wind Tunnel, Track Testing etc.

* How to combine them?


### Mountain Car Simulator

To illustrate the above mentioned concepts we we use the [mountain car simulator](https://github.com/openai/gym/wiki/MountainCarContinuous-v0). This simulator is widely used in machine learning to test reinforcement learning algorithms. The goal is to define a control policy on a car whose objective is to climb a mountain. Graphically, the problem looks as follows:

<img class="" src="./slides/diagrams/uq/mountaincar.png" width="negate" align="" style="background:none; border:none; box-shadow:none;">

The goal is to define a sequence of actions (push the car right or left with certain intensity) to make the car reach the flag after a number $T$ of time steps.

At each time step $t$, the car is characterized by a vector $\inputVector_{t} = (p_t,v_t)$ of states which are respectively the the position and velocity of the car at time $t$. For a sequence of states (an episode), the dynamics of the car is given by



$$\inputVector_{t+1} = \mappingFunction(\inputVector_{t},\textbf{u}_{t})$$



where $\textbf{u}_{t}$ is the value of an action force, which in this example corresponds to push car to the left (negative value) or to the right (positive value). The actions across a full episode are represented in a policy $\textbf{u}_{t} = \pi(\inputVector_{t},\theta)$ that acts according to the current state of the car and some parameters $\theta$. In the following examples we will assume that the policy is linear which allows us to write $\pi(\inputVector_{t},\theta)$ as




$$\pi(\inputVector,\theta)= \theta_0 + \theta_p p + \theta_vv.$$

For $t=1,\dots,T$ now given some initial state $\inputVector_{0}$ and some some values of each $\textbf{u}_{t}$, we can **simulate** the full dynamics of the car for a full episode using [Gym](https://gym.openai.com/envs/). The values of 
$\textbf{u}_{t}$ are fully determined by the parameters of the linear controller.

After each episode of length $T$ is complete, a reward function $R_{T}(\theta)$ is computed. In the mountain car example the reward is computed as 100 for reaching the target of the hill on the right hand side, minus the squared sum of actions (a real negative to push to the left and a real positive to push to the right) from start to goal.  Note that our reward depend on $\theta$ as we make it dependent on the parameters of the linear controller.

### Emulate the Mountain Car

```{.python}
import gym
```
```{.python}
env = gym.make('MountainCarContinuous-v0')
```

Our goal in this section is to find the parameters $\theta$ of the linear controller such that



$$\theta^* = arg \max_{\theta} R_T(\theta).$$ 



In this section, we directly use Bayesian optimization to solve this problem. We will use [GPyOpt](https://sheffieldml.github.io/GPyOpt/) so we first define the objective function:

```{.python}
import mountain_car as mc
import GPyOpt
```

```{.python}
obj_func = lambda x: mc.run_simulation(env, x)[0]
objective = GPyOpt.core.task.SingleObjective(obj_func)
```

For each set of parameter values of the linear controller we can run an episode of the simulator (that we fix to have a horizon of $T=500$) to generate the reward. Using as input the parameters of the controller and as outputs the rewards we can build a Gaussian process emulator of the reward. 

We start defining the input space, which is three-dimensional:

```{.python}
## --- We define the input space of the emulator

space= [{'name':'postion_parameter', 'type':'continuous', 'domain':(-1.2, +1)},
        {'name':'velocity_parameter', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space = GPyOpt.Design_space(space=space)
```

Now we initizialize a Gaussian process emulator.

```{.python}
model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
```

In Bayesian optimization an acquisition function is used to balance exploration and exploitation to evaluate new locations close to the optimum of the objective. In this notebook we select the expected improvement (EI). For further details have a look to the review paper of [Shahriari et al (2015)](http://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf).

```{.python}
aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)
acquisition = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator = GPyOpt.core.evaluators.Sequential(acquisition) # Collect points sequentially, no parallelization.
```

To initalize the model we start sampling some initial points (25) for the linear controler randomly.


```{.python}
from GPyOpt.experiment_design.random_design import RandomDesign
```
```{.python}
n_initial_points = 25
random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(n_initial_points)
```

Before we start any optimization, lets have a look to the behavior of the car with the first of these initial points that we have selected randomly.

```{.python}
import numpy as np
```

```{.python}
random_controller = initial_design[0,:]
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(random_controller), render=True)
anim=mc.animate_frames(frames, 'Random linear controller')
```

```{.python}
from IPython.core.display import HTML
```



```{.python}
mc.save_frames(frames, 
                  diagrams='./slides/diagrams/uq', 
				  filename='mountain_car_random.html')
```



<iframe src="./slides/diagrams/uq/mountain_car_random.html" width="1024" height="768" allowtransparency="true" frameborder="0">
</iframe>


As we can see the random linear controller does not manage to push the car to the top of the mountain. Now, let's optimize the regret using Bayesian optimization and the emulator for the reward. We try 50 new parameters chosen by the EI.

```{.python}
max_iter = 50
bo = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective, acquisition, evaluator, initial_design)
bo.run_optimization(max_iter = max_iter )
```

Now we visualize the result for the best controller that we have found with Bayesian optimization.

```{.python}
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller after 50 iterations of Bayesian optimization')
```



```{.python}
mc.save_frames(frames, 
                  diagrams='./slides/diagrams/uq', 
				  filename='mountain_car_simulated.html')
```



<iframe src="./slides/diagrams/uq/mountain_car_simulated.html" width="1024" height="768" allowtransparency="true" frameborder="0">
</iframe>

he car can now make it to the top of the mountain! Emulating the reward function and using the EI helped as to find a linear controller that solves the problem.

### Data Efficient Emulation



In the previous section we solved the mountain car problem by directly emulating the reward but no considerations about the dynamics $\inputVector_{t+1} = \mappingFunction(\inputVector_{t},\textbf{u}_{t})$ of the system were made. Note that we had to run 75 episodes of 500 steps each to solve the problem, which required to call the simulator $500\times 75 =37500$ times. In this section we will show how it is possible to reduce this number by building an emulator for $f$ that can later be used to directly optimize the control.

The inputs of the model for the dynamics are the velocity, the position and the value of the control so create this space accordingly.

```{.python}
import gym
```
```{.python}
env = gym.make('MountainCarContinuous-v0')
```

```{.python}
import GPyOpt
```
```{.python}
space_dynamics = [{'name':'position', 'type':'continuous', 'domain':[-1.2, +0.6]},
                  {'name':'velocity', 'type':'continuous', 'domain':[-0.07, +0.07]},
                  {'name':'action', 'type':'continuous', 'domain':[-1, +1]}]
design_space_dynamics = GPyOpt.Design_space(space=space_dynamics)
```

The outputs are the velocity and the position. Indeed our model will capture the change in position and velocity on time. That is, we will model


$$\Delta v_{t+1} = v_{t+1} - v_{t}$$

$$\Delta x_{t+1} = p_{t+1} - p_{t}$$



with Gaussian processes with prior mean $v_{t}$ and $p_{t}$ respectively. As a covariance function, we use a Matern52.  We need therefore two models to capture the full dynamics of the system.

```{.python}
position_model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
velocity_model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
```

Next, we sample some input parameters and use the simulator to compute the outputs. Note that in this case we are not running the full episodes, we are just using the simulator to compute $\inputVector_{t+1}$ given $\inputVector_{t}$ and $\textbf{u}_{t}$.

```{.python}
import numpy as np
from GPyOpt.experiment_design.random_design import RandomDesign
import mountain_car as mc
```

```{.python}
### --- Random locations of the inputs
n_initial_points = 500
random_design_dynamics = RandomDesign(design_space_dynamics)
initial_design_dynamics = random_design_dynamics.get_samples(n_initial_points)
```

```{.python}
### --- Simulation of the (normalized) outputs
y = np.zeros((initial_design_dynamics.shape[0], 2))
for i in range(initial_design_dynamics.shape[0]):
    y[i, :] = mc.simulation(initial_design_dynamics[i, :])

# Normalize the data from the simulation
y_normalisation = np.std(y, axis=0)
y_normalised = y/y_normalisation
```



In general we might use much smarter strategies to design our emulation of the simulator. For example, we could use the variance of the predictive distributions of the models to collect points using uncertainty sampling, which will give us a better coverage of the space. For simplicity, we move ahead with the 500 randomly selected points. 

Now that we have a data set, we can update the emulators for the location and the velocity.

```{.python}
position_model.updateModel(initial_design_dynamics, y[:, [0]], None, None)
velocity_model.updateModel(initial_design_dynamics, y[:, [1]], None, None)
```

We can now have a look to how the emulator and the simulator match. First, we show a contour plot of the car aceleration for each pair of can position and velocity. You can use the bar bellow to play with the values of the controler to compare the emulator and the simulator.

```{.python}
from IPython.html.widgets import interact
```

```{.python}
control = mc.plot_control(velocity_model)
interact(control.plot_slices, control=(-1, 1, 0.05))
```

<!---->

We can see how the emulator is doing a fairly good job approximating the simulator. On the edges, however, it struggles to captures the dynamics of the simulator. 

Given some input parameters of the linear controlling, how do the dynamics of the emulator and simulator match? In the following figure we show the position and velocity of the car for the 500 time steps of an episode in which the parameters of the linear controller have been fixed beforehand. The value of the input control is also shown.

```{.python}
controller_gains = np.atleast_2d([0, .6, 1])  # change the valus of the linear controller to observe the trayectories.
```

```{.python}
mc.emu_sim_comparison(env, controller_gains, [position_model, velocity_model], 
                      max_steps=500, diagrams='./slides/diagrams/uq')
```



<object class="svgplot" align="" data="./slides/diagrams/uq/emu_sim_comparison.svg"></object>

We now make explicit use of the emulator, using it to replace the simulator and optimize the linear controller. Note that in this optimization, we don't need to query the simulator anymore as we can reproduce the full dynamics of an episode using the emulator. For illustrative purposes, in this example we fix the initial location of the car. 

We define the objective reward function in terms of the simulator.

```{.python}
### --- Optimize control parameters with emulator
car_initial_location = np.asarray([-0.58912799, 0]) 

### --- Reward objective function using the emulator
obj_func_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_emulator = GPyOpt.core.task.SingleObjective(obj_func_emulator)
```

And as before, we use Bayesian optimization to find the best possible linear controller.

```{.python}
### --- Elements of the optimization that will use the multi-fidelity emulator
model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
```

The design space is the three continuous variables that make up the linear controller.

```{.python}
space= [{'name':'linear_1', 'type':'continuous', 'domain':(-1/1.2, +1)},
        {'name':'linear_2', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space         = GPyOpt.Design_space(space=space)
aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)

random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(25)
```

We set the acquisition function to be expected improvement using ```GPyOpt```.

```{.python}
acquisition          = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator            = GPyOpt.core.evaluators.Sequential(acquisition)
```

```{.python}
bo_emulator = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective_emulator, acquisition, evaluator, initial_design)
bo_emulator.run_optimization(max_iter=50)
```

```{.python}
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo_emulator.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller using the emulator of the dynamics')
```

```{.python}
from IPython.core.display import HTML
```



```{.python}
mc.save_frames(frames, 
                  diagrams='./slides/diagrams/uq', 
				  filename='mountain_car_emulated.html')
```




<iframe src="./slides/diagrams/uq/mountain_car_emulated.html" width="1024" height="768" allowtransparency="true" frameborder="0">
</iframe>



And the problem is again solved, but in this case we have replaced the simulator of the car dynamics by a Gaussian process emulator that we learned by calling the simulator only 500 times. Compared to the 37500 calls that we needed when applying Bayesian optimization directly on the simulator this is a great gain.

In some scenarios we have simulators of the same environment that have different fidelities, that is that reflect with different level of accuracy the dynamics of the real world. Running simulations of the different fidelities also have a different cost: hight fidelity simulations are more expensive the cheaper ones. If we have access to these simulators we can combine high and low fidelity simulations under the same model.

So let's assume that we have two simulators of the mountain car dynamics, one of high fidelity (the one we have used) and another one of low fidelity. The traditional approach to this form of multi-fidelity emulation is to assume that

$$\mappingFunction_i\left(\inputVector\right) = \rho\mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)$$

where $\mappingFunction_{i-1}\left(\inputVector\right)$ is a low fidelity simulation of the problem of interest and $\mappingFunction_i\left(\inputVector\right)$ is a higher fidelity simulation. The function $\delta_i\left(\inputVector \right)$ represents the difference between the lower and higher fidelity simulation, which is considered additive. The additive form of this covariance means that if $\mappingFunction_{0}\left(\inputVector\right)$ and $\left\{\delta_i\left(\inputVector \right)\right\}_{i=1}^m$ are all Gaussian processes, then the process over all fidelities of simuation will be a joint Gaussian process.

But with Deep Gaussian processes we can consider the form 



$$\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),$$

where the low fidelity representation is non linearly transformed by $\mappingFunctionTwo(\cdot)$ before use in the process. This is the approach taken in @Perdikaris:multifidelity17. But once we accept that these models can be composed, a highly flexible framework can emerge. A key point is that the data enters the model at different levels, and represents different aspects. For example these correspond to the two fidelities of the mountain car simulator.

We start by sampling both of them at 250 random input locations.

```{.python}
import gym
```
```{.python}
env = gym.make('MountainCarContinuous-v0')
```

```{.python}
import GPyOpt
```
```{.python}
### --- Collect points from low and high fidelity simulator --- ###

space = GPyOpt.Design_space([
        {'name':'position', 'type':'continuous', 'domain':(-1.2, +1)},
        {'name':'velocity', 'type':'continuous', 'domain':(-0.07, +0.07)},
        {'name':'action', 'type':'continuous', 'domain':(-1, +1)}])

n_points = 250
random_design = GPyOpt.experiment_design.RandomDesign(space)
x_random = random_design.get_samples(n_points)
```

Next, we evaluate the high and low fidelity simualtors at those locations.

```{.python}
import numpy as np
import mountain_car as mc
```

```{.python}
d_position_hf = np.zeros((n_points, 1))
d_velocity_hf = np.zeros((n_points, 1))
d_position_lf = np.zeros((n_points, 1))
d_velocity_lf = np.zeros((n_points, 1))

# --- Collect high fidelity points
for i in range(0, n_points):
    d_position_hf[i], d_velocity_hf[i] = mc.simulation(x_random[i, :])

# --- Collect low fidelity points  
for i in range(0, n_points):
    d_position_lf[i], d_velocity_lf[i] = mc.low_cost_simulation(x_random[i, :])
```
	
It is time to build the multi-fidelity model for both the position and the velocity.

As we did in the previous section we use the emulator to optimize the simulator. In this case we use the high fidelity output of the emulator.

```{.python}
### --- Optimize controller parameters 
obj_func = lambda x: mc.run_simulation(env, x)[0]
obj_func_emulator = lambda x: mc.run_emulation([position_model, velocity_model], x, car_initial_location)[0]
objective_multifidelity = GPyOpt.core.task.SingleObjective(obj_func)
```

And we optimize using Bayesian optimzation.

```{.python}
from GPyOpt.experiment_design.random_design import RandomDesign
```

```{.python}
model = GPyOpt.models.GPModel(optimize_restarts=5, verbose=False, exact_feval=True, ARD=True)
space= [{'name':'linear_1', 'type':'continuous', 'domain':(-1/1.2, +1)},
        {'name':'linear_2', 'type':'continuous', 'domain':(-1/0.07, +1/0.07)},
        {'name':'constant', 'type':'continuous', 'domain':(-1, +1)}]

design_space = GPyOpt.Design_space(space=space)
aquisition_optimizer = GPyOpt.optimization.AcquisitionOptimizer(design_space)

n_initial_points = 25
random_design = RandomDesign(design_space)
initial_design = random_design.get_samples(n_initial_points)
acquisition = GPyOpt.acquisitions.AcquisitionEI(model, design_space, optimizer=aquisition_optimizer)
evaluator = GPyOpt.core.evaluators.Sequential(acquisition)
```

```{.python}
bo_multifidelity = GPyOpt.methods.ModularBayesianOptimization(model, design_space, objective_multifidelity, acquisition, evaluator, initial_design)
bo_multifidelity.run_optimization(max_iter=50)
```

```{.python}
_, _, _, frames = mc.run_simulation(env, np.atleast_2d(bo_multifidelity.x_opt), render=True)
anim=mc.animate_frames(frames, 'Best controller with multi-fidelity emulator')
```

```{.python}
from IPython.core.display import HTML
```



```{.python}
mc.save_frames(frames, 
                  diagrams='./slides/diagrams/uq', 
				  filename='mountain_car_multi_fidelity.html')
```



<iframe src="./slides/diagrams/uq/mountain_car_multi_fidelity.html" width="1024" height="768" allowtransparency="true" frameborder="0">
</iframe>


And problem solved! We see how the problem is also solved with 250 observations of the high fidelity simulator and 250 of the low fidelity simulator.




### Conclusion

* Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.


### Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
* [Natural vs Artifical Intelligence](http://inverseprobability.com/2018/02/06/natural-and-artificial-intelligence)
* [Mike Jordan's Medium Post](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7)
