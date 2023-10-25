\ifndef{nigerianPopulationDataSql}
\define{nigerianPopulationDataSql}

\editme

\ifndef{databaseType}
  \define{databaseType}{sqlite}
\endif
\ifeq{\databaseType}{sqlite}
  \include{_systems/includes/nigerian-population-data-sqlite.md}
\else
  \ifeq{\databaseType}{mariadb}
    \include{_systems/includes/nigerian-population-data-mariadb.md}
  \endif
\endif


\endif
