\ifndef{rideSharingSoaDoa}
\define{rideSharingSoaDoa}

\editme

\notes{\subsection{Ride Sharing: Service Oriented to Data Oriented}}

\newslide{Ride Sharing: Service Oriented}

\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-soa}{80%}}{Service oriented architecture. The data access is buried in the cost allocation service. Data dependencies of the service cannot be found without trawling through the underlying code base.}{ride-share-service-soa}

\notes{The modern approach to software systems design is known as a
*service-oriented architectures* (SOA). The idea is that software
engineers are responsible for the availability and reliability of the
API that accesses the service they own. Quality of service is
maintained by rigorous standards around *testing* of software systems.}

\newslide{Ride Sharing: Data Oriented}

\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-doa}{80%}}{Data oriented architecture. Now the joins and the updates are exposed within the streaming ecosystem. We can programatically determine the factor graph which gives the thread through the model.}{ride-share-service-doa}

\notes{In data driven decision-making systems, the quality of decision-making
is determined by the quality of the data. We need to extend the notion
of *service*-oriented architecture to *data*-oriented architecture
(DOA).

The focus in SOA is eliminating *hard* failures. Hard failures can
occur due to bugs or systems overload. This notion needs to be
extended in ML systems to capture *soft failures* associated with
declining data quality, incorrect modeling assumptions and
inappropriate re-deployments of models. We need to focus on data
quality assessments. In data-oriented architectures engineering teams
are responsible for the *quality* of their output data streams in
addition to the *availability* of the service they support
[@Lawrence:drl17]. Quality here is not just accuracy, but fairness and
explainability. This important cultural change would be capable of
addressing both the challenge of *technical debt* [@Sculley:debt15]
and the social responsibility of ML systems.}

\notes{Software development proceeds with a *test-oriented*
culture. One where tests are written before software, and software is
not incorporated in the wider system until all tests pass. We must
apply the same standards of care to our ML systems, although for ML we need statistical tests for quality, fairness and consistency within the
environment. Fortunately, the main burden of this testing need not
fall to the engineers themselves: through leveraging *classical
statistics* and *emulation* we will automate the creation and
redeployment of these tests across the software ecosystem, we call
this *ML hypervision* (WP5 \textsection \ref{sec:hypervision}).

Modern AI can be based on ML models with many millions of parameters,
trained on very large data sets. In ML, strong emphasis is placed on
*predictive accuracy* whereas sister-fields such as statistics have a
strong emphasis on *interpretability*. ML models are said to be 'black
boxes' which make decisions that are not explainable.[^dark-secret]

[^dark-secret]: See for example
    ["The Dark Secret at the Heart of AI" in Technology Review](https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/).}

\newslide{Ride Sharing: Hypothetical}

\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-doa-hypothetical}{80%}}{Data-oriented programing. There is a requirement for an estimate of the driver allocation to give a rough cost estimate before the user has confirmed the ride. In data-oriented programming, this is achieved through declaring a hypothetical stream which approximates the true driver allocation, but with restricted input information and constraints on the computational latency.}{ride-share-service-doa-hypothetical}

\notes{For the ride sharing system, we start to see a common issue with a more complex algorithmic decision-making system. Several decisions are being made multilple times. Let's look at the decisions we need along with some design criteria.

1. Driver Availability: Estimate time to arrival for Anne's ride using Anne's location and local available car locations. Latency 50 milliseconds
2. Cost Estimate: Estimate cost for journey using Anne's destination, location and local available car current destinations and availability. Latency 50 milliseconds
3. Driver Allocation: Allocate car to minimize transport cost to destination. Latency 2 seconds.

So we need:

1. a hypothetical to estimate availability. It is constrained by lacking destination information and a low latency requirement.
2. a hypothetical to estimate cost. It is constrained by low latency requirement and 


Simultaneously, drivers in this data ecosystem have an app which notifies them about new jobs and recommends them where to go.

Further advantages. Strategies for data retention (when to snapshot) can be set globally.


A few decisions need to be made in this system. First of all, when the user opens the app, the estimate of the time to the nearest ride may need to be computed quickly, to avoid latency in the service. 

This may require a quick estimate of the ride availability.}
\endif
