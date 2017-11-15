### Variational Compression

\hfill\raggedleft{\andreasPicture{1.5cm}}\
\hfill\raggedleft{\citep{Damianou:deepgp13}}\

-   Augment each layer with inducing variables $\inducingVector_i$.

-   Apply variational compression, \begin{align}
          p(\dataVector, \{\hiddenVector_i\}_{i=1}^{\numLayers-1}|\{\inducingVector_i\}_{i=1}^{\numLayers}, \inputMatrix) \geq & 
          \tilde p(\dataVector|\inducingVector_{\numLayers}, \hiddenVector_{\numLayers-1})\prod_{i=2}^{\numLayers-1} \tilde p(\hiddenVector_i|\inducingVector_i,\hiddenVector_{i-1}) \tilde p(\hiddenVector_1|\inducingVector_i,\inputMatrix) \nonumber \\
          & \times
          \exp\left(\sum_{i=1}^\numLayers -\frac{1}{2\sigma^2_i}\trace{\conditionalCovariance_{i}}\right)
          \label{eq:deep_structure}
        \end{align} where
    $$\tilde p(\hiddenVector_i|\inducingVector_i,\hiddenVector_{i-1})
        = \gaussianDist{\hiddenVector_i}{\kernelMatrix_{\hiddenVector_{i}\inducingVector_{i}}\kernelMatrix_{\inducingVector_i\inducingVector_i}^{-1}\inducingVector_i}{\sigma^2_i\eye}.$$

### Nested Variational Compression

\hfill\raggedleft{\jamesPicture{1.5cm}}\
\hfill\raggedleft{\citep{Hensman:nested14}}

-   By sustaining explicity distributions over inducing variables James
    Hensman has developed a nested variatnt of variational compression.

-   Exciting thing: it mathematically looks like a deep neural network,
    but with inducing variables in the place of basis functions.

-   Additional complexity control term in the objective function.

\tikz{%
        %top layer
        \node[obs] (x) {$\mathbf \inputScalar_i$};
        \node[latent, below=1 of x] (h1) {$\hiddenVector_{1i}$};
        \node[obs, left=1 of h1] (u1) {$\inducingVector_{1}$};
        \node[const, left=2.88 of x, label=left:$\inducingInputVector_0$] (z0) {};
        \edge[] {z0}{u1};
        \edge[] x {h1};
        \edge[] {u1} {h1};
        \edge[] {z0} {h1};
        %
        %layer 1
        \node[const, left=1 of u1, label=left:$\inducingInputScalar_1$] (z1) {};
        \node[latent, below=1.3 of h1] (h2) {$\hiddenVector_{2i}$};
        \node[obs, left=1 of h2] (u2) {$\inducingVector_{2}$};
        \edge[] {z1}{u2};
        \edge[] {h1} {h2};
        \edge[] {u2} {h2};
        \edge[] {z1} {h2};
        %
        %layer 2
        \node[const, left=1 of u2, label=left:$\inducingInputScalar_2$] (z2) {};
        \node[obs, below=1.3 of h2] (y) {$\dataVector_{i}$};
        \node[obs, left=1 of y] (u3) {$\inducingVector_{3}$};
        \edge[] {z2}{u3};
        \edge[] {h2} {y};
        \edge[] {u3} {y};
        \edge[] {z2} {y};
        %
        %plates
        %\plate {hhu} {(h1)(u1)} {$d=1...{D_1}$};
        %\plate {hu} {(h2)(u2)} {$d=1...{D_2}$};
        %\plate {yu} {(y)(u3)} {$d=1...D$};
        \plate {yhx} {(y)(h2)(h1)(x)} {\,\,$i=1...\numData$};
      }

### Nested Bound

\begin{align}
    \log p(\dataVector|\inputMatrix )  \geq &
    %
    -\frac{1}{\sigma_1^2} \trace{\conditionalCovariance_1}
    % 
    -\sum_{i=2}^\numLayers \frac{1}{2\sigma_i^2} \left(\psi_{i}
    % 
    - \trace{{\boldsymbol \Phi}_{i}\kernelMatrix_{\inducingVector_{i} \inducingVector_{i}}^{-1}}\right) \nonumber \\
    %
    & - \sum_{i=1}^{\numLayers}\KL{q(\inducingVector_i)}{p(\inducingVector_i)} \nonumber \\
    %
    & - \sum_{i=2}^{\numLayers}\frac{1}{2\sigma^2_{i}}\trace{({\boldsymbol
        \Phi}_i - {\boldsymbol \Psi}_i^\top{\boldsymbol \Psi}_i)
      \kernelMatrix_{\inducingVector_{i}
        \inducingVector_{i}}^{-1}
      \expDist{\inducingVector_{i}\inducingVector_{i}^\top}{q(\inducingVector_{i})}\kernelMatrix_{\inducingVector_{i}\inducingVector_{i}}^{-1}} \nonumber \\
    %
    & + {\only<2>{\color{\redColor}}\log \gaussianDist{\dataVector}{{\boldsymbol
        \Psi}_{\numLayers}\kernelMatrix_{\inducingVector_{\numLayers}
        \inducingVector_{\numLayers}}^{-1}{\mathbf
        m}_\numLayers}{\sigma^2_\numLayers\eye}}
    \label{eq:deep_bound}
  \end{align}

### Required Expectations

$${\only<1>{\color{\redColor}}\log \gaussianDist{\dataVector}{{\only<2->{\color{\blueColor}}{\boldsymbol
          \Psi}_{\numLayers}}\kernelMatrix_{\inducingVector_{\numLayers}
          \inducingVector_{\numLayers}}^{-1}{\mathbf
          m}_\numLayers}{\sigma^2_\numLayers\eye}}$$ where \only<2->{\[
    {\color{\blueColor}{\boldsymbol \Psi}_i}= \expDist{\kernelMatrix_{\hiddenVector_i\inducingVector_i}}{{\only<3->{\color{\magentaColor}}q(\hiddenVector_{i-1})}}
    \]
  where elements of $\kernelMatrix_{\hiddenVector_i\inducingVector_i}$ are
  \[
  \kernelScalar_{\hiddenScalar_i\inducingScalar^\prime_i}(\hiddenVector_{i-1}, \inducingInputVector^\prime_{i})
  \]} \only<3->{
    And
    \[
      {\color{\magentaColor}q(\hiddenVector_1)} = \int \tilde p(\hiddenVector_1|\inducingVector_1, \inputMatrix)q(\inducingVector_1)\text{d}\inducingVector_1, 
      \]
    \[
      {\color{\magentaColor}q(\hiddenVector_i)} = \int \tilde p(\hiddenVector_i|\inducingVector_i, \mappingFunctionVector_{i-1})q(\inducingVector_i){\color{\magentaColor}q(\mappingFunctionVector_{i-1})}\text{d}\inducingVector_i \text{d}\mappingFunctionVector_i, 
    \]
  }
\only<4->{\begin{center} \emph{cf} wake sleep algorithm. {\color{\magentaColor}recognition network} and {\color{\blueColor}generation network} \citep{Hinton:science95}.\end{center} }


