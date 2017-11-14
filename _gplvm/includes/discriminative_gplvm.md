frame start

### Prior for Supervised Learning

\begin{flushright}
    {\scriptsize \citep{Urtasun:dgplvm07}}
\end{flushright}
-   We introduce a prior that is based on the Fisher criteria
    $$p(\latentMatrix) \propto \exp \left\{ -\frac{1}{\sigma_{d}^2}  \tr{ {\mathbf{S}_w^{-1} \mathbf{S}_b}}\right\} ~,$$
    with $\mathbf{S}_b$ the between class matrix and $\mathbf{S}_w$ the
    within class matrix

    columns start

    \begin{column}{3cm}
          \begin{figure}
            \only<1>{\includegraphics[width=0.92\columnwidth]{../../../gplvm/tex/diagrams/classif/original2}}
            \only<2>{\includegraphics[width=0.92\columnwidth]{../../../gplvm/tex/diagrams/classif/between2}}
            \only<3>{\includegraphics[width=0.92\columnwidth]{../../../gplvm/tex/diagrams/classif/within}}
          \end{figure}
        \end{column}
    \begin{column}{7cm}
          \only<2-3>{
            \[
            \mathbf{S}_w =\sum_{i=1}^L \frac{\numData_i}{\numData}(\mathbf{M}_i - \mathbf{M}_0)(\mathbf{M}_i - \mathbf{M}_0)^\top
            \]
          }
          \only<3>{
            \[
            \mathbf{S}_b =\sum_{i=1}^L\frac{\numData_i}{\numData}\left[
              \frac{1}{\numData_i} \sum_{k=1}^{\numData_i} (\latentVector_k^{(i)}-\mathbf{M}_i)(\latentVector_k^{(i)}-\mathbf{M}_i)^\top
            \right]
            \]
          }
          % \begin{eqnarray}
          %   \mathbf{S}_w =\sum_{i=1}^L \frac{\numData_i}{\numData}(\mathbf{M}_i - \mathbf{M}_0)(\mathbf{M}_i - \mathbf{M}_0)^\top\nonumber \\
          %   \mathbf{S}_b =\sum_{i=1}^L\frac{\numData_i}{\numData}\left[
          %     \frac{1}{\numData_i} \sum_{k=1}^{\numData_i} (\latentVector_k^{(i)}-\mathbf{M}_i)(\latentVector_k^{(i)}-\mathbf{M}_i)^\top
          %   \right]\nonumber
          % \end{eqnarray}
        \end{column}
    columns end

    \only<2-3>{
        where $\latentMatrix^{(i)} = [\latentVector_1^{(i)}, \cdots, \latentVector_{\numData_i}^{(i)}]$ are the $\numData_i$ training points
        of class $i$, $\mathbf{M}_i$ is the mean of the elements of class $i$, and $\mathbf{M}_0$ is the mean
        of all the training points of all classes. } \only<3>{
      \item As before the model is learned by maximizing $p(\dataMatrix|\latentMatrix) p(\latentMatrix)$.}

\only<4->{
  \begin{figure}
    \includegraphics[width=0.30\columnwidth]{../../../gplvm/tex/diagrams/oil_data/subset_100/d_5_kbr_01_l_1000000_a.pdf}
    \includegraphics[width=0.30\columnwidth]{../../../gplvm/tex/diagrams/oil_data/subset_100/d_5_kbr_01_l_10000}
    % \includegraphics[width=0.5\columnwidth]{../../../gplvm/tex/diagrams/oil_data/subset_100/d_5_kbr_01_l_1000}
    \includegraphics[width=0.30\columnwidth]{../../../gplvm/tex/diagrams/oil_data/subset_100/d_5_kbr_01_l_0}
    \caption{2D latent spaces learned by D-GPLVM on the oil dataset
      are shown, with 100 training examples and different values of
      $\sigma_{d}$.  Note that as $1 / \sigma_{d}^2$ increases the
      model becomes more discriminative but has worse generalization.
    }
    \label{fig:influence}
  \end{figure}
}

frame end
