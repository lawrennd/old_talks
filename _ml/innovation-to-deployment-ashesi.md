---
title: "Innovation to Deployment"
subtitle: Machine Learning Systems Design
abstract: >
  The AI systems we are developing and deploying are based on
  interconnected machine learning components. This proposal focuses on 
  AI-assisted design and monitoring of these systems to ensure they perform
  robustly, safely and accurately in their deployed environment. We address 
  the entire pipeline of AI system development, from data acquisition to 
  decision making. 
  
  We propose an ecosystem that includes system monitoring for performance, 
  interpretability and fairness. We place these ideas in a wider context 
  that also considers the availability, quality and ethics of data.
author: 
- given: Neil D. 
  family: Lawrence 
  url: http://inverseprobability.com 
  institute: University of Cambridge
  twitter: lawrennd 
  gscholar: r3SJcvoAAAAJ 
  orchid: 
layout: slides
date: 2019-10-24
venue: Data Science Africa Workshop, Ashesi, Ghana
transition: None
incremental: True
---

\include{talk-macros.gpp}

\section{Introduction}

\notes{Artificial Intelligence (AI) solutions
are based on machine learning algorithms (ML), but each ML
solution is only capable of solving a restricted task, e.g. a
supervised learning problem. Consequently, any AI that we deploy today
takes the form of an ML System with interacting
components. As these ML systems become larger and more complex,
challenges in interpretation, explanation, accuracy and fairness
arise. This project addresses these issues. The challenges
include [@Lawrence:threeds19]: the *decomposition* of the system, the
*data* availability, and the performance of the system in
*deployment*. Collectively we refer to these challenges as the "Three
Ds of ML Systems Design".}

\subsection{Fellowship Vision}

\slides{* Steer the international community
* Be a beacon for UK AI research
* An *inclusive* program 
* Provide tools and exemplar problems
* Develop students, RSDEs and PDRAs for modern ML design
}

\subsection{How?}

\slides{* Bridge between Academia, Industry, Public & 3rd Sector
* Influence beyond the fellowship
* Leverage the Alan Turing Institute
  * Chris Holmes (ATI Programme Director for Health and Medical Sciences)
  * Mark Girolami (ATI Programme Director for Data-Centric Engineering)
}

\subsection{Lay Description}

\slides{
> It used to be true that computers only did what we programmed them to do, but today AI systems are learning from our data. This introduces new problems in how these systems respond to their environment. 
>
>We need to better monitor how data is influencing decision making and take corrective action as required. 
>
>This fellowship addresses that challenge.}

\subsection{Technical Consequence}

\slides{* Classical systems design assumes *decomposability*.
* Data-driven systems interfere with decomponsability.}

\newslide{Technical Consequence}

\slides{$$\text{Bayesian Optimization} \rightarrow \text{Bayesian Systems Optimization}$$}

\newslide{Technical Consequence}

\slides{$$\text{Auto ML} \rightarrow \text{Auto AI}$$}


\notes{Our aim is to scale our ability to deploy safe and reliable AI
solutions. Our technical approach is to do this through *data-oriented
software engineering* practices and *deep system emulation*. Our proposal is a
significant extension of the notion of Automated ML
(AutoML) to Automated AI (AutoAI). We will
provide a toolkit for automating the deployment, maintenance and
monitoring of artificial intelligence systems.}

\subsection{Applications}

\figure{\includediagram{../slides/diagrams/ai/ride-allocation-prediction}{60%}}{Some software components in a ride allocation system. Circled components are hypothetical, rectangles represent actual data.}{ride-allocation-system}


\notes{For validating our efforts, the work is a close collaboration with
Data Science Africa (DSA)[^dsa]. They will provide applications and data to
inspire our methodologies and act as a testbed for deployment. We are
planning a series of exchange visits and a programme of workshops (see
Work Plan and Justification of Resources). Specific projects are not
detailed here because Africa-based collaborators will lead them
through DSA, but for the purposes of illustration imagine the
following possible application.

Boda bodas are motorcycle taxis that can be found across
East Africa, they transport people and goods, particularly within
cities. They provide income and work, particularly for
young men. Kudu[^kudu] was a live auction system for matching supply
of agricultural goods to markets. An exemplar ML system
would combine these two ideas. It could match jobs to boda boda
riders.[^safeboda] 

[^kudu]: <https://kudu.ug/>

[^safeboda]: See <https://safeboda.com/ug/>

Machine learning challenges in these systems are around pricing, boda
boda availability, and available jobs. The aim would be efficient and
fair matching of jobs to boda bodas. Each individual challenge is
within the current capabilities of, e.g. an ML practitioner with
master's level education. However, this example doesn't just require
domain expertise and expertise in ML it requires
*software engineering expertise* and *system design
expertise*. Further, once the system is deployed, there are challenges
around maintenance, understanding and redeployment. For example, while
the Kudu auction system was an initial success, sustainability was a
challenge and the system is currently inactive. Systems ML
expertise is not just scarce in the African context. Best practice in
deployment is also not yet well understood in developed
economies. SMEs, start-ups and even large digital companies will all
benefit from our solutions. The advantage of our African applications
is the lack of existing solutions and the growing community around
digital development around the continent. This allows us to access
applications which include the entire end-to-end pipeline from data
acquisition to model deployment, this access is critical for 
developing the right understanding and processes for deployment.

[^dsa]: <http://www.datascienceafrica.org/>

We will provide tools that automate and facilitate these steps,
enabling a complex AI system to be developed and safely and reliably
maintained by a small Africa-based team with master's level education
in ML.

The applicant has academic and industrial management experience in
these areas, including ML model development,
capacity building in Africa, software engineering and system
design leadership.

The proposal requires innovation around ML architecture and new
techniques for deploying, maintaining, understanding and redeploying
ML systems.}


\notes{Our objectives are to enable (1) Software Systems for Data Oriented
Architectures (\textsection \ref{sec:architecture} and
\textsection \ref{sec:readiness}) (2) Intelligent systems for monitoring and
emulating the underlying complexity of ML Systems (\textsection
\ref{sec:structure} and \textsection \ref{sec:dynamics}) (3) Automated deployment and redeployment of ML Systems, or "AutoAI" (\textsection
\ref{sec:architecture} and \textsection \ref{sec:hypervision}).

All of these objectives will be undertaken in the context of
real-world applications based on the African continent in
collaboration with Data Science Africa. For ethical considerations, we
will continue our collaboration with Professor Sylvie Delacroix (\textsection \ref{sec:ethics}) in the creation of regulatory
mechanisms to ensure ethical use of personal data.}

\section{Decomposability}
  
\notes{Supervised machine learning models are data-driven statistical functional
estimators. Each ML model is trained to perform a task. Machine learning
systems are created when these models are integrated as interacting
components in a more complex system that carries out a larger scale
task, e.g. an autonomous drone delivery system.

Artificial Intelligence can also be seen as *algorithmic
decision-making*. ML systems are *data driven* algorithmic
decision-makers. Designing decision-making engines requires us to
firstly decompose the system into its component parts. The
decompositions are driven by (1) system performance requirements (2)
the suite of ML algorithms at our disposal (3) the data
availability. Performance requirements could be computational speed,
accuracy, interpretability, and 'fairness'. The current generation of ML
Systems is often based around *supervised learning* and human
annotated data. But in the future, we may expect more use of
*reinforcement learning* and automated knowledge discovery using
*unsupervised learning*.

The classical systems approach assumes decomposability of
components. In ML, upstream components (e.g. a pedestrian detector in
an autonomous vehicle) make decisions that require revisiting once a
fuller picture is realized at a downstream stage (e.g. vehicle path
planning). The relative weaknesses and strengths of the different
component parts need to be assessed when resolving conflicts (WP6
\textsection \ref{sec:dynamics}).

In long-term planning, e.g. logistics and supply chain, a plan
may be computed multiple times under different constraints as data
evolves. In logistics, an initial plan for delivery may be computed
when an item is viewed on a webpage. Webpage waiting-time constraints
dominate the solution we choose. However, when an order is placed the
time constraint may be relaxed and an accuracy constraint or a cost
constraint may now dominate.

Such sub-systems will make inconsistent decisions, but we
should monitor and control the extent of the inconsistency (WP5 \textsection \ref{sec:architecture}).

One solution to aid with both the lack of decomposability of the
components and the inconsistency between components is *end-to-end*
learning of the system. End-to-end learning is when we use ML
techniques to fit parameters across the entire decision pipeline. We
exploit gradient descent and automated differentiation software to
achieve this. However, components in the system may themselves be
running a *simulation* (e.g. a transport delivery-time simulation) or
*optimization* (e.g. a linear program) as a subroutine. This limits
the universality of automatic differentiation. Another alternative is
to replace the entire system with a single ML model, such as in Deep
Reinforcement Learning. However, this can severely limit the
interpretability of the resulting system.

We envisage AutoAI as allowing us to take advantage of end-to-end
learning without sacrificing the interpretability of the underlying
system. Instead of optimizing each component individually, we
introduce *Bayesian system optimization* (BSO). We will make use of
the end-to-end learning signals and attribute them to the system
sub-components through the construction of an interconnected network
of *surrogate models*, known as emulators, each of which is associated
with an individual component from the underlying ML-system. Instead of
optimizing each component individually (e.g. by classical Bayesian
optimization) in BSO we account for upstream and downstream
interactions in the optimization, leveraging our end-to-end knowledge
without damaging the interpretability of the underlying system.}

\newslide{Emulation}

\figure{\includediagram{../slides/diagrams/uq/statistical-emulation004}{80%}}{A statistical emulator is a system that reconstructs the simulation with a statistical model. As well as reconstructing the simulation, a statistical emulator can be used to correlate with the real world.}{statistical-emulation-5}

\newslide{Emulation}

\figure{\includediagram{../slides/diagrams/uq/statistical-emulation005}{80%}}{In modern machine learning system design, the emulator may also consider the output of ML models (for monitoring bias or accuracy) and Operations Research models..}{statistical-emulation-6}
\include{_gp/includes/gp-intro-very-short.md}

<!--include{_ai/includes/ai-vs-data-science-2.md}-->

\slides{}


\notes{Conceptually thinking, we can think of any complex software
decision-making system as inter-relating different variables of
interest. From a probabilistic perspective, we might be interested in
answering any question about system state with the following
conditional density, $p(\dataVector^*|\dataVector)$, where $\dataVector$
is a vector of variables representing what we know about our system,
and $\dataVector^*$ is a vector of variables representing what we
*wish* to know about our system.  In the most general case this
involves creation of a joint distribution,
$p(\dataVector^*,\dataVector)$, which interrelates all variables of
interest. Inference is then the process of computing the conditional,
which requires marginalization of the unknowns to compute
$p(\dataVector)$, 
$$ 
p(\dataVector^*|\dataVector) =
\frac{p(\dataVector^*,\dataVector)}{p(\dataVector)}.
$$ 
Computation of this marginal probability is technically challenging:
it requires solving an integral across the joint probability. In complex
software systems, where individual component design has not taken
system-wide tractability into consideration, it will be impossible.}


\subsection{Deep Emulation}

\slides{\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-rider-allocation000}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}}

