\ifndef{gpBigDataTechnical}
\define{gpBigDataTechnical}
\editme
\newslide{Leads to Other Approximations ...}

* Let’s be explicity about storing approximate posterior of $\inducingVector$, $q(\inducingVector)$.
* Now we have
  $$p(\dataVector^*|\dataVector) = \int p(\dataVector^*| \inducingVector) q(\inducingVector | \dataVector) \text{d} \inducingVector$$

\newslide{Leads to Other Approximations ...}

* Inducing variables look a lot like regular parameters.
* *But*: their dimensionality does not need to be set at design time.
* They can be modified arbitrarily at run time without effecting the model likelihood.
* They only effect the quality of compression and the lower bound.

\newslide{In GPs for Big Data}

* Exploit the resulting factorization ...
  $$p(\dataVector^*|\dataVector) = \int p(\dataVector^*| \inducingVector) q(\inducingVector | \dataVector) \text{d} \inducingVector$$
* The distribution now *factorizes*:
  $$p(\dataVector^*|\dataVector) = \int \prod_{i=1}^{\numData^*}p(\dataScalar^*_i| \inducingVector) q(\inducingVector | \dataVector) \text{d} \inducingVector$$
* This factorization can be exploited for stochastic variational inference [@Hoffman:stochastic12].

\endif
