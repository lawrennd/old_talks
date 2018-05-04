---
title: Peppercorns and Machine Learning System Design
abstract: "Machine learning is fundamental to two important
  technological domains, artificial intelligence and data science. In
  this talk we will attempt to make a simple definition to distinguish
  between the two, then we will focus on the challenges of machine
  learning in *application* to artificial intelligence particularly from 
  the perspective of systems design. We expect a particular challenge to 
  be the deployment of such systems in real environment, where 
  unforeseen consequences of interaction with real world environments
  will produce embarrassing failures. Because these failures are not
  bugs, in that the system will be performing as designed, but
  failures of imagination of the designers we introduce a new term for
  them: 'peppercorns'."
css: talks.css
published: 2017-06-02
venue: Sheffield ML Research Retreat
layout: slides
transition: None
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

#### Peppercorns and Machine Learning System Design
#### 2017-06-02
#### Neil D. Lawrence
#### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_ai/includes/embodiment-factors.md}


### Internet of People

* Fog computing: barrier between cloud and device blurring.

* Stuxnet: Adversarial and Security implications for intelligent systems.

* Complex feedback between algorithm and implementation
  
### Deploying ML in Real World: Machine Learning Systems Design

* Major new challenge for systems designers.

* Internet of Intelligence but currently:

	* AI systems are currently *fragile*

\include{_ai/includes/ml-systems-design-long.md}
\include{_ai/includes/intelligent-system-paolo.md}

### Conclusion

* Difference between Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.

### Thanks!

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
