### Introducing $\inducingVector$ {data-transition="None"}

Take an extra $\numInducing$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$

### Introducing $\inducingVector$ {#introducing-inducingvector data-transition="None"}

\centering![image](./diagrams/cov_inducing_withX.png){height="60%" style="background:none; border:none; box-shadow:none;" align="center"}

<!--frame end-->
<!--frame start-->
### Introducing $\inducingVector$ {#introducing-inducingvector data-transition="None"}

Take and extra $M$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$
$$\begin{aligned}
    p(\dataVector\given\mappingFunctionVector) &= \gaussianDist{\dataVector}{\mappingFunctionVector}{\dataStd^2 \eye}\\
    p(\mappingFunctionVector\given\inducingVector) &= \gaussianDist{\mappingFunctionVector}{ \Kfu\Kuu^{-1}\inducingVector}{ \Ktilde}\\
    p(\inducingVector) &= \gaussianDist{\inducingVector}{ \zerosVector}{\Kuu}
  \end{aligned}$$


###  {data-transition="None"}

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------- --
   [\semitransp $$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ ]{} $$\begin{align}   <img src="./diagrams/nomenclature4" width="90%" style="background:none; border:none; box-shadow:none;" align="center">  
                                                                                                           &\qquad\inducingInputMatrix, \inducingVector\\                                                                                                                                                                                                    
                                                                                               &p({\color{red} \inducingVector})  = \gaussianSamp{\zerosVector}{\Kuu}                                                                                                                                                                                        
                                                                                                                          \end{align}$$                                                                                                                                                                                                                      
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------- --

###  {data-transition="None"}

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- --
   [\semitransp $$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ $$p(\inducingVector)  = \gaussianSamp{\zerosVector}{\Kuu}$$ ]{} $$\widetilde p({\color{red}\inducingVector}\given \dataVector,\inputMatrix)$$   <img src="./diagrams/nomenclature5.png" width="90% style="background:none; border:none; box-shadow:none;" align="center">  
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- --


