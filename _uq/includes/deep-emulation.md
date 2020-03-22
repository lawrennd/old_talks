\ifndef{deepEmulation}
\define{deepEmulation}

\editme

\subsection{Deep Emulation}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-rider-allocation000}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\notes{As a solution we can use of *emulators*. When constructing an ML system, software engineers,
ML engineers, economists and operations researchers are
explicitly defining relationships between variables of interest in the
system. That implicitly defines a joint distribution, $p(\dataVector^*,
\dataVector)$. In a decomposable system any sub-component may be
defined as $p(\dataVector_\mathbf{i}|\dataVector_\mathbf{j})$ where
$\dataVector_\mathbf{i}$ and $\dataVector_\mathbf{j}$ represent sub-sets
of the full set of variables $\left\{\dataVector^*, \dataVector
\right\}$. In those cases where the relationship is deterministic, the
probability density would collapse to a vector-valued deterministic
function, $\mappingFunctionVector_\mathbf{i}\left(\dataVector_\mathbf{j}\right)$.

Inter-variable relationships could be defined by, for example a neural network
(machine learning), an integer program (operational research), or a
simulation (supply chain). This makes probabilistic inference in this joint
density for real world systems is either very hard or
impossible. 

Emulation is a form of meta-modelling: we construct a model of the
model. We can define the joint density of an emulator as
$s(\dataVector*, \dataVector)$, but if this probability density is to be
an accurate representation of our system, it is likely to be
prohibitively complex. Current practice is to design an emulator to
deal with a specific question. This is done by fitting an ML model to
a simulation from the the appropriate conditional distribution,
$p(\dataVector_\mathbf{i}|\dataVector_\mathbf{j})$, which is
intractable. The emulator provides an approximated answer of the form
$s(\dataVector_\mathbf{i}|\dataVector_\mathbf{j})$. Critically, an
emulator should incorporate its uncertainty about its
approximation. So the emulator answer will be less certain than direct
access to the conditional $p(\dataVector_i|\dataVector_j)$, but it may
be sufficiently confident to act upon. Careful design of emulators to
answer a given question leads to efficient diagnostics and
understanding of the system. But in a complex interacting system an
exponentially increasing number of questions can be asked. This calls
for a system of automated construction of emulators which selects the
right structure and redeploys
the emulator as necessary. Rapid redeployment of emulators could
exploit pre-existing emulators through *transfer learning*.

Automatically deploying these families of emulators for full system
understanding is highly ambitious. It requires advances in engineering
infrastructure, emulation and Bayesian optimization.  However, the
intermediate steps of developing this architecture also allow for
automated monitoring of system accuracy and fairness. This facilitates
AutoML on a component-wise basis which we can see as a simple
implementation of AutoAI. The proposal is structured so that despite
its technical ambition there is a smooth ramp of benefits to be
derived across the programme of work.

In Applied Mathematics, the field studying these techniques is known
as *uncertainty quantification*. The new challenge is the automation
of emulator creation on demand to answer questions of interest and
facilitate the system design, i.e. AutoAI through BSO.

At design stage, any particular AI task could be decomposed in
multiple ways. Bayesian system optimization will assist both in
determining the large-scale system design through exploring different
decompositions  and in refinement of the deployed system.

So far, most work on emulators has focussed on emulating a single
component. Automated deployment and maintenance of ML systems requires
networks of emulators that can be deployed and redeployed on demand
depending on the particular question of interest. Therefore, the
technical innovations we require are in the mathematical composition
of emulator models
[@Damianou:deepgp13;@Pedikaris:nonlinear17]. Different chains of
emulators will need to be rapidly composed to make predictions of
downstream performance. This requires rapid retraining of emulators
and *propagation of uncertainty* through the emulation pipeline a
process we call *deep emulation*.

<!--Our main approach for this will be automated learning of the structure
of deep probabilistic models, such as deep Gaussian processes
[@Damianou:deepgp13]. The proposer is an international expert in this
domain.--> Recomposing the ML system requires structural learning of the network. By parameterizing covariance functions appropriately this can be done through Gaussian processes (e.g. [@Damianou:manifold12]), but one could also consider Bayesian neural networks and other generative models, e.g. Generative Adversarial Networks [@Goodfellow:gans14].}

<!-- This structural learning allows us to associate data with the relevant -->
<!-- layer of the model, rather than merely on the leaf nodes of the output -->
<!-- model. When deploying the deep Gaussian process as an emulator, this -->
<!-- allows for the possibility of learning the structure of the different -->
<!-- component parts of the underlying system. This should aid the user in -->
<!-- determining the ideal system decomposition. -->


\newslide{Deep Emulation}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-rider-allocation001}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\newslide{Deep Emulation}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-rider-allocation}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\endif
