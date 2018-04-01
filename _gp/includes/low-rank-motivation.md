### Low Rank Motivation {data-transition="None"}

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

[@Snelson:pseudo05,@Quinonero:unifying05,@Lawrence:larger07,@Titsias:variational09]

