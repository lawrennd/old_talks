### Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

<img src="../slides/diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!


### Data Quotes

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez)
* Getting money from management for data collection and annotation can
be a total nightmare.

### Value

* How do we measure value in the data economy?

* How do we encourage data workers: curation and management

	* Incentivization for sharing and production.

	* Quantifying the value in the contribution of *each actor*.


### Data Readiness Levels

   [Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels)
   (see also [arxiv](https://arxiv.org/pdf/1705.02245.pdf))

* Three Grades of Data Readiness:

* Grade C - accessibility

* Grade B - validity

* Grade A - usability


### Accessibility: Grade C

* Hearsay data.
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

### Recursive Effects

* Grade A may also require:

    * active collection of new data.

    * rebalancing of data to ensure fairness

	* annotation of data by human experts 

	* revisiting the collection (and running through the appropriate stages again)

### Contribute!

* <http://data-readiness.org>


### Also ...

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

* Analogies: For Software Engineers [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).

### See Also ...

* Data Joel Tests
    * [proposal by Damon Civin](https://medium.com/@damoncivin/the-joel-test-for-data-readiness-4882aae64753) and
    * [proposal by Nick Elprin](https://blog.dominodatalab.com/joel-test-data-science/)
