\newslide{Bernoulli Distribution}

\slides{* Binary classification: need a probability distribution for discrete variables. 
* Discrete probability is in some ways easier:  $P(\dataScalar=1) = \pi$ & specify distribution as a table.}
\notes{Our focus has been on models where the objective function is inspired by a probabilistic analysis of the problem. In particular we've argued that we answer questions about the data set by placing probability distributions over the various quantities of interest. For the case of binary classification this will normally involve introducing probability distributions for discrete variables. Such probability distributions, are in some senses easier than those for continuous variables, in particular we can represent a probability distribution over $\dataScalar$, where $\dataScalar$ is binary, with one value. If we specify the probability that $\dataScalar=1$ with a number that is between 0 and 1, i.e. let's say that $P(\dataScalar=1) = \pi$ (here we don't mean $\pi$ the number, we are setting $\pi$ to be a variable) then we can specify the probability distribution through a table.}

| \dataScalar      | 0
| 1     |
|:------:|:---------:|:-----:|
| $P(\dataScalar)$ | $(1-\pi)$ | $\pi$ |

* Mathematically we use a trick: use $\dataScalar$ as a mathematical switch:
  $$
  P(\dataScalar) = \pi^\dataScalar (1-\pi)^{(1-\dataScalar)}
  $$
  This is the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution).}

\newslide{Mathematical Switch}

\slides{* The Bernoulli distribution}\notes{Mathematically we can use a trick to implement this same table. We can use the value $\dataScalar$ as a mathematical switch and write that}
  $$
  P(\dataScalar) = \pi^\dataScalar (1-\pi)^{(1-\dataScalar)}
  $$
\notes{where our probability distribution is now written as a function of $\dataScalar$. This probability distribution is known as the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution). The Bernoulli distribution is a clever trick for mathematically switching between two probabilities if we were to write it as code it would be better described as}\slides{
* Is a clever trick for switching probabilities, as code it would be}

```python
def bernoulli(y_i, pi):
    if y_i == 1:
        return pi
else:
        return 1-pi
```

\notes{If we insert $\dataScalar=1$ then the function is equal to $\pi$, and if we insert $\dataScalar=0$ then the function is equal to $1-\pi$. So the function recreates the table for the distribution given above.}

