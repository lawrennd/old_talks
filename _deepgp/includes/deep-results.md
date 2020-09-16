\ifndef{deepResults}
\define{deepResults}
\editme

\include{_deepgp/includes/pydeepgp-include.md}
\downloadcode{deepgp_tutorial}

\setupcode{# Late bind setup methods to DeepGP object}
\loadcode{initialize}{deep_gptutorial}
\setupcode{deepgp.DeepGP.initialize=initialize}
\loadcode{staged_optimize}{deep_gptutorial}
\setupcode{deepgp.DeepGP.staged_optimize=staged_optimize}

\include{_deepgp/includes/olympic-marathon-deep-gp.md}
\include{_deepgp/includes/della-gatta-deep-gp.md}
\include{_deepgp/includes/step-function-deep-gp.md}
\include{_deepgp/includes/motorcycle-helmet-deep-gp.md}
\include{_deepgp/includes/robot-wireless-deep-gp.md}

\include{_deepgp/includes/high-five-deep-gp.md}
\include{_deepgp/includes/mnist-digits-subsample-deep-gp.md}

\endif
