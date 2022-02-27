\ifndef{mxfusionSoftware}
\define{mxfusionSoftware}
\editme

talk-macros.gpp}l/includes/mxfusion-intro.md}

\subsection{MxFusion}

\slides{
* Targeted at challenges we face in emulation. 
* Composition of Gaussian processes (Deep GPs)
* Combining GPs with neural networks.
* Example [PPCA Tutorial](https://github.com/amzn/MXFusion/blob/master/examples/notebooks/ppca_tutorial.ipynb).
}

\subsection{Why another framework?}

\slides{
* Existing libraries had either:
    * Probabilistic modelling with rich, flexible models and universal inference or
    * Specialized, efficient inference over a subset of models

**We need both**
}

\subsection{Key Requirements}
\slides{
* Integration with deep learning
* Flexiblility
* Scalability
* Specialized inference and models support
    * Bayesian Deep Learning methods
    * Rapid prototyping and software re-use
    * GPUs, specialized inference methods
}

\newslide{Modularity}
\slides{
 * Specialized Inference
 * Composability (tinkerability)
    * Better leveraging of expert expertise
}

\notes{Specialized inference methods + models, without requiring users to reimplement nor understand them every time. Leverage expert knowledge. Efficient inference, flexible framework.  Existing frameworks either did one or the other: flexible, or efficient.}

\subsection{What does it look like?}

**Modelling**

**Inference**

\newslide{Modelling}

\newslide{Directed Graphs}
\slides{
* Variable
* Function
* Distribution
}

\newslide{Example}

```python
m = Model()
m.mu = Variable()
m.s = Variable(transformation=PositiveTransformation())
m.Y = Normal.define_variable(mean=m.mu, variance=m.s)
```

\newslide{3 primary components in modeling}

* Variable
* Distribution
* Function 

\newslide{2 primary methods for models}

* `log_pdf`
* `draw_samples`

\newslide{Inference: Two Classes}

* Variational Inference
* MCMC Sampling (*soon*)
Built on MXNet Gluon (imperative code, not static graph)

\newslide{Example}

```python
infr = GradBasedInference(inference_algorithm=MAP(model=m, observed=[m.Y]))
infr.run(Y=data)
```

\newslide{Modules}

* Model + Inference together form building blocks.
    * Just doing modular modeling with universal inference doesn't really scale, need specialized inference methods for specialized modelling objects like non-parametrics.

\endif