\newslide{Jacob Bernoulli's Bernoulli}

\slides{* Bernoulli described the Bernoulli distribution in terms of an 'urn' filled with balls.
* There are red and black balls. There is a fixed number of balls in the urn.
* The portion of red balls is given by $\pi$.
* For this reason in Bernoulli's distribution there is *epistemic* uncertainty about the distribution parameter.}
\notes{The probability distribution is named for [Jacob Bernoulli](http://en.wikipedia.org/wiki/Jacob_Bernoulli), the swiss mathematician. In his book Ars Conjectandi he considered the distribution and the result of a number of 'trials' under the Bernoulli distribution to form the *binomial* distribution. Below is the page where he considers Pascal's triangle in forming combinations of the Bernoulli distribution to realise the binomial distribution for the outcome of positive trials.}

\setupcode{import pods}
\displaycode{pods.notebook.display_google_book('CF4UAAAAQAAJ', 87)}

\setupcode{from matplotlib.patches import Circle}
\plotcode{fig, ax = plt.subplots(figsize=(7,7))
ax.plot([0, 0, 1, 1], [1, 0, 0, 1], linewidth=3, color=[0,0,0])
ax.set_axis_off()
ax.set_aspect('equal')
black_prob = 0.3
ball_radius = 0.1
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
t = np.linspace(0, 2*np.pi, 24)
rows = 4
cols = round(1/ball_radius)
last_row_cols = 3;
for row in range(rows):
    if row == rows-1:
      cols = last_row_cols

    for col in range(cols):
        ball_x = col*2*ball_radius + ball_radius
        ball_y = row*2*ball_radius + ball_radius
        x = ball_x*np.ones(t.shape) + ball_radius*np.sin(t)
        y = ball_y*np.ones(t.shape) + ball_radius*np.cos(t);
  
        if np.random.rand()<black_prob:
            ball_color = [0, 0, 0]
        else: 
            ball_color = [1, 0, 0]
        plt.sca(ax)
        handle = Circle((ball_x, ball_y), ball_radius, fill=True, color=ball_color, figure=fig)
        print(ball_x, ball_y, ball_radius)}

\matlabcode{
      blackProb = 0.3;
      ballRadius = 0.1;
      set(gca, 'xlim', [0 1], 'ylim', [0 1])
      t = 0:pi/24:2*pi;
      rows = 4;
      cols = 1/ballRadius;
      lastRowCols = 3;
      for row = 0:rows-1
        if row == rows-1
          cols = lastRowCols;
        end
        for col = 0:cols-1
          ballX = col*2*ballRadius+ballRadius;
          ballY = row*2*ballRadius + ballRadius;
          x = ballX*ones(size(t)) + ballRadius*sin(t);
          y = ballY*ones(size(t)) + ballRadius*cos(t);
          if rand<blackProb
            ballColor = blackColor;
          else 
            ballColor = redColor;
          end
          handle = patch(x', y', ballColor);
        end
      end
      printLatexPlot('bernoulliUrn', '../../../ml/tex/diagrams/', plotWidth);
      }
    \end{comment}

\newslide{Thomas Bayes's Bernoulli}

\slides{* Bayes described the Bernoulli distribution (he didn't call it that!) in terms of a table and two balls.
* Each ball is rolled so it comes to rest at a uniform distribution across the table.
* The first ball comes to rest at a position that is a $\pi$ times the width of table.
* After placing the first ball you consider whether a second would land to the left or the right.
* For this reason in Bayes's distribution there is considered to be *aleatoric* uncertainty about the distribution parameter.}
\notes{Thomas Bayes also described the Bernoulli distribution, only he didn't refer to Jacob Bernoulli's work, so he didn't call it by that name. He described the distribution in terms of a table (think of a *billiard table*) and two balls. 
Bayes suggests that each ball can be rolled across the table such that it comes to rest at a position that is *uniformly distributed* between the sides of the table. 

Let's assume that the first ball is rolled, and that it comes to reset at a position that is $\pi$ times the width of the table from the left hand side. 

Now, we roll the second ball. We are interested if the second ball ends up on the left side (+ve result) or the right side (-ve result) of the first ball. We use the Bernoulli distribution to determine this.

For this reason in Bayes's distribution there is considered to be *aleatoric* uncertainty about the distribution parameter.}


\matlabcode{figure(1), clf
      plotWidth = textWidth*0.4;
      
      line([0 0 1 1 0], [0 1 1 0 0], 'linewidth', 3, 'color', blackColor)
      set(gca, 'xlim', [0 1], 'ylim', [0 1])
      axis off
      printLatexPlot('bayesBilliard0', '../../../ml/tex/diagrams/', plotWidth);
      ballX = rand(1);
      ballY = 0.5;
      r = 0.1;
      t = 0:pi/24:2*pi;
      x = ballX*ones(size(t)) + r*sin(t);
      y = ballY*ones(size(t)) + r*cos(t);
      handle = patch(x', y', blackColor);
      set(gca, 'xlim', [0 1], 'ylim', [0 1])
      printLatexPlot('bayesBilliard1', '../../../ml/tex/diagrams/', plotWidth);
      line([ballX ballX], [0 1], 'linestyle', ':', 'linewidth', 3, 'color', blackColor)
      printLatexPlot('bayesBilliard2', '../../../ml/tex/diagrams/', plotWidth);
      counter = 2;
      for ballX = rand(1, 7)
        ballY = 0.5;
        counter = counter+1;
        x = ballX*ones(size(t)) + r*sin(t);
        y = ballY*ones(size(t)) + r*cos(t);
        handle = patch(x', y', redColor);
        set(gca, 'xlim', [0 1], 'ylim', [0 1])
        printLatexPlot(['bayesBilliard' num2str(counter)], '../../../ml/tex/diagrams/', plotWidth);
        delete(handle)
      end
      
      \end{comment}
    \column{5cm}
    \only<1>{\input{../../../ml/tex/diagrams/bayesBilliard0}}\only<2>{\input{../../../ml/tex/diagrams/bayesBilliard1}}\only<3>{\input{../../../ml/tex/diagrams/bayesBilliard2}}\only<4>{\input{../../../ml/tex/diagrams/bayesBilliard3}}\only<5>{\input{../../../ml/tex/diagrams/bayesBilliard4}}\only<6>{\input{../../../ml/tex/diagrams/bayesBilliard5}}\only<7>{\input{../../../ml/tex/diagrams/bayesBilliard6}}\only<8>{\input{../../../ml/tex/diagrams/bayesBilliard7}}\only<9>{\input{../../../ml/tex/diagrams/bayesBilliard8}}\only<10>{\input{../../../ml/tex/diagrams/bayesBilliard9}}}
