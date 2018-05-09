### Data Science

* Industrial Revolution 4.0?
* *Industrial Revolution* (1760-1840) term coined by Arnold Toynbee,
late 19th century.
* Maybe: But this one is dominated by *data* not *capital*
* That presents *challenges* and *opportunities* 

compare [digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data) vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)

* Apple vs Nokia: How you handle disruption.

\notes{
Disruptive technologies take time to assimilate, and best practices, as well as the pitfalls of new technologies take time to share. Historically, new technologies led to new professions. [Isambard Kingdom Brunel](https://en.wikipedia.org/wiki/Isambard_Kingdom_Brunel) (born 1806) was a leading innovator in civil, mechanical and naval engineering. Each of these has its own professional institutions founded in 1818, 1847, and 1860 respectively.

[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla) developed the modern approach to electrical distribution, he was born in 1856 and the American Instiute for Electrical Engineers was founded in 1884, the UK equivalent was founded in 1871. 

[William Schockley Jr](https://en.wikipedia.org/wiki/William_Shockley), born 1910, led the group that developed the transistor, referred to as "the man who brought silicon to Silicon Valley", in 1963 the American Institute for Electical Engineers merged with the Institute of Radio Engineers to form the Institute of Electrical and Electronic Engineers. 

[Watts S. Humphrey](https://en.wikipedia.org/wiki/Watts_Humphrey), born 1927, was known as the "father of software quality", in the 1980s he founded a program aimed at understanding and managing the software process. The British Computer Society was founded in 1956.
}

\slides{
### A Time for Professionalisation?

* New technologies historically led to new professions:
    * Brunel (born 1806): Civil, mechanical, naval
    * Tesla (born 1856): Electrical and power
    * William Shockley (born 1910): Electronic 
    * Watts S. Humphrey (born 1927): Software
}

\slides{
### Why?

* Codification of best practice.
* Developing trust
}

\notes{
Why the need for these professions? Much of it is about codification of best practice and developing trust between the public and practitioners. These fundamental characteristics of the professions are shared with the oldest professions (Medicine, Law) as well as the newest (Information Technology).
}

\slides{

### Where are we?

* Perhaps around the 1980s of programming.
    * We understand ```if```, ```for```, and procedures
    * But we don't share best practice.

* Let's *avoid* the over formalisation of software engineering.

}

\notes{
So where are we today? My best guess is we are somewhere equivalent to the 1980s for Software Engineering. In terms of professional deployment we have a basic understanding of the equivalent of "programming" but much less understanding of *machine learning systems design* and *data infrastructure*. How the components we ahve developed interoperate together in a reliable and accountable manner. Best practice is still evolving, but perhaps isn't being shared widely enough. 

One problem is that the art of data science is superficially similar to regular software engineering. Although in practice it is rather different. Modern software engineering practice operates to generate code which is well tested as it is written, agile programming techniques provide the appropriate degree of flexibility for the individual programmers alongside sufficient formalization and testing. These techniques have evolved from an overly restrictive formalization that was proposed in the early days of software engineering.

While data science involves programming, it is different in the following way. Most of the work in data science involves understanding the data and the appropriate manipulations to apply to extract knowledge from the data. The eventual number of lines of code that are required to extract that knowledge are often very few, but the amount of thought and attention that needs to be applied to each line is much more than a traditional line of software code. Testing of those lines is also of a different nature, provisions have to be made for evolving data environments. Any development work is often done on a static snapshot of data, but deployment is made in a live environment where the nature of data changes. Quality control involves checking for degradation in performance arising form unanticipated changes in data quality. It may also need to check for regulatory conformity. For example, in the UK the General Data Protection Regulation stipulates standards of explainability and fairness that may need to be monitored. These concerns do not affect traditional software deployments.

Others are also pointing out these challenges, [this post](https://medium.com/@karpathy/software-2-0-a64152b37c35) from Andrej Karpathy (now head of AI at Tesla) covers the notion of "Software 2.0". Google researchers have highlighted the challenges of "Technical Debt" in machine learning [@Sculley:debt15]. Researchers at Berkeley have characterized the systems challenges associated with machine learning [@Stoica:systemsml17].
}

