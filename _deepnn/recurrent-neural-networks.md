---
layout: lecture
title: Recurrent Neural Networks
week: 4
session: 2
date: 2022-02-15
start: "14:00"
end: "15:00"
author:
- given: Ferenc
  family: Huszár
  institution: University of Cambridge
  url: https://www.inference.vc/about/
abstract: >
  This lecture will introduce recurrent neural networks, these structures allow us to deal with sequences.
youtube: ZwON3GGA_GI
oldyoutube:
- code: 0BwwedEJ5iU
  year: 2021
hackmdslides: fhuszar/SJRZ6QYkq#
time: "14:00"
start: "14:00"
end: "15:00"
---

\subsection{Different from what we've seen before:}

* different input type (sequences)
* different network building blocks
    * multiplicative interactions
    * gating
    * skip connections
* different objective
    * maximum likelihood
    * generative modelling

\subsection{Modelling sequences}

* input to the network: $x_1, x_2, \ldots, x_T$
* sequences of different length
* sometimes 'EOS' symbol
* sequence classification (e.g. text classification)
* sequence generation (e.g. language generation)
* sequence-to-sequence (e.g. translation)

\subsection{Recurrent Neural Network}

![](https://i.imgur.com/UJYrL7I.png)

\subsection{RNN: Unrolled through time}

![](https://i.imgur.com/YnkgS5P.png)

\subsection{RNN: different uses}

![](https://i.imgur.com/WGl90lv.jpg)

figure from [Andrej Karpathy's blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\subsection{Generating sequences}

Goal: model the distribution of sequences 

$$
p(x_{1:T}) = p(x_1, \ldots, x_T)
$$

Idea: model it one-step-at-a-time:

$$
p(x_{1:T}) = p(x_T\vert x_{1:T-1}) p(x_{T-1} \vert x_{1:T-2}) \cdots p(x_1)
$$

\subsection{Modeling sequence distributions}

![](https://i.imgur.com/WfPwnjZ.png)

\subsection{Training: maximum likelihood}

![](https://i.imgur.com/Z8sLsQI.png)

\subsection{Sampling sequences}

![](https://i.imgur.com/c9WcaD0.png)

\subsection{Char-RNN: Shakespeare}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

![](https://i.imgur.com/cN25jUL.png)

\subsection{Char-RNN: Wikipedia}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

![](https://i.imgur.com/Nr0UjtR.png)


\subsection{Char-RNN: Wikipedia}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

![](https://i.imgur.com/R91pDeJ.png)


\subsection{Char-RNN example: random XML}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

![](https://i.imgur.com/H3b3QjC.png)

\subsection{Char-RNN example: LaTeX}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

![](https://i.imgur.com/GgXRG4n.jpg)

\subsection{But, it was not that easy}

* vanilla RNNs forget too quickly
* vanishing gradients problem
* exploding gradients problem

\subsection{Vanishing/exploding gradients problem}

Vanilla RNN:

$$
\mathbf{h}_{t+1} = \sigma(W_h \mathbf{h}_t + W_x \mathbf{x}_t + \mathbf{b_h})
$$

$$
\hat{y} = \phi(W_y \mathbf{h}_{T} + \mathbf{b}_y)
$$

\subsection{The gradients of the loss are}

\begin{align}
\frac{\partial \hat{L}}{\partial \mathbf{h}_t} &= \frac{\partial \hat{L}}{\partial \mathbf{h}_T} \prod_{s=t}^{T-1} \frac{\partial h_{s+1}}{\partial h_s} \\
&= \frac{\partial \hat{L}}{\mathbf{h}_T} \left( \prod_{s=t}^{T-1} D_s \right) W^{T-t}_h,
\end{align}

where
* $D_t = \operatorname{diag} \left[\sigma'(W_t \mathbf{h}_{t-1} + + W_x \mathbf{x}_t + \mathbf{b_h})\right]$
* if $\sigma$ is ReLU, $\sigma'(z) \in \{0, 1\}$



\subsection{The norm of the gradient is upper bounded}

\begin{align}
\left\|\frac{\partial \hat{L}}{\partial \mathbf{h}_t}\right\| &\leq \left\|\frac{\partial \hat{L}}{\mathbf{h}_T}\right\| \left\|W_h\right\|^{T-t} \prod_{s=t}^{T-1} \left\|D_s\right\|,
\end{align}

* the norm of $D_s$ is less than 1 (ReLU)
* the norm of $W_h$ can cause gradients to explode

\newslide

![](https://i.imgur.com/DVFyskJ.png)

\subsection{More typical solution: gating}

Vanilla RNN:

$$
\mathbf{h}_{t+1} = \sigma(W_h \mathbf{h}_t + W_x \mathbf{x}_t + \mathbf{b_h})
$$

Gated Recurrent Unit:

\begin{align}
\mathbf{h}_{t+1} &= \mathbf{z}_t \odot \mathbf{h}_t + (1 - \mathbf{z}_t) \tilde{\mathbf{h}}_t \\
\tilde{\mathbf{h}}_t &= \phi\left(W\mathbf{x}_t + U(\mathbf{r}_t \odot \mathbf{h}_t)\right)\\
\mathbf{r}_t &= \sigma(W_r\mathbf{x}_t + U_r\mathbf{h}_t)\\
\mathbf{z}_t &= \sigma(W_z\mathbf{x}_t + U_z\mathbf{h}_t)\\
\end{align}

\subsection{GRU diagram}

![](https://i.imgur.com/TrhwIcC.png)

\subsection{LSTM: Long Short-Term Memory}

* by Hochreiter and Schmidhuber (1997)
* improved/tweaked several times since
* more gates to control behaviour
* 2009: Alex Graves, ICDAR connected handwriting recognition competition
* 2013: sets new record in natural speech dataset
* 2014: GRU proposed (simplified LSTM)
* 2016: neural machine translation

\subsection{RNNs for images}

![](https://karpathy.github.io/assets/rnn/house_read.gif)

([Ba et al, 2014](https://arxiv.org/abs/1412.7755))

\subsection{RNNs for images}

![](https://karpathy.github.io/assets/rnn/house_generate.gif)
([Gregor et al, 2015](https://arxiv.org/abs/1502.04623))

\subsection{RNNs for painting}

![](https://i.imgur.com/DhbBAl2.png)

([Mellor et al, 2019](https://learning-to-paint.github.io/))

\subsection{RNNs for painting}

![](https://i.imgur.com/KKg33WR.jpg)

\subsection{Spatial LSTMs}

![](https://i.imgur.com/4fOP3FR.png)

([Theis et al, 2015](https://arxiv.org/pdf/1506.03478.pdf))

\subsection{Spatial LSTMs generating textures}

![](https://i.imgur.com/uLYyB3l.jpg)

\subsection{Seq2Seq: sequence-to-sequence}

![](https://i.imgur.com/Ki8xpvY.png)

([Sutskever et al, 2014](https://arxiv.org/pdf/1409.3215.pdf))

\subsection{Seq2Seq: neural machine translation}

![](https://i.imgur.com/WrZg5r4.png)

\subsection{Show and Tell: "Image2Seq"}

![](https://i.imgur.com/hyUtUjl.png)

([Vinyals et al, 2015](https://arxiv.org/pdf/1411.4555.pdf))

\subsection{Show and Tell: "Image2Seq"}

![](https://i.imgur.com/MSU5mIw.jpg)

([Vinyals et al, 2015](https://arxiv.org/pdf/1411.4555.pdf))

\subsection{Sentence to Parsing tree "Seq2Tree"}

![](https://i.imgur.com/ywwmSCK.png)

([Vinyals et al, 2014](https://arxiv.org/abs/1412.7449))

\subsection{General algorithms as Seq2Seq}

travelling salesman

![](https://i.imgur.com/B8jsaMt.png)

([Vinyals et al, 2015](https://arxiv.org/abs/1506.03134))

\subsection{General algorithms as Seq2Seq}

convex hull and triangulation

![](https://i.imgur.com/mTQhCTi.png)

\subsection{Pointer networks}

![](https://i.imgur.com/JhFpOkZ.png)

\subsection{Revisiting the basic idea}

![](https://i.imgur.com/Ki8xpvY.png)

"Asking the network too much"

\subsection{Attention layer}

![](https://i.imgur.com/nskRYts.png)

\subsection{Attention layer}

Attention weights:

$$
\alpha_{t,s} = \frac{e^{\mathbf{e}^T_t \mathbf{d}_s}}{\sum_u e^{\mathbf{e}^T_t \mathbf{d}_s}} 
$$

Context vector:

$$
\mathbf{c}_s = \sum_{t=1}^T \alpha_{t,s} \mathbf{e}_t
$$

\subsection{Attention layer visualised}

![](https://i.imgur.com/MVt50yl.png =500x)

---

![](https://i.imgur.com/uNwTRux.png)

\subsection{To engage with this material at home}

Try the [char-RNN Exercise](https://github.com/udacity/deep-learning-v2-pytorch/blob/master/recurrent-neural-networks/char-rnn/Character_Level_RNN_Exercise.ipynb) from Udacity.


\subsection{Side note: dealing with depth}

![](https://i.imgur.com/sTaW6fT.png)

\subsection{Side note: dealing with depth}

![](https://i.imgur.com/2oCXEIh.png)

\subsection{Side note: dealing with depth}

![](https://i.imgur.com/w8BmEfS.png =260x)

\subsection{Deep Residual Networks (ResNets)}

![](https://i.imgur.com/hJK6Rx4.png)

\subsection{Deep Residual Networks (ResNets)}

![](https://i.imgur.com/wjBWNn9.png)

\subsection{ResNets}

* allow for much deeper networks (101, 152 layer)
* performance increases with depth
* new record in benchmarks (ImageNet, COCO)
* used almost everywhere now

\subsection{Resnets behave like ensembles}

![](https://i.imgur.com/LNPB4e8.png)

from ([Veit et al, 2016](https://arxiv.org/pdf/1605.06431.pdf))

\subsection{DenseNets}

![](https://i.imgur.com/Eyyx1uK.png)

\subsection{DenseNets}

![](https://i.imgur.com/a5dQUl8.png)

\subsection{Back to RNNs}

* like ResNets, LSTMs and GRU create "shortcuts"
* allows information to skip processing
* data-dependent gating
* data-dependent shortcuts

\subsection{Different from what we had before:

* different input type (sequences)
* different network building blocks
    * multiplicative interactions
    * gating
    * skip connections
* different objective
    * maximum likelihood
    * generative modelling

---
