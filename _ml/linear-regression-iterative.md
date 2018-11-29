\include{_ml/includes/regression.md}

### Contour Plot of Error Function

* Visualise the error function surface,
create vectors of values.

\code{# create an array of linearly separated values around m_true
m_vals = np.linspace(m_true-3, m_true+3, 100) 
# create an array of linearly separated values ae
c_vals = np.linspace(c_true-3, c_true+3, 100)}

* create a grid of values to evaluate the error function in 2D.

\code{m_grid, c_grid = np.meshgrid(m_vals, c_vals)}

* compute the error function at each  combination of $c$ and $m$.

\code{E_grid = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        E_grid[i, j] = ((y - m_grid[i, j]*x - c_grid[i, j])**2).sum()}

### Contour Plot of Error

\slides{* We can now make a contour plot.}

\code{%load -s regression_contour teaching_plots.py}

\plotcode{f, ax = plt.subplots(figsize=(5,5))
regression_contour(f, ax, m_vals, c_vals, E_grid)
mlai.write_figure(filename='../slides/diagrams/ml/regression_contour.svg')}

\includesvg{../slides/diagrams/ml/regression_contour.svg}

### Steepest Descent

\slides{* Minimize the sum of squares error function. 
* One way of doing that is gradient descent. 
* Initialize with a guess for $m$ and $c$ 
* update that guess by subtracting a portion of the gradient from the guess. 
* Like walking down a hill in the steepest direction of the hill to get to the
bottom.}

### Algorithm

* We start with a guess for $m$ and $c$.

\code{m_star = 0.0
c_star = -5.0}

### Offset Gradient

* Now we need to compute the gradient of the error
function, firstly with respect to $c$,

  $$\frac{\text{d}\errorFunction(m, c)}{\text{d} c} =
-2\sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)$$

* This is computed in python as follows

\code{c_grad = -2*(y-m_star*x - c_star).sum()
print("Gradient with respect to c is ", c_grad)}

### Deriving the Gradient

To see how the gradient was derived, first note that
the $c$ appears in every term in the sum. So we are just differentiating $(\dataScalar_i -
m\inputScalar_i - c)^2$ for each term in the sum. The gradient of this term with respect to
$c$ is simply the gradient of the outer quadratic, multiplied by the gradient
with respect to $c$ of the part inside the quadratic. The gradient of a
quadratic is two times the argument of the quadratic, and the gradient of the
inside linear term is just minus one. This is true for all terms in the sum, so
we are left with the sum in the gradient.

### Slope Gradient

The gradient with respect tom $m$ is similar, but now the
gradient of the quadratic's argument is $-\inputScalar_i$ so the gradient with respect to
$m$ is

$$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i - m\inputScalar_i -
c)$$

which can be implemented in python (numpy) as

\code{m_grad = -2*(x*(y-m_star*x - c_star)).sum()
print("Gradient with respect to m is ", m_grad)}

### Update Equations

* Now we have gradients with respect to $m$ and $c$.
* Can update our inital guesses for $m$ and $c$ using the gradient. 
* We don't want to just subtract the gradient from $m$ and $c$, 
* We need to take a *small* step in the gradient direction. 
* Otherwise we might overshoot the minimum. 
* We want to follow the gradient to get to the minimum, the gradient
changes all the time.

### Move in Direction of Gradient

\setupcode{import teaching_plots as plot}
\plotcode{f, ax = plt.subplots(figsize=plot.big_figsize)
plot.regression_contour(f, ax, m_vals, c_vals, E_grid)
ax.plot(m_star, c_star, 'g*', markersize=20)
ax.arrow(m_star, c_star, -m_grad*0.1, -c_grad*0.1, head_width=0.2)
mlai.write_figure(filename='../slides/diagrams/ml/regression_contour_step001.svg', transparent=True)}

\includesvg{../slides/diagrams/ml/regression_contour_step001.svg}

### Update Equations 

* The step size has already been introduced, it's again known as the learning rate and is denoted by $\learnRate$. 
  $$
  c_\text{new}\leftarrow c_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}c}
$$ 

* gives us an update for our estimate of $c$ (which in the code we've been calling `c_star` to represent a common way of writing a parameter estimate, $c^*$) and
$$
m_\text{new} \leftarrow m_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}m}
$$
* Giving us an update for $m$.

### Update Code

* These updates can be coded as

\code{print("Original m was", m_star, "and original c was", c_star)
learn_rate = 0.01
c_star = c_star - learn_rate*c_grad
m_star = m_star - learn_rate*m_grad
print("New m is", m_star, "and new c is", c_star)}

\section{Iterating Updates}

* Fit model by descending gradient.

### Gradient Descent Algorithm

