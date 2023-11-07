<!--frame start-->
### Direct Construction of Covariance Matrix

\only<1->{Use matrix notation to write function,
    \[
    {f}\left({{\bf {x}}}_i;{\mathbf{{w}}}\right) = \sum_{k=1}^{m}{w}_k {\phi}_k\left({{\bf {x}}}_i\right)
    \]} \only<2->{computed at training data gives a vector
      \[
      {\mathbf{{f}}}= {\boldsymbol{\Phi}}{\mathbf{{w}}}.
      \]}\only<3->{\[{\mathbf{{w}}}\sim {\mathcal{N}\left({\mathbf{0}},\alpha{\mathbf{I}}\right)}\]}

\only<4->{\begin{center}${\mathbf{{w}}}$ and ${\mathbf{{f}}}$ are only
      related by an \emph{inner product}.\end{center}}
\only<5->{\begin{center}${\boldsymbol{\Phi}}\in \Re^{{n}\times{p}}$ is a \emph{design matrix}\end{center}}
\only<6->{\begin{center}${\boldsymbol{\Phi}}$ is fixed and non-stochastic for a given training set.\end{center}}
\only<7->{\begin{center}${\mathbf{{f}}}$ is
      Gaussian distributed.\end{center}}

<!--frame end-->
<!--frame start-->
### Expectations

-   &lt;1-&gt; We have $${\left<{\mathbf{{f}}}\right>} =
      {\boldsymbol{\Phi}}{\left<{\mathbf{{w}}}\right>}.$$

-   &lt;2-&gt; Prior mean of ${\mathbf{{w}}}$ was zero giving
    $${\left<{\mathbf{{f}}}\right>} = {\mathbf{0}}.$$

-   &lt;3-&gt; Prior covariance of ${\mathbf{{f}}}$ is
    $${\mathbf{\MakeUppercase{{k}}}}={\left<
        {\mathbf{{f}}}{\mathbf{{f}}}^\top\right>} -
      {\left<{\mathbf{{f}}}\right>}{\left<{\mathbf{{f}}}\right>}^\top$$
    \only<4->{
      \[
      {\left<{\mathbf{{f}}}{\mathbf{{f}}}^\top\right>} = {\boldsymbol{\Phi}}{\left<{\mathbf{{w}}}{\mathbf{{w}}}^\top\right>}{\boldsymbol{\Phi}}^\top, 
      \]
      giving
      \[
      {\mathbf{\MakeUppercase{{k}}}}= \alpha {\boldsymbol{\Phi}}{\boldsymbol{\Phi}}^\top.
      \]}

**We use ${\left<\cdot\right>}$ to denote expectations under prior
distributions.**

<!--frame end-->