\newslide{Deep Emulation}

\slides{\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-rider-allocation001}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}}

\newslide{Deep Emulation}

\figure{\includediagram{../slides/diagrams/ai/ml-system-downstream-rider-allocation}{75%}}{A potential path of models in a machine learning system.}{ml-system-downstream-pedestrain}

\include{_deepgp/includes/stochastic-process-composition.md}

\newslide{Bayesian Optimisation}

* Acquisition function influenced by component's objective.

\newslide{Bayesian Systems Optimisation}

* Acquisition function influenced by component, upstream and downstream objectives.

\notes{As a solution we propose the use of emulators. Emulators are
meta-models; they are be deployed to model the underlying system. They
allow BSO: optimization of the system via the surrogates rather than
direct optimization of system itself.

When constructing an ML system, software engineers,
ML engineers, economists and operations researchers are
explicitly defining relationships between variables of interest in the
system. That implicitly defines a joint distribution, $p(\dataVector^*,
\dataVector)$. In a decomposable system any sub-component may be
defined as $p(\dataVector_\mathbf{i}|\dataVector_\mathbf{j})$ where
$\dataVector_\mathbf{i}$ and $\dataVector_\mathbf{j}$ represent sub-sets
of the full set of variables $\left\{\dataVector^*, \dataVector
\right\}$. In those cases where the relationship is deterministic, the
probability density would collapse to a vector-valued deterministic
function, $\mathbf{f}_\mathbf{i}\left(\dataVector_\mathbf{j}\right)$.

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
right structure (WP4 \textsection \ref{sec:structure}) and redeploys
the emulator as necessary. Rapid redeployment of emulators could
exploit pre-existing emulators through *transfer learning* (WP5
\textsection \ref{sec:hypervision}).

Automatically deploying these families of emulators for full system
understanding is highly ambitious. It requires advances in engineering
infrastructure, emulation and Bayesian optimization.  However, the
intermediate steps of developing this architecture also allow for
automated monitoring of system accuracy and fairness. This facilitates
AutoML on a component-wise basis which we can see as a simple implementation of AutoAI. The
proposal is structured so that despite its technical ambition there is
a smooth ramp of benefits to be derived across the programme of work.

In Applied Mathematics, the field studying these techniques is known
as *uncertainty quantification*. The new challenge is the automation of emulator creation on demand to answer questions of interest and facilitate the system design, i.e. AutoAI through BSO.

At design stage, any particular AI task could be decomposed in
multiple ways. Bayesian system optimization will assist both in
determining the large-scale system design through exploring different
decompositions (WP4 in \textsection \ref{sec:structure}) and in refinement of the deployed system.

So far, most work on emulators has focussed on emulating a
single component. Automated deployment and maintenance of ML systems
requires networks of emulators that can be deployed and redeployed on
demand depending on the particular question of interest (WP4
\textsection \ref{sec:structure} & WP5 \textsection
\ref{sec:hypervision}). Therefore, the technical innovations we
require are in the mathematical composition of emulator models
[@Damianou:deepgp13;@Pedikaris:nonlinear17]. Different chains of
emulators will need to be rapidly composed to make predictions of
downstream performance. This requires rapid retraining of emulators
and *propagation of uncertainty* through the emulation pipeline a process we call *deep emulation*.

Recomposing the ML system requires structural learning of the network. By parameterizing covariance functions appropriately this can be done through Gaussian processes (e.g. [@Damianou:manifold12]), but we will also consider Bayesian neural networks and other generative models, e.g. Generative Adversarial Networks [@Goodfellow:gans14] (see \textsection \ref{sec:structure}).}

