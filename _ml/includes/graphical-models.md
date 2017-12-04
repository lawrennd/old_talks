### Graphical Models {data-transition="None"}

* Represent joint distribution through *conditional dependencies*.

* E.g. Markov chain

$$p(\dataVector) = p(\dataScalar_\numData | \dataScalar_{\numData-1}) p(\dataScalar_{\numData-1}|\dataScalar_{\numData-2}) \dots p(\dataScalar_{2} | \dataScalar_{1})$$


<object class="svgplot" data="../slides/diagrams/markov.svg"></object>

### {data-transition="None"}

Predict Perioperative Risk of Clostridium Difficile Infection Following Colon Surgery

<img src="../slides/diagrams/bayes-net-diagnosis.png" class="negate" width="40%" align="center" style="background:none; border:none; box-shadow:none;">

[@Steele:predictive12]
