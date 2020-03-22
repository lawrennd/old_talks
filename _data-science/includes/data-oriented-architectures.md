\ifndef{dataOrientedArchitectures}
\define{dataOrientedArchitectures}

\editme


\subsection{Data Oriented Architectures}
\slides{
* Convert data to a *first-class citizen*.
* View system as operations on *data streams*.
* Expose data operations in a programmatic way.
}
\notes{In a streaming architecture we shift from management of services, to management of data streams. Instead of worrying about availability of the services we shift to worrying about the quality of the data those services are producing.}

\newslide{Data Orientated Architectures}

\slides{
* Historically we've been *software first*
    * A necessary but not sufficient condition for *data first*
* Move from
    1. service orientated architectures
	2. *data orientated architectures*
}
\notes{Historically we've been *software first*, this is a necessary but insufficient condition for *data first*. We need to move from software-as-a-service to data-as-a-service, from service oriented architectures to *data oriented architectures*.}

\subsection{Streaming System}
\slides{
* Move from pull updates to push updates.
* Operate on rows rather than columns.
* Lead to stateless logic: persistence handled by system.
* Example Apache Kafka + Apache Flink
}
\notes{Characteristics of a streaming system include a move from *pull* updates to *push* updates, i.e. the computation is driven by a change in the input data rather than the service calling for input data when it decides to run a computation. Streaming systems operate on 'rows' of the data rather than 'columns'. This is because the full column isn't normally available as it changes over time. As an important design principle, the services themselves are stateless, they take their state from the streaming ecosystem. This ensures the inputs and outputs of given computations are easy to declare. As a result, persistence of the data is also handled by the streaming ecosystem and decisions around data retention or recomputation can be taken at the systems level rather than the component level.}


\newslide{Streaming Architectures}
\slides{
* AWS Kinesis, Apache Kafka
* Not just about streaming
    * Nodes in the architecture are *stateless* 
	* They persist through storing state on *streams*
* This brings the data *inside out*
}

\recommendation{We should consider a major re-architecting of systems around our services. In particular we should scope the use of a *streaming architecture* (such as Apache Kafka) that ensures data persistence and enables asynchronous operation of our systems.[^data-orientated-architecture] This would enable the provision of QC streams, and real time dash boards as well as hypervisors.

[^data-orientated-architecture]: These approaches are one area of focus for my own team's research. A data first architecture is a prerequisite for efficient deployment of machine learning systems.

Importantly a streaming architecture implies the services we build are
*stateless*, internal state is deployed on streams alongside external
state. This allows for rapid assessment of other services' data.
}


\include{_data-science/includes/data-oriented-programming.md}

\subsection{Trading System}

\slides{* High frequency share trading.
* Stream of prices with millisecond updates.
* Trades required on millisecond time line
}
\notes{As a simple example we'll consider a high frequency trading system. Anne wishes to build a share trading system. She has access to a high frequency trading system which provides prices and allows trades at millisecond intervals. She wishes to build an automated trading system.

Let's assume that price trading data is available as a data stream. But the price now is not the only information that Anne needs, she needs an estimate of the price in the future.}

\setupcode{import pandas as pd
import numpy as np
import os}

\code{# Generate an artificial trading stream
days=pd.date_range(start='21/5/2017', end='21/05/2020')
z = np.random.randn(len(days), 1)
x = z.cumsum()+400}

\code{prices = pd.Series(x, index=days)
hypothetical = prices.loc['21/5/2019':]
real = prices.copy()
real['21/5/2019':] = np.NaN}

\setupplotcode{import mlai
import teaching_plots as plot
import matplotlib.pyplot as plt}

\plotcode{diagrams = '\diagramsDir/data-science/'
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


\newslide{Real Price}

\slides{\includediagram{\diagramsDir/data-science/real-prices}{80%}}

\newslide{Future Price}

\slides{\includediagram{\diagramsDir/data-science/hypothetical-prices}{80%}}


\notes{\figure{\includediagram{\diagramsDir/data-science/hypothetical-prices}{80%}}{Anne has access to the share prices in the black stream but not in the blue stream. A hypothetical stream is the stream of future prices. Anne can define this hypothetical under constraints (latency, input etc). The need for a model is now exposed in the software infrastructure}{hypothetical-prices}}

\subsection{Hypothetical Streams}

\slides{
* Real stream --- share prices
    * derived *hypothetical* stream --- share prices in future.
* Hypothetical constrained by
    * input constraints.
    * decision functional
    * computational requirements (latency)
}


\notes{We'll call the future price a hypothetical stream. 

A hypothetical stream is a desired stream of information which cannot be directly accessed. The lack of direct access may be because the events happen in the future, or there may be some latency between the event and the availability of the data. 

Any hypothetical stream will only be provided as a prediction, ideally with an error bar. 

The nature of the hypothetical Anne needs is dependent on her decision-making process. In Anne's case it will depend over what period she is expecting her returns. In MDOP Anne specifies a hypothetical that is derived from the pricing stream. 

It is not the price stream directly, but Anne looks for *future* predictions from the price stream, perhaps for price in $T$ days' time.

At this stage, this stream is merely typed as a hypothetical.

There are constraints on the hypothetical, they include: the *input* information, the upper limit of latency between input and prediction, and the decision Anne needs to make (how far ahead, what her upside, downside risks are). These three constraints mean that we can only recover an approximation to the hypothetical.}

\subsection{Hypothetical Advantage}

\slides{* Modelling is now required.
* But modelling is declared in the ecosystem.
* If it's manual, warnings can be used 
     * calibration, fairness, dataset shift
* Opens door to Auto AI.
}

\notes{What is the advantage to defining things in this way? By defining, clearly, the two streams as real and hypothetical variants of each other, we now enable automation of the deployment and any redeployment process. The hypothetical can be *instantiated* against the real, and design criteria can be constantly evaluated triggering retraining when necessary.}

\include{_ai/includes/safe-boda.md}

\include{_ai/includes/ride-allocation-prediction.md}


\notes{Let's consider a ride sharing app, for example the SafeBoda system. 

Anne is on her way home now; she wishes to hail a car using a ride sharing app. 

The app is designed in the following way. On opening her app Anne is notified about drivers in the nearby neighborhood. She is given an estimate of the time a ride may take to come.

Given this information about driver availability, Anne may feel encouraged to enter a destination. Given this destination, a price estimate can be given. This price is conditioned on other riders that may wish to go in the same direction, but the price estimate needs to be made before the user agrees to the ride. 

Business customer service constraints dictate that this price may not change after Anne's order is confirmed. 

In this simple system, several decisions are being made, each of them on the basis of a hypothetical.

When Anne calls for a ride, she is provided with an estimate based on the expected time a ride can be with her. But this estimate is made without knowing where Anne wants to go. There are constraints on drivers imposed by regional boundaries, reaching the end of their shift, or their current passengers mean that this estimate can only be a best guess.

This best guess may well be driven by previous data.
}

\include{_data-science/includes/ride-sharing-soa-doa.md}
\include{_data-science/includes/information-dynamics.md}



\endif
