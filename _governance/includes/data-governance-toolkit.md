\ifndef{dataGovernanceToolkit}
\define{dataGovernanceToolkit}

\editme

\subsection{Data Governance Toolkit}

\figure{\includepng{\diagramsDir/governance/decision-tree-for-data-sharing}{50%}}{Decision tree for data sharing. The root node splits agreements into those where the data has and hasn’t been collected. The scope and nature of rights pertaining to the data is the next branch.}{decision-tree-for-data-sharing}

\figure{\includediagramclass{\diagramsDir/governance/color-wheel}{100%}}{Governance considerations can be grouped in four parts, individuals, society, enfranchisement and vulnerabilities.}{data-governance-color-wheel}

\notes{With Sylvie Delacroix and Jessica Montgomery we've been working towards a data governance toolkit. Trying to understand the different approaches to data sharing and access we may need for different types of data. Some of the }

\notes{One major challenge to data sharing is that it means different things to different people and different institutions. The objectives of data sharing can differ amoung different sharing parties. This leads to a great deal of confusion when discussing mechanisms for data sharing.}

\notes{For example, in 2016, inspired by conversations with Jonathan Price, I proposed the idea of Data Trusts. This was a data sharing idea specifically targeted at protecting indviduals from the vulnerabilities they are exposed to when sharing personal data.}

\notes{Unfortunately, the idea has since been promoted as a universal panacea for data sharing. As a result, the original concept is inevitably misunderstood, watered down or derided. It seems clear that we need a better understanding of the data sharing landscape. Some steps have been taken to outlining the legal implications of different data sharing structures in a report ["Exploring legal mechanisms for data stewardship"](https://www.adalovelaceinstitute.org/report/legal-mechanisms-data-stewardship/) from the Ada Lovelace Institute in collaboration with the UK's AI Council.}

\notes{The framework we're using comes from discussions with Sylvie Delacroix and Jess Montgomery on how to characterise the data governenance process. We've developed the color wheel shown above. See our [blog post here](https://datatrusts.uk/blogs/selectingdatastructures).}

\notes{The color wheel is meant to broadly characterise the different considerations we need to have when developing data governance frameworks and some of the tensions we experience when describing different approaches to data sharing.}

\newbanner{Society}{\societyColor}

\figure{\includediagramclass{\diagramsDir/governance/society}{100%}}{The society diagram shows the different words associated with positive outcomes and negative outcomes for different data sharing frameworks based around society. On the positive spectrum we can imagine wordslike safety, health, egality all associated with the utopian version of society. At the dystopian end we have terror, pollution, disease.}{society}

\notes{Typical social benefits derived from data sharing include better health, and better security. By sharing information widely about society we can better understand how to manage society to wider benefit.}

\newbanner{Vulnerabilities}{\vulnerabilityColor}

\figure{\includediagramclass{\diagramsDir/governance/vulnerabilities}{100%}}{Thinking of how data governance must protect vulnerability. In the utopian case we can image support and the flourishing of people regardless of vulnearabilities, at the dystopian end we can imagin moder slavery, abuse, exploitation.}{vulnerability}

\notes{There are individuals in society who are vulnerable due to disempowerment. Many of these vulnerabilities are due to minority status or particular conditions. Protecting vulnerable individuals is a vital component of good governance. This is reflected in, for example, data rights legislation such as the GDPR which defines protected characteristics and prohibited discriminations around sensitive areas such as health, race, religion, sexuality and gender. These protections very often recognise past injustices or systemic biases that we wish to prevent in future. Other vulnerable groups include those we don't empower to decide for themselves, such as children.}


\newbanner{Enfranchisement}{\enfranchisementColor}

\figure{\includediagramclass{\diagramsDir/governance/enfranchisement}{100%}}{How our opinons are represented is another important part of data governance, the enfrahcnisement. In the utopian case we have representation, redress, empowerment, whereas in the dystopian extreme we have autocracy, authoratarianism or anarchy.}{enfranchisement}

\notes{In any governance structure, the route for individuals (or institutions) that are participating in the structure to represent their own opinion, query decision making and realign the values of the governance organisation with there own is a criticial component. Considering groups that are currently disenfranchised (for example, in digital systems, the elderly) also forms a component of the design of the governance structure. Dealing with power asymmetries, such as those we're experiencing in our current somewhat feudal system of data governance is also a key challenge for the enfranchisement.}

\newbanner{Individuals}{\individualColor}

\figure{\includediagramclass{\diagramsDir/governance/individuals}{100%}}{}{individuals}

\notes{Representing individual aspirations as part of the governance structure relates strongly to traditional notions of liberty which involve freedom of action. A particular sense in which we think of individual liberty in digital systems is in terms of control we each have around our individual aspirations.}

\endif
