\subsection{Basis Function Covariance}

\notes{The fixed basis function covariance just comes from the properties of a multivariate Gaussian, if we decide 
$$
\mappingFunctionVector=\basisMatrix\mappingVector
$$
and then we assume
$$
\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha\eye}
$$
then it follows from the properties of a multivariate Gaussian that
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha\basisMatrix\basisMatrix^\top}
$$
meaning that the vector of observations from the function is jointly distributed as a Gaussian process and the covariance matrix is $\kernelMatrix = \alpha\basisMatrix \basisMatrix^\top$, each element of the covariance matrix can then be found as the inner product between two rows of the basis funciton matrix.}
$$
\kernel(\inputVector, \inputVector^\prime) = \basisVector(\inputVector)^\top \basisVector(\inputVector^\prime)
$$

\matlabcode{close all
t = linspace(-3, 3, N)';
tdisp = linspace(-3, 3, Ndisp)';

muVec = [-1 0 1]';
phi = exp(-dist2(tdisp, muVec));
K = phi*phi';
ax = axes('Position', [0 0 1 1]);
plotMatrix(K, ax, 'boxes', 'imagesc');
printLatexPlot('rbfbasisCovarianceImage', '../../../kern/tex/diagrams/', colWidth);

clf
phi = exp(-dist2(t, muVec));
K = phi*phi';
y = gsamp(zeros(size(K, 1), 1), K, numSamps);
a= plot(t, y')
if negative
  for i = 1:length(a)
    set(a(i), 'color', 1-get(a(i), 'color'))
  end
end
box off
xlim = get(gca, 'xlim');
ylim = get(gca, 'ylim');
line([xlim(1) xlim(1)], ylim, 'color', blackColor)
line(xlim, [ylim(1) ylim(1)], 'color', blackColor)

printLatexPlot('rbfbasisCovarianceSamples', '../../../kern/tex/diagrams/', colWidth);
}

\columns{\includesvg{../slides/diagrams/kern/basis_covariance.svg}}{\includeimg{../slides/diagrams/kern/basis_covariance.gif}{100%}{negate}{center}}{45%}{45%}
