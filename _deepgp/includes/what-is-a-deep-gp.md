\include{../_deepgp/includes/deep-nn.md}

### Mathematically 

$$
\begin{align}
    \hiddenVector_{1} &= \basisFunction\left(\mappingMatrix_1 \inputVector\right)\\
    \hiddenVector_{2} &=  \basisFunction\left(\mappingMatrix_2\hiddenVector_{1}\right)\\
    \hiddenVector_{3} &= \basisFunction\left(\mappingMatrix_3 \hiddenVector_{2}\right)\\
    \dataVector &= \mappingVector_4 ^\top\hiddenVector_{3}
\end{align}
$$

### Overfitting 

-   Potential problem: if number of nodes in two adjacent layers is big,
    corresponding $\mappingMatrix$ is also very big and there is the
    potential to overfit.

-   Proposed solution: “dropout”.

-   Alternative solution: parameterize $\mappingMatrix$ with its SVD.
    $$\mappingMatrix = \eigenvectorMatrix\eigenvalueMatrix\eigenvectwoMatrix^\top$$
    or $$\mappingMatrix = \eigenvectorMatrix\eigenvectwoMatrix^\top$$
    where if $\mappingMatrix \in \Re^{k_1\times k_2}$ then
    $\eigenvectorMatrix\in \Re^{k_1\times q}$ and
    $\eigenvectwoMatrix \in \Re^{k_2\times q}$, i.e. we have a low rank
    matrix factorization for the weights.
	
\plotcode{
fig, ax = plt.subplots(1, 4,figsize=plot.big_wide_figsize)
fontsize=40
q = 3
k1 = 10
k2 = 12
plot.blank_canvas(ax[3])
ax[3].text(0.145, 0.55, r'$\times$', 
           horizontalalignment='center',
           fontsize=fontsize)
ax[3].text(0.47, 0.55, r'$=$', 
           horizontalalignment='center',
           fontsize=fontsize)
ax[3].text(0.075, 0.55, r'$\mathbf{U}$', 
           horizontalalignment='center',
           fontsize=fontsize, color=[1, 1, 1])
ax[3].text(0.3, 0.55, r'$\mathbf{V}^\top$', 
           horizontalalignment='center',
           fontsize=fontsize, color=[1, 1, 1])
ax[3].text(0.65, 0.55, r'$\mathbf{W}$', 
           horizontalalignment='center',
           fontsize=fontsize, color=[1, 1, 1])
U = np.random.randn(k1, q)
VT = np.random.randn(q, k2)
basewidth = 0.15
ax[0].set_position([0.0, 0.15, basewidth, basewidth/q*k1])
plot.matrix(U, ax=ax[0], type='image')
ax[1].set_position([0.0, 0.5, basewidth/q*k2, basewidth])
ax[1].set_aspect('equal')
plot.matrix(VT, ax=ax[1], type='image')
ax[2].set_position([0.35, 0.15, basewidth/q*k2, basewidth/q*k1])
plot.matrix(np.dot(U,VT), ax=ax[2], type='image')
ax[3].set_frame_on(True)
ax[3].axes.get_yaxis().set_visible(True)
mlai.write_figure(figure=fig, filename='../../slides/diagrams/wisuvt.svg')
}

### Low Rank Approximation

\includesvg{../../slides/diagrams/wisuvt.svg}

\plotcode{plot.deep_nn_bottleneck(diagrams='../../slides/diagrams/deepgp')}

### Deep Neural Network

\includesvg{../../slides/diagrams/deepgp/deep-nn-bottleneck2.svg}

### What is a Deep Gaussian Process?

* Function Composition
 (Introduce as stacked processes ... check Oxford Talk fromw ay back.

* Stochastic Process Composition

* Geoff Hinton's view of Deep Learning

\include{../../_deepgp/includes/deep-nn-gp.md}

<!--Deep Gaussian Process Models-->

\include{../../_deepgp/includes/deeptheory.md}

<!--Bayesian GP-LVM-->


<!--include{../../_gplvm/includes/ard_gplvm.md} -->
<!-- \include{../../_gplvm/includes/bayes_gplvm_intro.md} -->
<!-- \include{../../_gplvm/includes/variational_bayes_gplvm_long.md} -->

<!-- \include{../../_gp/includes/gp_big_data_technical.md} -->
<!--\include{../../_gp/includes/gp_big_data.md}-->

\include{../../_deepgp/includes/deep_gps.md}

\include{../../_deepgp/includes/stack-gp-intro.md}
\include{../../_deepgp/includes/stacked-pca.md}
\include{../../_deepgp/includes/stacked-gp.md}
\include{../../_deepgp/includes/deep-pathologies.md}
\include{../../_deepgp/includes/deep-results.md}
\include{../../_deepgp/includes/deep_step_function.md}
\include{../../_deepgp/includes/deep_loop_detection.md}

\include{../../_health/includes/deep-health-model.md}


<!--Conclusions-->

<!-- \include{../../_gplvm/includes/ard_model.md} -->
<!-- \include{../../_gplvm/includes/ard_results.md} -->

<!--Gaussian Process Dynamical Systems-->

<!-- \include{../../_gplvm/includes/gpds.md} -->

<!--Shared GP-LVM-->

<!-- \include{../../_gplvm/includes/mrd_gplvm.md} -->

### What Can We Do that Google Can’t?

-   Google’s resources give them access to volumes of data (or Facebook,
    or Microsoft, or Amazon).

-   Is there anything for Universities to contribute?

-   Assimilation of multiple views of the patient: each perhaps from a
    different patient.

-   This may be done by small companies (with support of Universities).

-   A Facebook app for your personalised health.

-   These methodologies are part of that picture.

\include{../../_health/includes/deep_health_model.md}
\include{../../_health/includes/deep_health_rangers.md}
