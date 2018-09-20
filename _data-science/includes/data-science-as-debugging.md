\section{Data Science as Debugging}

\newslide{Data Science as Debugging}
\slides{
* Analogies: For Software Engineers [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).
}

\notes{One challenge for existing information technology professionals is realizing the extent to which a software ecosystem based on data differs from a classical ecosystem. In particular, by ingesting data we bring unknowns/uncontrollables into our decision making system. This presents opportunity for adversarial exploitation and unforeseen operation.

Starting with the analysis of a data set, the nature of data science is somewhat difference from classical software engineering. I sometimes use the following analogy to help software engineers understand. Imagine you are given a USB stick, and on that USB stick you know, for some reason, that there is some software that would make a significant improvement to your production system. However, you don't know which of the many library functions on the USB stick are the ones that will help. And it could be that some of those library functions will hinder, perhaps because they are just inappropriate or perhaps because they have been placed there malisciously. How would you integrate this software into your production system? The answer is *very carefully*. An enormous amount of debugging would be required. As the nature of the code base is understood, software tests to verify it also need to be constructed. At the end of all your work, the lines of software you write to actually interact with the software on the USB stick are likely to be minimal. But more thought would be put into those lines than perhaps any other lines of code in the system. 

This analogy is very close to what is required when integrating machine learning systems into a software ecosystem, because the injection of data through the machine learning model is equivalent to that discarded USB stick. A further challenge is that in production, if any adaptation to live data is proposed, then this process is ongoing. The nature of the software changes as the data changes. 

It might see that this process is easy to formalize now, we simply need to check what the formal software engineering process is for debugging, because that is the current software engineering activity that data science is closest to. But when we look for a formalization of debugging we find that there is none. Indeed, modern software engineering mainly focusses on ensuring that code is written without bugs in the first place.}
