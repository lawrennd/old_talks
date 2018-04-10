\setupcode{import teaching_plots as plot}

\code{plot.under_determined_system(diagrams='../slides/diagrams/ml')}

### Underdetermined System {data-transition="none"}

* What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

. . .

Can compute $m$
given $c$. $$m = \frac{\dataScalar_1 - c}{\inputScalar}$$

\displaycode{pods.notebook.display_plots('under_determined_system{samp:0>3}.svg', 
                            directory='../slides/diagrams/ml', samp=(0, 10))}
\slides{							
### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system000.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system001.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system002.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system003.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system004.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system005.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system006.svg}

### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system007.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system008.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system009.svg}


### Underdetermined System {data-transition="none"}

\svgplot{../slides/diagrams/ml/under_determined_system010.svg}

}
