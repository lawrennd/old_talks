\ifndef{milan}
\define{milan}

\editme

\subsection{Milan}
\slides{
1.  A general-purpose stream algebra that encodes relationships between
      data streams (the Milan Intermediate Language or Milan IL)

2.  A Scala library for building programs in that algebra.

3.  A compiler that takes programs expressed in Milan IL and produces a
     Flink application that executes the program.
}

\newslide{}

\slides{
\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic000}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}
}
\slides{
\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic001}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}
}
\slides{
\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic002}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}
}
\slides{
\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic003}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}
}
\slides{
\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic004}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}
}

\newslide{}

\figure{\includediagram{\diagramsDir/software/milan-schematic}{80%}}{The Milan Software has a general purpose stream algebra at its core, the Milan IL.}{milan-schematic}

\newslide{}

\figure{\includepng{\diagramsDir/software/milan}{80%}}{The Milan Software is designed for building modern AI systems. <https://github.com/amzn/milan/>}{milan-software-page}


\notes{At Amazon my team built a *data-oriented programming* language which is
[now available through BSD license](https://github.com/amzn/milan). The language is called Milan. The
team was led by Tom Borchert, quoting from [Tom's blog
on Milan](https://tborchertblog.wordpress.com/2020/02/13/28/):

> Milan has three components:
>
> 1.  A general-purpose stream algebra that encodes relationships between
>      data streams (the Milan Intermediate Language or Milan IL)
>
> 2.  A Scala library for building programs in that algebra.
>
> 3.  A compiler that takes programs expressed in Milan IL and produces a
>     Flink application that executes the program.
>
> Component (2) can be extended to support interfaces in additional
> languages, and component (3) can be extended to support additional
> runtime targets. Considering just the multiple interfaces and the
> multiple runtimes, Milan looks a lot like the much more mature Apache
> Beam. The difference lies in (1), Milan's general-purpose stream
> algebra.

It is through the general-purpose stream algebra that we hope to make
significant inroads on the intellectual debt challenge.

The stream algebra defines the relationship between different machine
learning components in the wider software architecture. Composition of
multiple services cannot occur without a signature existing within the
stream algebra. The Milan IL becomes the key information structure that
is required to reason about the wider software system.}

\notes{\subsection{Context}}

\notes{This deals with the challenges that arise through the *death of the
programmer* because we can now see the context around each service. This
allows us to design the relevant validation checks to ensure that
accuracy and fairness are maintained. By recompiling the algebra to
focus on a particular decision within the system we can also derive new
statistical tests to validate performance. These are the checks that we
refer to as progression testing. The loss of programmer control means
that we can no longer rely on software tests written at design time, we
must have the capability to deploy new (statistical) tests after
deployment as the uses to which each service is placed extend to
previously un-envisaged domains.}

\notes{\subsection{Stateless Services}}

\notes{Importantly, Milan does not place onerous constraints on the builders of
individual machine learning models (or other components). Standard
modelling frameworks can be used. The main constraint is that any code
that is not visible to the ecosystem does not maintain or store global
state. This condition implies that the parameters of any machine
learning model need to also be declared as an input to the model within
the Milan IL.}

\subsection{Meta Modelling}

\figure{\includepng{\diagramsDir/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://amzn.github.io/emukit/>}{emukit-software-page}

\notes{Where does machine learning come in? The strategy I propose is that the
Milan IL is integrated with meta-modelling approaches to assist in the
explanation of the decision-making framework. At their simplest these
approaches may be novelty detection algorithms on the data streams that
are emerging from a given service. This is a form of *progression
testing*. But we can go much further. By knowing the training data, the
inputs and outputs of the individual services in the software ecosystem,
we can build meta-models that test for fairness, accuracy not just of
individual system components, but short or long cascades of decision
making. Through the use of the Milan IL algebra all these tests could be
automatically deployed. The focus of machine learning is on the
models-that-model-the-models. The meta-models.

In Amazon, our own focus was on the use of statistical emulators,
sometimes known as surrogate models, for fulfilling this task. The work
we were putting into this route is available through another software
package, [Emukit, a framework for decision making under
uncertainty](https://amzn.github.io/emukit/). With collaborators my
current focus for addressing these issues is a form of fusion of Emukit
and Milan (Milemukit??). But the nature of this fusion requires testing
on real world problem sets. A task we hope to carry out in close
collaboration with colleagues at [Data Science
Africa](http://www.datascienceafrica.org/).}


\endif
