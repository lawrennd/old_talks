---
title: "Practical 1"
practical: 1
featured_image: assets/images/practical-one.png
abstract:  >
  In this lab session we look at setting up a SQL server and making joins between different data sets.
layout: practical
venue: Intel Lab, William Gates Building
author:
- family: Cabrera
  given: Christian
  institute: University of Cambridge
  url: https://www.cst.cam.ac.uk/people/chc79
- family: Meissner
  given: Eric
- family: Sendyka
  given: Radzim
  institute: University of Cambridge
  url: https://www.cst.cam.ac.uk/people/rs2071
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
time: "15:00"
postsdir: ../../../mlatcl/advds/_practicals/
date: 2023-10-31
transition: None
reveal: false
ipynb: true
---


<!-- have students use AWS details we provided -->
\define{awsSignUp}

\notes{Check Session for this Practical is 2nd November 2023}

\notes{- This practical should prepare you for Part 1 of the course assessment. Ensure that you have a solid understanding of the material, with particular emphasis on the AWS database setup. You should be able to use the same database that you set up here for the final assessment.
- In that assessment, you will be working with significantly larger datasets, often requiring extended waiting times for query execution. **Start your work on Part 1 setup early** to avoid being blocked from work on subsequent stages later on.
- Some tasks will require you to develop skills for searching for multiple solutions and experimenting with different approaches, which may not have been covered in the lectures. This environment closely resembles real-world data science and software engineering challenges, where there might not be a single correct solution.}

\define{databaseType}{mariadb}
\include{_systems/includes/nigeria-nmis-installs.md}

\include{_systems/includes/nigeria-health-intro.md}
\include{_systems/includes/nigeria-nmis-data-systems.md}
\include{_data-science/includes/data-science-and-large-language-models.md}
\include{_systems/includes/databases-and-joins.md}
\include{_systems/includes/nigeria-nmis-spatial-join.md}
\include{_systems/includes/nigeria-nmis-sql.md}
\include{_data-science/includes/databases-and-large-language-models.md}
\include{_systems/includes/nigeria-nmis-covid-join.md}


\codeassignment{Interact with LLMs using the tools shown above to describe and visualise an aspect of the dataframe from question 4.}{}{10}
\thanks

\references
