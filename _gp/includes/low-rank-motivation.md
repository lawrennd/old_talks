\ifndef{lowRankMotivation}
\define{lowRankMotivation}
\editme

\newslide{Low Rank Motivation}

\slides{
* Inference in a GP has the following demands:

  ------------- ---------------------
    Complexity: $\bigO(\numData^3)$
       Storage: $\bigO(\numData^2)$
  ------------- ---------------------

* Inference in a low rank GP has the following demands:

  ------------- ---------------------------------
    Complexity: $\bigO(\numData\numInducing^2)$
       Storage: $\bigO(\numData\numInducing)$
  ------------- ---------------------------------

  where $\numInducing$ is a user chosen parameter.

\smalltext{@Snelson:pseudo05,@Quinonero:unifying05,@Lawrence:larger07,@Titsias:variational09,@Thang:unifying17}
}
\notes{Inference in a Gaussian process has computational complexity of $\bigO(\numData^3)$ and storage demands of $\bigO(\numData^2)$. This is too large for many modern data sets. 

Low rank approximations allow us to work with Gaussian processes with computational complexity of $\bigO(\numData\numInducing^2)$ and storage demands of $\bigO(\numData\numInducing)$, where $\numInducing$ is a user chosen parameter.

In machine learning, low rank approximations date back to @Smola:sparsegp00, @Williams:nystrom00, who considered the Nyström approximation and @Csato:sparse02;@Csato:thesis02 who considered low rank approximations in the context of on-line learning. Selection of active points for the approximation was considered by @Seeger:fast03 and  @Snelson:pseudo05 first proposed that the active set could be optimized directly. Those approaches were reviewed by @Quinonero:unifying05 under a unifying likelihood approximation perspective. General rules for deriving the maximum likelihood for these sparse approximations were given in @Lawrence:larger07. 

Modern variational interpretations of these low rank approaches were first explored in @Titsias:variational09. A more modern summary which considers each of these approximations as an $\alpha$-divergence is given by @Thang:unifying17.}

\endif

