\newslide{Probability Review}

\slides{
* We are interested in trials which result in two random variables,
  $X$ and $Y$, each of which has an ‘outcome’
  denoted by $x$ or $y$.
* We summarise the notation and terminology for these distributions in
  the following table.}

\newslide{ }

Terminology | Mathematical notation | Description
------|-------------|-------------
joint | $P(X=x, Y=y)$ | prob. that X=x *and* Y=y
marginal | $P(X=x)$ | prob. that X=x *regardless of* Y
conditional | $P(X=x\vert Y=y)$ | prob. that X=x *given that* Y=y

\aligncenter{The different basic probability distributions.}
  

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.prob_diagram(diagrams='../slides/diagrams/mlai')}

\subsection{A Pictorial Definition of Probability}

\setupplotcode{import teaching_plots as plot}

\plotcode{plot.prob_diagram(diagrams='../slides/diagrams')}

\includesvg{../slides/diagrams/mlai/prob_diagram.svg}

\alignright{Inspired by lectures from Christopher Bishop}

\subsection{Definition of probability distributions}

Terminology       |              Definition                  |      Probability Notation
------------------|------------------------------------------|------------------------------
Joint Probability | $\lim_{N\rightarrow\infty}\frac{n_{X=3,Y=4}}{N}$ | $P\left(X=3,Y=4\right)$ 
Marginal Probability |  $\lim_{N\rightarrow\infty}\frac{n_{X=5}}{N}$ | $P\left(X=5\right)$
Conditional Probability | $\lim_{N\rightarrow\infty}\frac{n_{X=3,Y=4}}{n_{Y=4}}$ | $P\left(X=3\vert Y=4\right)$
 

\subsection{Notational Details}

\slides{
* Typically we should write out $P\left(X=x,Y=y\right)$.

* In practice, we often use $P\left(x,y\right)$.
* This looks very much like we might write a multivariate function, *e.g.*  $f\left(x,y\right)=\frac{x}{y}$.
  * For a multivariate function though, $f\left(x,y\right)\neq f\left(y,x\right)$.
  * However $P\left(x,y\right)=P\left(y,x\right)$ because $P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right)$.
* We now quickly review the ‘rules of probability’.}

