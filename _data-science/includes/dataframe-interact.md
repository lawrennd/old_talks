\ifndef{dataframeInteract}
\define{dataframeInteract}

\editme

\subsection{Interaction in Jupyter Notebook}

\notes{As well as providing plotting capabilities, the notebook gives us the capability to interact with python objects. We can design custom interaces to work with the data we have.}

\notes{Here we are inspired by a blog post from Tony Hirst [@Hirst-interactive16].}

\notes{The Jupyter notebook was originally introduced by the IPython project. For that reason it's widgets are nown as `ipywidgets`. These widgets are one of the most powerful features of the notebook. They allow you to create your own customised interaction interfaces for the data.}

\notes{The key functionality is included in the function `interact`.}


\setupcode{import ipywidgets as widgets
from ipywidgets import interact, fixed
from IPython.display import display}
 
\notes{The first trick is to write a callback function. This callback function will display the data frame as required.}

\helpercode{def view_df(dataframe, column=None, item="all"):
	"""This helper function displays a DataFrame, filtering a given column on a particular item"""
    if column is None:
        column = dataframe.columns[0]
    if item=="all": 
        display(dataframe)
    display(dataframe[dataframe[column]==item])}
 
\notes{Now we can easily create selection boxes by passing a keyword arguments to `interact` alongside the callback function. If the keyword arguments contain lists, then interact interprets that as a request to form a selection box to pass to the callback function for that keyword argument. The special interact style `fixed` is interpreted as information that is passed directly to the function (i.e. not user selected).}

\notes{We'll select column `z` to operate on and allow us to select from the unique values in that column (which represent the classes `a` through `d` for filtering.}

\code{column = "z"
items = ["all"] + sorted(data_interact[column].unique().tolist())}

\notes{Now we can create the interact.}

\code{_ = interact(view_df,
             dataframe=fixed(data_interact), 
             column=fixed(column),
             item=items)}

\note{Note that we passed the full list of items to the `interact` function. That function calls the callback when the values are changed.}

\note{The `interact` function will try and infer the right sort of interface widget give the data you pass. But you can also be explicit about it, for example to force the "Select" element you can use}

\code{items = widgets.Select(options=["all"] + sorted(data_interact[column].unique().tolist()))}

\notes{You can [read more about the available widgets in the documentation](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html).}

\notes{Let's make use of the `IntSlider` widget and the `Select` widget to limit the number of rows we display from the data frame. To do this we first introduce a new callback function.}

\helpercode{def view_df2(dataframe, item="all", column=None, number=3):
    if column is None:
        column = dataframe.columns[0]
    if item=="all": 
	    display(dataframe.head(number))
    display(dataframe[dataframe[column]==item].head(number))}

\notes{Now we introduce a slider.}

\code{number_slider = widgets.IntSlider(min=0, max=15, step=1, value=5)
item_select = widgets.Select(options=items)}

\code{_ = interact(view_df2, dataframe=fixed(data_interact),
             column=fixed("z"),
             item=item_select,
	         number=number_slider)}

\codeassignment{Update the interact to have a `FloatSlider` element that filters out elements from column `x` or `y` (by choice) if they are above a particular value.}{}{10}


\endif
