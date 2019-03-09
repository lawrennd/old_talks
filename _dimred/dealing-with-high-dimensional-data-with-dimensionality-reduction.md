---
title: Dealing with High Dimensional Data with Dimensionality Reduction
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Machine Learning Group, University of Manchester
  twitter: lawrennd
  url: http://inverseprobability.com
- family: Barker
  given: Jon
  institute: SpandH, University of Sheffield
date: 2009-09-06
venue: Interspeech Tutorial 2009
published: 2009-09-06
---

\include{talk-macros.tex}


\begin{frame}
\frametitle{Online Resources}

\textbf{All source code and slides are available online}
\begin{itemize}
\item Tutorial homepage is 

\begin{itemize}
\item \url{http://www.cs.man.ac.uk/~neill/interspeech_tutorial.html}.
\item MATLAB/Octave commands used for examples given in \texttt{typewriter
font}.
\end{itemize}
\end{itemize}
\end{frame}

\include{_dimred/includes/thinking.md}
\include{_dimred/includes/linear.md}
\include{_dimred/includes/spectral.md}
\include{_dimred/includes/generative.md}
\include{_dimred/includes/gplvm.md}

### Conclusions

### References

\include{_dimred/includes/supplementary.md}

\section{Thinking in High Dimensions}
\include{_dimred/tex/talks/thinking}
\section{Probabilistic Linear Dimensionality Reduction}
\include{_dimred/tex/talks/linear}
\section{Spectral Methods}
\include{_dimred/tex/talks/spectral}
\section{Density Networks and GTM}
\include{_dimred/tex/talks/generative}
\section{Dual Probabilistic PCA and GP-LVM}
\include{_dimred/tex/talks/gplvm}
\section{Conclusions}
\include{_dimred/tex/talks/conclusions}

\begin{frame}[allowframebreaks]
  \frametitle{References}

  {\tiny \bibliographystyle{pdf_abbrvnat}
    \bibliography{lawrence,other,zbooks}
  }
  
  
\end{frame}
\appendix
\section{Probabilistic PCA Proof}{_dimred/tex/talks/supplementary}

\thanks

\references
