\ifndef{dataOrientedArchitecturesIntro}
\define{dataOrientedArchitecturesIntro}

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


\notes{The philosphy of DOA is also possible with more standard data infrastructures, such as SQL data bases, but more work has to be put into place to ensure that book-keeping around data provenance and origin is stored, as well as approaches for snapshotting the data ecosystem.}

\endif
