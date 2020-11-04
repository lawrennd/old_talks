\ifndef{recommenderData}
\define{recommenderData}
\editme

\subsection{Obtaining the Data}

\notes{We are using a functionality of the Open Data Science software
library to obtain the data. This functionality involves some
prewritten code which distributes to each of you a google spreadsheet
where you can rate movies that you've seen. For completeness the code
follows. Try and read and understand the code, but don't run it! It
has already been run centrally by me.}

```python
import pods
import pandas as pd
import numpy as np
user_data = pd.DataFrame(index=movies.index, columns=['title', 'year', 'rating', 'prediction'])
user_data['title']=movies.Film
user_data['year']=movies.Year

accumulator=pods.lab.distributor(spreadsheet_title='COM4509/6509 Movie Ratings:', user_sep='\t')
# function to apply to data before giving it to user 
# Select 50 movies at random and order them according to year.
max_movies = 50
function = lambda x: x.loc[np.random.permutation(x.index)[:max_movies]].sort(columns='year')
accumulator.write(data_frame=user_data, comment='Film Ratings', 
                  function=function)
accumulator.write_comment('Rate Movie Here (score 1-5)', row=1, column=4)
accumulator.share(share_type='writer', send_notifications=True)
```

\notes{In your Google drive account you should be able to find a
spreadsheet called 'COM4509/6509 Movie Ratings: Your Name'. In the
spreadsheet You should find a number of movies listed according to
year. In the column titled 'rating' please place your rating using a
score of 1-5 for *any* of the movies you've seen from the list.}

Once you have placed your ratings we can download the data from your
spreadsheets to a central file where the ratings of the whole class
can be stored. We will build an algorithm on these ratings and use
them to make predictions for the rest of the class. Firstly, here's
the code for reading the ratings from each of the spreadsheets.

```python
import numpy as np
import pandas as pd
import os

accumulator = pods.lab.distributor(user_sep='\t')
data = accumulator.read(usecols=['rating'], dtype={'index':int, 'rating':np.float64}, header=2)

for user in data:
    if data[user].rating.count()>0: # only add user if they rated something
        # add a new field to movies with that user's ratings.
        movies[user] = data[user]['rating']

# Store the csv on disk where it will be shared through dropbox.
movies.to_csv(os.path.join(pods.lab.class_dir,'movies.csv'), index_label='index')
```

Now we will convert our data structure into a form that is appropriate
for processing. We will convert the `movies` object into a data base
which contains the movie, the user and the score using the following
command.

\setupcode{import pandas as pd
import os}

\code{# uncomment the line below if you are doing this task by self study.
pods.util.download_url('https://dl.dropboxusercontent.com/u/4347554/mlai_movies.csv', store_directory = 'class_movie', save_name='movies.csv')
#pods.util.download_url('https://www.dropbox.com/s/s6gqvp9b383b59y/movies.csv?dl=0&raw=1', store_directory = 'class_movie', save_name='movies.csv')
movies = pd.read_csv(os.path.join('class_movie', 'movies.csv'),encoding='latin-1').set_index('index')}

\writeassignment{The movies data is now in a data frame which contains
one column for each user rating the movie. There are some entries that
contain 'NaN'. What does the 'NaN' mean in this context?}{5}

\subsection{Processing the Data}

We will now prepare the data set for processing. To do this we are
going to conver the data into a new format using the `melt` command.

\code{user_names = list(set(movies.columns)-set(movies.columns[:9]))
Y = pd.melt(movies.reset_index(), id_vars=['Film', 'index'], 
            var_name='user', value_name='rating', 
            value_vars=user_names)
Y = Y.dropna(axis=0)}

\subsection{What is a pivot table? What does the `pandas` command
`pd.melt` do?}{3}{10}

\endif