\code{num_plots = plot.regression_contour_fit(x, y, diagrams='../slides/diagrams/ml')}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('regression_contour_fit{num:0>3}.svg', directory='../slides/diagrams/ml', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\startslides{regression_contour_fit}{1}{28}
\includesvg{../slides/diagrams/ml/regression_contour_fit000.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit001.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit002.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit003.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit004.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit005.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit006.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit007.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit008.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit009.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit010.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit011.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit012.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit013.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit014.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit015.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit016.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit017.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit018.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit019.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit020.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit021.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit022.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit023.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit024.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit025.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit026.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit027.svg}{}{regression_contour_fit}
\includesvg{../slides/diagrams/ml/regression_contour_fit028.svg}{}{regression_contour_fit}
}

\notesfigure{\includesvg{../slides/diagrams/ml/regression_contour_fit028.svg}}
\notes{\caption{Stochastic gradient descent for linear regression}}

### Stochastic Gradient Descent

* If $\numData$ is small, gradient descent is fine.
* But sometimes (e.g. on the internet $\numData$ could be a billion.
* Stochastic gradient descent is more similar to perceptron.
* Look at gradient of one data point at a time rather than summing across *all* data points) 
* This gives a stochastic estimate of gradient.

### Stochastic Gradient Descent

* The real gradient with respect to $m$ is given by 

  $$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i -
m\inputScalar_i - c)$$

  but it has $\numData$ terms in the sum. Substituting in the gradient we can see that the full update is of the form

  $$m_\text{new} \leftarrow
m_\text{old} + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 - c_\text{old}) + (\inputScalar_2 (\dataScalar_2 -   m_\text{old}\inputScalar_2 - c_\text{old}) + \dots + (\inputScalar_n (\dataScalar_n - m_\text{old}\inputScalar_n - c_\text{old})\right]$$

  This could be split up into lots of individual updates
$$m_1 \leftarrow m_\text{old} + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 -
c_\text{old})\right]$$
$$m_2 \leftarrow m_1 + 2\learnRate \left[\inputScalar_2 (\dataScalar_2 -
m_\text{old}\inputScalar_2 - c_\text{old})\right]$$
$$m_3 \leftarrow m_2 + 2\learnRate
\left[\dots\right]$$
$$m_n \leftarrow m_{n-1} + 2\learnRate \left[\inputScalar_n (\dataScalar_n -
m_\text{old}\inputScalar_n - c_\text{old})\right]$$

which would lead to the same final update.

### Updating $c$ and $m$

* In the sum we don't  $m$ and $c$ we use for computing the gradient term at each update. 
* In stochastic gradient descent we *do* change them.
* This means it's not quite the same as steepest desceint.
* But we  can present each data point in a random order, like we did for the
perceptron.
* This makes the algorithm suitable for large scale web use (recently this domain is know as 'Big Data') and algorithms like this are widely used by Google, Microsoft, Amazon, Twitter and Facebook.

### Stochastic Gradient Descent

* Or more accurate, since the data is normally presented in a random order we just can write
  $$
  m_\text{new} = m_\text{old} + 2\learnRate\left[\inputScalar_i (\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right]
  $$

\code{# choose a random point for the update 
i = np.random.randint(x.shape[0]-1)
# update m
m_star = m_star + 2*learn_rate*(x[i]*(y[i]-m_star*x[i] - c_star))
# update c
c_star = c_star + 2*learn_rate*(y[i]-m_star*x[i] - c_star)}

### SGD for Linear Regression

Putting it all together in an algorithm, we can
do stochastic gradient descent for our regression data.

\plotcode{num_plots = plot.regression_contour_sgd(x, y, diagrams='../slides/diagrams/ml')}

\displaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('regression_sgd_contour_fit{num:0>3}.svg', 
    directory='../slides/diagrams/mlai', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\startslides{regression_sgd_contour_fit}{0}{58}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit000.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit001.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit002.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit003.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit004.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit005.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit006.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit007.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit008.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit009.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit010.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit011.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit012.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit013.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit014.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit015.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit016.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit017.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit018.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit019.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit020.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit021.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit022.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit023.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit024.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit025.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit026.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit027.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit028.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit029.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit030.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit031.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit032.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit033.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit034.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit035.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit036.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit037.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit038.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit039.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit040.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit041.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit042.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit043.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit044.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit045.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit046.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit047.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit048.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit049.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit050.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit051.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit052.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit053.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit054.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit055.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit056.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit057.svg}{}{regression_sgd_contour_fit}
\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit058.svg}{}{regression_sgd_contour_fit}
}

\notesfigure{\includesvg{../slides/diagrams/ml/regression_sgd_contour_fit058.svg}}
\notes{\caption{Stochastic gradient descent for linear regression}}

### Reflection on Linear Regression and Supervised Learning

Think about:

1. What effect does the learning rate have in the optimization? What's the effect of making it too small, what's the effect of making it too big? Do you get the same result for both stochastic and steepest gradient descent?

2. The stochastic gradient descent doesn't help very much for such a small data set. It's real advantage comes when there are many, you'll see this in the lab.
