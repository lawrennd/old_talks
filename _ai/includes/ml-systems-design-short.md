\ifndef{mlSystemsDesignShort}
\define{mlSystemsDesignShort}
\editme

\subsection{Machine Learning Systems Design}
	
\notes{The challenges of integrating different machine learning components into a whole that acts effectively as a system seem unresolved. In software engineering, separating parts of a system in this way is known as [component-based software engineering](). The core idea is that the different parts of the system can be independently designed according to a sub-specfication. This is sometimes known as *separation of concerns*. However, once the components are machine learning based, tighter coupling becomes a side effect of the learned nature of the system. For example if a driverless car's detection of cyclist is dependent on its detection of the road surface, a change in the road surface detection algorithm will have downstream effects on the cyclist detection. Even if the road detection system has been improved by objective measures, the cyclist detection system may have become sensitive to the foibles of the previous version of road detection and will need to be retrained. 

Most of our experience with deployment relies on some approximation to the component based model, this is also important for verification of the system. If the components of the system can be verified then the composed system can also, potentially, be verified.}

\newslide{Fragility of AI Systems}

\slides{
* They are componentwise built from ML Capabilities.
* Each capability is independently constructed and verified.
   * Pedestrian detection
   * Road line detection
* Important for verification purposes.
}

\endif
