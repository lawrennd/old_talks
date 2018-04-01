<!--frame start-->
### Parametric but Non-parametric

-   Augment with a vector of *inducing* variables, $\inducingVector$.

-   Form a variational lower bound on true likelihood.

-   Bound *factorizes* given inducing variables.

-   Inducing variables appear in bound similar to parameters in a
    parametric model.

-   *But* number of inducing variables can be changed at run time.

<!--frame end-->
<!--frame start-->
### Inducing Variable Approximations

-   Date back to
    [\scriptsize[@Williams:nystrom00; @Smola:sparsegp00; @Csato:sparse02; @Seeger:fast03; @Snelson:pseudo05]]{}.
    See [\scriptsize[@Quinonero:unifying05]]{} for a review.

-   We follow variational perspective of
    [\scriptsize[@Titsias:variational09]]{}.

-   This is an augmented variable method, followed by a collapsed
    variational approximation
    [\scriptsize[@King:klcorrection06; @Hensman:fast12]]{}.

<!--frame end-->
<!--frame failure start-->

### Augmented Variable Model: Not Wrong but Useful?

  \begin{columns}
    \column{0.6\textwidth}
    \only<1-2>{Augment standard model with a set of $\numInducing$ new inducing variables, $\inducingVector$.}
    \only<3>{\textbf{Important:} Ensure inducing variables are \emph{also} Kolmogorov consistent (we have $\numInducing^\ast$ other inducing variables we are not \emph{yet} using.)}
    \only<4>{Assume that relationship is through $\mappingFunctionVector$ (represents `fundamentals'---push Kolmogorov consistency up to here).}
    \only<5>{Convenient to assume factorization (\emph{doesn't} invalidate model---think delta function as worst case).}
    \only<6-7>{Focus on integral over $\mappingFunctionVector$.}
    \only<1>{\[
      p(\dataVector) = \int p(\dataVector, \inducingVector) \text{d}\inducingVector 
      \]}
    \only<2>{\[
      p(\dataVector) = \int p(\dataVector| \inducingVector) p(\inducingVector)\text{d}\inducingVector 
      \]}
    \only<3>{\[
      p(\inducingVector) = \int p(\inducingVector, \inducingVector^\ast) \text{d}\inducingVector^\ast 
      \]}
    \only<4>{\[
      p(\dataVector) = \int p(\dataVector| \mappingFunctionVector) p(\mappingFunctionVector|\inducingVector) p(\inducingVector) \text{d}\mappingFunctionVector \text{d}\inducingVector 
      \]}
    \only<5>{\[
      p(\dataVector) = \int \prod_{i=1}^\numData p(\dataScalar_i| \mappingFunction_i) p(\mappingFunctionVector|\inducingVector) p(\inducingVector) \text{d}\mappingFunctionVector \text{d}\inducingVector 
      \]}
    \only<6>{\[
      p(\dataVector) = \int \int \prod_{i=1}^\numData p(\dataScalar_i| \mappingFunction_i) p(\mappingFunctionVector|\inducingVector) \text{d}\mappingFunctionVector p(\inducingVector)  \text{d}\inducingVector 
      \]}
    \only<7>{\[
      p(\dataVector|\inducingVector) = \int \prod_{i=1}^\numData p(\dataScalar_i| \mappingFunction_i) p(\mappingFunctionVector|\inducingVector) \text{d}\mappingFunctionVector  
      \]}
    %\only<3>{Focus on bounding $p(\dataVector|\inducingVector)$}
    \column[c]{0.4\textwidth}
    \begin{center}
      \begin{tikzpicture}
        
        % Define nodes
        \draw<1-4> node[obs] (y) {$\dataVector$};
        \draw<4> node[latent, above=of y] (f) {$\mappingFunctionVector$};
        \draw<5-> node[obs] (y) {$\dataScalar_i$};
        \draw<5-> node[latent, above=of y] (f) {$\mappingFunction_i$};
        \draw<2> node[latent, above=of y] (u) {$\inducingVector$};
        \draw<3> node[latent, above left=of y] (u) {$\inducingVector$};
        \draw<3> node[latent, above right=of y] (ustar) {$\inducingVector^\ast$};
        \draw<4-6> node[latent, above=of f] (u) {$\inducingVector$};
        \draw<4-7> node[latent, above right=of f, draw=gray] (ustar) {\color{gray}$\inducingVector^\ast$};
        \draw<7-> node[const, above=of f] (u) {$\inducingVector$};
        
        % Connect the nodes
        \draw<2-3> [->] (u) to (y);%
        \draw<3> [->] (ustar) to (y);%
        \draw<3> [-] (ustar) to (u);%
        \draw<4-> [-, draw=gray] (ustar) to (u);%
        \draw<4-> [->, draw=gray,color=gray] (ustar) to (f);%
        \draw<4-> [->] (f) to (y);%
        \draw<4-> [->] (u) to (f);%

        \only<5->{\plate[inner sep=10pt] {fy} {(f)(y)} {$i=1\dots\numData$} ;}
        
      \end{tikzpicture}
    \end{center}
  \end{columns}
  

<!--frame failure end-->

