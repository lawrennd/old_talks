\subsection{MxFusion}

\columns{* Work by Eric Meissner and Zhenwen Dai.
* Probabilistic programming.
* Available on [Github](https://github.com/amzn/mxfusion)}{\includeimg{../slides/diagrams/mxfusion-logo.png}}{70%}{30%}

\subsection{MxFusion}

\slides{
* Targeted at challenges we face in emulation. 
* Composition of Gaussian processes (Deep GPs)
* Combining GPs with neural networks.
* Example [PPCA Tutorial](https://github.com/amzn/MXFusion/blob/master/examples/notebooks/ppca_tutorial.ipynb).
}

\subsection{Why another one?}

\slides{
Existing libraries had either:
* Probabilistic modelling with rich, flexible models and universal inference or
* Specialized, efficient inference over a subset of models

**We needed both**
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
m.s =
Variable(transformation=PositiveTransformation())
m.Y =
Normal.define_variable(mean=m.mu, variance=m.s)
```

\newslide{}

* 3 primary components in modeling
   * Variable
   * Distribution
   * Function 
* 2 primary methods for models 
   * log_pdf
   * draw_samples

\newslide{Inference: Two Classes}

* Variational Inference
* MCMC Sampling (*soon*)
Built on MXNet Gluon (imperative code, not static graph)

\newslide{Example}

```
infr = GradBasedInference(inference_algorithm=MAP(model=m, observed=[m.Y]))
infr.run(Y=data)
```

```python
infr = GradBasedInference(inference_algorithm=MAP(model=m, observed=[m.Y]))
infr.run(Y=data)
```

\newslide{Modules}

* Model + Inference together form building blocks.
    * Just doing modular modeling with universal inference doesn't really scale, need specialized inference methods for specialized modelling objects like non-parametrics.