\section{Data}

\notes{The availability and quality of data place particular constraints on
how we choose to decompose our ML system.

Machine learning systems often use sensitive personal data (e.g. in
health). A key challenge is how to gain benefits from this
data, such as early diagnosis of disease, without infringing on
individual rights (such as the right to privacy). One idea for a
regulatory framework to ensure that users have a voice in these
trade-offs is *data trusts*. The proposer suggested Data Trusts in
2016 for rebalancing power asymmetries between data controllers and
data subjects [@Lawrence:trusts16]. This regulatory mechanism has
gained increasing policy interest [@Delacroix:trusts18]. Project
partner Element AI has been working with Nesta to drive this debate
[@Nesta:datatrusts19]. We will integrate these regulatory ideas within
our data management plans (WP2 \textsection \ref{sec:readiness}).}

\notes{
\include{_data-science/includes/ride-sharing-soa-doa.md}
}
\notes{While the existence and/or substance of a right to explanation in the
General Data Protection Regulation has been questioned
[@Mittelstadt:explanation17] there is no doubt about the *intent* of
the legislation. Further, from an engineering perspective, it is good practice to deploy software which takes actions that have motivations which can be understood. We will develop ML techniques for automation of
the process of causal explanation (WP4 \textsection \ref{sec:structure}).

For hypervision and AutoAI we need to revisit the software
infrastructure for the *deployment* of ML systems (WP1 \textsection \ref{sec:architecture}).}

