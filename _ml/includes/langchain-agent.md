\ifndef{langchainAgent}
\define{langchainAgent}

\include{_software/includes/langchain-software.md}



\editme
\subsection{Langchain agent}

\notes{Now we should configure a Langchain `agent`. This agent is the interface between our code and the LLM. The `agent` receives our questions in natural language and will provide, hopefully, the answer we are looking for.}

\notes{First let's import the required libraries.}

\setupcode{import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from getpass import getpass
import openai
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI}

\notes{We need to create an agent using our OpenAI API key now. The agent receives the data we want to analyse as a parameter. In this case, it is the data frame. The verbosity is set to True to track the workflow the agent follows to get the required answer.}

\code{openai_api_key = [INSERT_YOUR_OPENAI_API_HERE]
os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key = openai_api_key}

\code{agent = create_pandas_dataframe_agent(OpenAI(temperature=0, openai_api_key=openai_api_key), data, verbose=True)}

\notes{Once the agent is configured we can start by asking questions about our data. For example, we can ask the agent for the names of the columns of the dataframe.}

\code{results = agent("What are Column names?")}

\notes{If you look at the output closer, you will see in green the "thoughts" and "actions" the agent performs. It is of particular interest the second "action" of this agent execution chain. This "action" corresponds to the execution ot the `df.columns` command, where `df` is the dataframe the agent received as a parameter during its configuration (i.e., the `data` dataframe). You should get a similar output to the `Observation` in blue if you execute the `data.columns` Python command.}

\code{data.columns}

\notes{Let's go a bit deeper in our analysis. We want to know which columns in our data frame are categorical and which columns store numeric values. Let's see what the agent says ...}

\code{results = agent("Which columns are categorical and which are numeric?")}

\codeassignment{What is the main command the agent executes to get the answer according to its "actions" and "observations"? Write and execute the Python command using the `data` data frame in the next box. Compare the output of this execution with the output of the agent "observation".}{}{10}

\notes{In a final example to describe our data, we want to know if there are any missing values in our data frame.}

\code{results = agent("Are there any missing values in columns")}

\codeassignment{Again, please identify the main command the agend executed and compare the output you get.}

\notes{The last steps were useful to know the data better. It looks like the integration of LLMs in the process was useful. But, what about data visualisation?}

\notes{Well, there are already specific libraries designed to this end. That is the case of [`autoplotlib`](https://github.com/rdnfn/autoplotlib), which generates plots of your data from text descriptions.}

\installcode{autoplotlib}

\notes{Now we can use the library. Let's ask for a plot of the Nigerian health facilities. The autoplotlib plot function receives the figure description and the data we want to visualise as parameters. The function returns the code of the plot, the figure, and the response from the LLM. These outputs are then prompted to you for checking.}

\setupplotcode{import autoplotlib as aplt}

\plotcode{figure_description = "Plot a map with the nigerian health facilities."
code, fig, llm_response = aplt.plot(figure_description, data=data)}

\codeassignment{One nice property of `autoplotlib` is that it prompts the code before execution. So, you can inspect the code the LLM generates. What do you think of the plotted map? Is it similar to the one we created before?}{}{10}

\notes{Certainly, it is similar, but there are some differences. You can add more details to the figure description to make it more similar or change the plot's appearance. For example, we can change the value of the parameter `alpha` for the figure. This parameter changes the transparency of the graph, so we can see the places with more density of healthcare facilities.}

\setupplotcode{import autoplotlib as aplt}
\plotcode{figure_description = "Plot a map with the nigerian health facilities with alpha=0.01."
code, fig, llm_response = aplt.plot(figure_description, data=data)}

\notes{Now, you have initial ideas about integrating LLMs into the data science process. We will come back to this later in this lab and we expect you to continue thinking of and exploring its potential. For now, let's save our data frame in a more self-descriptive variable for later. In our next section, we will start learning about Databases.}

\endif
