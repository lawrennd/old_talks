\ifndef{robotWirelessPpca}
\define{robotWirelessPpca}

\editme 

\subsection{Robot Navigation Example}

In the next example we will load in data from a
robot navigation problem. The data consists of wireless access point strengths
as recorded by a robot performing a loop around the University of Washington's
Computer Science department in Seattle. The robot records all the wireless
access points it can cache and stores their signal strength.

\setupcode{import pods}
\code{data = pods.datasets.robot_wireless()
Y = data['Y']
Y.shape}

There are 215 observations of 30 different access points. In this case the model
is suggesting that the access point signal strength should be linearly dependent
on the location in the map. In other words we are expecting the access point
strength for the $j$th access point at robot position $x_{i, :}$ to be
represented by $y_{i, j} = \weightVector_{j, :}^\top \latentVector_{i, :} +
\epsilon_{i,j}$.

\setupcode{import matplotlib.pyplot as plt}

\code{q = 2
U, ell, sigma2 = ppca(Y, q)
mu_x, C_x = posterior(Y, U, ell, sigma2)

fig, ax = plt.subplots(figsize=(8,8))
ax.plot(mu_x[:, 0], mu_x[:, 1], 'rx-')
ax.set_title('Latent Variable: Robot Inferred Locations')
fig, ax = plt.subplots(figsize=(8,8))
W = U*ell[None, :]
ax.plot(W[:, 0], W[:, 1], 'bo')
ax.set_title('Access Point Inferred Locations')}

\code{U, ell, sigma2 = ppca(Y.T, q)}

\endif
