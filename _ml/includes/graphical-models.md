### Graphical Models

* Represent joint distribution through *conditional dependencies*.

* E.g. Markov chain

$$p(\dataVector) = p(\dataScalar_\numData | \dataScalar_{\numData-1}) p(\dataScalar_{\numData-1}|\dataScalar_{\numData-2}) \dots p(\dataScalar_{2} | \dataScalar_{1})$$


<object class="svgplot" data="../slides/diagrams/markov.svg"></object>

NADE

### Shared LVM

<object class="svgplot" data="../slides/diagrams/shared.svg"></object>
