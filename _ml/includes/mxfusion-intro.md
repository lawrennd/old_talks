\ifndef{mxfusionIntro}
\define{mxfusionIntro}
\editme

\subsection{MXFusion: Modular Probabilistic Programming on MXNet}

\notes{One challenge for practitioners in Gaussian processes, is flexible software that allows the construction of the relevant GP modle. With this in mind, the Amazon Cambridge team has developed MXFusion. It is a modular probabilistic programming language focussed on efficient implementation of hybrid GP-neural network models, but with additional probabilistic programming capabilities.} 

\figure{\includepng{\diagramsDir/ml/mxfusion}{70%}}{MXFusion is a probabilistic programming language targeted specifically at Gaussian process models and combining them with probaiblistic neural network. It is available through the MIT license and we welcome contributions throguh the Github repository <https://github.com/amzn/MXFusion>.}{mxfusion-software}

\notes{We developed the framework for greater ease of transitioning models from 'science' to 'production', our aim was to have code that could be created by scientists, but deployed in our systems through solutions such as AWS SageMaker.}


\slides{\aligncenter{<https://github.com/amzn/MXFusion>}}

\newslide{MxFusion}

\ericMeissner{15%}\zhenwenDai{15%}

\figure{\columns{

* Work by Eric Meissner and Zhenwen Dai.
* Probabilistic programming.
* Available on [Github](https://github.com/amzn/mxfusion)

}{\includepng{\diagramsDir/mxfusion-logo}{80%}}{70%}{30%}}{The MXFusion software.}{mxfusion-software-logo}

\endif
