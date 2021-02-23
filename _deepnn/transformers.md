---
layout: lecture
title: Transformers
week: 5
session: 2
date: 2021-02-23
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
time: "14:00"
start: "14:00"
end: "15:00"
---

\include{talk-macros.gpp}

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


\aligncenter{<img src=inputs3/encoder-decoder-example.png alt="Drawing" style="width: 1300px;"/>}

-   **Memory, and gradient stability, remain the key limitation even
    when LSTMs and GRUs are used.**

\subsection{Neural Machine Translation by Jointly Learning to Align and Translate}

  \aligncenter{<table> <tr>
<ul><img src=inputs3/encoder-decoder-example.png alt="Drawing" style="width: 1200px;"/></ul>
<ul><img src=inputs3/LSTM.png alt="Drawing" style="width: 700px;"/></ul>
</tr> </table>\
}

\subsection{Learning Alignment - the first Attention}

<p><img src=inputs3/rnnAttention.png align="right" alt="Drawing" style="width: 600px;"/>
<ul>

<li>Fixed-length context vector was a key performance bottleneck in 2015.</li>
<li>Bahdanau et al. (2015) propose to (soft-)search for parts of a source <br>sentence that are relevant to predicting a target word.</li>
<li>The method, based on the Cho et al. (2014) Encoder–Decoder:</li>    
    <ul><li><b>Encoder:</b> bi-directional RNN.</li></ul>
    <ul><li><b>Decoder:</b> gated RNN.</li></ul> 
    <ul><li><b>Innovation:</b> each time-step gets its own separate context vector:</li></ul> 
        <ul><ul><pp> $\large c_t = \sum_{j=1}^{T} ( \alpha_{t,j} h_t)$ </pp></ul></ul>
        <ul><ul><pp> <br> </pp></ul></ul>
        <ul><ul><pp> $\large \alpha_{t,j} = \frac{exp(e_{t,j})} {\sum_{k=1}^{T}e_{t,k}}$ </pp></ul></ul>
        <ul><ul><pp> <br> </pp></ul></ul>
        <ul><ul><pp> $\large e_{t,j} = f(s_{t-1}, h_j)$ </pp></ul></ul>  
</ul>
</p>

 <i>Function $f$ implemented as a fully connected
layer.</i>

\subsection{Attention, Attention!}


\aligncenter{<img src=inputs3/learned_attention.png alt="Drawing" style="width: 1100px;"/>}


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


\aligncenter{<img src=inputs3/attention.jpg alt="Drawing" style="width: 1300px;"/>}


\subsection{Attention is All You Need}

<p><img align="right" src=inputs3/scaled.png alt="Drawing" style="width: 1200px;"/>

<li>Scaled dot-product attention (no parameters):</li>

    <ul><pp>$ attention(Q,K,V)=softmax(\frac{QK^{T}}{\sqrt{d_{K}}}) V$</pp></ul>

<p>


\subsection{Attention is All You Need}

\aligncenter{<img src=inputs3/QKV.png alt="Drawing" style="width: 1600px;"/>}


\subsection{Attention is All You Need}

<p><img align="right" src=inputs3/multihead.png alt="Drawing" style="width: 1100px;"/>

<li>Scaled dot-product attention (no parameters):</li>

    <ul><pp>$ attention(Q,K,V)=softmax(\frac{QK^{T}}{\sqrt{d_{K}}}) V$</pp></ul>

<pp></pp>
<pp></pp>
<pp></pp> <li>Multi-head
attention (parameters: $W_0, W_1^Q, W_1^K, W_1^V, ...$):</li>
<ul><pp>\$
MultiHead(Q,K,V)=concat(head\_{1},\...,head\_{h})
W\_{0}$</pp></ul>  <ul><pp>$ head_i=attention(QW_i\^Q, KW_i\^K,
VW_i\^V)\$</pp></ul> <p>

\subsection{Attention is All You Need: the Transformer}

\aligncenter{

<table>
<tr>
    <ul><img src=inputs3/rnnAttention.png alt="Drawing" style="width: 575px;"/></ul>
    <ul><img src=inputs3/transformer.png alt="Drawing" style="width: 675px;"/></ul>
        </tr>
</table>
}

\subsection{Attention is All You Need}

\aligncenter{<ul><pp><i>The Transformer
achieves better BLEU scores than previous state-of-the-art models on the
English-to-German <br> and English-to-French newstest 2014
tests at a fraction of the training
cost.</i></pp></ul>}

\aligncenter{<img src=inputs3/transformer_perf.png alt="Drawing" style="width: 1500px;"/>}


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


\aligncenter{<img src=inputs3/reformers.jpg alt="Drawing" style="width: 1300px;"/>}


\subsection{Reformers: Locality Sensitive Hashing}

