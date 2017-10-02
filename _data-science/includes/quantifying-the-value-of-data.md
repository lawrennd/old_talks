### Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

<img src="../slides/diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!


### Data --- Quotes from NIPS Workshop on ML for Healthcare

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez)
* In health care clinicians collect the data and often control the direction of research through guardianship of data.

### Value

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
    * Incentivization for sharing and production.
    * Quantifying the value in the contribution of *each actor*.


### Embodiment: Data Readiness Levels

* Three Bands of Data Readiness:

* Band C - accessibility

* Band B - validity

* Band A - usability


### Accessibility: Band C

* Hearsay data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)

### Validity: Band B

*  faithfulness and representation
* visualisations.
* noise characterisation.
* Missing values.
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?

### Usability: Band A

* The usability of data
* Band A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.

### Recursive Effects

* Band A may also require
    * active collection of new data. 
    * annotation of data by human experts
    * revisiting the collection (and running through the appropriate stages again)

### Also ...

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

### See Also ...

* Data Joel Tests proposal by Damon Civin (ARM)
