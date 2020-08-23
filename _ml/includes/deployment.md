\ifndef{deployment}
\define{deployment}

\editme

\subsection{Deployment}
\slides{
* Introduced almost in order of difficulty of deployment.
* Supervised learning requires more data annotation, but more straightforward to deploy.
* Therefore major focus with supervised learning should always be on maintaining data quality.}
\notes{The methods we have introduced are roughly speaking introduced in order of difficulty of deployment. While supervised learning is more involved in terms of collection of data, it is the most straightforward method to deploy once that data is recovered. For this reason, a major focus with supervised learning should always be on maintaining data quality, increasing the efficiency and accountability[^datareadiness] of the data collection pipeline and the quality of features used.

[^datareadiness]: To try and better embody the state of data readiness in organizations I've been proposing "Data Readiness Levels". More needs to be done in this area to improve the efficiency of the data science pipeline.} 

You can also check my \addblog{Data Readiness Levels}{2017/01/12/data-readiness-levels} and my \addblog{The 3Ds of Machine Learning Systems Design}{2018/11/05/the-3ds-of-machine-learning-systems-design}.

\subsection{Where to Deploy?}
\notes{In relation to what AI can and can't do today Andrew Ng is quoted as saying:}

> If a typical person can do a mental task with less than one second of thought, we can probably automate it using AI either now or in the near future.[^ngquote]
> Andrew Ng

[^ngquote]: The quote can be found in the Harvard Business Review Article ["What Artificial Intelligence Can and Can't Do Right Now"](https://hbr.org/2016/11/what-artificial-intelligence-can-and-cant-do-right-now).

\subsection{Is this Right?}
\slides{* Broadly agree with this quote but only in the context of supervised learning.
* The picture with regard to unsupervised learning and reinforcement learning is more clouded.}
\notes{I would broadly agree with this quote but only in the context of supervised learning. If a human expert takes around that amount of time, then it's also likely we can acquire the data necessary to build a supervised learning algorithm that can emulate that human's response.

The picture with regard to unsupervised learning and reinforcement learning is more clouded. 

One observation is that for *supervised* learning we seem to be moving beyond the era where very deep machine learning expertise is required to deploy methods. A solid understanding of machine learning (say to Masters level) is certainly required, but the quality of the final result is likely more dependent on domain expertise and the quality of the data and the information processing pipeline. This seems part of a wider trend where some of the big successes in machine learning are moving rapidly from the domain of science to that of engineering.[^dontpanic]

[^dontpanic]: This trend was very clear at the moment, [I spoke about it]({{site.baseurl }}/) at a recent Dagstuhl workshop on new directions for kernel methods and Gaussian processes.} 

You can check my \addblog{New Directions in Kernels and Gaussian Processes}{2016/11/29/new-directions-in-kernels-and-gaussian-processes}.

\notes{So if we can only emulate tasks that humans take around a second to do, how are we managing to deliver on self driving cars? The answer is that we are constructing engineered systems from sub-components, each of which is a machine learning subsystem. But they are tied together as a component based system in line with our traditional engineering approach. This has an advantage that each component in the system can be verified before its inclusion. This is important for debugging and safety. But in practice we can expect these systems to be very brittle. A human adapts the way in which they drive the car across their lifetime. A human can react to other road users. In extreme situations, such as a car jacking, a human can set to one side normal patterns of behavior, and purposely crash their car to draw attention to the situation.}


\newslide{Getting Easier}
\slides{
* We seem to be moving beyond the era where very deep machine learning expertise is required to deploy methods.
* Just require a  solid understanding of machine learning (say to Masters level)
}

\newslide{Streaming Data}
\slides{
* Supervised machine learning solutions are normally trained offline.
* They do not adapt when deployed because this makes them less verifiable.
* This compounds the brittleness of our solutions.}
\notes{Supervised machine learning solutions are normally trained offline. They do not adapt when deployed because this makes them less verifiable. But this compounds the brittleness of our solutions. By deploying our solutions we actually change the environment in which they operate. Therefore, it's important that they can be quickly updated to reflect changing circumstances. This updating happens offline. For a complex mechanical system, such as a delivery drone, extensive testing of the system may be required when any component is updated. It is therefore imperative that these data processing pipelines are well documented so that they can be redeployed on demand. 

In practice there can be challenges with the false dichotomy between reproducibility and performance. It is likely that most of our data scientists are caring less about their ability to redeploy their pipelines and only about their ability to produce an algorithm that achieves a particular performance. A key question is how reproducible is that process? There is a *false* dichotomy because ensuring reproducibility will typically improve performance as it will make it easier to run a rigorous set of explorative experiments. A worry is that, currently, we do not have a way to quantify the scale of this potential problem within companies.}


\subsection{Model Choice}
\slides{
* For  all machine learning methods is the initial choice of useful classes of functions.
* The deep learning revolution is associated with a particular class of mathematical functions.}
\notes{Common to all machine learning methods is the initial choice of useful classes of functions. The deep learning revolution is associated with a particular class of mathematical functions that is proving very successful in what were seen to be challenging domains: speech, vision, language. This has meant that significant advances in problems that have been seen as hard have occurred in artificial intelligence.}


\endif


<!-- Machine learning solutions When we deploy our solutions in the real world, we find that the situation is more complex. ThereAnother potential problem with our rush to supervised learning solutions is the false dichotomy between reproducibility and performance. Across Amazon we are using data science to design solutions which are deployed into production.  -->


<!-- It also requires more expertise on the machine learning side to develop and deploy solutions in un, and requires more expertise.  -->

<!-- such as avoiding a crash, to deliberately ram into another vehicle -->
<!-- To deliver complex solutions, like self driving cars, many sub-components from a  -->

<!-- Domain expertise becomWith regard to deIn particular, we are moving beyond the era where there is a short -->


