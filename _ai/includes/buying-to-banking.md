\ifndef{buyingToBanking}
\define{buyingToBanking}

\editme

\newslide{Buying ...}

\slides{
\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-purchasing000}{60%}}{A potential path of models in a machine learning system for making a purchase in an automated buying system.}{ml-system-downstream-purchasing}}

\notes{\subsection{Buying to Banking}

The same model we consider for buying, can also be considered in the case of, for example, a banking application. In a typical banking application, we receive loan requests from customers. For an individual customer, before making a loan, the bank may wish to make a forecast around their costs (expenditures on food, housing, entertainment etc) and their income (salary, rental income etc). These forecasts would inform the conditions of the loan. For example how much the bank is willing to lend, and under what interest rates and repayment conditions. These terms will be based on previous experience of loaning, but also constrained by regulatory conditions often imposed by a financial regulator.}



\newslide{... to Banking}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-banking000}{60%}}{A potential path of models in a machine learning system where a decision about a loan is being made on the basis of (potentially personal) data from a customer.}{ml-system-downstream-banking}

\notes{In many regulatory environments, the bank will be restricted in terms of what information they are allowed to use in dictating loan terms. For example, with in the EU there are prohibited characteristics such as race, gender, sexuality, religion and health status which cannot be used (even indirectly) for making the loan. Along with stipulating these characteristics, the badly-named GDPR[^gdpr-footnote] also gives particular stipulations for rights individuals have for explanation around consequential decisions, such as obtaining a loan.

The challenge of Intellectual Debt means that it's possible for a bank to produce an automated loan decision system, which even the bank itself doesn't understand, which makes it rather hard to conform to the intent of the GDPR which requires the bank to explain to customers the reasoning behind decisions based on personal data.}


[^gdpr-footnote]: The GDPR is "General Data Protection Regulation" but it does not 'protect data' it 'protects individuals' with regard to decision making based on their personal data. The misnomer data-protection is unfortunate, a better way of viewing this legislation is "personal data rights" legislation. 


\editme
