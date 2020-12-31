\ifndef{maxwellsDemon}
\define{maxwellsDemon}

\editme 

\subsection{Maxwell's Demon}

\includegooglebook{0p8AAAAAMAAJ}{PA308}

\newslide{}

\figure{<div>
<canvas id="maxwell-canvas" width="900" height="500" style="border:1px solid black;display:inline;text-align:center "></canvas>
<div><button id="maxwell-newball" style="text-align:right">New Ball</button><button id="maxwell-pause" style="text-align:right">Pause</button></div>
\include{_scripts/includes/maxwell-js.md}
</div>}{Maxwell's Demon. The demon decides balls are either cold (blue) or hot (red) according to their velocity. Balls are allowed to pass the green membrane from right to left only if they are cold, and from left to right, only if they are hot.}{maxwells-demon}


\notes{Maxwell's demon allows us to connect thermodynamics with information theory (see e.g. @Hosoya-demon15;@Hosoya-maxwell11;@Bub-maxwell01;@Brillouin-maxwell51;@Szilard-intelligenter29). The connection arises due to a fundamental connection between information erasure and energy consumption @Landauer-irreversibility61.}

\notes{@Alemi-therml18}

\endif
