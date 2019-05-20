\ifndef{apacheFlink}
\define[apacheFlink}

\editme

\subsection{Apache Flink}

```
DataSet<User> input1 = // [...]
DataSet<Store> input2 = // [...]
// result dataset is typed as Tuple2
DataSet<Tuple2<User, Store>>
            result = input1.join(input2)
                           .where("zip")       // key of the first input (users)
                           .equalTo("zip");    // key of the second input (stores)
```

\notes{Apache Flink allows operations on streams. For example the join operation above. In a traditional data base management system, this join operation may be written in SQL and called on demand. In a streaming ecosystem, this join is processed as and when the streams update. 

The join is handled by the ecosystem surrounding the}

\endif
