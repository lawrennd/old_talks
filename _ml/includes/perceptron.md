\ifndef{perceptron}
\define{perceptron}
\editme 

\include{_ml/includes/classification.md}

\newslide{Mathematical Drawing of Decision Boundary}

\slides{
**Refresher**: draw a hyper plane at decision boundary.
 - *Decision boundary*: plane where a point moves from being classified as -1 to +1. 
 - We have

   $$\text{sign}(\inputVector^\top \mappingVector) = \text{sign}(w_0 + w_1\inputScalar_{i,1} + w_2 \inputScalar_{i, 2})$$

   $\inputScalar_{i, 1}$ is first feature $\inputScalar_{i, 2}$ is second feature assume $\inputScalar_{0,i}=1$. 
 
 - Set $w_0 = b$ we have
 
   $$\text{sign}\left(w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b\right)$$}
   
\newslide{Equation of Plane}

\slides{$$\text{sign}\left(w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b\right)$$

- Equation of plane is 
  
  $$w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b = 0$$ 
  
  or
  
  $$w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} = -b$$ 
    
- Next we will initialise the model and draw a decision boundary.}

\newslide{Perceptron Algorithm: Initialisation Maths}

\slides{
- For a randomly chosen data point, $i$, set
  $$\mappingVector = \dataScalar_i \inputVector_i$$

- If predicted label of the $i$th point is 
  $$\text{sign}(\mappingVector^\top\inputVector_i)$$

- Setting $\mappingVector$ to $\dataScalar_i\inputVector_i$ implies
  $$\text{sign}(\mappingVector^\top\inputVector_i) = \text{sign}(\dataScalar_i\inputVector_i^\top \inputVector_i) = \dataScalar_i$$}
  
\code{%load -s init_perceptron mlai.py}

\newslide{Computing Decision Boundary}

\setupplotcode{import teaching_plots as plot}

\plotcode{f, ax = plt.subplots(1, 2, figsize=(14,7))
w, b = init_perceptron(x_plus, x_minus)
handle = plot.init_perceptron(f, ax, x_plus, x_minus, w, b)}

\subsection{Drawing Decision Boundary}

\notes{
The decision boundary is where the output of the function changes from -1 to +1 (or vice versa) so it's the point at which the argument of the $\text{sign}$ function is zero. So in other words, the decision boundary is given by the *line* defined by $\inputScalar_1 w_1 + \inputScalar_2 w_2 = -b$ (where we have dropped the index $i$ for convenience). In this two dimensional space the decision boundary is defined by a line. In a three dimensional space it would be defined by a *plane*  and in higher dimensional spaces it is defined by something called a *hyperplane* (http://en.wikipedia.org/wiki/Hyperplane). This equation is therefore often known as the *separating hyperplane* because it defines the hyperplane that separates the data. To draw it in 2-D we can choose some values to plot from $\inputScalar_1$ and then find the corresponding values for $\inputScalar_2$ to plot using the rearrangement of the hyperplane formula as follows

$$\inputScalar_2 = -\frac{(b+\inputScalar_1w_1)}{w_2}$$

Of course, we can also choose to specify the values for $\inputScalar_2$ and compute the values for $\inputScalar_1$ given the values for $\inputScalar_2$,

$$\inputScalar_1 = -\frac{b + \inputScalar_2w_2}{w_1}$$}

\subsection{Switching Formulae}

\notes{It turns out that sometimes we need to use the first formula, and sometimes we need to use the second. Which formula we use depends on how the separating hyperplane leaves the plot. 

We want to draw the separating hyperplane in the bounds of the plot which is showing our data. To think about which equation to use, let's consider two separate situations (actually there are a few more). 

1. If the separating hyperplane leaves the top and bottom of the plot then we want to plot a line with values in the $y$ direction (given by $\inputScalar_2$) given by the upper and lower limits of our plot. The values in the $x$ direction can then be computed from the formula for the plane. 

2. Conversely if the line leaves the sides of the plot then we want to plot a line with values in the $x$ direction given by the limits of the plot. Then the values in the $y$ direction can be computed from the formula. Whether the line leaves the top/bottom or the sides of the plot is dependent on the relative values of $w_1$ and $w_2$. 

This motivates a simple `if` statement to check which situation we're in.}

\newslide{Code for Perceptron}

\code{%load -s update_perceptron mlai.py}

\plotcode{plots = plot.perceptron(x_plus, x_minus, diagrams='../slides/diagrams/mlai')}

\setupcode{import pods}

\displaycode{pods.notebook.display_plots('perceptron{samp:0>3}.svg', directory='../slides/diagrams/ml', samp=(0, plots))}

\slides{
\startanimation{perceptron}{0}{14}
\newframe{\includediagram{../slides/diagrams/ml/perceptron000}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron001}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron002}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron003}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron004}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron005}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron006}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron007}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron008}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron009}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron010}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron011}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron012}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron013}}{perceptron}
\newframe{\includediagram{../slides/diagrams/ml/perceptron014}}{perceptron}
\endanimation
}

\notesfigure{\includediagram{../slides/diagrams/ml/perceptron014}}
\notes{\caption{The perceptron decision boundary.}}

\newslide{Perceptron Reflection}

\slides{
- The perceptron is an algorithm. 
 - What is it doing? When will it fail?
 - We can explain the update equations and proove it converges.
 - Normally it is far easier to first define an *objective function*.
 - Also known as a:
     - loss function
     - error function
     - cost function}
}
\endif
