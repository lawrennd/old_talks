### Data Readiness Levels

[\includeimg{../slides/diagrams/data-science/data-readiness-levels.png}](https://arxiv.org/pdf/1705.02245.pdf)


   [Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels)

### Three Grades of Data Readiness:

* Grade C - accessibility

* Grade B - validity

* Grade A - usability


### Accessibility: Grade C

* *Hearsay* data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)
* At the end of Grade C data is ready to be loaded into analysis software (R, SPSS, Matlab, Python, Mathematica)

### Validity: Grade B

* faithfulness and representation
* visualisations.
* exploratory data analysis
* noise characterisation.
* Missing values.
* Schema alignment, record linkage, data fusion? 
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?
* At the end of Grade B, ready to define a candidate question, the
  context, load into OpenML

### Usability: Grade A

* The usability of data
* Grade A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.
* Data integration?
* At the end of Grade A it's ready for data platforms such as RAMP, Kaggle, define a *task* in OpenML.

