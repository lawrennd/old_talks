### Multi-fidelity Modelling {data-transition=None}


### Multi-Fidelity Emulation {data-transition="None"}

* Normally assume that [@Kandasamy:multifidelity16,@Alonso:virtual17]:

$$\mappingFunction_i\left(\inputVector\right) = \rho \mappingFunction_{i-1}\left(\inputVector\right) + \delta_i\left(\inputVector \right)$$

### Deep GP Emulation {data-transition="None"}

But with Deep Gaussian processes [@Perdikaris:multifidelity17] we can consider the form 

$$\mappingFunction_i\left(\inputVector\right) = \mappingFunctionTwo_{i}\left(\mappingFunction_{i-1}\left(\inputVector\right)\right) + \delta_i\left(\inputVector \right),$$

### Notebook Example {data-transition=None}
