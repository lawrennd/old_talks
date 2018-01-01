### Graphical Models {data-transition="None"}

* Represent joint distribution through *conditional dependencies*.

* E.g. Markov chain

$$p(\dataVector) = p(\dataScalar_\numData | \dataScalar_{\numData-1}) p(\dataScalar_{\numData-1}|\dataScalar_{\numData-2}) \dots p(\dataScalar_{2} | \dataScalar_{1})$$


\includesvg{../slides/diagrams/ml/markov.svg}

### {data-transition="None"}

Predict Perioperative Risk of Clostridium Difficile Infection Following Colon Surgery

\includeimg{../slides/diagrams/bayes-net-diagnosis.png}{40%}{negate}

[@Steele:predictive12]
