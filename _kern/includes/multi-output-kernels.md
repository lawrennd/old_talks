\ifndef{multiOutputKernels}
\define{multiOutputKernels}

\editme


\matlabcode{gpKalmanMultiTaskInit}

\subsection{Kernels for Vector Valued Outputs: A Review}

\subsection{Kronecker Structure GPs}

-   This Kronecker structure leads to several published models.
    $$
	(\kernelMatrix(\inputVector,\inputVector^\prime))_{\dataIndex,\dataIndex^\prime}=\kernelScalar(\inputVector,\inputVector^\prime)\kernelScalar_T(\dataIndex,\dataIndex^\prime),
	$$
    where $\kernelScalar$ has $\inputVector$ and $\kernelScalar_T$ has $\numData$ as inputs.

-   Can think of multiple output covariance functions as covariances
    with augmented input.

-   Alongside $\inputVector$ we also input the $\dataIndex$ associated with the
    *output* of interest.
	
\subsection{Separable Covariance Functions}

-   Taking $\coregionalizationMatrix= {\mappingMatrix}{\mappingMatrix}^\top$ we
    have a matrix expression across outputs.
    $$\kernelMatrix(\inputVector,\inputVector^\prime)=\kernelScalar(\inputVector,\inputVector^\prime)\coregionalizationMatrix,$$
    where $\coregionalizationMatrix$ is a $\dataDim\times \dataDim$
    symmetric and positive semi-definite matrix.

-   $\coregionalizationMatrix$ is called the
    *coregionalization* matrix.

-   We call this class of covariance functions *separable* due to their
    product structure.
	
\subsection{Sum of Separable Covariance Functions}

-   In the same spirit a more general class of kernels is given by
    $$\kernelMatrix(\inputVector,\inputVector^\prime)=\sum_{j=1}^\latentDim\kernelScalar_{j}(\inputVector,\inputVector^\prime)\coregionalizationMatrix_{j}.$$

-   This can also be written as
    $$\kernelMatrix(\inputMatrix, \inputMatrix) = \sum_{j=1}^\latentDim\coregionalizationMatrix_{j}\otimes \kernelScalar_{j}(\inputMatrix, \inputMatrix),$$

-   This is like several Kalman filter-type models added together, but
    each one with a different set of latent functions.

-   We call this class of kernels sum of separable kernels
    (SoS kernels).
	
\subsection{Geostatistics}

-   Use of GPs in Geostatistics is called kriging.

-   These multi-output GPs pioneered in geostatistics: prediction over
    vector-valued output data is known as *cokriging*.

-   The model in geostatistics is known as the *linear model of
    coregionalization* (LMC, @Journel:miningBook78
    @Goovaerts:book97).

-   Most machine learning multitask models can be placed in the context
    of the LMC model.
	
\subsection{Weighted sum of Latent Functions}

-   In the linear model of coregionalization (LMC) outputs are expressed
    as linear combinations of independent random functions.

-   In the LMC, each component $\mappingFunction_\dataIndex$ is expressed as a linear sum
    $$\mappingFunction_\dataIndex(\inputVector) = \sum_{j=1}^\latentDim{w}_{\dataIndex,{j}}{u}_{j}(\inputVector).$$
    where the latent functions are independent and have covariance
    functions $\kernelScalar_{j}(\inputVector,\inputVector^\prime)$.

-   The processes $\{\mappingFunction_j(\inputVector)\}_{j=1}^\latentDim$ are
    independent for $\latentDim \neq {j}^\prime$.
	
\subsection{Kalman Filter Special Case}

-   The Kalman filter is an example of the LMC where
    ${u}_i(\inputVector) \rightarrow {x}_i(t)$.

-   I.e. we’ve moved form time input to a more general input space.

-   In matrix notation:
    1.  Kalman filter
        $$\mappingFunctionMatrix= {\mappingMatrix}\inputMatrix$$
    2.  LMC
        $$\mappingFunctionMatrix= {\mappingMatrix}{\mathbf{U}}$$
    where the rows of these matrices ${\mappingFunctionMatrix}$,
    $\inputMatrix$, ${\mathbf{U}}$ each
    contain $\latentDim$ samples from their corresponding functions at a
    different time (Kalman filter) or spatial location (LMC).
	
