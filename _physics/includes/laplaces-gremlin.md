\ifndef{laplacesGremlin}
\define{laplacesGremlin}

\editme


\subsection{Laplace's Gremlin}

\slides{\figure{\includepng{\diagramsDir/physics/philosophicaless00lapliala_18_cropped}{60%}}{To Laplace, determinism is a strawman. Ignorance of mechanism and data leads to uncertainty which should be dealt with through probability.}{probability-relative-in-part}
>
> *Philosophical Essay on Probabilities* @Laplace-essai14 pg 5
}

\notes{
> The curve described by a simple molecule of air or vapor is regulated
> in a manner just as certain as the planetary orbits; the only
> difference between them is that which comes from our ignorance. 
> Probability is relative, in part to this ignorance, in part to our
> knowledge. We know that of three or greater number of events a single
> one ought to occur; but nothing induces us to believe that one of them
> will occur rather than the others. In this state of indecision it is
> impossible for us to announce their occurrence with certainty. It is,
> however, probable that one of these events, chosen at will, will not
> occur because we see several cases equally possible which exclude its
> occurrence, while only a single one favors it.
>
> --- Pierre-Simon Laplace [@Laplace-essai14], pg 5
}

\speakernotes{I like to refer to this notion as "Laplace's Gremlin", because the lack of knowledge is the "gremlin of uncertainty" that inhibits the "deterministic demon"}

\notes{The representation of ignorance through probability is the true message of Laplace, I refer to this message as "Laplace's gremlin", because it is the gremlin of uncertainty that interferes with the demon of determinism to mean that our predictions are not deterministic. 

Our separation of the uncertainty into the data, the model and the computation give us three domains in which our doubts can creep into our ability to predict. Over the last three lectures we've introduced some of the basic tools we can use to unpick this uncertainty. You've been introduced to, (or have yow reviewed) *Bayes' rule*. The rule, which is a simple consequence of the product rule of probability, is the foundation of how we update our beliefs in the presence of new information.}

\notes{The real point of Laplace's essay was that we don't have access to all the data, we don't have access to a complete physical understanding, and as the example of the Game of Life shows, even if we did have access to both (as we do for "Conway's universe") we still don't have access to all the compute that we need to make deterministic predictions. There is uncertainty in the system which means we can't make precise predictions.}


\notes{I like to call this "Laplace's Gremlin". Gremlins are imaginary creatures used as an explanation of failure in aircraft, causing crashes. In that sense the Gremlin represents the uncertainty that a pilot felt about what might go wrong in a plane which might be "theoretically sound" but in practice is poorly maintained or exposed to conditions that take it beyond its design criteria. Laplace's gremlin is all the things that your model, data and ability to compute don't account for bringing about failures in your ability to predict. Laplace's Gremlin is the uncertainty in the system.}

\newslide{}

\figure{\includejpg{\diagramsDir/ai/gremlins-think-its-fun-to-hurt-you}{40%}}{Gremlins are seen as the cause of a number of challenges in this World War II poster.}{germlins-think-its-fun-to-hurt-you}

\endif
