### Breadth vs Depth Paradox

\slides{* Able to quantify to a greater and greater degree the actions of individuals

* But less able to characterize society

* As we measure more, we understand less}

\notes{As we increase the amount of data we acquire, we seem to be able to get better at characterizing the actions of individuals, predicting how they will behave. But we seem, somehow, to be becoming less capable at understanding society. Somehow it seems that as we measure more, we understand less.}

\slides{### What?

* Perhaps greater preponderance of data is making society itself more complex

* Therefore traditional approaches to measurement are failing

* Curate's egg of a society: it is only 'measured in parts'}

\notes{That seems counter-intuitive. But perhaps the preponderance of data is making society itself, or the way we measure society, somehow more complex. And in turn, this means that traditional approaches to measurement are failing. So when we realize we are getting better at characterising individuals, perhaps we are only measuring society in parts.}

\slides{### Breadth vs Depth

* Modern Measurement deals with *depth* (many subjects)
    ... or *breadth* lots of detail about subject.
	
* Can deal with large *\dataDim* or large *\numData*
* But what about 
    * *\dataDim* roughly equal to *\numData*?
    * Stratification of populations: batch effects etc.}

\notes{Classical approaches to data analysis made use of many subjects to achieve statistical power. Traditionally, we measure a few things about many people. For example cardiac disease risks can be based on a limited number of factors inmany patients (such as whether the patient smokes, blood pressure, cholesterol levels etc). Because, traditionally, data matrices are stored with individuals in rows and features in columns[^depth-measurement], we refer to this as *depth* of measurement. In statistics this is sometimes known as the *large $p$, small $n$* domain because traditionally $p$ is used to denote the number of features we know about an individual and $n$ is used to denote the number of individuals. 

The data-revolution is giving us access to far more detail about each individual, this is leading to a *breadth* of coverage. This characteristic first came to prominence in computational biology and genomics where we became able to record information about mutations and transcription in millions of genes. So $p$ became very large, but due to expense of measurement, the number of patients recorded, $n$, was relatively small. But we now see this increasingly for other domains. With an increasing number of sensors on our wrists or in our mobile phones, we are characterizing indivdiuals in unprecedented detail. This domain can also be effectively dealt with by modifying the models that are used for the data. 

[^depth-measurement]: In statistics this is known as a *design matrix*, representing the design of a study. But in databases, one might think of each patient being in a row, or record of the database.}

\slides{### Wood or Tree

* Can either see a wood or a tree.}

\includeimg{../slides/diagrams/Grib_skov.jpg}{50%}
<!-- https://upload.wikimedia.org/wikipedia/commons/5/5b/Grib_skov.jpg-->

\notes{So we can know an individual extremely well, or we can know a population well. The saying "Can't see the wood for the trees", means we are distracted by the individual trees in a forest, and can't see the wider context. This seems appropriate for what may be going on here. We are becoming distracted by the information on the individual and we can't see the wider context of the data. 

We know that a rigorous, randomized, study would characterize that forest well, but it seems we are unwilling to invest the money required to do that and the proxies we are using are no longer effective, perhaps because of shifting patterns of behaviour driven by the rapidly evolving digital world. 

Further, it's likely that we are interested in *strata* within our data set. Equivalent to the structure within the forest: a clearing, a transition between types of tree, a shift in the nature of the undergrowth.}

### Examples

\slides{* Election polls (UK 2015 elections, EU referendum, US 2016 elections)

* Clinical trials vs personalized medicine: Obtaining statistical power where interventions are subtle. e.g. social media}

\notes{Examples exhibiting this phenomenon include recent elections, which have proven difficult to predict. Including, the UK 2015 elections, the EU referendum, the US 2016 elections and the UK 2017 elections. In each case individuals may have taken actions on the back of polls that showed one thing or another but turned out to be inaccurate. Indeed, the only accurate pre-election poll for the UK 2017 election, [the YouGov poll](https://yougov.co.uk/news/2017/05/31/how-yougov-model-2017-general-election-works/), was not a traditional poll, it contains a new type of statistical model called [Multilevel Regression and Poststratification (MRP)](http://andrewgelman.com/2013/10/09/mister-p-whats-its-secret-sauce/).

Another example is stratified medicine. If a therapy is effective only in a sub-type of a disease, then statistical power can be lost across the whole population, particularly when that sub-type is a minority. But characterization of that sub-type is difficult. For example, new cancer immunotherapy treatments can have a dramatic effect, leading to almost total elimination of the cancer in some patients, but characterizing this sub-population is hard. This also makes it hard to develop clinical trials that prove the efficacy of the drugs.

A final example is our measurement of our economy, which increasingly may not capture where value is being generated. This is characterized by the changing nature of work, and the way individuals contribute towards society. For example, the open source community has driven the backbone of the majority of operating system software we use today, as well as cloud compute. But this value is difficult to measure as it was contributed by volunteers, not by a traditional corporate structure. Data itself may be driving this change, because the value of data accumulates in a similar way to the value of capital. The movement of data in the economy, and the value it generates is also hard to measure, and it seems there may be a large class of "have nots", in terms of those industries whose productivity has suffered relative to the top performers. The so-called productivity gap may not just be due to skills and infrastructure, but also due to data-skills and data-infrastructure.}

### Challenges

\notes{The nature of the digital society has a closed loop feedback on itself. This is characterized by social media memes, which focus attention on particular issues very quickly. A good example being the photograph of Aylan Kurdi, the young Syrian boy found drowned on a Turkish beach. This photograph had a dramatic effect on attitudes towards immigration, more than the statistics that were showing that thousands were dieing in the Mediterranean each month (see [this report by the University of Sheffield's Social Media Lab](https://www.dropbox.com/s/hnydewwtido6nhv/VISSOCMEDLAB_AYLAN%20KURDI%20REPORT.pdf?dl=0)). Similarly, the changed dynamics of our social circles. Filter bubbles, where our searches and/or newsfeed has been personalized to things that algorithms already know we like. Echo chambers, where we interact mainly with people we agree with and our opinions aren't challenged. Each of these is changing the dynamic of society, and yet there is a strong temptation to use digital media for surveying information.}

\slides{* Social media memes

* Filter bubbles and echo chambers}


### Solutions

\notes{The solutions to these challenges come in three flavours. Firstly, there is a need for more data. In particular data that is actively acquired to cover the gaps in our knowledge. We also need more use of classical statistical techniques, and a wider understanding of what they involve. This situation reminds me somewhat of the idea of the 'paperless office'. The innovative research at Xerox PARC that brought us the Graphical User Interface, so prevalent today, was driven by the realization, in the 1970s that eventually offices would stop using paper. Xerox focussed research on what that office would look like as it was a perceived threat to their business. The paperless office may still come, but in practice computers brought about a significant increase in the need for paper due to the additional amounts of information that they caused to be summarized or generated. In a similar way, the world of *big data* is driving a need for more experimental design and more classical statistics. Any perception of the automated computer algorithm that drives all before it is at least as far away as the paperless office was in the 1970s. 

We also need a better social, cognitive and biological understanding of humans and how we and our social structures respond to these interventions. Over time some of the measurables will likely stabilize, but it is not yet clear which ones.}

\slides{* More classical statistics!
    * Like the 'paperless office'

* A better characterization of human needs and flaws

* Larger studies (100,000 genome)}
