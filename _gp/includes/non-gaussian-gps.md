\ifndef{nonGaussianGps}
\define{nonGaussianGps}

\editme

\section{Non Gaussian Likelihoods}

\notes[Gaussian processes model functions. If our observation is a corrupted version of this function and the corruption process is *also* Gaussian, it is trivial to account for this. However, there are many circumstances where our observation may be non Gaussian. In these cases we need to turn to approximate inference techniques. As a simple illustration, we'll use a dataset of binary observations of the language that is spoken in different regions of East-Timor. First we will load the data and a couple of libraries to visualize it.}


\setupcode{from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import cPickle as pickle
import urllib}

\code{urllib.urlretrieve('http://staffwww.dcs.sheffield.ac.uk/people/M.Zwiessele/gpss/lab2/EastTimor.pickle', 'EastTimor2.pickle')}

\code{# Load the data
with open("./EastTimor2.pickle","rb") as f:
    X,y,polygons = pickle.load(f)}

\notes{Now we will create a map of East Timor and, using GPy, plot the data on top of it. 
A classification model can be defined in a similar way to the regression model, but now using `GPy.models.GPClassification`. However, once we've define the model, we also need to update the approximation to the likelihood. This runs the Expectation propagation updates.}


\plotcode{#Visualize a map of East-Timor
fig = plt.figure()
ax = fig.add_subplot(111)
for p in polygons:
    ax.add_collection(PatchCollection([Polygon(p)],facecolor="#F4A460"))
ax.set_xlim(124.,127.5)
ax.set_ylim(-9.6,-8.1)
ax.set_xlabel("longitude")
ax.set_ylabel("latitude")}

\setupcode{import GPy}

\code{#Define the model
kern = GPy.kern.RBF(2)
m = GPy.models.GPClassification(X,y, kernel=kern)
print(m)}


\plotcode{m.plot(ax=ax)}

\notes{The decision boundary should be quite poor! However we haven't optimized the model. Try the following:}

\code{m.optimize()
print(m)}

\plotcode{m.plot()}



\notes{The optimization is based on the likelihood approximation that was made after we constructed the model. However, because we've now changed the model parameters the quality of that approximation has now probably deteriorated. To improve the model we should iterate between updating the Expectation propagation approximation and optimizing the model parameters. }

\codeAssignment{Write a for loop to optimize the model by iterating between EP and kernel parameters optimization. What happens with the decision boundary after these iterations?}{}{10}

\include{_gp/includes/olympic-marathon-gp-student-t.md}

\section{Sparse GP Classification}

\notes{In this section we'll combine expectation propagation with the low rank approximation to build a simple image classification application. For this toy example we'll classify whether or not the subject of the image is wearing glasses.}


\include{_datasets/includes/olivetti-glasses-data.md}

\notes{Next we choose some inducing inputs. Here we've chosen inducing inputs by applying k-means clustering to the training data. Think about whether this is a good scheme for choosing the inputs? Can you devise a better one?}


\code{X.shape
y.shape
print(X)}

\setupcode{from scipy import cluster}

\code{M = 8
X = (X - X.mean(0)[np.newaxis,:])/X.std(0)[np.newaxis,:]
Z = np.random.permutation(X)[:M]}


\notes{Finally, we're ready to build the classifier object.}


\code{kern = GPy.kern.RBF(X.shape[1],lengthscale=20) + GPy.kern.White(X.shape[1],0.001)
model = GPy.models.SparseGPClassification(X, y, kernel=kern, Z=Z)
model.optimize(messages=True)
display(model)}


\writeAssignment{Look at the following figure. What is being shown? Why does it look
like this?}{}{10}

\newslide{}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.imshow(m.Z.gradient[0].reshape(64,64,order='F'),interpolation='nearest',cmap=pb.cm.gray)

mlai.write_figure('olivetti-inducing-variable-gradients.png', directory='\writeDiagramsDir/gp')}


\figure{\includepng{'\diagramsDir/datasets/olivetti-inducing-variable-gradients}{60%}}{The gradients of the inducing variable.}{olivetti-inducing-variable-gradients}


\codeAssignment{Write some code to evaluate the model's performance, using the held-out data that we separated earlier. How is the error rate? Is that better than random guessing? *Hint:* `GPy.util.classification.conf_matrix(prob_estimate,ytest)`}{}{10}

\codeAssignment{Write another simple for loop to optimize the model. How low can you get the error rate to go? What kind of kernel do you think might be appropriate for this classification task?}{}{10}

\endif