\subsection{Intrinsic Coregionalization Model}

-   If one covariance used for latent functions (like in Kalman filter).

-   This is called the intrinsic coregionalization model (ICM,
    @Goovaerts:book97).

-   The kernel matrix corresponding to a dataset
    $\inputMatrix$ takes the form
    $$
	\kernelMatrix(\inputMatrix, \inputMatrix) =  \coregionalizationMatrix\otimes \kernelScalar(\inputMatrix, \inputMatrix).
	$$
	

\subsection{Autokrigeability}

-   If outputs are noise-free, maximum likelihood is equivalent to
    independent fits of $\coregionalizationMatrix$ and
    $\kernelScalar(\inputVector, \inputVector^\prime)$
    [@Helterbrand:universalCR94].

-   In geostatistics this is known as autokrigeability
    [@Wackernagel:multivariate03].

-   In multitask learning its the cancellation of intertask transfer
    [@Bonilla:multi07].
	
\subsection{Intrinsic Coregionalization Model}

$$
\kernelMatrix(\inputMatrix, \inputMatrix) =  \mappingVector\mappingVector^\top  \otimes \kernelScalar(\inputMatrix, \inputMatrix).
$$

$$
\mappingVector= \begin{bmatrix} 1 \\ 5\end{bmatrix}
$$
$$
\coregionalizationMatrix= \begin{bmatrix} 1 & 5\\ 5&25\end{bmatrix}
$$

\matlabcode{gpKalmanToMultiTaskIcm}

![image](../../../multigp/tex/diagrams/icmCovarianceImage)![image](../../../multigp/tex/diagrams/icmCovarianceSample1)![image](../../../multigp/tex/diagrams/icmCovarianceSample2)![image](../../../multigp/tex/diagrams/icmCovarianceSample3)![image](../../../multigp/tex/diagrams/icmCovarianceSample4)

\include{_kern/includes/icm-covariance.md}

\subsection{Intrinsic Coregionalization Model}

$$
\kernelMatrix(\inputMatrix, \inputMatrix) =  \coregionalizationMatrix\otimes \kernelScalar(\inputMatrix, \inputMatrix).
$$


$$
\coregionalizationMatrix= \begin{bmatrix} 1 & 0.5\\ 0.5& 1.5\end{bmatrix}
$$

\matlabcode{gpKalmanToMultiTaskIcm2}

![image](../../../multigp/tex/diagrams/icm2CovarianceImage)![image](../../../multigp/tex/diagrams/icm2CovarianceSample1)![image](../../../multigp/tex/diagrams/icm2CovarianceSample2)![image](../../../multigp/tex/diagrams/icm2CovarianceSample3)![image](../../../multigp/tex/diagrams/icm2CovarianceSample4)

\subsection{LMC Samples}

$$\kernelMatrix(\inputMatrix, \inputMatrix) = \coregionalizationMatrix_1 \otimes \kernelScalar_1(\inputMatrix, \inputMatrix) + \coregionalizationMatrix_2 \otimes \kernelScalar_2(\inputMatrix, \inputMatrix)$$


$$\coregionalizationMatrix_1 = \begin{bmatrix} 1.4 & 0.5\\ 0.5& 1.2\end{bmatrix}$$
$${\ell}_1 = 1$$
$$\coregionalizationMatrix_2 = \begin{bmatrix} 1 & 0.5\\ 0.5& 1.3\end{bmatrix}$$
$${\ell}_2 = 0.2$$

\matlabcode{gpKalmanToMultiTaskLmc}

![image](../../../multigp/tex/diagrams/lmc2CovarianceImage)![image](../../../multigp/tex/diagrams/lmc2CovarianceSample1)![image](../../../multigp/tex/diagrams/lmc2CovarianceSample2)![image](../../../multigp/tex/diagrams/lmc2CovarianceSample3)![image](../../../multigp/tex/diagrams/lmc2CovarianceSample4)

