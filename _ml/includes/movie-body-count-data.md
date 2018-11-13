\section{Movie Body Count Example}

\notes{There is a crisis in the movie industry, deaths are
occuring on a massive scale. In every feature film the body count is tolling up.
But what is the cause of all these deaths? Let's try and investigate.}

\notes{For our first example of data science, we take inspiration from work by [researchers at NJIT](http://www.theswarmlab.com/r-vs-python-round-2/). They researchers were comparing the qualities of Python with R (my brief thoughts on the subject are available in a Google+ post here: https://plus.google.com/116220678599902155344/posts/5iKyqcrNN68). They put together a data base of results from the  the "Internet Movie Database" and the [Movie Body Count](http://www.moviebodycounts.com/) website which will allow us to do some preliminary investigation.}

\notes{We will make use of data that has already been 'scraped' from the [Movie Body Count](http://www.moviebodycounts.com/) website. Code and the data is available at [a github repository](https://github.com/sjmgarnier/R-vs-
Python/tree/master/Deadliest%20movies%20scrape/code). Git is a version control
system and github is a website that hosts code that can be accessed through git.
By sharing the code publicly through github, the authors are licensing the code
publicly and allowing you to access and edit it. As well as accessing the code
via github you can also [download the zip file](https://github.com/sjmgarnier/R-vs-Python/archive/master.zip).}

\notes{For ease of use we've packaged this data set in the ```pods``` library}

\include{_ml/includes/pods.md}

\code{data = pods.datasets.movie_body_count()['Y']
data.head()}

\notes{Once it is loaded in the data can be summarized using the `describe` method in pandas.}

\code{data.describe()}

\notes{In jupyter and jupyter notebook it is possible to see a list of all possible
functions and attributes by typing the name of the object followed by .<Tab> for
example in the above case if we type data.<Tab> it show the columns
available (these are attributes in pandas dataframes) such as Body_Count, and
also functions, such as .describe().}

\notes{For functions we can also see the
documentation about the function by following the name with a question mark.
This will open a box with documentation at the bottom which can be closed with
the x button.}

\code{data.describe?}

\notes{The film deaths data is stored in an object known as a 'data frame'. Data frames
come from the statistical family of programming languages based on `S`, the most
widely used of which is
[`R`](http://en.wikipedia.org/wiki/R_(programming_language)). The data frame
gives us a convenient object for manipulating data. The describe method
summarizes which columns there are in the data frame and gives us counts, means,
standard deviations and percentiles for the values in those columns. To access a
column directly we can write}

\code{print(data['Year'])
#print(data['Body_Count'])}

\notes{This shows the number of deaths per film across the years. We can plot the data as follows.}

\setupcode{# this ensures the plot appears in the web browser
%matplotlib inline 
import matplotlib.pyplot as plt # this imports the plotting library in python}

\code{plt.plot(data['Year'], data['Body_Count'], 'rx')}

\notes{You may be curious what the arguments we give to ```plt.plot``` are for, now is the perfect time to look at the documentation}

\code{plt.plot?}

\notes{We immediately note that some films have a lot of deaths, which prevent us seeing the detail of the main body of films. First lets identify the films with the most deaths.}

\code{data[data['Body_Count']>200]}

\notes{Here we are using the command `data['Kill_Count']>200` to index the films in the pandas data frame which have over 200 deaths. To sort them in order we can also use the `sort` command. The result of this command on its own is a data series of `True` and `False` values. However, when it is passed to the
`data` data frame it returns a new data frame which contains only those
values for which the data series is `True`. We can also sort the result. To sort
the result by the values in the `Kill_Count` column in *descending* order we use
the following command.}

\code{data[data['Body_Count']>200].sort_values(by='Body_Count', ascending=False)}

\notes{We now see that the 'Lord of the Rings' is a large outlier with a very large number of kills. We can try and determine how much of an outlier by histograming the data.}

\notes{
### Plotting the Data
}

\code{data['Body_Count'].hist(bins=20) # histogram the data with 20 bins.
plt.title('Histogram of Film Kill Count')}

\writeassignment{Read on the internet about the following python
libraries: `numpy`, `matplotlib`, `scipy` and `pandas`. What functionality does
each provide python. What is the `pylab` library and how does it relate to the
other libraries?}{2}{10}

\notes{We could try and remove these outliers, but another approach would be plot the logarithm of the counts against the year.}

\code{plt.plot(data['Year'], data['Body_Count'], 'rx')
ax = plt.gca() # obtain a handle to the current axis
ax.set_yscale('log') # use a logarithmic death scale
# give the plot some titles and labels
plt.title('Film Deaths against Year')
plt.ylabel('deaths')
plt.xlabel('year')}

\notes{Note a few things. We are interacting with our data. In particular, we are
replotting the data according to what we have learned so far. We are using the
progamming language as a *scripting* language to give the computer one command
or another, and then the next command we enter is dependent on the result of the
previous. This is a very different paradigm to classical software engineering.
In classical software engineering we normally write many lines of code (entire
object classes or functions) before compiling the code and running it. Our
approach is more similar to the approach we take whilst debugging. Historically,
researchers interacted with data using a *console*. A command line window which
allowed command entry. The notebook format we are using is slightly different.
Each of the code entry boxes acts like a separate console window. We can move up
and down the notebook and run each part in a different order. The *state* of the
program is always as we left it after running the previous part.}
