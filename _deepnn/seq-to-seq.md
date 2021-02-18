---
layout: lecture
title: Sequence to Sequence
week: 5
session: 1
date: 2021-02-18
start: "14:00"
end: "15:00"
author:
- given: Ferenc
  family: Huszár
  institution: 
  url: https://www.inference.vc/about/
abstract: >
  This lecture will continue on RNNs and their evolution as methods for performing sequence to sequence.
talkscam:
youtube: KgrerFfLv1k
time: "14:00"
start: "14:00"
end: "15:00"
---

\include{talk-macros.gpp}

\subsubsection{RNN: Recap}

\aligncenter{\includepng{https://i.imgur.com/YnkgS5P}{}{nnegate}}



\subsubsection{The state update rule: naive}

$$
\mathbf{h}_{t+1} = \phi(W_h \mathbf{h}_t + W_x \mathbf{x}_t + \mathbf{b_h})
$$



\subsubsection{The state update rule: GRU}

\begin{align}
\mathbf{h}_{t+1} &= \mathbf{z}_t \odot \mathbf{h}_t + (1 - \mathbf{z}_t) \odot \tilde{\mathbf{h}}_t \\
\tilde{\mathbf{h}}_t &= \phi\left(W\mathbf{x}_t + U(\mathbf{r}_t \odot \mathbf{h}_t)\right)\\
\mathbf{r}_t &= \sigma(W_r\mathbf{x}_t + U_r\mathbf{h}_t)\\
\mathbf{z}_t &= \sigma(W_z\mathbf{x}_t + U_z\mathbf{h}_t)\\
\end{align}



\subsubsection{implementing branching logic}

...in code:

```
if r:
    return 5
else:
    return 3
```

...in algebra:

```
return r*5 + (1-r)*3
```



\subsubsection{The state update rule: GRU}

\begin{align}
\mathbf{h}_{t+1} &= \mathbf{z}_t \odot \mathbf{h}_t + (1 - \mathbf{z}_t) \odot \tilde{\mathbf{h}}_t \\
\tilde{\mathbf{h}}_t &= \phi\left(W\mathbf{x}_t + U(\mathbf{r}_t \odot \mathbf{h}_t)\right)\\
\mathbf{r}_t &= \sigma(W_r\mathbf{x}_t + U_r\mathbf{h}_t)\\
\mathbf{z}_t &= \sigma(W_z\mathbf{x}_t + U_z\mathbf{h}_t)\\
\end{align}



\subsubsection{Side note: dealing with depth}

\aligncenter{\includepng{https://i.imgur.com/n72rvhO}{}{nnegate}}



\subsubsection{Side note: dealing with depth}

\aligncenter{\includepng{https://i.imgur.com/w8BmEfS}{260px}{nnegate}}



\subsubsection{Very deep networks are hard to train}

* exploding/vanishing gradients
* their performance degrades with depth
* VGG19: 19-layer ConvNet



\subsubsection{Deep Residual Networks (ResNets)}

\aligncenter{\includepng{https://i.imgur.com/wjBWNn9}}



\subsubsection{Deep Residual Networks (ResNets)}

\aligncenter{\includepng{https://i.imgur.com/hJK6Rx4}}



\subsubsection{ResNets}

* allow for much deeper networks (101, 152 layer)
* performance increases with depth
* new record in benchmarks (ImageNet, COCO)
* used almost everywhere now



\subsubsection{Resnets behave like ensembles}

\aligncenter{\includepng{https://i.imgur.com/LNPB4e8}}

from ([Veit et al, 2016](https://arxiv.org/pdf/1605.06431.pdf))



\subsubsection{DenseNets}

\aligncenter{\includepng{https://i.imgur.com/4aTzmR7}}



\subsubsection{Back to RNNs}

* like ResNets, LSTMs create "shortcuts"
* allows information to skip processing
* data-dependent gating
* data-dependent shortcuts



\subsubsection{Visualising RNN behaviours}

See this [distill post](https://distill.pub/2019/memorization-in-rnns/)



\subsubsection{RNN: different uses}

\aligncenter{\includejpg{https://i.imgur.com/WGl90lv}}

figure from [Andrej Karpathy's blog post](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)



\subsubsection{RNNs for images}

\aligncenter{\includegif{https://karpathy.github.io/assets/rnn/house_read}}

([Ba et al, 2014](https://arxiv.org/abs/1412.7755))



\subsubsection{RNNs for images}

\aligncenter{\includegif{https://karpathy.github.io/assets/rnn/house_generate}}

([Gregor et al, 2015](https://arxiv.org/abs/1502.04623))



\subsubsection{RNNs for painting}

\aligncenter{\includepng{https://i.imgur.com/DhbBAl2}}

([Mellor et al, 2019](https://learning-to-paint.github.io/))



\subsubsection{RNNs for painting}

\aligncenter{\includejpg{https://i.imgur.com/KKg33WR}}



\subsubsection{Spatial LSTMs}

\aligncenter{\includepng{https://i.imgur.com/4fOP3FR}}

([Theis et al, 2015](https://arxiv.org/pdf/1506.03478.pdf))



\subsubsection{Spatial LSTMs generating textures}

\aligncenter{\includejpg{https://i.imgur.com/uLYyB3l}}



\subsubsection{Seq2Seq: sequence-to-sequence}

\aligncenter{\includepng{https://i.imgur.com/Ki8xpvY}}

([Sutskever et al, 2014](https://arxiv.org/pdf/1409.3215.pdf))



\subsubsection{Seq2Seq: neural machine translation}

\aligncenter{\includepng{https://i.imgur.com/WrZg5r4}}



\subsubsection{Show and Tell: "Image2Seq"}

\aligncenter{\includepng{https://i.imgur.com/hyUtUjl}}

([Vinyals et al, 2015](https://arxiv.org/pdf/1411.4555.pdf))



\subsubsection{Show and Tell: "Image2Seq"}

\aligncenter{\includejpg{https://i.imgur.com/MSU5mIw}}

([Vinyals et al, 2015](https://arxiv.org/pdf/1411.4555.pdf))



\subsubsection{Sentence to Parsing tree "Seq2Tree"}

\aligncenter{\includepng{https://i.imgur.com/ywwmSCK}}

([Vinyals et al, 2014](https://arxiv.org/abs/1412.7449))



\subsubsection{General algorithms as Seq2Seq}

travelling salesman

\aligncenter{\includepng{https://i.imgur.com/B8jsaMt}}

([Vinyals et al, 2015](https://arxiv.org/abs/1506.03134))



\subsubsection{General algorithms as Seq2Seq}

convex hull and triangulation

\aligncenter{\includepng{https://i.imgur.com/mTQhCTi}}



\subsubsection{Pointer networks}

\aligncenter{\includepng{https://i.imgur.com/JhFpOkZ}}



\subsubsection{Revisiting the basic idea}

\aligncenter{\includepng{https://i.imgur.com/Ki8xpvY}}

"Asking the network too much"



\subsubsection{Attention layer}

\aligncenter{\includepng{https://i.imgur.com/nskRYts}}



\subsubsection{Attention layer}

Attention weights:

$$
\alpha_{t,s} = \frac{e^{\mathbf{e}^T_t \mathbf{d}_s}}{\sum_u e^{\mathbf{e}^T_t \mathbf{d}_s}} 
$$

Context vector:

$$
\mathbf{c}_s = \sum_{t=1}^T \alpha_{t,s} \mathbf{e}_t
$$



\subsubsection{Attention layer visualised}

\aligncenter{\includepng{https://i.imgur.com/MVt50yl.png}{500px)}



\subsubsection{To engage with this material at home}

Try the [char-RNN Exercise](https://github.com/udacity/deep-learning-v2-pytorch/blob/master/recurrent-neural-networks/char-rnn/Character_Level_RNN_Exercise.ipynb) from Udacity.

\newslide{}

* neural machine translation (historical note)
* image captioning: encoder is a CNN, decoder is RNN
* forgetting problem revisited
    * asking the network too much
* allowing the decoder to look back at encoder states
* pointer networks


