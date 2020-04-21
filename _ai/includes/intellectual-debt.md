\ifndef{intellectualDebt}
\define{intellectualDebt}

\editme

\section{Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/2020-02-12-intellectual-debt}{70%}}{Jonathan Zittrain's term to describe the challenges of explanation that come with AI is Intellectual Debt.}{intellectual-debt}

\newslide{Technical Debt}

\notes{In computer systems the concept of *technical debt* has been surfaced by
authors including @Sculley:debt15. It is an important concept, that I
think is somewhat hidden from the academic community, because it is a
phenomenon that occurs when a computer software system is deployed.}

\subsection{Lean Startup Methodology}

\notes{In technology, there is the notion of a "minimum viable product" (MVP).
Sometimes called "minimum loveable product" (MLP). A minimum viable
product is the smallest thing that you need to ship to test your
commercial idea. There is a methodology known as the "lean start-up"
methodology, where you use the least effort to create your machine
learning model is deployed.

The idea is that you should build the quickest thing possible to test
your market and see if your idea works. Only when you know your idea is
working should you invest more time and personnel in the software.

Unfortunately, there is a tension between deploying quickly and
deploying a maintainable system. To build an MVP you deploy quickly, but
if the system is successful you take a 'maintenance hit' in the future
because you've not invested early in the right maintainable design for
your system.

You save on engineer time at the beginning, but you pay it back with
high interest when you need a much higher operations load once the
system is deployed.

The notion of the Sculley paper is that there are particular challenges
for machine learning models around technical debt.}

\subsection{The Mythical Man-month}

\figure{\includejpg{\diagramsDir/ai/Mythical_man-month_(book_cover)}{40%}}{The Mythical Man-month [@Brooks:mythical75] is a 1975 book focussed on the challenges of software project coordination.}{intellectual-debt}

\notes{However, when managing systems in production, you soon discover
maintenance of a rapidly deployed system is not your only problem.

To deploy large and complex software systems, an engineering approach
known as "separation of concerns" is taken. Frederick Brooks' book "The
Mythical Man-month" [@Brooks:mythical75], has itself gained almost
mythical status in the community. It focuses on what has become known as
Brooks' law "adding manpower to a late software project makes it later".

Adding people (men or women!) to a project delays it because of the
communication overhead required to get people up to speed.}

\subsection{Separation of Concerns}

\notes{To construct such complex systems an approach known as "separation of
concerns" has been developed. The idea is that you architect your
system, which consists of a large-scale complex task, into a set of
simpler tasks. Each of these tasks is separately implemented. This is
known as the decomposition of the task.

This is where Jonathan Zittrain's beautifully named term "intellectual
debt" rises to the fore. Separation of concerns enables the construction
of a complex system. But who is concerned with the overall system?}

\newslide{Intellectual Debt}

-   Technical debt is the inability to *maintain* your complex software
    system.

-   Intellectual debt is the inability to *explain* your software
    system.

\notes{It is right there in our approach to software engineering. "Separation
of concerns" means no one is concerned about the overall system itself.}

\endif
