\ifndef{apacheFlink}
\define{apacheFlink}

\editme

\subsection{Apache Flink}

* Streams and transformations
* a stream is a (potentially never-ending) flow of data records
* a transformation is an operation that takes one or more streams as input, and produces one or more output streams as a result.

\newslide{Join}

```
stream.join(otherStream)
    .where(<KeySelector>)
    .equalTo(<KeySelector>)
    .window(<WindowAssigner>)
    .apply(<JoinFunction>)
```

\notes{Apache Flink allows operations on streams. For example the join operation above. In a traditional data base management system, this join operation may be written in SQL and called on demand. In a streaming ecosystem, computations occur as and when the streams update. 

The join is handled by the ecosystem surrounding the business logic.}

\endif
