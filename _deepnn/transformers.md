---
layout: lecture
title: Transformers
week: 5
session: 2
date: 2022-02-22
start: "14:00"
end: "15:00"
author:
- given: Nic
  family: Lane
  institution: 
  url: http://niclane.org/
abstract: >
  This lecture will introduce transformers.
talkscam:
reveal: true
youtube: wXgWXDpVrM4
talktheme: white
talkcss: ../assets/css/talks-small.css
time: "14:00"
start: "14:00"
end: "15:00"
---

\subsection{Plan for the Day}

-   **Attention, Attention!**
-   Transformers: Attention is All You Need.
-   Transformer extensions:
    -   Reformers - alternative attention operator
    -   Linformers - linear complexity
    -   Transformer training difficulty\
    -   Switch Transformers
-   Going beyond NLP
    -   Image is Worth 16x16 Words
    -   AlphaFold 2

\subsection{Think back to last week: Seq2Seq}

-   **Encoder** compresses inut into a number of hidden notes - the
    state vector.
-   **Decoder** , initialized with the context vector, generates the
    output (translation)


\aligncenter{\includepng{\diagramsDir/transformers/encoder-decoder-example}{1300px}}

-   **Memory, and gradient stability, remain the key limitation even
    when LSTMs and GRUs are used.**

\subsection{Neural Machine Translation by Jointly Learning to Align and Translate}

  \aligncenter{<table> <tr>
<ul>\includepng{\diagramsDir/transformers/encoder-decoder-example}{1200px}</ul>
<ul>\includepng{\diagramsDir/transformers/LSTM}{700px}</ul>
</tr> </table>\
}

\subsection{Learning Alignment - the first Attention}

\alignright{\includepng{\diagramsDir/transformers/rnnAttention}{600px}}

* Fixed-length context vector was a key performance bottleneck in 2015.
* Bahdanau et al. (2015) propose to (soft-)search for parts of a source <br>sentence that are relevant to predicting a target word.
* The method, based on the Cho et al. (2014) Encoder–Decoder:</li>    
  * **Encoder:** bi-directional RNN.
  * **Decoder:** gated RNN. 
  * **Innovation:** each time-step gets its own separate context vector:
    $$\large c_t = \sum_{j=1}^T ( \alpha_{t,j} h_t)$$
    $$\large \alpha_{t,j} = \frac{\exp(e_{t,j})} {\sum_{k=1}^T\exp(e_{t,k})}$$
    $$\large e_{t,j} = f(s_{t-1}, h_j)$$

*Function $f$ implemented as a fully connected
layer.*

\subsection{Attention, Attention!}

\aligncenter{\includepng{\diagramsDir/transformers/learned_attention}{1100px}}

\subsection{Plan for the Day}

-   Attention, Attention!
-   **Transformers: Attention is All You Need.**
-   Transformer extensions:
    -   Reformers - alternative attention operator
    -   Linformers - linear complexity
    -   Transformer training difficulty\
    -   Switch Transformers
-   Going beyond NLP
    -   Image is Worth 16x16 Words
    -   AlphaFold 2

\subsection{Attention is All You Need}

\aligncenter{\includejpg{\diagramsDir/transformers/attention}{1300px}}


\subsection{Attention is All You Need}

\alignright{\includepng{\diagramsDir/transformers/scaled}{1200px}}

* Scaled dot-product attention (no parameters):

$$ \text{attention}(Q,K,V)=\text{softmax}\left(\frac{QK^{\top}}{\sqrt{d_{K}}}\right) V$$



\subsection{Attention is All You Need}

\aligncenter{\includepng{\diagramsDir/transformers/QKV}{1600px}}


\subsection{Attention is All You Need}

\alignright{\includepng{\diagramsDir/transformers/multihead}{1100px}}

* Scaled dot-product attention (no parameters):

$$ \text{attention}(Q,K,V)=\text{softmax}\left(\frac{QK^{\top}}{\sqrt{d_{K}}}\right) V$$

* Multi-head attention (parameters: $W_0, W_1^Q, W_1^K, W_1^V, \dots$):
$\text{MultiHead}(Q,K,V)=\text{concat}(\text{head}_{1},\dots,\text{head}_{h})
W_{0}$ $\text{head}_i=\text{attention}(QW_i^Q, KW_i^K, VW_i^V)$

\subsection{Attention is All You Need: the Transformer}

\aligncenter{
<table>
<tr>
<td>\includepng{\diagramsDir/transformers/rnnAttention}{575px}</td>
<td>\includepng{\diagramsDir/transformers/transformer}{675px}</td>
</tr>
</table>
}

\subsection{Attention is All You Need}

\aligncenter{*The Transformer
achieves better BLEU scores than previous state-of-the-art models on the
English-to-German <br> and English-to-French newstest 2014
tests at a fraction of the training
cost.*}

\aligncenter{\includepng{\diagramsDir/transformers/transformer_perf}{1500px}}


\subsection{Plan for the Day}

-   Attention, Attention!
-   Transformers: Attention is All You Need.
-   **Transformer extensions:**
    -   Reformers - alternative attention operator
    -   Linformers - linear complexity
    -   Transformer training difficulty\
    -   Switch Transformers
