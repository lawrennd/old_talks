\ifndef{supplyChainSystem}
\define{supplyChainSystem}

\editme

\subsection{Supply Chain Optimization}

\centerdiv{\llewMasonPicture{15%}\deveshMishraPicture{15%}}

\notes{Supply chain is the process of matching between the supply of the product and demand for the product. This matching process is done through the deployment of resources: places to store the products, ways and means of transporting the product and even the ability to transform products from one form to another (e.g. transforming paper into books through printing).}

\figure{\includeyoutube{ncwsr1Of6Cw}{600}{450}}{Promotional video for the Amazon supply chain optimization team.}{scot-promo-video}

\notes{Arugably the Amazon supply chain is the largest automated decision making system in the world in terms of the amount of money spent and the quantity of product moved through automated decision making.}

\subsection{Supply Chain Optimization}

\centerdiv{\llewMasonPicture{15%}\deveshMishraPicture{15%}}

\notes{At the heart of an automated supply chain is the buying system, which determines the optimal stock level for products and makes purchases based on the difference between that stock level and the current stock level.}

\figure{\includediagram{\diagramsDir/software/buying-schematic}{40%}}{A schematic of a typical buying system for supply chain.}{buying-schematic}


\notes{To make these decisions predictive models (often machine learning or statistical models) have to be moved. For example, the demand for a particular product needs to be pforecast.}

\subsection{Forecasting}

\centerdiv{\jennyFreshwaterPicture{15%}\pingXuPicture{15%}\deanFosterPicture{15%}}

\figure{\includeyoutube{wa8DU-Sui8Q}{600}{450}{1358}{2060}}{Jenny Freshwater speaking at the Amazon re:MARS event in June 2019.}{jenny-freshwater-remars}

\notes{The process of forecasting is described by Jenny Freshwater (at the time Director for Forecasting within Amazon's Supply Chain Optimization team in the video in Figure \ref{jenny-freshwater-remars}.}

\notes{For each product in the Amazon catalogue, the demand is forecast across the a given future period.}

\subsection{Inventory and Buying}

\centerdiv{\deepakBhatiaPicture{15%}\piyushSaraogiPicture{15%}\ramanIyerPicture{15%}\salalHumairPicture{15%}\narayanVenkatasubramanyanPicture{15%}}

\slides{* Automated buying based on:
  * Supplier lead times.
  * Demand Forecast.
  * Cost basis of the product.}
\notes{Forecast information is combined with predictions around lead times from suppliers, understanding of the network's capacity (in terms of how much space is available in which fulfillment centres), the cost of storing and transporting products and the "value" for the consumer in finding the product is in stock. These models are typically operational research models (such as the "newsvendor problem" combined with machine learning and/or statistical forecasts.}

\endif
