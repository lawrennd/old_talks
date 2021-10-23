\ifndef{saveCredentialsFile}
\define{saveCredentialsFile}

\editme

\subsubsection{Saving a Credentials File}

\setupcode{import yaml
from ipywidgets import interact_manual, Text, Password}

\helpercode{@interact_manual(username=Text(description="Username:"), 
                 password=Password(description="Password:"))
def write_credentials(username, password):
    with open("credentials.yaml", "w") as file:
        credentials_dict = {'username': username, 
                            'password': password}
        yaml.dump(credentials_dict, file)}
        
\notes{If you click `Run Interact` then the credentials you've selected will be saved in the `yaml` file. Remember them, as you'll need them when you set up the database server below.}

\endif
