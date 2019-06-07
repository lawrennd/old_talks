\ifndef{regression}
\define{regression}
\editme

\subsection{Objective Functions and Regression}

\slides{
* Classification: map feature to class label.
* Regression: map feature to real value our *prediction function* is

    $$\mappingFunction(\inputScalar_i) = m\inputScalar_i + c$$

* Need an *algorithm* to fit it. 

* Least squares: minimize an error.

$$\errorFunction(m, c) = \sum_{i=1}^\numData (\dataScalar_i * \mappingFunction(\inputScalar_i))^2$$}

\newslide{Regression}

\slides{
* Create an artifical data set.
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}
\code{x = np.random.normal(size=4)}

\slides{We now need to decide on a *true* value for $m$ and a *true* value for $c$ to use for generating the data. }

\code{m_true = 1.4
c_true = -3.1}

\slides{We can use these values to create our artificial data. The formula 
$$\dataScalar_i = m\inputScalar_i + c$$ is translated to code as follows:}

\code{y = m_true*x+c_true}

\newslide{Plot of Data}

\slides{We can now plot the artifical data we've created.}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{plt.plot(x, y, 'r.', markersize=10) # plot data as red dots
plt.xlim([-3, 3])
mlai.write_figure(filename="../slides/diagrams/ml/regression.svg", transparent=True)}

\figure{\includediagram{../slides/diagrams/ml/regression}{60%}}{A simple linear regression.}{linear-regression}

\slides{These points lie exactly on a straight line, that's not very realistic, let's corrupt them with a bit of Gaussian 'noise'.}

\subsection{Noise Corrupted Plot}

\code{noise = np.random.normal(scale=0.5, size=4) # standard deviation of the noise is 0.5
y = m_true*x + c_true + noise
plt.plot(x, y, 'r.', markersize=10)
plt.xlim([-3, 3])
mlai.write_figure(filename="../slides/diagrams/ml/regression_noise.svg", transparent=True)}

\figure{\includediagram{../slides/diagrams/ml/regression_noise}{60%}}{A simple linear regression with noise.}{linear-regression-noise}

\endif
