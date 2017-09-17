### Reinforcement Learning

* The final domain of learning we will review is known as reinforcement learning. 

* Many researchers seem to believe is offering a route to *general intelligence*.

* Idea of general intelligence is develop algorithms that are adaptable to many different circumstances.

### Reinforcement Learning

* Supervised learning algorithms are designed to resolve particular challenges.

* Data is annotated with those challenges in mind.

* Unsupervised attempts to build representations without any context. 

### "Reward"

* In reinforcement learning some context is given, in the form of a reward. But it is often *delayed*

* Credit allocation problem: many actions that affected the outcome, but which actions had a positive effect and which a negative effect?

### A/B Testing and Reward

* Advert clicks can be seen as a reward.

* Testing the customer experience, A/B testing, prioritises short term reward.

* The internet is currently being driven by short term rewards which make it distracting in the short term, but perhaps less useful in the long term.

* Click-bait is an example, but there are more subtle effects.

* Success of Facebook is driven by its ability to draw us in when likely we should be doing something else. This is driven by large scale A/B testing. 

### Longer Term

* One open question is how to drive non-visual interfaces through equivalents to A/B testing.

* Speech interfaces, such as those used in intelligent agents, are less amenable to A/B testing when determining the quality of the interface.

* Improving interaction with them is therefore less exact science than the visual interface.

### Data Efficiency

* Data efficient reinforcement learning methods are likely to be key to improving these agent's ability to interact.

* However, they are not yet mature enough to be deployed yet. 

### Game Play

* Reinforcement learning methods have been deployed with high profile success is game play.

* Reward is delayed to the end of the game, victory or defeat.

* Can acquire lots of data through simulation.

* Many of the recent advances in reinforcement learning have occurred with methods that are not data efficient. 

### DeepMind

* The company DeepMind is set up around reinforcement learning as an approach to general intelligence.

* Best known achievements are centered around artificial intelligence in game play.

* For example, Atari game play and AlphaGo. 

### Deep Q Learning

* DeepMind uses an approach to Machine Learning where there are two mathematical functions at work.

* The *policy function* determines the action to be taken at any given moment,

* The *value function* estimates the quality of a board position at any given time.

* In AlphaGo make use of convolutional neural networks for both these models. 

### AlphaGo

* Go was considered a challenge for artificial intelligence for two reasons.

1. Game tree has a very high `branching factor'.

    In Go, there are so many legal moves that the game tree increases exponentially. 

2. Evaluating the quality of any given board position was deemed to be very hard.[^chess].

* AlphaGo played more than 30,000,000 games to learn value and policy.

### Model Based Approach

* An alternative approach to reinforcement learning is to use a prediction function.

* This is similar to *classical control* and field of *system identification*.

* Known as *model based* reinforcement learning.

### Optimization Methods

* Reinforcement learning can also used to improve user experience.

* Reward is gained when the user buys a product from us.

* This makes it closely allied to the area of optimization.

* Optimization of our user interfaces is like reinforcement learning task, but normally approached through *Bayesian optimization* or *bandit learning*.

### Optimization

* Normal optimization we have a mathematical representation of our objective function as a direct function of the parameters.

* In Bayesian Optimization we don't.

* E.g. Examples in this form of optimization include:

1. What is the best user interface for presenting adverts?

2. What is the best design of wing for an F1 car?

3. Which product should I return top of the list in response to this user's search?

### Bayesian Optimization

* Can't directly relate the parameters in the system of interest to our objective through a mathematical function.

* E.g. What is the mathematical function that relates a user's experience to the probability that they will buy a product? 

### Bayesian Optimization

* Use machine learning to develop a  *surrogate model* for the optimization task.

* Surrogate model is a prediction function that attempts to recreate the process we are finding hard to model.

* Try to simultaneously fit the surrogate model and optimize the process.

### Surrogate Models

* Bayesian optimization methods use a *surrogate model* (normally a specific form of regression model).

* Use this to predict how the real system will perform.

* Optimize in the surrogate model. 


### Conclusion

* Introduce range of ML approaches.

* Focussed on where they use mathematical functions as a general overview.

