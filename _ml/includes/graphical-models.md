\subsection{Graphical Models}

\slides{
* Represent joint distribution through *conditional dependencies*.
* E.g. Markov chain}
\notes{One way of representing a joint distribution is to consider conditional dependencies between data. Conditional dependencies allow us to factorize the distribution. For example, a Markov chain is a factorization of a distribution into components that represent the conditional relationships between points that are neighboring, often in time or space. It can be decomposed in the following form.}
$$p(\dataVector) = p(\dataScalar_\numData | \dataScalar_{\numData-1}) p(\dataScalar_{\numData-1}|\dataScalar_{\numData-2}) \dots p(\dataScalar_{2} | \dataScalar_{1})$$

\setupplotcode{import daft
from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica']}, size=30)
rc("text", usetex=True)}

\plotcode{pgm = daft.PGM(shape=[3, 1],
               origin=[0, 0], 
               grid_unit=5, 
               node_unit=1.9, 
               observed_style='shaded',
              line_width=3)


pgm.add_node(daft.Node("y_1", r"$y_1$", 0.5, 0.5, fixed=False))
pgm.add_node(daft.Node("y_2", r"$y_2$", 1.5, 0.5, fixed=False))
pgm.add_node(daft.Node("y_3", r"$y_3$", 2.5, 0.5, fixed=False))
pgm.add_edge("y_1", "y_2")
pgm.add_edge("y_2", "y_3")

pgm.render().figure.savefig("../slides/diagrams/ml/markov.svg", transparent=True)}

\includesvg{../slides/diagrams/ml/markov.svg}

\newslide{}

\slides{
Predict Perioperative Risk of Clostridium Difficile Infection Following Colon Surgery [@Steele:predictive12]}
\notes{By specifying conditional independencies we can reduce the parameterization required for our data, instead of directly specifying the parameters of the joint distribution, we can specify each set of parameters of the conditonal independently. This can also give an advantage in terms of interpretability. Understanding a conditional independence structure gives a structured understanding of data. If developed correctly, according to causal methodology, it can even inform how we should intervene in the system to drive a desired result [@Pearl:causality95]. 

However, a challenge arise when the data becomes more complex. Consider the graphical model shown below, used to predict the perioperative risk of *C Difficile* infection following colon surgery [@Steele:predictive12].}

\includepng{../slides/diagrams/bayes-net-diagnosis}{50%}{negate}

\notes{To capture the complexity in the interelationship between the data the graph becomes more complex, and less interpretable.}
