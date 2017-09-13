### {data-transition="none"}


<large>$$y = mx + c$$</large>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system001.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system002.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system003.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system004.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system005.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system006.svg">
</object>

### {data-transition="none"}

<object class="svgplot" data="../_ml/diagrams/over_determined_system007.svg">
</object>



### $y = mx + c$ {data-transition="none"}

. . . 

<div align="left">point 1: $x = 1$, $y=3$</div>

$$3 = m + c$$

. . .

<div align="left">point 2: $x = 3$, $y=1$</div>

$$1 = 3m + c$$

. . . 

<div align="left">point 3: $x = 2$, $y=2.5$</div>

$$2.5 = 2m + c$$

### {data-transition="none"}

![](../_ml/diagrams/Pierre-Simon_Laplace.png){height="100%"}

### {data-transition="none"}

![](../_ml/diagrams/laplacesDeterminismFrench.png){height="100%"}

### {data-transition="none"}

![](../_ml/diagrams/laplacesDeterminismEnglish.png){height="100%"}

### {data-transition="none"}

![](../_ml/diagrams/philosophicaless00lapliala.png){height="100%"}

### $y = mx + c + \epsilon$ {data-transition="None"}

. . . 

<div align="left">point 1: $x = 1$, $y=3$</div>

$$3 = m + c + \epsilon_1$$

. . .

<div align="left">point 2: $x = 3$, $y=1$</div>

$$1 = 3m + c + \epsilon_2$$

. . . 

<div align="left">point 3: $x = 2$, $y=2.5$</div>

$$2.5 = 2m + c + \epsilon_3$$


### Laplace's Idea

<div align="left">The Probabilistic Process</div>

. . .

<div align="left">Set the mean of Gaussian to be a function.</div>

$$p\left(y_i|x_i\right)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp \left(-\frac{\left(y_i-f\left(x_i\right)\right)^{2}}{2\sigma^2}\right).$$

. . .

<div align="left">This gives us a ‘noisy function’.</div>

. . .

<div align="left">This is known as a stochastic process.</div>
