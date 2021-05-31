\ifndef{hypotheticalTradingSystem}
\define{hypotheticalTradingSystem}

\editme

\subsection{Trading System}

\slides{* High frequency share trading.
* Stream of prices with millisecond updates.
* Trades required on millisecond time line
}
\notes{As a simple example we'll consider a high frequency trading system. Anne wishes to build a share trading system. She has access to a high frequency trading system which provides prices and allows trades at millisecond intervals. She wishes to build an automated trading system.

Let's assume that price trading data is available as a data stream. But the price now is not the only information that Anne needs, she needs an estimate of the price in the future.}

\setupplotcode{import pandas as pd
import numpy as np
import os}

\plotcode{# Generate an artificial trading stream
days=pd.date_range(start='21/5/2017', end='21/05/2020')
z = np.random.randn(len(days), 1)
x = z.cumsum()+400}

\plotcode{prices = pd.Series(x, index=days)
hypothetical = prices.loc['21/5/2019':]
real = prices.copy()
real['21/5/2019':] = np.NaN}

\setupplotcode{import mlai
import teaching_plots as plot
import matplotlib.pyplot as plt}

\plotcode{fontsize=16}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
real.plot(color='k', fontsize=fontsize)

hypothetical.plot(color='b')
ylim = ax.get_ylim()}
mlai.write_figure('hypothetical-prices.svg', directory='\writeDiagramsDir/data-science/')

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
real.plot(color='k', fontsize=fontsize)
ax.set_ylim(ylim)

mlai.write_figure('real-prices.svg', directory='\writeDiagramsDir/data-science/')}


\newslide{Real Price}

\slides{\figure{\includediagram{\diagramsDir/data-science/real-prices}{80%}}{A set of prices from a a trading stream.}{real-prices}}

\newslide{Future Price}


\figure{\includediagram{\diagramsDir/data-science/hypothetical-prices}{80%}}{Anne has access to the share prices in the black stream but not in the blue stream. A hypothetical stream is the stream of future prices. Anne can define this hypothetical under constraints (latency, input etc). The need for a model is now exposed in the software infrastructure}{hypothetical-prices}

\subsection{Hypothetical Streams}

\slides{
* Real stream --- share prices
    * derived *hypothetical* stream --- share prices in future.
* Hypothetical constrained by
    * input constraints.
    * decision functional
    * computational requirements (latency)
}


\notes{We'll call the future price a hypothetical stream.}

\notes{A hypothetical stream is a desired stream of information which cannot be directly accessed. The lack of direct access may be because the events happen in the future, or there may be some latency between the event and the availability of the data.}

\notes{Any hypothetical stream will only be provided as a prediction, ideally with an error bar.}

\notes{The nature of the hypothetical Anne needs is dependent on her decision-making process. In Anne's case it will depend over what period she is expecting her returns. In MDOP Anne specifies a hypothetical that is derived from the pricing stream. }

\notes{It is not the price stream directly, but Anne looks for *future* predictions from the price stream, perhaps for price in $T$ days' time.}

\notes{At this stage, this stream is merely typed as a hypothetical.}

\notes{There are constraints on the hypothetical, they include: the *input* information, the upper limit of latency between input and prediction, and the decision Anne needs to make (how far ahead, what her upside, downside risks are). These three constraints mean that we can only recover an approximation to the hypothetical.}

\subsection{Hypothetical Advantage}

\slides{* Modelling is now required.
* But modelling is declared in the ecosystem.
* If it's manual, warnings can be used 
     * calibration, fairness, dataset shift
* Opens door to Auto AI.
}

\notes{What is the advantage to defining things in this way? By defining, clearly, the two streams as real and hypothetical variants of each other, we now enable automation of the deployment and any redeployment process. The hypothetical can be *instantiated* against the real, and design criteria can be constantly evaluated triggering retraining when necessary.}

\endif
