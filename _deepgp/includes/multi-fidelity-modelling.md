\ifndef{multiFidelityModelling}
\define{multiFidelityModelling}
\editme

\slides{Multi-Fidelity Emulation}
\slides{
* Normally assume that [@Kandasamy:multifidelity16;@Alonso:virtual17]:

$$\mappingFunction_i\left(\inputVector\right) = \rho \mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)$$
}

\newslide{Deep GP Emulation}

\slides{
But with Deep Gaussian processes [@Perdikaris:multifidelity17] we can consider the form 

$$\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),$$
}

\newslide{Notebook Example}

\todo{Add notes and reference from most recent paper}

\endif
