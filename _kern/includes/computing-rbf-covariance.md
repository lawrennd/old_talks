### Where Did This Covariance Matrix Come From?
$$
k(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\left\Vert \inputVector - \inputVector^\prime\right\Vert^2_2}{2\lengthScale^2}\right)$$

<table cellspacing="0" cellpadding="0" border="none">
<tr><td>
<ul><li>Covariance matrix is
built using the *inputs* to
the function, $\inputVector$.</li>

<li>For the example above it
was based on Euclidean
distance.</li>

<li>The covariance function
is also know as a kernel.</li>
</ul></td><td>\includesvg{../slides/diagrams/kern/eq_covariance.svg}</td></tr>
</table>

\plotcode{pods.notebook.display_plots('computing_eq_covariance{sample:0>3}.svg', 
                            '../slides/diagrams/kern', sample=(1,57))}


\slides{
###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance001.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance002.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance003.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance004.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance005.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance006.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance007.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance008.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance009.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance010.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance011.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance012.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance013.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance014.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance015.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance016.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance017.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance018.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance019.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance020.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance021.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance022.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance023.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance024.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance025.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance026.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance027.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance028.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance029.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance030.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance031.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance032.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance033.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance034.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance035.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance036.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance037.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance038.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance039.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance040.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance041.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance042.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance043.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance044.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance045.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance046.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance047.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance048.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance049.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance050.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance051.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance052.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance053.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance054.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance055.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance056.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance057.svg}

###  {data-transition="None"}

\includesvg{../slides/diagrams/kern/computing_eq_covariance058.svg}

}
