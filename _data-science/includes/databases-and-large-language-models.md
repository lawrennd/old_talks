\ifndef{databasesAndLargeLanguageModels}
\define{databasesAndLargeLanguageModels}

\editme

\subsection{Databases and Large Language Models}

\notes{In a previous section, we integrated LLMs in the data exploration and visualisation process. Now we will see the potential of integrating LLMs for databases. We will use the agend we created before using langchain and describe the instruction we need the agent to execute.}

\code{sql_code = agent("The database 'nigeria_nmis' is hosted in AWS the endpoint is '" + url + "'. The user is '" + username + "' and the password '" + password + "'. The database has the table hospitals_zones_joined with columns facility_name and num_nurses_fulltime (number of full time nurses), give pymysql mariadb code to show the 20 hospitals which have the most full time nurses. Print the results of the query as a dataframe at the end")}

\notes{If you analyse the input that the agent receives, we need to be more specific this time. We passed the name of the database we wanted to use, the AWS endpoint, the username, and the password of our database. Then we provide information about the table we want to query (e.g., table name and columns). Finally, we provide the data requirement we need to satisfy (i.e., show the 20 hospitals which have the most full time nurses), and specify how these should be printed.

Similarly, the "actions" and "observations are a bit more complex compared to the output of previous data exploration tasks.}

\notes{For comparison, we can execute the SQL command that the model generates directly in our database.}

\code{%sql SELECT facility_name, num_nurses_fulltime FROM hospitals_zones_joined ORDER BY num_nurses_fulltime DESC LIMIT 20}

\notes{As the interaction with the LLM becomes more and more complex, it is a good idea to think about code wrappers that we can reuse in our pipeline. For example, we can define a set of Python functions that facilitate the database and LLMs integration. A way to define these functions, but not the only one, is presented as follows:}

\code{def simple_llm_sql(command, dbname='nigeria_nmis', tables=('hospitals_zones_joined',)):
    sql_code = llm_prompt(f"In this database '{dbname}' with: " + ", ".join([f"table {table} described {sql_query(f'DESCRIBE {table}')}" for table in tables]) + f", give pymysql mariadb code to: {command}. Format your response as only the SQL query, not python code, not description.") # experiment with prompts
    print(sql_code)
    y = input('safe to execute? (y/n)')
    if y == 'y':
      return sql_query(sql_code)

def sql_query(query, host='database-ads.cgrre17yxw11.eu-west-2.rds.amazonaws.com', user=username, password=password, db='nigeria_nmis'):
  conn = create_connection(user, password, host, db)
  return pd.read_sql(query, conn)

def llm_prompt(llm_prompt, model="gpt-3.5-turbo"):
  return openai.ChatCompletion.create(
      model=model,
      messages = [{"role": "user", "content": llm_prompt}],
      temperature=0.2,
      max_tokens=2000,
      frequency_penalty=0.0
  ).choices[0].message.content}

\notes{Then, we can call our wrapper in a simplified fashion.}

\code{simple_llm_sql("show the 20 hospitals which have the most full time nurses")}

\notes{We will return to the SQL command style after downloading and adding the other
datasets to the database using a combination of `pandas` and the
database utilities.

Our next task will be to introduce data on COVID19 so that we can join
that to our other data sets.}
\endif
