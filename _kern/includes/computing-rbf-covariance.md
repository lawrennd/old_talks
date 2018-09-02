\subsection{Where Did This Covariance Matrix Come From?}
$$
k(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\left\Vert \inputVector - \inputVector^\prime\right\Vert^2_2}{2\lengthScale^2}\right)$$

\columns{* Covariance matrix is built using the *inputs* to the function, $\inputVector$.

* For the example above it was based on Euclidean distance.

* The covariance function is also know as a kernel.
}{\includesvg{../slides/diagrams/kern/eq_covariance.svg}}{50%}{50%}


\setupplotcode{import pods
from ipywidgets import IntSlider}
\plotcode{pods.notebook.display_plots('computing_eq_covariance{sample:0>3}.svg', 
                            '../slides/diagrams/kern', sample=IntSlider(1, 1, 58, 1))}

\slides{
\startslides{computing_eq_covariance}{1}{57}
\includesvg{../slides/diagrams/kern/computing_eq_covariance001.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance002.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance003.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance004.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance005.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance006.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance007.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance008.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance009.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance010.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance011.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance012.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance013.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance014.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance015.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance016.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance017.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance018.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance019.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance020.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance021.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance022.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance023.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance024.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance025.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance026.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance027.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance028.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance029.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance030.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance031.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance032.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance033.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance034.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance035.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance036.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance037.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance038.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance039.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance040.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance041.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance042.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance043.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance044.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance045.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance046.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance047.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance048.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance049.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance050.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance051.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance052.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance053.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance054.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance055.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance056.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance057.svg}{}{computing_eq_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_covariance058.svg}{}{computing_eq_covariance}
}
\notesfigure{\includesvg{../slides/diagrams/kern/computing_eq_covariance058.svg}{}}\notes{\caption{Entrywise fill in of the covariance matrix from the covariance function.}}