\notes{Typically we should write out
$P\left(X=x,Y=y\right)$, but in practice we often shorten this to $P\left(x,y\right)$. This looks very much like we might write a multivariate function, *e.g.*
  $$
  f\left(x,y\right)=\frac{x}{y},
  $$ 
but for a multivariate function
$$
f\left(x,y\right)\neq f\left(y,x\right).
$$
However,
$$
P\left(x,y\right)=P\left(y,x\right)
$$
because
$$
P\left(X=x,Y=y\right)=P\left(Y=y,X=x\right).
$$
Sometimes I think of this as akin to the way in Python we can write 'keyword arguments' in functions. If we use keyword arguments, the ordering of arguments doesn't matter.}

\notes{We've now introduced conditioning and independence to the notion of probability and computed some conditional probabilities on a practical example The scatter plot of deaths vs year that we created above can be seen as a *joint* probability distribution. We represent a joint probability using the notation $P(Y=y, X=x)$ or $P(y, x)$ for short. Computing a joint probability is equivalent to answering the simultaneous questions, what's the probability that the number of nurses was over 2 and the number of doctors was 1? Or any other question that may occur to us. Again we can easily use pandas to ask such questions.}

\code{num_doctors = 1
large = (data.num_nurses_fulltime[data.num_doctors_fulltime==num_doctors]>2).sum()
total_facilities = data.num_nurses_fulltime.count() # this is total number of films
prob_large = float(large)/float(total_facilities)
print("Probability of nurses being greater than 2 and number of doctors being", num_doctors, "is:", prob_large)}

\newslide{Normalization}

\slides{
*All* distributions are normalized. This is clear from the fact that
$\sum_{x}n_{x}=N$, which gives
$$\sum_{x}P\left(x\right)={\lim_{N\rightarrow\infty}}\frac{\sum_{x}n_{x}}{N}={\lim_{N\rightarrow\infty}}\frac{N}{N}=1.$$
A similar result can be derived for the marginal and conditional
distributions.}

\subsection{The Product Rule}

\slides{
* $P\left(x|y\right)$ is
  $$
  {\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{n_{y}}.
  $$
* $P\left(x,y\right)$ is
  $$
  {\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{N}={\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{n_{y}}\frac{n_{y}}{N}
  $$
  or in other words
  $$
  P\left(x,y\right)=P\left(x|y\right)P\left(y\right).
  $$
  This is known as the product rule of probability.}
	
\notes{This number is the joint probability, $P(Y, X)$ which is
much *smaller* than the conditional probability. The number can never be bigger
than the conditional probabililty because it is computed using the *product
rule*.
$$
p(Y=y, X=x) = p(Y=y|X=x)p(X=x)
$$
and $$p(X=x)$$ is a probability distribution, which is equal or less than 1, ensuring the joint distribution is typically smaller than the conditional distribution.}

\notes{The product rule is a *fundamental* rule of probability, and you must remember it! It gives the relationship between the two questions: 1) What's the probability that a facility has over two nurses *and* one doctor? and 2) What's the probability that a facility has over two nurses *given that* it has one doctor?}

\notes{In our shorter notation we can write the product rule as
$$
p(y, x) = p(y|x)p(x)
$$
We can see the
relation working in practice for our data above by computing the different
values for $x=1$.}

\code{num_doctors=1
num_nurses=2
p_x = float((data.num_doctors_fulltime==num_doctors).sum())/float(data.num_nurses_fulltime.count())
p_y_given_x = float((data.num_nurses_fulltime[data.num_doctors_fulltime==num_doctors]>num_nurses).sum())/float((data.num_doctors_fulltime==num_doctors).sum())
p_y_and_x = float((data.num_nurses_fulltime[data.num_doctors_fulltime==num_doctors]>num_nurses).sum())/float(data.num_nurses_fulltime.count())

print("P(x) is", p_x)
print("P(y|x) is", p_y_given_x)
print("P(y,x) is", p_y_and_x)}

\subsection{The Sum Rule}

\slides{Ignoring the limit in our definitions:
* The marginal probability $P\left(y\right)$ is ${\lim_{N\rightarrow\infty}}\frac{n_{y}}{N}$ .
* The joint distribution $P\left(x,y\right)$ is ${\lim_{N\rightarrow\infty}}\frac{n_{x,y}}{N}$.
* $n_{y}=\sum_{x}n_{x,y}$ so
  $$
  {\lim_{N\rightarrow\infty}}\frac{n_{y}}{N}={\lim_{N\rightarrow\infty}}\sum_{x}\frac{n_{x,y}}{N},
  $$
  in other words
  $$
  P\left(y\right)=\sum_{x}P\left(x,y\right).
  $$
  This is known as the sum rule of probability.}

\notes{The other *fundamental rule* of probability is the *sum rule*
this tells us how to get a *marginal* distribution from the joint distribution.
Simply put it says that we need to sum across the value we'd like to remove.
$$
P(Y=y) = \sum_{x} P(Y=y, X=x)
$$
Or in our shortened notation
$$
P(y) = \sum_{x} P(y, x)
$$}

\codeassignment{Write code that computes $P(y)$ by adding $P(y, x)$
for all values of $x$.}{3}{10}

\subsection{Bayes’ Rule}

\slides{
* From the product rule,
  $$
  P\left(y,x\right)=P\left(x,y\right)=P\left(x|y\right)P\left(y\right),$$
  so
  $$
  P\left(y|x\right)P\left(x\right)=P\left(x|y\right)P\left(y\right)
  $$
  which leads to Bayes’ rule,
  $$
  P\left(y|x\right)=\frac{P\left(x|y\right)P\left(y\right)}{P\left(x\right)}.
  $$
}

\notes{Bayes rule is a very simple rule, it's hardly worth the name of a rule at all. It follows directly from the product rule of probability. Because $P(y, x) = P(y|x)P(x)$ and by symmetry $P(y,x)=P(x,y)=P(x|y)P(y)$ then by equating these two equations and dividing through by $P(y)$ we have
$$
P(x|y) =
\frac{P(y|x)P(x)}{P(y)}
$$
which is known as Bayes' rule (or Bayes's rule, it depends how you choose to pronounce it). It's not difficult to derive, and its importance is more to do with the semantic operation that it enables. Each of these probability distributions represents the answer to a question we have about the world. Bayes rule (via the product rule) tells us how to *invert* the probability.}

\newslide{Bayes' Theorem Example}

\slides{* There are two barrels in front of you. Barrel One contains 20 apples and 4 oranges. Barrel Two other contains 4 apples and 8 oranges. You choose a barrel randomly and select a fruit. It is an apple. What is the probability that the barrel was Barrel One?}

\newslide{Bayes’ Theorem Example: Answer I}

\slides{
* We are given that: 
  $$\begin{aligned}
    P(\text{F}=\text{A}|\text{B}=1) = & 20/24 \\
    P(\text{F}=\text{A}|\text{B}=2) = & 4/12 \\
    P(\text{B}=1) = & 0.5 \\
    P(\text{B}=2) = & 0.5
  \end{aligned}$$
}

\newslide{Bayes’ Theorem Example: Answer II}

\slides{
* We use the sum rule to compute: 
  $$\begin{aligned}
    P(\text{F}=\text{A}) = & P(\text{F}=\text{A}|\text{B}=1)P(\text{B}=1) \\& + P(\text{F}=\text{A}|\text{B}=2)P(\text{B}=2) \\
          = & 20/24\times 0.5 + 4/12 \times 0.5 = 7/12
   \end{aligned}$$
* And Bayes’ theorem tells us that: 
  $$\begin{aligned}
    P(\text{B}=1|\text{F}=\text{A}) = & \frac{P(\text{F} = \text{A}|\text{B}=1)P(\text{B}=1)}{P(\text{F}=\text{A})}\\ 
         = & \frac{20/24 \times 0.5}{7/12} = 5/7
  \end{aligned}$$}


\newslide{Reading & Exercises}

\slides{
* @Bishop:book06 on probability distributions: page 12–17 (Section 1.2).
* Complete Exercise 1.3 in @Bishop:book06.}

\include{_ml/includes/probability-examples.md}

\notes{
\subsection{Probabilities for Extracting Information from Data}

What use is all this probability in data science? Let's think about how we might use the probabilities to do some decision making. Let's look at the
information data.}

\code{data.columns}

\writeassignment{Now we see we have several additional features. Let's assume we want to predict `maternal_health_delivery_services`. How would we go about
doing it? 

Using what you've learnt about joint, conditional and marginal
probabilities, as well as the sum and product rule, how would you formulate the
question you want to answer in terms of probabilities? Should you be using a
joint or a conditional distribution? If it's conditional, what should the
distribution be over, and what should it be conditioned on?}{4}{20}

