\ifndef{dimensionalityReductionIntro}
\define{dimensionalityReductionIntro}

\editme

\subsection{Dimensionality Reduction}
\slides{
* Compress the data by replacing the original data with reduced number of continuous variables.}
\notes{Dimensionality reduction methods compress the data by replacing the original data with a reduced number of continuous variables. One way of thinking of these methods is to imagine a marionette.}

\figure{\includediagramclass{\diagramsDir/ml/marionette}{40%}}{Thinking of dimensionality reduction as a marionette. We observe the high dimensional pose of the puppet, $\inputVector$, but the movement of the puppeteer's hand, $\latentVector$ remains hidden to us. Dimensionality reduction aims to recover those hidden movements which generated the observations.}{marionette}

\newslide{Dimensionality Reduction}
\slides{
* Position of each body part of a marionette could be thought of as our data, $\inputVector_i$.
* Each data point is the 3-D co-ordinates of all the different body parts 
* Movement of parts determined by puppeteer via strings.
* For a simple puppet with one stick can move the stick up and down, left and right and twist.}
\notes{The position of each body part of a marionette could be thought of as our data, $\inputVector_i$. So, each data point consists of the 3-D co-ordinates of all the different body parts of the marionette. Let's say there are 13 different body parts (2 each of feet, knees, hips, hands, elbows, shoulders, one head). Each body part has an x, y, z position in Cartesian coordinates. So that's 39 numbers associated with each observation.} 


\newslide{Dimensionality Reduction}
\slides{
* This gives three parameters in the puppeteers control.
* Implies that the puppet we see moving is controlled by only 3 variables.
* These 3 variables are often called the hidden or *latent variables*. 
* Assume similar for real world data, observations are derived from lower dimensional underlying process}
\notes{The movement of these 39 parts is determined by the puppeteer via strings. Let's assume it's a very simple puppet, with just one stick to control it. The puppeteer can move the stick up and down, left and right. And they can twist it. This gives three parameters in the puppeteers control. This implies that the 39 variables we see moving are controlled by only 3 variables. These 3 variables are often called the hidden or *latent variables*. 

Dimensionality reduction assumes something similar for real world data. It assumes that the data we observe is generated from some lower dimensional underlying process. It then seeks to recover the values associated with this low dimensional process.} 

\subsubsection{Examples in Social Sciences}
\slides{
* Underpins *psychological scoring* such as *IQ* or *personality tests*
* Myers-Briggs assumes personality is four dimensional.
* Political belief (left/right wing).
* Also language modelling has taken similar approaches: [word2vec](https://arxiv.org/abs/1301.3781)}
\notes{Dimensionality reduction techniques underpin a lot of psychological scoring tests such as IQ tests or personality tests. An IQ test can involve several hundred questions, potentially giving a rich, high dimensional, characterization of some aspects of your intelligence. It is then summarized by a single number. Similarly, the Myers-Briggs personality test involves answering questions about preferences which are reduced to a set of numbers reflecting personality.

These tests are assuming that our intelligence is implicitly one-dimensional and that our personality is implicitly four dimensional. Other examples include political belief which is typically represented on a left to right scale. A one-dimensional distillation of an entire philosophy about how a country should be run. Our own leadership principles imply that our decisions have a fourteen-dimensional space underlying them. Each decision could be characterized by judging to what extent it embodies each of the principles. 

Political belief, personality, intelligence, leadership. None of these exist as a directly measurable quantity in the real world, rather they are inferred based on measurables. Dimensionality reduction is the process of allowing the computer to automatically find such underlying dimensions. This automatically allowing us to characterize each data point according to those explanatory variables. Each of these characteristics can be scored, and individuals can then be turned into vectors. 

This doesn't only apply to individuals, in recent years work on language modeling has taken a similar approach to words. The [word2vec](https://arxiv.org/abs/1301.3781) algorithm performed a dimensionality reduction on words, now you can take any word and map it to a latent space where similar words exhibit similar characteristics. A 'personality space' for words.}

\endif
