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
talkscam:
youtube: 0BwwedEJ5iU
hackmdslides: fhuszar/B1TCGA_bd#
time: "14:00"
start: "14:00"
end: "15:00"
---

## Different from what we had before:

* different input type (sequences)
* different network building blocks
    * multiplicative interactions
    * gating
    * skip connections
* different objective
    * maximum likelihood
    * generative modelling



## Modelling sequences

* input to the network: $x_1, x_3, \ldots, x_T$
* sequences of different length
* sometimes 'EOS' symbol
* sequence classification (e.g. text classification)
* sequence generation (e.g. language generation)
* sequence-to-sequence (e.g. translation)



\subsubsection{Recurrent Neural Network}

\aligncenter{\includepng{https://i.imgur.com/UJYrL7I}{}{nnegate}}



\subsubsection{RNN: Unrolled through time}

\aligncenter{\includepng{https://i.imgur.com/YnkgS5P}{}{nnegate}}



\subsubsection{RNN: different uses}

\aligncenter{\includejpg{https://i.imgur.com/WGl90lv}{}}

figure from [Andrej Karpathy's blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)



\subsubsection{Generating sequences}

Goal: model the distribution of sequences 

$$
p(x_{1:T}) = p(x_1, \ldots, x_T)
$$

Idea: model it one-step-at-a-time:

$$
p(x_{1:T}) = p(x_T\vert x_{1:T-1}) p(x_{T-1} \vert x_{1:T-2}) \cdots p(x_1)
$$



\subsubsection{Modeling sequence distributions}

\aligncenter{\includepng{https://i.imgur.com/WfPwnjZ}{}{nnegate}}



\subsubsection{Training: maximum likelihood}

\aligncenter{\includepng{https://i.imgur.com/Z8sLsQI}{}{nnegate}}



\subsubsection{Sampling sequences}

\aligncenter{\includepng{https://i.imgur.com/c9WcaD0}{}{nnegate}}



\subsubsection{Char-RNN: Shakespeare}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\aligncenter{\includepng{https://i.imgur.com/cN25jUL}{}}



\subsubsection{Char-RNN: Wikipedia}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\aligncenter{\includepng{https://i.imgur.com/Nr0UjtR}{}}




\subsubsection{Char-RNN: Wikipedia}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\aligncenter{\includepng{https://i.imgur.com/R91pDeJ}{}}




\subsubsection{Char-RNN example: random XML}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\aligncenter{\includepng{https://i.imgur.com/H3b3QjC}{}}



\subsubsection{Char-RNN example: LaTeX}
from [Andrej Karpathy's 2015 blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

\aligncenter{\includejpg{https://i.imgur.com/GgXRG4n}{}}



\subsubsection{But, it was not that easy}

* vanilla RNNs forget too quickly
* vanishing gradients problem
* exploding gradients problem
* colab illustration



\subsubsection{Vanishing gradient problem}

\aligncenter{\includepng{https://i.imgur.com/cLhmhjv}{}}



\subsubsection{Vanishing/exploding gradients problem}

Vanilla RNN:

$$
\mathbf{h}_{t+1} = \sigma(W_h \mathbf{h}_t + W_x \mathbf{x}_t + \mathbf{b_h})
$$

$$
\hat{y} = \phi(W_y \mathbf{h}_{T} + \mathbf{b}_y)
$$



\subsubsection{The gradients of the loss are}

\begin{align}
\frac{\partial \hat{L}}{\partial \mathbf{h}_t} &= \frac{\partial \hat{L}}{\mathbf{h}_T} \prod_{s=t}^{T-1} \frac{\partial h_{t+1}}{\partial h_t} \\
&= \frac{\partial \hat{L}}{\mathbf{h}_T} \prod_{s=t}^{T-1} D_s W^{T-t}_h,
\end{align}

where

* $D_t = \operatorname{diag} \left[\sigma'(W_t \mathbf{h}_{t-1} + + W_x \mathbf{x}_t + \mathbf{b_h})\right]$

* if $\sigma$ is ReLU, $\sigma'(z) \in \{0, 1\}$




\subsubsection{The norm of the gradient is upper bounded}

\begin{align}
\left\|\frac{\partial \hat{L}}{\partial \mathbf{h}_t}\right\| &\leq \left\|\frac{\partial \hat{L}}{\mathbf{h}_T}\right\| \prod_{s=t}^{T-1} \left\|D_s\right\| \left\|W_h\right\|^{T-t},
\end{align}

* the norm of $D_s$ is less than 1 (ReLU)
* the norm of $W_h$ can cause gradients to explode

\newslide{}

\aligncenter{\includepng{https://i.imgur.com/DVFyskJ}{}}



\subsubsection{Unitary Evolution RNNs}

Idea: constrain $W_h$ to be unit-norm.

\aligncenter{\includepng{https://i.imgur.com/9Thc6AS}{}}



\subsubsection{Unitary Evolution RNNs}

Compose weight matrix out of simple unitary transforms:

$$
W_h = D_3R_2\mathcal{F}^{-1}D_2\Pi R_1\mathcal{F}D_1
$$



\subsubsection{More typical solution: gating}

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



## GRU diagram

\aligncenter{\includepng{https://i.imgur.com/TrhwIcC}{}}



\subsubsection{LSTM: Long Short-Term Memory}

* by Hochreiter and Schmidhuber (1997)
* improved/tweaked several times since
* more gates to control behaviour
* 2009: Alex Graves, ICDAR connected handwriting recognition competition
* 2013: sets new record in natural speech dataset
* 2014: GRU proposed (simplified LSTM)
* 2016: neural machine translation



\subsubsection{Side note: dealing with depth}

\aligncenter{\includepng{https://i.imgur.com/sTaW6fT}{}{nnegate}}



\subsubsection{Side note: dealing with depth}

\aligncenter{\includepng{https://i.imgur.com/2oCXEIh}{}{nnegate}}



\subsubsection{Side note: dealing with depth}

\aligncenter{\includepng{https://i.imgur.com/w8BmEfS}{260x}{nnegate}}



\subsubsection{Deep Residual Networks (ResNets)}

\aligncenter{\includepng{https://i.imgur.com/hJK6Rx4}{}}



\subsubsection{Deep Residual Networks (ResNets)}

\aligncenter{\includepng{https://i.imgur.com/wjBWNn9}{}}



\subsubsection{ResNets}

* allow for much deeper networks (101, 152 layer)
* performance increases with depth
* new record in benchmarks (ImageNet, COCO)
* used almost everywhere now



\subsubsection{Resnets behave like ensembles}

\aligncenter{\includepng{https://i.imgur.com/LNPB4e8}{}}

from ([Veit et al, 2016](https://arxiv.org/pdf/1605.06431.pdf))



\subsubsection{DenseNets}

\aligncenter{\includepng{https://i.imgur.com/Eyyx1uK}{}}



\subsubsection{DenseNets}

\aligncenter{\includepng{https://i.imgur.com/a5dQUl8}{}}



\subsubsection{Back to RNNs}

* like ResNets, LSTMs and GRU create "shortcuts"
* allows information to skip processing
* data-dependent gating
* data-dependent shortcuts



## Different from what we had before:

* different input type (sequences)
* different network building blocks
    * multiplicative interactions
    * gating
    * skip connections
* different objective
    * maximum likelihood
    * generative modelling




\subsubsection{RNN: different uses}

\aligncenter{\includejpg{https://i.imgur.com/WGl90lv}{}}

figure from [Andrej Karpathy's blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)


\subsubsection{To engage with this material at home}

Try the [char-RNN Exercise](https://github.com/udacity/deep-learning-v2-pytorch/blob/master/recurrent-neural-networks/char-rnn/Character_Level_RNN_Exercise.ipynb) from Udacity.
