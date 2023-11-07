\ifndef{dataTrusts}
\define{dataTrusts}
\editme

\subsection{Personal Data Trusts}

\notes{The machine learning solutions we are dependent on to drive automated decision making are dependent on data. But with regard to personal data there are important issues of privacy. Data sharing brings benefits, but also exposes our digital selves. From the use of social media data for targeted advertising to influence us, to the use of genetic data to identify criminals, or natural family members. Control of our virtual selves maps on to control of our actual selves. 

The feudal system that is implied by current data protection legislation has significant power asymmetries at its heart, in that the data controller has a duty of care over the data subject, but the data subject may only discover failings in that duty of care when it's too late. Data controllers also may have conflicting motivations, and often their primary motivation is *not* towards the data-subject, but that is a consideration in their wider agenda.

[Personal Data Trusts](https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy) [@Edwards:privacy04;@Lawrence:trusts16;@Delacroix:trusts18] are a potential solution to this problem. Inspired by *land societies* that formed in the 19th century to bring democratic representation to the growing middle classes. A land society was a mutual organization where resources were pooled for the common good. 

A Personal Data Trust would be a legal entity where the trustees' responsibility was entirely to the members of the trust. So the motivation of the data-controllers is aligned only with the data-subjects. How data is handled would be subject to the terms under which the trust was convened. The success of an individual trust would be contingent on it satisfying its members with appropriate balancing of individual privacy with the benefits of data sharing. 

Formation of Data Trusts became the number one recommendation of the Hall-Presenti report on AI, but unfortunately, the term was confounded with more general approaches to data sharing that don't necessarily involve fiduciary responsibilities or personal data rights. It seems clear that we need to better characterize the data sharing landscape as well as propose mechanisms for tackling specific issues in data sharing.

It feels important to have a diversity of approaches, and yet it feels important that any individual trust would be large enough to be taken seriously in representing the views of its members in wider negotiations.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/data-trusts}{100%}}{For thoughts on data trusts see \addguardian{Data Trusts}{https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy}.}{data-trusts}


\newslide{}

\figure{\includepng{\diagramsDir/data-science/data-trusts-review}{50%}}{Data Trusts were the first recommendation of the \href{https://www.out-law.com/en/articles/2017/october/review-calls-for-data-trusts-to-help-grow-artificial-intelligence-in-the-uk/}{Hall-Presenti Report}. More recently the nature of different data intermediaries was clarified in a report on \href{legal mechanisms for data sharing}{https://www.adalovelaceinstitute.org/report/legal-mechanisms-data-stewardship/} from the Ada Lovelace Institute.}{hall-presenti-report}


\newslide{Motivation}
\slides{
1. Indsidious decision-making that has downstream instrumental effects we don’t control.
2. A power-asymmetry between data-controllers and data-subjects
3. A loss of personhood in the re-representation of ourselves in the digital world.
4. The GDPR’s endeavour to curb contractual freedom cannot by itself reverse the power-asymmetry between data-controllers and data-subjects. 
}

\newslide{Analogy}

\slides{
* Digital Democracy vs Digital Oligarchy @Lawrence:digitaloligarchy15 or Information Feudalism @Lawrence:informationbarons15
* Data *subjects*, data *controllers* and data *processors*.
}
\notes{See }\addguardian{Digital Oligarchies}{https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data}\notes{ and }\addguardian{Information Feudalism}{https://www.theguardian.com/media-network/2015/nov/16/information-barons-threaten-autonomy-privacy-online}\notes{.}



\newslide{Legal Mechanism of Trusts}
\slides{
* Fiduciary responsibility of Trustees.
  * Burden of proof in negligence is reversed. 
* Trustees are data *controllers*
* Beneficiaries are data *subjects*
* Power of data accumulation wielded on the beneficiaries behalf
* See @Edwards:privacy04, @Delacroix:trusts19 and @Lawrence:trusts16
}
\include{_governance/includes/data-trusts-initiative.md}

\endif
