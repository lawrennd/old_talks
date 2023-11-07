\ifndef{olivettiEigenfaces}
\define{olivettiEigenfaces}

\editme

\subsection{Olivetti Faces}

You too can create your own eigenfaces. In this example we load in the 'Olivetti Face' data set, a small data set of 200 faces from the [Olivetti Research Laboratory](http://en.wikipedia.org/wiki/Olivetti_Research_Laboratory). Below we load in the data and display an image of the second face in the data set (i.e., indexed by 1).

\setupcode{import pods
import matplotlib.pyplot as plt}

\code{data = pods.datasets.olivetti_glasses()
Y = data['X'] # this data set is set up for classification, but we will model the outputs.
lbls = data['Y']
import matplotlib.cm as cm # import color map
display_index = 0
plt.imshow(np.reshape(Y[display_index, :].flatten(), (64, 64)).T, cmap = cm.Greys_r)}

Note that to display the face we had to reshape the appropriate row of the data matrix. This is because the images are turned into vectors by stacking columns of the image on top of each other to form a vector. The operation

```im = np.reshape(Y[1, :].flatten(), (64, 64)).T}```

recovers the original image into a matrix `im` by using the `np.reshape` function to return the vector to a matrix.

\subsection{Visualizing the Eigenvectors}

Each retained eigenvector is stored in the $j$th column of $\mathbf{U}$. Each of these eigenvectors is associated with particular directions of variation in the original data. Principal component analysis implies that we can reconstruct any face by using a weighted sum of these eigenvectors where the weights for each face are given by the relevant vector of the latent variables, $\latentVector_{i, :}$ and the diagonal elements of the matrix $\mathbf{L}$. We can visualize the eigenvectors $\mathbf{U}$ as images by performing the same reshape operation we used to recover the image associated with a data point above. Below we do this for the first nine eigenvectors of the Olivetti Faces data.

\code{width=3
height=3
q = width*height
fig, ax = plt.subplots(width,height,figsize=(12,12))

U, ell, sigma2 = ppca(Y, q)
lat = 0
for i in range(width):
    for j in range(height):
        ax[i, j].imshow(np.reshape(U[:, lat].flatten(), (64, 64)).T, cmap = cm.Greys_r)
        ax[i, j].set_title('Principle Component ' + str(lat+1))
        lat += 1}

\subsection{Reconstruction}

We can now attempt to reconstruct a given training point from these eigenvectors. As we mentioned above, the reconstruction is dependent on the value of the latent variable and the weights from the matrix $\mathbf{L}$. First let's compute the value of the latent variables for the point we want to construct. Then we'll use them to compute the weightings of each of the eigenvectors.

\code{mu_x, C_x = posterior(Y, U, ell, sigma2)
reconstruction_weights = mu_x[display_index, :]*ell
print(reconstruction_weights)}

This vector of reconstruction weights is applied to the 'template images' given by the eigenvectors to give us our reconstruction. Below we weight these templates and combine to form the reconstructed image, and show the comparison to the original image.

\code{fig, ax = plt.subplots(1, 2,figsize=(12,6))
ax[0].imshow(np.reshape(Y[display_index, :].flatten(), (64, 64)).T, cmap = cm.Greys_r)
ax[0].set_title('Original Example no ' + str(display_index))
ax[1].imshow(np.reshape(np.dot(U,reconstruction_weights) + Y.mean(axis=0)[None, :], (64, 64)).T, cmap = cm.Greys_r)
ax[1].set_title('Reconstruction of Example from ' + str(len(reconstruction_weights)) + ' Latent Variables')}

The quality of the reconstruction is a bit blurry, it can be improved by increasing the number of template images used (i.e. increasing the *latent dimensionality*).


\endif
