\ifndef{basisFunctions}
\define{basisFunctions}

\section{Basis Functions}

\include{_ml/includes/basis-functions-intro.md}

\editme

\subsection{Different Bases}

\notes{Our choice of basis can be made based on what our beliefs about what is appropriate for the data. For example, the polynomial basis extends the quadratic basis to aribrary degree, so we might define the $j$th basis function associated with the model as}
$$
\basisFunc_j(\inputScalar_i) = \inputScalar_i^j
$$
\notes{which is known as the *polynomial basis*.}

\include{_ml/includes/polynomial-basis.md}

\notes{To aid in understanding how a basis works, we've provided you with a small interactive tool for exploring this polynomial basis. The tool can be summoned with the following command.}

\setupdisplaycode{import pods}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_prediction(basis=mlai.polynomial, num_basis=5)}

\notes{Try moving the sliders around to change the weight of each basis function. Click the control box `display_basis` to show the underlying basis functions (in red). The prediction function is shown in a thick blue line. *Warning* the sliders aren't presented quite in the correct order. `w_0` is associated with the bias, `w_1` is the linear term, `w_2` the quadratic and here (because we have four basis functions) we have `w_3` for the *cubic* term. So the subscript of the weight parameter is always associated with the corresponding polynomial's degree.}

\exercise{Try increasing the number of basis functions (thereby increasing the *degree* of the resulting polynomial). Describe what you see as you increase number of basis up to 10. Is it easy to change the function in intiutive ways?}

\subsection{Different Basis}

\notes{The polynomial basis is widely used in Engineering and graphics, but it has some drawbacks in machine learning: outside the input region between -1 and 1, the values of the polynomial basis rise very quickly.}

\notes{Now we look at basis functions that have been used as the *activation* functions in neural network model.}

\include{_ml/includes/radial-basis.md}
\include{_ml/includes/relu-basis.md}
\include{_ml/includes/hyperbolic-tangent-basis.md}
\include{_ml/includes/fourier-basis.md}





\endif
