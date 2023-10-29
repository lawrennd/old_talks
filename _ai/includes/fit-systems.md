\ifndef{fitSystems}
\define{fitSystems}

\editme

\subsection{FIT Models to FIT Systems}

\slides{* Focus in machine learning has been on FAcT learning.
* Fairness, accountability and Transparency in individual models.
* But individual models aren't the problem. 
* Fariness, interpetability and transparency required for whole system.}

\include{_ai/includes/intellectual-debt-blog-post.md}

\notes{So, this is where, my understanding of intellectual debt in ML systems
departs, I believe from John Zittrain's. The long-term challenge is
*not* in the individual model. We have excellent statistical tools for
validating what any individual model, the long-term challenge is the
complex interaction between different components in the decomposed
system, where the original intent of each component has been forgotten
(except perhaps by Lancelot) and each service has been repurposed. We need to move from FIT models to FIT systems.}

\notes{How to address these challenges? With collaborators I've been working
towards a solution that contains broadly two parts. The first part is
what we refer to as "Data-Oriented Architectures". The second part is "meta modelling", machine learning techniques that help us model the models. }


\endif
