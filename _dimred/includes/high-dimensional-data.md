\ifndef{highDimensionalData}
\define{highDimensionalData}

\editme

\subsection{High Dimensional Data}

* USPS Data Set Handwritten Digit
* 3648 dimensions (64 rows, 57 columns)
* Space contains much more than just this digit.

\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai}
\plotcode{fig, ax = plt.subplots(figsize=(5,5))

six_image = mlai.load_pgm('br1561_6.3.pgm', directory ='\writeDiagramsDir/ml')
rows = six_image.shape[0]
col = six_image.shape[1]
      
ax.imshow(six_image,interpolation='none').set_cmap('gray')
mlai.write_figure(\diagramsDir/ml/dem_six000.png')
for i in range(3):
    rand_image = np.random.rand(rows, col)<((six_image>0).sum()/float(rows*col))
    ax.imshow(rand_image,interpolation='none').set_cmap('gray')
    mlai.write_figure(\diagramsDir/ml/dem_six{i:0>3}.png'.format(i=i+1))}

\setupdisplaycode{from ipywidgets import IntSlider
import pods}
\displaycode{pods.notebook.display_plots('dem_six{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=IntSlider(0, 0, 3, 1))}

\figure{\includepng{\diagramsDir/ml/dem_six000}{30%}}{}{dem_six000}
\figure{\includepng{\diagramsDir/ml/dem_six001}{30%}}{}{dem_six001}
\figure{\includepng{\diagramsDir/ml/dem_six002}{30%}}{}{dem_six002}
\figure{\includepng{\diagramsDir/ml/dem_six003}{30%}}{}{dem_six003}

\subsection{USPS Samples}

* Even if we sample every nanonsecond from now until end of universe you won't see original six!

\subsection{Simple Model of Digit}

* Rotate a prototype 

\setupcode{from scipy.misc import imrotate}

\code{six_image = np.hstack([np.zeros((rows, 3)), six_image, np.zeros((rows, 4))])
dim_one = np.asarray(six_image.shape)
angles = range(360)
i = 0
Y = np.zeros((len(angles), np.prod(dim_one)))
for angle in angles:
    rot_image = imrotate(six_image, angle, interp='nearest')
    dim_two = np.asarray(rot_image.shape)
    start = [int(round((dim_two[0] - dim_one[0])/2)), int(round((dim_two[1] - dim_one[1])/2))]
    crop_image = rot_image[start[0]+np.array(range(dim_one[0])), start[1]+np.array(range(dim_one[1]))]
    Y[i, :] = crop_image.flatten()}

\displaycode{pods.notebook.display_plots('dem_six_rotate{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=(0, 3))}

\figure{\includepng{\diagramsDir/ml/dem_six_rotate000}{30%}}{}{dem_six_rotate000}
\figure{\includepng{\diagramsDir/ml/dem_six_rotate001}{30%}}{}{dem_six_rotate001}
\figure{\includepng{\diagramsDir/ml/dem_six_rotate002}{30%}}{}{dem_six_rotate002}
\figure{\includepng{\diagramsDir/ml/dem_six_rotate003}{30%}}{}{dem_six_rotate003}

\subsection{Low Dimensional Manifolds}

* Pure rotation is too simple
  * In practice data may undergo several distortions.
* For high dimensional data with *structure*:
  * We expect fewer distortions than dimensions;
  * Therefore we expect the data to live on a lower dimensional manifold.
  * Conclusion: Deal with high dimensional data by looking for a lower dimensional non-linear embedding.

\endif
