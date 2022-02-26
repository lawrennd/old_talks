\ifndef{olivettiGlassesData}
\define{olivettiGlassesData}

\editme

\notes{Correspond to whether the subject of the image is wearing glasses.
Set up the ipython environment and download the data:}

\setupcode{from scipy import io}

\notes{First let's retrieve some data. We will use the ORL faces data
set, our objective will be to classify whether or not the subject in
an image is wearing glasess.}

\notes{Here's a simple way to visualise the data. Each pixel in the
image will become an input to the GP.}

\setupcode{import pods}

\code{data = pods.datasets.olivetti_glasses()
X = data['X']
y = data['Y']
Xtest = data['Xtest']
ytest = data['Ytest']
print(data['info'], data['details'], data['citation'])}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.imshow(X[120].reshape(64, 64, order='F'),interpolation='nearest',cmap=pb.cm.gray)

mlai.write_figure('olivetti-glasses-image.png', directory='\writeDiagramsDir/datasets')}

\newslide{}

\figure{\includepng{'\diagramsDir/datasets/olivetti-glasses-image}{60%}}{Image from the Oivetti glasses data sets.}{olivetti-glasses-image}


\endif
