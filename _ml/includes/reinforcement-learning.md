\ifndef{reinforcementLearning}
\define{reinforcementLearning}

\editme

\section{Reinforcement Learning}
\newslide{Reinforcement Learning}
\slides{
* The final domain of learning we will review is known as reinforcement learning. 
* Many researchers seem to believe is offering a route to *general intelligence*.
* Idea of general intelligence is develop algorithms that are adaptable to many different circumstances.}
\notes{The final domain of learning we will review is known as reinforcement learning. 
The domain of reinforcement learning is one that many researchers seem to believe is offering a route to *general intelligence*. The idea of general intelligence is to develop algorithms that are adaptable to many different circumstances. Supervised learning algorithms are designed to resolve particular challenges. Data is annotated with those challenges in mind. Unsupervised attempts to build representations without any context. But normally the algorithm designer has an understanding of what the broader objective is and designs the algorithms accordingly (for example, characterizing users). In reinforcement learning some context is given, in the form of a reward, but the reward is normally delayed. There may have been many actions that affected the outcome, but which actions had a positive effect and which a negative effect?}

\newslide{Reinforcement Learning}
\slides{
* Supervised learning algorithms are designed to resolve particular challenges.
* Data is annotated with those challenges in mind.
* Unsupervised attempts to build representations without any context. }

\subsection{"Reward"}

* In reinforcement learning some context is given, in the form of a reward. But it is often *delayed*

* Credit allocation problem: many actions that affected the outcome, but which actions had a positive effect and which a negative effect?

\newslide{A/B Testing and Reward}
\slides{
* Advert clicks can be seen as a reward.
* Testing the customer experience, A/B testing, prioritises short term reward.
* The internet is currently being driven by short term rewards which make it distracting in the short term, but perhaps less useful in the long term.
* Click-bait is an example, but there are more subtle effects.
* Success of Facebook is driven by its ability to draw us in when likely we should be doing something else. This is driven by large scale A/B testing.}
\notes{One issue for many companies is that the best way of testing the customer experience, A/B testing, prioritizes short term reward. The internet is currently being driven by short term rewards which make it distracting in the short term, but perhaps less useful in the long term. Click-bait is an example, but there are more subtle effects. The success of Facebook is driven by its ability to draw us in when likely we should be doing something else. This is driven by large scale A/B testing.}



