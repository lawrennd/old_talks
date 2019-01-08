---
title: Gaussian Processes
abstract: >
  Classical machine learning and statistical approaches to learning, such as neural networks and linear regression, assume a parametric form for functions. Gaussian process models are an alternative approach that assumes a probabilistic prior over functions. This brings benefits, in that uncertainty of function estimation is sustained throughout inference, and some challenges: algorithms for fitting Gaussian processes tend to be more complex than parametric models. 
  
  In these sessions I will introduce Gaussian processes and explain why sustaining uncertainty is important. We’ll then look at some extensions of Gaussian process models, in particular composition of Gaussian processes, or deep Gaussian processes.
ipynb: 2019-01-09-gaussian-processes.ipynb
pdfnotes: 2019-01-09-gaussian-processes.notes.pdf
reveal: 2019-01-09-gaussian-processes.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2019-01-09
venue: MLSS, Stellenbosch, South Africa
transition: None
---

\include{talk-macros.tex}
\include{_gp/includes/gp-book.md}
\include{_gp/includes/what-is-a-gp.md}

<!--include{_gp/includes/gp-optimize.md}-->
\include{_gp/includes/gpss.md}
\include{_gp/includes/gpy.md}
\include{_gp/includes/other-software.md}
\include{_ml/includes/mxfusion-intro.md}

\subsection{Acknowledgments}

Stefanos Eleftheriadis, John Bronskill, Hugh Salimbeni, Rich Turner, Zhenwen Dai, Javier Gonzalez, Andreas Damianou, Mark Pullin.


\newslide{Thanks!}

\slides{
* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
}

\subsection{References}





TODO: Additive Covariance
TODO: multpilicitabe covariance
TODO: PARAMETER OPTIMIZATION