\section{Deployment: Initial Application Domains}

\notes{The proposal focuses on the technical advances in AI algorithms and
software engineering infrastructure we need to deliver machine
learning systems. But we will work closely with specific application
areas arising from Data Science Africa. Past applications have
included: monitoring of wildlife, air pollution, malaria
[@Mubangizi:malaria14] as well as agricultural auction systems, crop
disease analysis and under-resourced language recognition.

Our application domains will arise from working closely with partners
at Element AI and Data Science Africa (DSA). Co-creation of solutions
with users will ensure our technical innovations are practical and
deployable. Each PhD student will work in partnership with one or more
application domains, visiting Africa at regular intervals to ensure
our technical work stays grounded in practical deployment. Our
software will be available via open source software using licenses
that do not restrict industry use (e.g. Apache, BSD or MIT
license). We will collaborate with OpenML.org[^openml] in approaches to
make streaming solutions available to wider audiences, but we will
work particularly closely with Element AI and DSA as end users.

[^openml]: <https://www.openml.org>

Data Science Africa is an NGO which focuses on
ground up capability building in ML, AI and data science
in the African context. The organization runs two workshops and two
summer schools each year with attendees from local companies,
Universities, NGOs and Governmental organizations. A past
collaboration was on disease monitoring with UN Global Pulse,
leading to a countrywide disease monitoring system with spatial
visualization [@Mubangizi:malaria14].

Element AI is a Canadian startup with offices in London, which focus
on 'AI for Good', giving a natural affinity with Data Science
Africa. Element AI are funding two post-doctoral Research assistants as
part of the proposal.}

