\ifndef{databasesAndJoins}
\define{databasesAndJoins}

\editme

\notes{
\subsection{Databases and Joins}

The main idea we will be working with today is called the 'join'.  A join does exactly what it sounds like, it combines two database tables.

You may have already started to look at data structures and learning about `pandas` which is a great way of storing and structuring your data set to make it easier to plot and manipulate your data.

Pandas is great for the data scientist to analyze data because it makes many operations easier. But it is not so good for building the machine learning system. In a machine learning system, you may have to handle a lot of data. Even if you start with building a system where you only have a few customers, perhaps you build an online taxi system (like SafeBoda) for Kampala. Maybe you will have 50 customers. Then maybe your system can be handled with some python scripts and `pandas`.

\subsection{Scaling ML Systems}

But what if you are successful? What if everyone in Kampala wants to use your system? There are 1.5 million people in Kampala and maybe 100,000 Boda Boda drivers.

What if you are even more succesful? What if everyone in Lagos wants to use your system? There are around 20 million people in Lagos ... and maybe as many Okada drivers as people in Kampala!

We want to build safe and reliable machine learning systems. Building them from `pandas` and python is about as safe and reliable as [taking six children to school on a boda boda](https://www.monitor.co.ug/News/National/Boda-accidents-kill-10-city-UN-report-Kampala/688334-4324032-15oru2dz/index.html).

To build a reliable system, we need to turn to *databases*. In this notebook [we'll be focusing on SQL databases](https://en.wikipedia.org/wiki/Join_(SQL)) and how you bring together different streams of data in a Machine Learning System.

In a machine learning system, you will need to bring different data sets together. In database terminology this is known as a 'join'. You have two different data sets, and you want to join them together. Just like you can join two pieces of metal using a welder, or two pieces of wood with screws.

But instead of using a welder or screws to join data, we join it using columns of the data. We can join data together using people's names. One database may contain where people live, another database may contain where they go to school. If we join these two databases, we can have a database which shows where people live and where they got to school.

In the notebook, we will join some data about where the health centers are in Nigeria with data about where there have been cases of Covid19. There are other challenges in the ML System Design that are not going to be covered here. They include how to update the databases and how to control access to the databases from different users (boda boda drivers, riders, administrators etc). }

\endif