\subsection{LMC in Machine Learning and Statistics}

-   Used in machine learning for GPs for multivariate regression and in
    statistics for computer emulation of expensive multivariate
    computer codes.

-   Imposes the correlation of the outputs explicitly through the set of
    coregionalization matrices.

-   Setting $\coregionalizationMatrix = \eye_\dataDim$ assumes
    outputs are conditionally independent given the parameters
    $\parameterVector$.
    [@Minka:learningtolearn97; @Lawrence:learning04; @Kai:multitask05].

-   More recent approaches for multiple output modeling are different
    versions of the linear model of coregionalization.
	
\subsection{Semiparametric Latent Factor Model}

-   Coregionalization matrices are rank 1
    @Teh:semiparametric05. rewrite equation as
    $$\kernelMatrix(\inputMatrix, \inputMatrix) = \sum_{j=1}^\latentDim\mappingVector_{:, {j}}\mappingVector^{\top}_{:, {j}} \otimes \kernelScalar_{j}(\inputMatrix, \inputMatrix).$$

-   Like the Kalman filter, but each latent function has a
    *different* covariance.

-   Authors suggest using an exponentiated quadratic characteristic
    length-scale for each input dimension.

\include{_kern/includes/slfm-covariance.md}

\subsection{Semiparametric Latent Factor Model Samples}

$$
\kernelMatrix(\inputMatrix, \inputMatrix) = \mappingVector_{:, 1}\mappingVector_{:, 1}^\top \otimes \kernelScalar_1(\inputMatrix, \inputMatrix) + \mappingVector_{:, 2} \mappingVector_{:, 2}^\top \otimes \kernelScalar_2(\inputMatrix, \inputMatrix)
$$

$$
\mappingVector_1 = \begin{bmatrix} 0.5 \\ 1\end{bmatrix}
$$
$$
\mappingVector_2 = \begin{bmatrix} 1 \\ 0.5\end{bmatrix}
$$

\matlabcode{gpKalmanToMultiTaskSlfm}

![image](../../../multigp/tex/diagrams/slfmCovarianceImage)![image](../../../multigp/tex/diagrams/slfmCovarianceSample1)![image](../../../multigp/tex/diagrams/slfmCovarianceSample2)![image](../../../multigp/tex/diagrams/slfmCovarianceSample3)![image](../../../multigp/tex/diagrams/slfmCovarianceSample4)

\subsection{Gaussian processes for Multi-task, Multi-output and Multi-class}

-   @Bonilla:multi07 suggest ICM for multitask learning.

-   Use a PPCA form for $\coregionalizationMatrix$: similar to our
    Kalman filter example.

-   Refer to the autokrigeability effect as the cancellation of
    inter-task transfer.

-   Also discuss the similarities between the multi-task GP and the ICM,
    and its relationship to the SLFM and the LMC.
	
\subsection{Multitask Classification}

-   Mostly restricted to the case where the outputs are conditionally
    independent given the hyperparameters $\boldsymbol{\phi}$
    [@Minka:learningtolearn97; @Williams:multiclass98; @Lawrence:learning04; @Seeger:multiple04; @Kai:multitask05; @Rasmussen:book06].

-   Intrinsic coregionalization model has been used in the
    multiclass scenario. @Skolidis:multiclass11 use the intrinsic
    coregionalization model for classification, by introducing a probit
    noise model as the likelihood.

-   Posterior distribution is no longer analytically tractable:
    approximate inference is required.
	
\subsection{Computer Emulation}

-   A statistical model used as a surrogate for a computationally
    expensive computer model.

-   @Higdon:high08 use the linear model of coregionalization to model
    images representing the evolution of the implosion of
    steel cylinders.

-   In @Conti:multi09 use the ICM to model a vegetation model: called
    the Sheffield Dynamic Global Vegetation Model
    @Woodward:vegetation98.

\endif
