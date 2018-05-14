\setupcode{import teaching_plots as plot}
\plotcode{plot.over_determined_system(diagrams='../slides/diagrams/ml')}

### {data-transition="none"}

<large>$$\dataScalar = m\inputScalar + c$$</large>

\displaycode{pods.notebook.display_plots('over_determined_system{samp:0>3}.svg', directory='../slides/diagrams/ml', samp=(1, 7))}

\slides{
### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system001.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system002.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system003.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system004.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system005.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system006.svg}

### {data-transition="none"}

\includesvg{../slides/diagrams/ml/over_determined_system007.svg}
}


\slides{### $\dataScalar = m\inputScalar + c$ 

. . . 

\alignleft{point 1: $\inputScalar = 1$, $\dataScalar=3$}

$$3 = m + c$$

. . .

\alignleft{point 2: $\inputScalar = 3$, $\dataScalar=1$}

$$1 = 3m + c$$

. . . 

\alignleft{point 3: $\inputScalar = 2$, $\dataScalar=2.5$}

$$2.5 = 2m + c$$}

### 

\includeimg{../slides/diagrams/ml/Pierre-Simon_Laplace.png}{30%}

### {data-transition="none"}

\includeimg{../slides/diagrams/laplacesDeterminismFrench.png}{80%}

### {data-transition="none"}

\includeimg{../slides/diagrams/laplacesDeterminismEnglish.png}{80%}

### {data-transition="none"}

\includeimg{../slides/diagrams/philosophicaless00lapliala.png}{80%}

\slides{
### $\dataScalar = m\inputScalar + c + \noiseScalar$ {data-transition="None"}

. . . 

\alignleft{point 1: $\inputScalar = 1$, $\dataScalar=3$}

$$3 = m + c + \noiseScalar_1$$

. . .

\alignleft{point 2: $\inputScalar = 3$, $\dataScalar=1$}

$$1 = 3m + c + \noiseScalar_2$$

. . . 

\alignleft{point 3: $\inputScalar = 2$, $\dataScalar=2.5$}

$$2.5 = 2m + c + \noiseScalar_3$$
}

\slides{
### Laplace's Idea

\alignleft{The Probabilistic Process}

. . .

\alignleft{Set the mean of Gaussian to be a function.}

$$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp \left(-\frac{\left(\dataScalar_i-\mappingFunction\left(\inputScalar_i\right)\right)^{2}}{2\dataStd^2}\right).$$

. . .

\alignleft{This gives us a 'noisy function'.}

. . .

\alignleft{This is known as a stochastic process.}
}
