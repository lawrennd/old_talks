\ifndef{apacheFlink}
\define{apacheFlink}

\editme

\subsection{Apache Flink}
\slides{
* Streams and transformations
* a stream is a (potentially never-ending) flow of data records
* a transformation: streams as input, produces transformed streams as output}

\notes{[Apache Flink](https://en.wikipedia.org/wiki/Apache_Flink) is a stream processing framework. Flink is a foundation for event driven processing. This gives a high throughput and low latency framework that operates on dataflows.}

\notes{Data storage is handled by other systems such as Apache Kafka or AWS Kinesis.}

\newslide{Join}

```
stream.join(otherStream)
    .where(<KeySelector>)
    .equalTo(<KeySelector>)
    .window(<WindowAssigner>)
    .apply(<JoinFunction>)
```

\notes{Apache Flink allows operations on streams. For example, the join operation above. In a traditional data base management system, this join operation may be written in SQL and called on demand. In a streaming ecosystem, computations occur as and when the streams update.}

\notes{The join is handled by the ecosystem surrounding the business logic.}

\endif
