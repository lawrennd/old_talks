\ifndef{dataframeInteract}
\define{dataframeInteract}

\editme

\subsection{Interaction in Jupyter Notebook}

\notes{As well as providing plotting capabilities, the notebook gives us the capability to interact with python objects. We can design custom interaces to work with the data we have.}

\notes{Here we are inspired by a blog post from Tony Hirst [@Hirst-interactive16].}

\notes{The Jupyter notebook was originally introduced by the IPython project. For that reason it's widgets are nown as `ipywidgets`. These widgets are one of the most powerful features of the notebook. They allow you to create your own customised interaction interfaces for the data.}

\setupcode{import ipywidgets as widgets
from ipywidgets import interactive}
 
\code{items = ['All']+sorted(df['Asset Type Description'].unique().tolist())
 
def view(x=''):
    if x=='All': return df
    return df[df['Asset Type Description']==x]
 
w = widgets.Select(options=items)
interactive(view, x=w)}

We can also create multiple controller widgets and bind them into a single interactive display function. For example, we might have one control to filter rows according to the value contained within a particular column, and another widget limiting how many rows are displayed by creating two widgets and accessing them via an interactive ipywidgets construction call:

\helpercode{def view2(x='',y=3):
    if x=='All': return df.head(y)
    return df[df['Asset Type Description']==x].head(y)
 
a_slider = widgets.IntSlider(min=0, max=15, step=1, value=5)
b_select =  widgets.Select(options=items)
widgets.interactive(view2,y=a_slider,x=b_select)}

\code{c_slider = widgets.IntSlider(min=0, max=len(df), step=1, value=5)
d_select =  widgets.Select(options=items)
 
def update_c_range(*args):
    if d_select.value=='All':
        c_slider.max = len(df)
    else:
        c_slider.max = len(df[df['Asset Type Description']==d_select.value])
 
d_select.observe(update_c_range, 'value')
 
def view3(x='',y=3):
    if x=='All': return df.head(y)
    return df[df['Asset Type Description']==x].head(y)
 
widgets.interactive(view3,y=c_slider,x=d_select)}

\endif