\aligncenter{<ul><pp><i>Rather than
attending all-to-all, split the sequence up. Kitaev et al. (2020) employ
a hashing scheme first proposed by Andoni et al.
(2015).</i></pp></ul>}

\aligncenter{<img src=inputs3/reformer_mechanism.png alt="Drawing" style="width: 1500px;"/>}


\subsection{Reformers performance}


\aligncenter{<img src=inputs3/reformer_performance.png alt="Drawing" style="width: 1400px;"/>}


\aligncenter{<ul><pp><i>Loss: log-likelyhood and perplexity expressed in bits per dimension.</i></pp></ul>}


\subsection{Linformers}


\aligncenter{<img src=inputs3/linformers.jpg alt="Drawing" style="width: 1300px;"/>}


\subsection{Linformers}

<li>Basic attention (no parameters):</li>

    <ul><pp>$ attention(Q,K,V)=\underbrace{softmax(\frac{QK^{T}}{\sqrt{d_{K}}})}_\text{P} V$</pp></ul>

<li>Wang et al. prove theoretically and check empirically that P is low rank.</li>


\aligncenter{<img src=inputs3/linformer_eigen.png alt="Drawing" style="width: 1600px;"/>}


\subsection{Linformers}


\aligncenter{<ul><pp><i>The idea is very simple - add a simple projection between the weighted K, Q and their joint dot product. <br>This fixes to a constant the dimension of the matrices entering the self-attention mechanism. </i></pp></ul>}


\aligncenter{<img src=inputs3/linformer_arch.png alt="Drawing" style="width: 1200px;"/>}


\subsection{Linformers performance}


\aligncenter{<img src=inputs3/linformer_performance.png alt="Drawing" style="width: 1400px;"/>}


\subsection{Training Transformers}


\aligncenter{<img src=inputs3/training.jpg alt="Drawing" style="width: 1300px;"/>}


\subsection{Layer Normalization in Transformers}

\aligncenter{<img src=inputs3/layerNorm.png alt="Drawing" style="width: 1400px;"/>}

\subsection{Training Transformers}


<table>

<tr>
<td> \aligncenter{ <h2> Unbalanced Gradients </h2> } </td>
<td> \aligncenter{ <h2> Amplification-induced Instability </h2> } </td></tr>

<tr>
<td> <img src=inputs3/training_sec3.png alt="Drawing" style="width: 1200px;"/> </td>
<td> <img src=inputs3/training_sec4.png alt="Drawing" style="width: 1050px;"/> </td>
</tr>

</table>


\subsection{Switch Transformers}


\aligncenter{<img src=inputs3/switch.jpg alt="Drawing" style="width: 1300px;"/>}


\subsection{Switch Transformers}

\aligncenter{<img src=inputs3/switch.png alt="Drawing" style="width: 1200px;"/>}

\subsection{Switch Transformers - speed-up}

\aligncenter{<img src=inputs3/switch_speed.png alt="Drawing" style="width: 1200px;"/>}

\subsection{Switch Transformers - multi-task performance}

\aligncenter{<img src=inputs3/switch_multitask.png alt="Drawing" style="width: 1900px;"/>}

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


\aligncenter{<img src=inputs3/image16wordsModel.png alt="Drawing" style="width: 1400px;"/>}


\subsection{Image is Worth 16x16 Words}

 
\aligncenter{<img src=inputs3/image16wordsViz.png alt="Drawing" style="width: 2000px;"/>}


\subsection{Image is Worth 16x16 Words}

 
\aligncenter{<img src=inputs3/image16wordsRes.png alt="Drawing" style="width: 1100px;"/>}

<ul>
\aligncenter{<img src=inputs3/image16wordsRes2.png alt="Drawing" style="width: 800px;"/>}
</ul>

<ul>
\aligncenter{<img src=inputs3/image16wordsRes3.png alt="Drawing" style="width: 800px;"/>}
</ul>


\subsection{AlphaFold - the protein folding problem}


\aligncenter{<img src=inputs3/protein.gif alt="Drawing" style="width: 1600px;"/>}


\subsection{Convolutional solution: AlphaFold 1}

 <table> <tr>
<td>\aligncenter{<img src=inputs3/AlphaFold1a.png  alt="Drawing" style="width: 1100px;"/>}</td>
<td>\aligncenter{<img src=inputs3/AlphaFold1.png  alt="Drawing" style="width: 1000px;"/>}</td>
</tr> </table>

\subsection{Transformer-based solution: AlphaFold 2}

 <table> <tr>
<td>\aligncenter{<img src=inputs3/AlphaFold.png alt="Drawing" style="width: 1800px;"/>}</td>
<td>\aligncenter{<img src=inputs3/AlphaFold_performance.jpg  alt="Drawing" style="width: 1200px;"/>}</td>
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