\section{Work Packages}


\notes{Our proposal formalizes the notion of ML systems design, and will
develop best practices for deployment monitoring, maintenance and
augmentation of Artificial Intelligence solutions. The key idea is to
build a layer of monitoring systems above the deployed
technology. These systems will review and monitor deployment of the
architecture. To develop these tools and techniques we will leverage a
co-creation approach to support deployments of AI systems
with a focus on the developing economies.}


\newslide{Thanks!}
\slides{
* podcast: [The Talking Machines](http://thetalkingmachines.com)
* newspaper: [Guardian Profile Page](http://www.theguardian.com/profile/neil-lawrence)
* advocacy: UK AI Council, Royal Society ML Working Group
}


\newslide{Too Ambitious?}
\slides{
* Is the proposal too ambitious?
* Precedent for Academic Success: Berkeley Systems
}
\newslide{UK Industry}
\slides{
* User panel (Renault F1, Mercedes F1, Fusion Group, Center for Digital Built Britain, Data Centric Engineering)
* Advisory Board: Sylvie Delacroix, Denis Therien, Joaquin Vanschoren, Mark Girolami
* Element AI and Democratisation of ML
}

\newslide{More Detail}
\slides{
* Context: interpretable ML, fairness.
* Automatic deployment and redployment of ML systems.
* Significant advances from Bayesian Optimization to Bayesian Systems Optimization
}
\newslide{How WPs interact}
\slides{
* Synergistic, but not critically interdependent
}
\newslide{Why not in a Company?}
\slides{
* Big tech companies are too large to be responsive to user needs.
* Companies do not have convening power:
  * Open source, community building. Sweet spot is close interaction between industry and academia.
* Success is *not* one company, but *many* companies
}

\newslide{Why a Fellowship?}
\slides{
* Project critically relies on applicants convening power. 
   * Also technical ability as a research leader.
   * Industrial experience from Amazon at leading systems.
* Candidate develops as an advocate for an internationally recognized advocate for AI in UK.
}

