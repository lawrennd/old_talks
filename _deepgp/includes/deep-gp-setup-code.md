\ifndef{deepGpSetupCode}
\define{deepGpSetupCode}

\editme

\include{_deepgp/includes/pydeepgp-include.md}

\downloadcode{deepgp_tutorial}
\setupcode{# Late bind setup methods to DeepGP object
from deepgp_tutorial import initialize
from deepgp_tutorial import staged_optimize
from deepgp_tutorial import posterior_sample
from deepgp_tutorial import visualize
from deepgp_tutorial import visualize_pinball

import deepgp
deepgp.DeepGP.initialize=initialize
deepgp.DeepGP.staged_optimize=staged_optimize
deepgp.DeepGP.posterior_sample=posterior_sample
deepgp.DeepGP.visualize=visualize
deepgp.DeepGP.visualize_pinball=visualize_pinball}

\endif
