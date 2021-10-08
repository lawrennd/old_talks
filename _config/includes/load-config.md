\ifndef{loadConfig}
\define{loadConfig}

\editme

\subsection{Load Config File}

\notes{This code is for loading in local configuration files where, for example, you might be storing keys or passwords that should not be uploaded online.}

\notes{To store information create a new file called `_config.yml`. That file should be in yaml format, for example

```
---
database:
  ip: 127.0.0.1
  port: 3306
  username: admin
---
```

\installcode{ndlpy}
\code{from ndlpy import config}

\endif