-   Going beyond NLP
    -   Image is Worth 16x16 Words
    -   AlphaFold 2

\subsection{Reformers}


\aligncenter{\includejpg{\diagramsDir/transformers/reformers}{1300px}}


\subsection{Reformers: Locality Sensitive Hashing}

\aligncenter{*Rather than
attending all-to-all, split the sequence up. Kitaev et al. (2020) employ
a hashing scheme first proposed by Andoni et al. (2015).*}

\aligncenter{\includepng{\diagramsDir/transformers/reformer_mechanism}{1500px}}


\subsection{Reformers performance}


\aligncenter{\includepng{\diagramsDir/transformers/reformer_performance}{1400px}}


\aligncenter{*Loss: log-likelihood and perplexity expressed in bits per dimension.*}


\subsection{Linformers}


\aligncenter{\includejpg{\diagramsDir/transformers/linformers}{1300px}}


\subsection{Linformers}

* Basic attention (no parameters):

    $$ \text{attention}(Q,K,V)=\underbrace{\text{softmax}\left(\frac{QK^{\top}}{\sqrt{d_{K}}}\right)}_\text{P} V$$

* Wang et al. prove theoretically and check empirically that P is low rank.


\aligncenter{\includepng{\diagramsDir/transformers/linformer_eigen}{1600px}}


\subsection{Linformers}


\aligncenter{*The idea is very simple - add a simple projection between the weighted K, Q and their joint dot product. <br>This fixes to a constant the dimension of the matrices entering the self-attention mechanism.*}


\aligncenter{\includepng{\diagramsDir/transformers/linformer_arch}{1200px}}


\subsection{Linformers performance}


\aligncenter{\includepng{\diagramsDir/transformers/linformer_performance}{1400px}}


\subsection{Training Transformers}


\aligncenter{\includejpg{\diagramsDir/transformers/training}{1300px}}


\subsection{Layer Normalization in Transformers}

\aligncenter{\includepng{\diagramsDir/transformers/layerNorm}{1400px}}

\subsection{Training Transformers}

<table>
<tr>
<th> \aligncenter{Unbalanced Gradients} </th>
<th> \aligncenter{Amplification-induced Instability} </th></tr>
<tr>
<td> \includepng{\diagramsDir/transformers/training_sec3}{1200px} </td>
<td> \includepng{\diagramsDir/transformers/training_sec4}{1050px} </td>
</tr>

</table>


\subsection{Switch Transformers}


\aligncenter{\includejpg{\diagramsDir/transformers/switch}{1300px}}


\subsection{Switch Transformers}

\aligncenter{\includepng{\diagramsDir/transformers/switch}{1200px}}

\subsection{Switch Transformers - speed-up}

\aligncenter{\includepng{\diagramsDir/transformers/switch_speed}{1200px}}

\subsection{Switch Transformers - multi-task performance}

\aligncenter{\includepng{\diagramsDir/transformers/switch_multitask}{1900px}}

\subsection{Plan for the Day}

-   Attention, Attention!
-   Transformers: Attention is All You Need.
-   Transformer extensions:
    -   Reformers - alternative attention operator
    -   Linformers - linear complexity
    -   Transformer training difficulty\
    -   Switch Transformers
-   **Going beyond NLP**
    -   Image is Worth 16x16 Words
    -   AlphaFold 2

\subsection{Image is Worth 16x16 Words Embedding and Architecture}

\aligncenter{\includepng{\diagramsDir/transformers/image16wordsModel}{1400px}}


\subsection{Image is Worth 16x16 Words}
 
\aligncenter{\includepng{\diagramsDir/transformers/image16wordsViz}{2000px}}


\subsection{Image is Worth 16x16 Words}

 
\aligncenter{\includepng{\diagramsDir/transformers/image16wordsRes}{1100px}}

<ul>
\aligncenter{\includepng{\diagramsDir/transformers/image16wordsRes2}{800px}}
</ul>

<ul>
\aligncenter{\includepng{\diagramsDir/transformers/image16wordsRes3}{800px}}
</ul>


\subsection{AlphaFold - the protein folding problem}


\aligncenter{\includegif{\diagramsDir/transformers/protein}{1600px}}


\subsection{Convolutional solution: AlphaFold 1}

 <table> <tr>
<td>\aligncenter{\includepng{\diagramsDir/transformers/AlphaFold1a}{1100px}}</td>
<td>\aligncenter{\includepng{\diagramsDir/transformers/AlphaFold1}{1000px}}</td>
</tr> </table>

\subsection{Transformer-based solution: AlphaFold 2}

 <table> <tr>
<td>\aligncenter{\includepng{\diagramsDir/transformers/AlphaFold}{1800px}}</td>
<td>\aligncenter{\includejpg{\diagramsDir/transformers/AlphaFold_performance}{1200px}}</td>
</tr> </table>

\subsection{Summary of the Day}

-   Attention, Attention!
-   Transformers: Attention is All You Need.
-   Transformer extensions:
    -   Reformers - alternative attention operator
    -   Linformers - linear complexity
    -   Transformer training difficulty\
    -   Switch Transformers
-   Going beyond NLP
    -   Image is Worth 16x16 Words
    -   AlphaFold 2



