\ifndef{nigerianPopulationDataSql}
\define{nigerianPopulationDataSql}

\editme

\ifndef{databaseType}
  \define{databaseType}{sqlite}
\endif
\ifeq{databaseType}{sqlite}
  talk-macros.gpp}ystems/includes/nigerian-population-data-sqlite.md}
\else
  \ifeq{databaseType}{mariadb}
    talk-macros.gpp}ystems/includes/nigerian-population-data-mariadb.md}
  \endif
\endif


\endif
