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

\newsection{Thinking in High Dimensions}{../../../dimred/tex/talks/thinking}
\newsection{Probabilistic Linear Dimensionality Reduction}{../../../dimred/tex/talks/linear}
\newsection{Spectral Methods}{../../../dimred/tex/talks/spectral}
\newsection{Density Networks and GTM}{../../../dimred/tex/talks/generative}
\newsection{Dual Probabilistic PCA and GP-LVM}{../../../dimred/tex/talks/gplvm}
\newsection{Conclusions}{../../../dimred/tex/talks/conclusions}

\begin{frame}[allowframebreaks]
  \frametitle{References}

  {\tiny \bibliographystyle{pdf_abbrvnat}
    \bibliography{lawrence,other,zbooks}
  }
  
  
\end{frame}
\appendix
\newsection{Probabilistic PCA Proof}{../../../dimred/tex/talks/supplementary}

\end{document}
