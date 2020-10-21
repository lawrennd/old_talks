---
title: "Data Sharing and Data Trusts"
abstract: >
  Computational biologists know better than perhaps any other domain the importance of data sharing in progress in understanding complex decisions. Underlying the revolution in "artificial intelligence" is really a revolution in data. But when data is persona or has legal protections placed upon there are challenges to data sharing. In this talk we introduce the ideas behind data sharing and the model of data trusts, an approach to data sharing that relies on trust law to form its governance structure.
reveal: True
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-10-20
venue: Wellcome Human Cell Atlas Meeting
transition: None
---

\include{../talk-macros.tex}

\notes{Data is not property, at least not in the modern sense of the word. But if we look back over time, we see different notions of property. In particular, associated with different resources. For example, common land is a particular type of property, which may or may not be explicitly owned, but members of a community have a particular set of rights to.

In Sheffield, where I used to live, work, run and cycle. The moorland was historically common land until the enclosures acts applied in the 1860s. Until that time, local people had the right to, for example, collect sand from the moorland for use in building their houses. After enclosure, the crime of 'sand poaching' evolved. On Houndkirk Moor, south West of Sheffield, after enclosure [sand poachers went to collect sand at night](https://slidelegend.com/from-cairns-to-craters-conservation-heritage-moors-for-the-future_59e1b4f91723dd4240b3158c.html) for houses being build in the village of Dore.}

\newslide{}

\figure{\includejpg{\diagramsDir/supply-chain/2355371_64d04518}{80%}}{Milestone on Houndkirk Road on Houndkirk Moor. Sand poaching took place near here after the Moor was enclosed, also restricting access to this ancient route.}{milestone-houndkirk-moor}

\notes{Computational Biologists at the forefront of data sharing, particularly public data sharing. Transcriptomic, genomic, epigenomic data is publicly available and have allowed people, like me, not even working directly with biologists to develop algorithms for interpreting and analyzing that data.}

\notes{But as we transition from biological data to health data, that data starts to pertain to individuals. It falls under the domain of personal data.}

\notes{These rights to a resource become particularly interesting when considering rivers. Sheffield itself emerged as the home of cutlers, knife makers. Their small mills were driven by water-power flowing from Houndkirk Moor to the center of town. There the lakes they built are called dams, today they line the streams of the city's parkland, but 200 years ago they were a bustling industry of forges, grinders and polishers.

Important, regardless of who owned the river, different mills on the river had different rights to the water. If an upstream mill damns the entire flow, the downstream mill has to stop working in times of drought.

The rivers of Sheffield are streams, but as they flow down into the Don and eventually the Humber new rights to this water emerge. As well as power from the river, there is its use as a source of drinking water, for navigation and for irrigation.}

\newslide{}

\figure{\includejpg{\diagramsDir/supply-chain/1280px-Shepherd_Wheel_millpond_April_2017_01}{80%}}{Shepherd Wheel in Whitely Wood. In Sheffield the millpond itself is called a damn. This Wheel is [now a working museum](http://www.simt.co.uk/shepherd-wheel-workshop) on Porter Brook, but it dates originally to the 1500s. It now sits in Bingham Park, but historically the river would have had several Wheels operating from the Porter Brook.}{shepherd-wheel}

\newslide{}

\figure{\includejpg{\diagramsDir/supply-chain/1280px-Shepherd's_Wheel_Workshop_1}{80%}}{Interior of Shepherd Wheel showing spinning wheel in background, and stationary wheel in foreground with the wooden saddle of the grinder's 'horse'.}{shepherd-wheel-interior}

\notes{Many of these rights are in tension. Mills working on the river may pollute the stream. If the water is damned or  used for irrigation, then it can be too low for navigation. There is complex interplay of demands on the river that creates tensions between different users.

The general data protection regulation is poorly named. It doesn't protect data, what it does instead is give us some limited rights around access to and control of processing of our personal data. 

Personal data has some of the characteristics of a river. My choice to share my data has effects on other individuals. If I share my genome, I am sharing information about my children's genome. If I share my address book (e.g. with Facebook or Linkedin) I'm sharing information about what people know me. If I share a photo of myself with friends, I'm sharing the location of friends. 

What the GDPR does is give us limited personal data rights. It outlines a limited right of deletion. It also allows us access to our personal data, which in turn confers a portability right.

A pure notion of ownership, in that I own a ball, or I own a car, is that I have the absolute right to share and restrict access to my property as I choose. Personal data rights are not absolute, but nevertheless they return some control to the individual.

There's been much recent talk about GDPR, Sarion mentioned that it began to be introduced in 2012, but in reality, its origins are much older. [It dates back to 1981](https://en.wikipedia.org/wiki/Convention_for_the_protection_of_individuals_with_regard_to_automatic_processing_of_personal_data), and [28th January is "Data Potection day"](https://en.wikipedia.org/wiki/Data_Privacy_Day). The essence of the law didn't change much in the previous iterations. The critical chance was the size of the fines that the EU stipulated may be imposed for infringements. Paul Nemitz, who was closely involved with the drafting, told me that they were initially inspired by competition law, which levies fines of 10% of international revenue. The final implementation is restricted to 5%, but it's worth pointing out that Facebook's fine (imposed in the US by the FTC) was $5 billion dollars. Or approximately 7% of their international revenue at the time. 

So the big change is the seriousness with which regulators are taking breaches of the intent of GDPR. And indeed, this newfound will on behalf of the EU led to an amount of panic around companies who rushed to see if they were complying with this strengthened legislation.

But is it really the big bad regulator coming down hard on the poor scientist or company, just trying to do an honest day's work? I would argue not. The stipulations of the GDPR include fairly simple things like the 'right to an explanation' for consequential decision-making. Or the right to deletion, to remove personal private data from a corporate data ecosystem.


\addguardian{Digital Oligarchies}{2015/mar/05/digital-oligarchy-algorithms-personal-data}


While these are new stipulations, if you reverse the argument and ask a company "would it not be a good thing if you could explain why your automated decision making system is making decision X about customer Y" seems perfectly reasonable. Or "Would it not be a good thing if we knew that we were capable of deleting customer Z's data from our systems, rather than being concerned that it may be lying unregistered in an S3 bucket somewhere?". 

Phrased in this way, you can see that GDPR perhaps would better stand for "Good Data Practice Rules", and should really be being adopted by the scientist, the company or whoever in an effort to respect the rights of the people they aim to serve.

So how do Data Trusts fit into this landscape? Well it's appropriate that we've mentioned the commons, because a current challenge is how we manage data rights within our community. And the situation is rather akin to that which one might have found in a feudal village (in the days before Houndkirk Moor was enclosed).}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/information-barons-threaten-our-autonomy}{80%}}{This article published in 2015 in the Guardian outlines the challenges behind our feudal data infrastructure.}{information-barons}


\addguardian{Information Feudalism}{https://www.theguardian.com/media-network/2015/nov/16/information-barons-threaten-autonomy-privacy-online}

\notes{Data rights legislation has some unfortunate terminology, including the notion of the 'data subject' and the 'data controller'. The term 'subject' is unfortunate, but perhaps appropriate. Because while the legislation gives you rights around *consequential* processing of your data. There is a power-asymmetry between yourself and the data controller. The data controller is akin to a feudal lord, who owes a duty of care to his or her vassals. The unfortunate challenge is that by the time it has become apparent that the feudal lord has failed in this duty of care, it is too late for the data-subjects. In the medieval village, the duty was for protection, but when the Lord underinvests, the Vikings, or Saracens arrive, and the village is pillaged, it's a little bit too late. 

Similarly, in our feudal data ecosystem, the fines around consequential decision-making come too late for the damage to have been done. And the short-termism of our data-lords means that they do not provide the protections we should demand for such personally sensitive data.

Further, the GDPR only provides protection for 'consequential' decision making. If decision-making is considered inconsequential, such as the posting of an advert or the ranking of a search query or a news feed entry, then its stipulations do not apply. But the modern era is one where a chain of *inconsequential decisions* can combined together to have a consequential effect. Consider, for example, the member of a minority group who is never shown adverts for higher paying jobs by an algorithm that is expressing some form of bias.

So how do we respond? One answer lies in collectivisation of our rights.}


\newslide{}

\figure{\includeyoutube{-8bqQ-C1PSE}}{Monty Python mocks the feudal system in Monty Python and the Holy Grail. "I'm your King! Well I didn't vote for you!". "Strange women lying in ponds distributing swords is no basis for a system of government"}{monty-python-feudal}

\notes{The feudal system was initially augmented and finally replaced by a system of direct representation through voting. Modern democracies. In the data ecosystem, the equivalent would be a data-controller who had better alignment with the interests of their data-subjects. 

So how do we regulate for such an eventuality? I'm fond of a quote from Rodney Brooks that says: "You can't regulate what doesn't exist". Indeed, it seems we have enough problems with regulating technologies and ideas that already exist today. But again, we can be inspired by the way that regulation has evolved in the past to take into account evolving technology. In particular, in intellectual property, patents emerged from the notion of 'letters patent', which were monopolies granted by the monarch for a guild to work in a certain domain, such as weaving. They have evolved to be a mechanism for intellectual property rights.

Similarly, when motorised vehicles were introduced, after some false starts (including the poorly formed Red Flag Act) a Highway Code emerged that lays out the different responsibilities of road users in sharing the highway.}

\newslide{}

\figure{\includejpg{\diagramsDir/health/page1-368px-The_Highway_Code_1931_djvu}{40%}}{Evolving previous legislation is one route to develop new legislation in the presence of new technologies.}{the-highway-code}

\addguardian{Let's learn the rules of the digital road before talking about a web Magna Carta}{2015/apr/02/rules-digital-technology-internet-bill-rights}

\notes{What mechanism should we look to for forming these 'data collectives'. There are many inspirations from history including credit unions, building societies, co-operatives and land societies. Many of these have the bottom-up flavour of a collective that feels appropriate for managing data rights. 

One particularly interesting mechanism also dates back to Medieval law. The Courts of Equity is a separate system of law that runs alongside Common Law. One of the domains of law it recognises are Trusts.

Trusts are institutions where there is an enhanced duty of care, known as "fiducirary duty" or "undivided loyalty" over the trustees to implement the constituent terms of the trust. 

Broadly speaking a Trust has three components. There are the settlors. This group is the group that starts with assets. These might be rights to the property, or in the data trust, the rights to data. Then there are the beneficiaries. This is the group that will benefit from the operation of the trust. Finally there are the Trustees. This group oversees the management of the trust and ensures that the settlors intent is being conformed to in the management of the assets.

In a Data Trust [@Delacroix:trusts19] the settlors and the beneficiaries will be the same, or significantly overlapping groups. Unusually, because the value of data only comes when it accumulates, it is only once the data is within the Trust that it becomes useful. In the data trust, the Trustee takes on the role of data-controller. But they are now obliged to conform to the constitutional terms of the trust that is formed.

The data trust is not a specfic solution for data sharing. It is a set of legal mechanisms that can be used to create solutions. The consitutional terms of the trust will depend on what data is being shared and for what purpose. One can imagine data trusts that are associated with special interests, like a group of patients with a particular cancer. Or data trusts that might be associated with a region (the Hackney Data Trust) for assisting with local issues like transport links etc. Or one could imagine general data trusts, that would interact with individual specialized data trusts.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/data-trusts}{80%}}{This article published in 2016 in the Guardian outlines the ideas behind data trusts.}{data-trusts-guardian}

\addguardian{Data Trusts}{2016/jun/03/data-trusts-privacy-fears-feudalism-democracy}

\notes{Importantly, any data governance approach is going to have tensions. In particular, there is a need to represent the interests of the *individual*, the interests of *society* and those of *vulnerable people* (such as children). Any data constitutional terms should also consider issues such as *enfranchisement* of the data subjects. There is a [value based choice for how particular data should be shared](https://datatrusts.uk/blogs/selectingdatastructures).

But in order to enact such choices, and ensure that the correct responsibilities are applied to the data controllers, Trust law seems a promising avenue to pursue in institutionalising data sharing.}

\thanks

\references
