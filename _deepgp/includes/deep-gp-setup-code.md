\ifndef{deepGpSetupCode}
\define{deepGpSetupCode}

\editme

\include{_deepgp/includes/pydeepgp-include.md}

\downloadcode{deepgp_tutorial}
\setupcode{# Late bind setup methods to DeepGP object
from deepgp_tutorial import initialize
from deepgp_tutorial import staged_optimize

import deepgp
deepgp.DeepGP.initialize=initialize
deepgp.DeepGP.staged_optimize=staged_optimize}

\endif
