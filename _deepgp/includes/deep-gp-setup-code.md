\ifndef{deepGpSetupCode}
\define{deepGpSetupCode}

\editme

\include{_deepgp/includes/pydeepgp-include.md}

\downloadcode{deepgp_tutorial}
\setupcode{# Late bind setup methods to DeepGP object}
\loadcode{initialize}{deepgp_tutorial}
\setupcode{deepgp.DeepGP.initialize=initialize}
\loadcode{staged_optimize}{deepgp_tutorial}
\setupcode{deepgp.DeepGP.staged_optimize=staged_optimize}

\endif
