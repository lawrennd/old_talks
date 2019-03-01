\ifndef{emukitSoftware}
\define{emukitSoftware}
\editme

\include{_ml/includes/xfer-intro.md}

\subsection{Xfer}

<!--\figure{\includepng{../slides/diagrams/uq/xfer-software-page}{80%}}{The Xfer software is a set of software tools for emulation and surrogate modeling. <https://medium.com/apache-mxnet/xfer-an-open-source-library-for-neural-network-transfer-learning-cd5eac4accf0>}{xfer-software-page}-->


\newslide{Transer Learning in 3 Lines}

```repurposer = xfer.LrRepurposer(source_model, feature_layer_names=['fc7'])
repurposer.repurpose(train_iterator)
predictions = repurposer.predict_label(test_iterator)```

<!--\newslide{Xfer}
\slides{
\includepng{../slides/diagrams/uq/xfer-software-page2}{80%}
\center{<https://medium.com/apache-mxnet/xfer-an-open-source-library-for-neural-network-transfer-learning-cd5eac4accf0>}
}-->



\endif