\newslide{Longer Term}
\slides{
* One open question is how to drive non-visual interfaces through equivalents to A/B testing.
* Speech interfaces, such as those used in intelligent agents, are less amenable to A/B testing when determining the quality of the interface.
* Improving interaction with them is therefore less exact science than the visual interface.}
\notes{One open question is how to drive non-visual interfaces through equivalents to A/B testing. Speech interfaces, such as those used in intelligent agents, are less amenable to A/B testing when determining the quality of the interface. Improving interaction with them is therefore less exact science than the visual interface. Data efficient reinforcement learning methods are likely to be key to improving these agent's ability to interact with the user and understand intent. However, they are not yet mature enough to be deployed in this application.} 

\newslide{Data Efficiency}
\slides{
* Data efficient reinforcement learning methods are likely to be key to improving these agent's ability to interact.
* However, they are not yet mature enough to be deployed yet.}

\subsection{Game Play}
\slides{
* Reinforcement learning methods have been deployed with high profile success is game play.
* Reward is delayed to the end of the game, victory or defeat.
* Can acquire lots of data through simulation.
* Many of the recent advances in reinforcement learning have occurred with methods that are not data efficient.}
\notes{An area where reinforcement learning methods have been deployed with high profile success is game play. In game play the reward is delayed to the end of the game, and it comes in the form of victory or defeat. A significant advantage of game play as an application area is that, through simulation of the game, it is possible to generate as much data as is required to solve the problem. For this reason, many of the recent advances in reinforcement learning have occurred with methods that are not data efficient.}

\newslide{DeepMind}
\slides{
* The company DeepMind is set up around reinforcement learning as an approach to general intelligence.
* Best known achievements are centered around artificial intelligence in game play.
* For example, Atari game play and AlphaGo. }
\notes{The company DeepMind is set up around reinforcement learning as an approach to general intelligence. All their most well-known achievements are centered around artificial intelligence in game play. In reinforcement learning a decision made at any given time have a downstream effect on the result. Whether the effect if beneficial or not is unknown until a future moment. 

We can think of reinforcement learning as providing a label, but the label is associated with a series of data involving a number of decisions taken. Each decision was taken given the understanding of game play at any given moment. Understanding which of these decisions was important in victory or defeat is a hard problem. 

In machine learning the process of understanding which decisions were beneficial and which were detrimental is known as the credit allocation problem. You wish to reward decisions that led to success to encourage them, but punish decisions that lead to failure.}

\newslide{Deep Q Learning}
\slides{
* DeepMind uses an approach to Machine Learning where there are two mathematical functions at work.
* The *policy function* determines the action to be taken at any given moment,
* The *value function* estimates the quality of a board position at any given time.
* In AlphaGo make use of convolutional neural networks for both these models.}
\notes{Broadly speaking, DeepMind uses an approach to Machine Learning where there are two mathematical functions at work. One determines the action to be taken at any given moment, the other estimates the quality of the board position at any given time. These are respectively known as the *policy network* and the *value network*.[^qlearning] DeepMind made use of convolutional neural networks for both these models.}


\subsection{AlphaGo}
\slides{
* Go was considered a challenge for artificial intelligence for two reasons.
1. Game tree has a very high `branching factor'.
    In Go, there are so many legal moves that the game tree increases exponentially. 
2. Evaluating the quality of any given board position was deemed to be very hard.[^chess].
* AlphaGo played more than 30,000,000 games to learn value and policy.}
\notes{
The ancient Chinese game of Go was considered a challenge for artificial intelligence for two reasons. Firstly, the game tree has a very high branching factor. The game tree is a discrete representation of the game. Every node in the game tree is associated with a board position. You can move through the game tree by making legal a move on the board to change the position. In Go, there are so many legal moves that the game tree increases exponentially. This challenge in Go was addressed by using stochastic game tree search. Rather than exploring the game tree exhaustively they explored it randomly.

Secondly, evaluating the quality of any given board position was deemed to be very hard.[^chess] The value function determines for each player whether they are winning or losing. Skilled Go players can assess a board position, but they do it by instinct, by intuition. Just as early AI researchers struggled to give rules for detecting cancer, it is challenging to give rules to assess a Go board. The machine learning approach that AlphaGo took is to train a value function network to make this assessment. 

[^chess]: The situation in chess is much easier, firstly the number of possible moves at any time is about an order of magnitude lower, meaning the game tree doesn't grow as quickly. Secondly, in chess, there are well defined value functions. For example, a value function could be based on adding together the points that are associated with each piece.

The approach that DeepMind took to conquering Go is a *model-free* approach known as *Q-learning*.[^qlearning] The model-free approach refers to the fact that they don't directly include a model of how the world evolves in the reinforcement learning algorithm. They make extensive use of the game tree, but they don't model how it evolves. They do model the expected reward of each position in the game tree (the value function) but that is not the same as modeling how the game will proceed.

[^qlearning]: The approach was described early on in the history of machine learning by Chris Watkins, during his PhD thesis in the 1980s. It is known as Q-learning. It's recent success in the games domain is driven by the use of deep learning for the policy and value functions as well as the use of fast compute to generate and process very large quantities of data. In its standard form it is not seen as a very data-efficient approach.}

\notes{\subsection{Reinforcement Learning and Classical Control}}
\newslide{Model-Based Approach}
\slides{
* An alternative approach to reinforcement learning is to use a prediction function.
* This is similar to *classical control* and field of *system identification*.
* Known as *model-based* reinforcement learning.}
\notes{An alternative approach to reinforcement learning is to use a prediction function to suggest how the world will evolve in response to your actions. To predict how the game tree will evolve. You can then use this prediction to indirectly infer the expected reward associated with any action. This is known as *model-based* reinforcement learning.

This model-based approach is also closer to a control system. A classical control system is one where you give the system a set point. For example, a thermostat in the house. You set the temperature and the boiler switches off when it reaches it. Optimal control is about getting the house to the right temperature as quickly as possible. Classical control is widely used in robotic control and flight control.

One interesting crossover between classical control and machine learning arises because classical optimal control can be seen as a form of model-based reinforcement learning. One where the reward is recovered when the set point is reached. In control engineering the prediction function is known as the *transfer function*. The process of fitting the transfer function in control is known as *system identification*. 

There is some exciting work emerging at the interface between the areas of control and reinforcement learning. Results at this interface could be very important for improving the quality of robotic and drone control.}


\subsection{Optimization Methods}
\slides{
* Reinforcement learning can also used to improve user experience.
* Reward is gained when the user buys a product from us.
* This makes it closely allied to the area of optimization.
* Optimization of our user interfaces is like reinforcement learning task, but normally approached through *Bayesian optimization* or *bandit learning*.}
\notes{As we implied above, reinforcement learning can also used to improve user experience. In that case the reward is gained when the user buys a product from us. This makes it closely allied to the area of optimization. Optimization of our user interfaces can be seen as a reinforcement learning task, but more commonly it is thought about separately in the domains of *Bayesian optimization* or *bandit learning*.}


\newslide{Optimization}
\slides{
* Normal optimization we have a mathematical representation of our objective function as a direct function of the parameters.
* In Bayesian Optimization we don't.
* E.g. Examples in this form of optimization include:
1. What is the best user interface for presenting adverts?
2. What is the best design of wing for an F1 car?
3. Which product should I return top of the list in response to this user's search?}
\notes{We use optimization in machine learning to find the parameters of our models. We can do that because we have a mathematical representation of our objective function as a direct function of the parameters. 

Examples in this form of optimization include, what is the best user interface for presenting adverts? What is the best design for a front wing for an F1 racing car? Which product should I return top of the list in response to this user's search?

Bayesian optimization arises when we can't directly relate the parameters in the system of interest to our objective through a mathematical function. For example, what is the mathematical function that relates a user's experience to the probability that they will buy a product?}

\subsection{Bayesian Optimization}
\slides{
* Can't directly relate the parameters in the system of interest to our objective through a mathematical function.
* E.g. What is the mathematical function that relates a user's experience to the probability that they will buy a product?}

\newslide{Bayesian Optimization}
\slides{
* Use machine learning to develop a  *surrogate model* for the optimization task.
* Surrogate model is a prediction function that attempts to recreate the process we are finding hard to model.
* Try to simultaneously fit the surrogate model and optimize the process.}
\notes{One approach to these problems is to use machine learning methods to develop a *surrogate model* for the optimization task. The surrogate model is a prediction function that attempts to recreate the process we are finding hard to model. We try to simultaneously fit the surrogate model and optimize the process.}

\subsection{Surrogate Models}
\slides{
* Bayesian optimization methods use a *surrogate model* (normally a specific form of regression model).
* Use this to predict how the real system will perform.
* Optimize in the surrogate model.}
\notes{Bayesian optimization methods use a *surrogate model* (normally a specific form of regression model). They use this to predict how the real system will perform. The surrogate model makes a prediction (with an estimate of the uncertainty) of what the response will be to any given input. Parameters to test are chosen by considering this prediction. Similar to reinforcement learning, this can be viewed as a *model-based* approach because the surrogate model can be seen as a model of the real world. In bandit methods strategies are determined without turning to a model to motivate them. They are *model free* methods.}

\subsection{Model-Based and Model Free: Performance}

\notes{Because of their different philosophies, if a class of prediction functions is chosen, then a model-based approach might have better average case performance. At least in terms of *data efficiency*. A model free approach may well have better worst-case performance though, because it makes less assumptions about the nature of the data. To put it another way, making assumptions about the data is helpful if they are right: and if the model is sensible they'll be right on average. However, it is unhelpful if the model is wrong. Indeed, it could be actively damaging. Since we can't usually guarantee the model is absolutely right, the worst-case performance of a model-based approach would be poor.}


\endif




