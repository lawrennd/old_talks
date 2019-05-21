\ifndef{dataOrientedArchitectures}
\define{dataOrientedArchitectures}

\editme

\subsection{Data Oriented Architectures}

* Convert data to a *first class citizen*.
* View system as operations on *data streams*.
* Expose data operations in a programmatic way.

\subsection{Streaming System}

* Move from pull updates to push updates.
* Operate on rows rather than columns.
* Lead to stateless logic: persistence handled by system.
* Example Apache Kafka + Apache Flink

\include{_data-science/includes/apache-flink.md}

\subsection{Trading System}

\slides{* High frequency share trading.
* Stream of prices with millisecond updates.
* Trades required on millisecond time line
}

\setupcode{import pandas as pd
import numpy as np
import os}

\code{days=pd.date_range(start='21/5/2017', end='21/05/2020')
z = np.random.randn(len(days), 1)
x=z.cumsum()+400}

\code{prices = pd.Series(x, index=days)
hypothetical = prices.loc['21/5/2019':]
real = prices.copy()
real['21/5/2019':] = np.NaN}

\setupplotcode{import mlai
import teaching_plots as plot
import matplotlib.pyplot as plt}

\plotcode{diagrams = '../slides/diagrams/data-science/'
fontsize=16}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
real.plot(color='k', fontsize=fontsize)

hypothetical.plot(color='b')
mlai.write_figure(os.path.join(diagrams, 'hypothetical-prices.svg'), transparent=True)
ylim = ax.get_ylim()}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
real.plot(color='k', fontsize=fontsize)
mlai.write_figure(os.path.join(diagrams, 'real-prices.svg'), transparent=True)
ax.set_ylim(ylim)}

\notes{Anne wishes to build a share trading system. She has access to a high frequency trading system which provides prices and allows trades at millisecond intervals. She wishes to build an automated trading system.

Let's assume that price trading data is available as a data stream. But the price now is not the only information that Anne needs, she needs an estimate of the price in the future.}

\newslide{Real Price}

\slides{\includediagram{../slides/diagrams/data-science/real-prices}{80%}}

\newslide{Future Price}

\slides{\includediagram{../slides/diagrams/data-science/hypothetical-prices}{80%}}


\figure{\includediagram{../slides/diagrams/data-science/hypothetical-prices}{80%}}{Anne has access to the share prices in the black stream but not in the blue stream. A hypothetical stream is the stream of future prices. Anne can define this hypothetical under constraints (latency, input etc). The need for a model is now exposed in the software infrastructure}{hypothetical-prices}

\subsection{Hypothetical Streams}

\slides{
* Real stream --- share prices
    * derived *hypothetical* stream --- share prices in futrure.
* Hypothetical constrained by
    * input constraints.
    * decision functional
    * computational requirements (latency)
}


\notes{We'll call the future price a hypothetical stream. 

A hypothetical stream is a desired stream of information which cannot be directly accessed. The lack of direct access may be because the events happen in the future, or there may be some latency between the event and the availability of the data. 

Any hypothetical stream will only be provided as a prediction, ideally with an error bar. 

The nature of the hypothetical Anne needs is dependent on her decision making process. In Anne's case it will depend over what period she is expecting her returns. In MDOP Anne specifies a hypothetical that is derived from the pricing stream. 

It is not the price stream directly, but Anne looks for *future* predictions from the price stream, perhaps for price in $T$ days' time.

At this stage, this stream is merely typed as a hypothetical.

There are constraints on the hypothetical, they include: the *input* information, the upper limit of latency between input and prediction, and the decision Anne needs to make (how far ahead, what her upside, downside risks are). These three constraints mean that we can only recover an approximation to the hypothetical.}

\subsection{Hypothetical Advantage}

\slides{* Modelling is now required.
* But modelling is declared in the ecosystem.
* If it's manual, warnings can be used 
     * calibration, fairness, dataset shift
* Opens door to auto-adaptable ML.
}

\notes{What is the advantage to defining things in this way? By defining clearly the two streams as real and hypothetical variants of each other, we now enable automation of the deployment and any redeployment process. The hypothetical can be *instantiated* against the real, and design criteria can be constantly evaluated triggering retraining when necessary.}

\subsection{Ride Sharing System}

\notes{As a second example, we'll consider a ride sharing app. 

Anne is on her way home now, she wishes to hail a car using a ride sharing app. 

The app is designed in the following way. On opening her app Anne is notified about driverss in the nearby neighborhood, and given an estimate of the time a ride may take to come.

Given this information about driver availability, Anne may feel encouraged to enter a destination. Given this destination, a price estimate can be given. This price is conditioned on other riders that may wish to go in the same direction, but the price estimate needs to be made before the user agrees to the ride. 

Business customer service constraints dictate that this price may not change after Anne's order is confirmed. 

In this simple system, several decisions are being made, each of them on the basis of a hypothetical.

When Anne calls for a ride, she is provided with an estimate based on the expected time a ride can be with her. But this estimate is made without knowing where Anne wants to go. There are constraints on drivers imposed by regional boundaries, reaching the end of their shift, or their current passengers mean that this estimate can only be a best guess.

This best guess may well be driven by previous data.
}

\newslide{Ride Sharing: Service Oriented}

\slides{\includediagram{../slides/diagrams/data-science/ride-share-service-soa}{80%}}

\newslide{Ride Sharing: Data Oriented}

\slides{\includediagram{../slides/diagrams/data-science/ride-share-service-doa}{80%}}

\newslide{Ride Sharing: Hypothetical}

\slides{\includediagram{../slides/diagrams/data-science/ride-share-service-doa-hypothetical}{80%}}

\notes{\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-soa}{80%}}{Service oriented architecture. The data access is buried in the cost allocation service. Data dependencies of the service cannot be found without trawling through the underlying code base.}{ride-share-service-soa}}

\notes{\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-doa}{80%}}{Data oriented architecture. Now the joins and the updates are exposed within the streaming ecosystem. We can programatically determine the factor graph which gives the thread through the model.}{ride-share-service-doa}}

\notes{\figure{\includediagram{../slides/diagrams/data-science/ride-share-service-doa-hypothetical}{80%}}{Data oriented programing. There is a requirement for an estimate of the driver allocation to give a rough cost estimate before the user has confirmed the ride. In data oriented programming, this is achieved through declaring a *hypothetical* stream which approximates the true driver allocation, but with restricted input information and constraints on the computational latency.}{ride-share-service-doa-hypothetical}}

\notes{For the ride sharing system, we start to see a common issue with a more complex algorithmic decision making system. Several decisions are being made multilple times. Let's look at the decisions we need along with some design criteria.

1. Car Availability: Estimate time to arrival for Anne's ride using Anne's location and local available car locations. Latency 50 milliseconds
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
