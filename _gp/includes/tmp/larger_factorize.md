<!--frame start-->
### Factorizing Likelihoods

-   If the likelihood, $p(\dataVector|\mappingFunctionVector)$,
    factorizes \only<1-2>{\[
          p(\dataVector|\inducingVector) \geq \exp \int p(\mappingFunctionVector|\inducingVector){\only<2>{\color{\blueColor} \log \prod_{i=1}^\numData}}\only<1>{\log \prod_{i=1}^\numData} p(\dataScalar_i|\mappingFunction_i)\text{d}\mappingFunctionVector.
          \]} \only<3-4>{\[
          p(\dataVector|\inducingVector) \geq \exp \only<4>{{\color{\blueColor}\int p(\mappingFunctionVector|\inducingVector) \sum_{i=1}^{\numData}}\log} \only<3>{\int p(\mappingFunctionVector|\inducingVector) {\color{\blueColor}\sum_{i=1}^{\numData}\log}}  p(\dataScalar_i|\mappingFunction_i)\text{d}\mappingFunctionVector.
          \]} \only<5-6>{\[
          p(\dataVector|\inducingVector) \geq \only<5>{\exp {\color{\blueColor}\sum_{i=1}^{\numData}\int p(\mappingFunction_i|\inducingVector)}} \only<6>{{\color{\blueColor}\exp\sum_{i=1}^{\numData}}\int p(\mappingFunction_i|\inducingVector)}\log p(\dataScalar_i|\mappingFunction_i)\text{d}\mappingFunctionVector.
          \]} \only<7-8>{\[
          p(\dataVector|\inducingVector) \geq {\only<7>{\color{\blueColor}}\prod_{i=1}^\numData \exp} \int p(\mappingFunction_i|\inducingVector) \log p(\dataScalar_i|\mappingFunction_i)\text{d}\mappingFunctionVector.
          \]} \only<9-10>{\[
          p(\dataVector|\inducingVector) \geq \prod_{i=1}^\numData \exp \only<10>{\color{\blueColor}}\expDist{\log p(\dataScalar_i|\mappingFunction_i)}{p(\mappingFunction_i|\inducingVector)}
          \]}

-   &lt;8-&gt; Then the bound factorizes.

-   &lt;10-&gt; Now need a choice of distributions for
    $\mappingFunctionVector$ and $\dataVector|\mappingFunctionVector$
    ...

<!--frame end-->

