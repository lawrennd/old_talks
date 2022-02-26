\ifndef{highDimensionalData}
\define{highDimensionalData}

\editme

\subsection{High Dimensional Data}

\slides{* USPS Data Set Handwritten Digit
* 3648 dimensions (64 rows, 57 columns)
* Space contains much more than just this digit.}

\notes{To introduce high dimensional data, we will first of all introduce a hand written digit from the U.S. Postal Service handwritten digit data set (originally collected from scanning enveolopes) and used in the first convolutional neural network paper [@LeCun:zip89].}

\notes{@LeCun:zip89 downscaled the images to $16 \times 16$, here we use an image at the original scale, containing 64 rows and 57 columns. Since the pixels are binary, and the number of dimensions is 3,648, this space contains $2^{3,648}$ possible images. So this space contains a lot more than just one digit.}


\subsection{USPS Samples}

\notes{If we sample from this space, taking each pixel independently from a probability which is given by the number of pixels which are 'on' in the original image, over the total number of pixels, we see images that look nothing like the original digit.}


\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai}
\plotcode{fig, ax = plt.subplots(figsize=(5,5))

six_image = mlai.load_pgm('br1561_6.3.pgm', directory ='\diagramsDir/ml')
rows = six_image.shape[0]
col = six_image.shape[1]
      
ax.imshow(six_image,interpolation='none').set_cmap('gray')
mlai.write_figure('\writeDiagramsDir/dimred/dem_six000.png')
for i in range(3):
    rand_image = np.random.rand(rows, col)<((six_image>0).sum()/float(rows*col))
    ax.imshow(rand_image,interpolation='none').set_cmap('gray')
    mlai.write_figure('\writeDiagramsDir/dimred/dem_six{i:0>3}.png'.format(i=i+1))}

\setupdisplaycode{from ipywidgets import IntSlider
import pods}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('dem_six{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=IntSlider(0, 0, 3, 1))}


\slides{\define{width}{40%}
\startanimation{dem-six-sample}{0}{4}
\newframe{\includepng{\diagramsDir/dimred/dem_six000}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six001}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six002}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six003}{\width}}{dem-six-sample}
\endanimation}

\notes{\figure{\threeColumns{\includepng{\diagramsDir/dimred/dem_six000}{100%}}{\includepng{\diagramsDir/dimred/dem_six001}{100%}}{\includepng{\diagramsDir/dimred/dem_six002}{100%}}{30%}{30%}{30%}}{Even if we sample every nano second from now until the end of the universe we won't see the original six again.}{dem-six-sample}}

\slides{* Even if we sample every nanonsecond from now until end of universe you won't see original six!}

\notes{Even if we sample every nanosecond from now until the end of the universe you won't see the original six again.}

\subsection{Simple Model of Digit}

\notes{So, an independent pixel model for this digit doesn't seem sensible. The total space is enormous, and yet the space occupied by the type of data we're interested in is relatively small.}

\notes{Consider a different type of model. One where we take a prototype six and we rotate it left and right to create new data.}

\slides{* Rotate a prototype }

\setupcode{from scipy.misc import imrotate}

\code{six_image = mlai.load_pgm('br1561_6.3.pgm', directory ='\diagramsDir/dimred')
six_image = np.hstack([np.zeros((rows, 3)), six_image, np.zeros((rows, 4))])
dim_one = np.asarray(six_image.shape)
angles = range(360)
i = 0
Y = np.zeros((len(angles), np.prod(dim_one)))
for angle in angles:
    rot_image = rotate(six_image, angle, mode='nearest')
    dim_two = np.asarray(rot_image.shape)
    start = [int(round((dim_two[0] - dim_one[0])/2)), int(round((dim_two[1] - dim_one[1])/2))]
    crop_image = rot_image[start[0]+np.array(range(dim_one[0])), :][:, start[1]+np.array(range(dim_one[1]))]
    Y[i, :] = crop_image.flatten()}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('\diagramsDir/dimred/dem_six_rotate{counter:0>3}.png', directory='\writeDiagramsDir/ml', counter=(0, 6))}

\slides{\define{width}{40%}
\startanimation{dem-six-rotate}{1}{6}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate001}{\width}}{dem-six-rotate}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate002}{\width}}{dem-six-rotate}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate003}{\width}}{dem-six-rotate}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate004}{\width}}{dem-six-rotate}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate005}{\width}}{dem-six-rotate}
\newframe{\includepng{\diagramsDir/dimred/dem_six_rotate006}{\width}}{dem-six-rotate}
\endanimation}

\notes{\figure{\threeColumns{\includepng{\diagramsDir/dimred/dem_six_rotate001}{100%}}{\includepng{\diagramsDir/dimred/dem_six_rotate003}{100%}}{\includepng{\diagramsDir/dimred/dem_six_rotate005}{100%}}{30%}{30%}{30%}}{Rotate a prototype six to form a set of plausible sixes.}{dem-six-rotate}}

\newslide{}

\figure{\columns{\includepng{\diagramsDir/dimred/dem_manifold_print001}{100%}}{\includepng{\diagramsDir/dimred/dem_manifold_print002}{100%}}{30%}{30%}}{The rotated sixes projected onto the first two principal components of the 'rotated data set'. The data lives on a one dimensional manifold in the 3,648 dimensional space.}{dem-six-mainfold-print}

\subsection{Low Dimensional Manifolds}

\slides{* Pure rotation is too simple
  * In practice data may undergo several distortions.
* For high dimensional data with *structure*:
  * We expect fewer distortions than dimensions;
  * Therefore we expect the data to live on a lower dimensional manifold.
  * Conclusion: Deal with high dimensional data by looking for a lower dimensional non-linear embedding.}
  
\notes{Of course, in practice pure rotation of the image is too simple a model. Digits can undergo several distortions and retain their nature. For example, they can be scaled, they can go through translation, they can udnergo 'thinning'. But, for data with 'structure' we expect fewer of these distortions than the dimension of the data. This means we expect data to live on a lower dimensonal manifold. This implies that we should deal with high dimensional data by looking for a lower dimensional (non-linear) embedding.}

\endif
