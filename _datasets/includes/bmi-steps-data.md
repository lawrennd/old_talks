\ifndef{bmiStepsData}
\define{bmiStepsData}
\editme

\subsection{BMI Steps Data}

\notes{The BMI Steps example is taken from @Yanai-hypothesis20. We are given a data set of body-mass index measurements against step counts. For convenience we have packaged the data so that it can be easily downloaded.}

\setupcode{import pods}

\code{data = pods.datasets.bmi_steps()
X = data['X'] 
y = data['Y']}

\notes{It is good practice to give our variables interpretable names so that the analysis may be clearly understood by others. Here the `steps` count is the first dimension of the covariate, the `bmi` is the second dimension and the `gender` is stored in `y` with `1` for female and `0` for male.}

\code{steps = X[:, 0]
bmi = X[:, 1]
gender = y[:, 0]}

\notes{We can check the mean steps and the mean of the BMI.}

\code{print('Steps mean is {mean}.'.format(mean=steps.mean()))}

\code{print('BMI mean is {mean}.'.format(mean=bmi.mean()))}


\endif
