\ifndef{nigeriaNmisDataExplore}
\define{nigeriaNmisDataExplore}


\include{_datasets/includes/nigeria-nmis-data.md}

\editme

\subsection{Exploring the NMIS Data}

\notes{The NMIS facility data is stored in an object known as a 'data frame'. Data frames come from the statistical family of programming languages based on `S`, the most widely used of which is [`R`](http://en.wikipedia.org/wiki/R_(programming_language)). The data frame gives us a convenient object for manipulating data. The describe method summarizes which columns there are in the data frame and gives us counts, means, standard deviations and percentiles for the values in those columns. To access a column directly we can write}

\code{print(data['num_doctors_fulltime'])
#print(data['num_nurses_fulltime'])}

\notes{This shows the number of doctors per facility, number of nurses and number of community health workers (CHEWS). We can plot the number of doctors against the number of nurses as follows.}

\setupcode{import matplotlib.pyplot as plt # this imports the plotting library in python}

\code{_ = plt.plot(data['num_doctors_fulltime'], data['num_nurses_fulltime'], 'rx')}

\notes{You may be curious what the arguments we give to `plt.plot` are for, now is the perfect time to look at the documentation}

\code{plt.plot?}

\notes{We immediately note that some facilities have a lot of nurses, which prevent's us seeing the detail of the main number of facilities. First lets identify the facilities with the most nurses.}

\code{data[data['num_nurses_fulltime']>100]}

\notes{Here we are using the command `data['num_nurses_fulltime']>100` to index the facilities in the pandas data frame which have over 100 nurses. To sort them in order we can also use the `sort` command. The result of this command on its own is a data `Series` of `True` and `False` values. However, when it is passed to the `data` data frame it returns a new data frame which contains only those values for which the data series is `True`. We can also sort the result. To sort the result by the values in the `num_nurses_fulltime` column in *descending* order we use the following command.}

\code{data[data['num_nurses_fulltime']>100].sort_values(by='num_nurses_fulltime', ascending=False)}

\notes{We now see that the 'University of Calabar Teaching Hospital' is a large outlier with 513 nurses. We can try and determine how much of an outlier by histograming the data.}

\notes{\subsection{Plotting the Data}}

\code{data['num_nurses_fulltime'].hist(bins=20) # histogram the data with 20 bins.
plt.title('Histogram of Number of Nurses')}

\notes{We can't see very much here. Two things are happening. There are so many facilities with zero or one nurse that we don't see the histogram for hospitals with many nurses. We can try more bins and using a *log* scale on the $y$-axis.}

\code{data['num_nurses_fulltime'].hist(bins=100) # histogram the data with 20 bins.
plt.title('Histogram of Number of Nurses')
ax = plt.gca()
ax.set_yscale('log')}

\notes{Let's try and see how the number of nurses relates to the number of doctors.}

\code{fig, ax = plt.subplots(figsize=(10, 7)) 
ax.plot(data['num_doctors_fulltime'], data['num_nurses_fulltime'], 'rx')
ax.set_xscale('log') # use a logarithmic x scale
ax.set_yscale('log') # use a logarithmic Y scale
# give the plot some titles and labels
plt.title('Number of Nurses against Number of Doctors')
plt.ylabel('number of nurses')
plt.xlabel('number of doctors')}

\notes{Note a few things. We are interacting with our data. In particular, we are replotting the data according to what we have learned so far. We are using the progamming language as a *scripting* language to give the computer one command or another, and then the next command we enter is dependent on the result of the previous. This is a very different paradigm to classical software engineering. In classical software engineering we normally write many lines of code (entire object classes or functions) before compiling the code and running it. Our approach is more similar to the approach we take whilst debugging. Historically, researchers interacted with data using a *console*. A command line window which allowed command entry. The notebook format we are using is slightly different. Each of the code entry boxes acts like a separate console window. We can move up and down the notebook and run each part in a different order. The *state* of the program is always as we left it after running the previous part.}

\endif
