\ifndef{kappenball}
\define{kappenball}

\editme 

\newslide{}

\figure{<div><div style="width:900px;text-align:center;display:inline"><span style="float:left;">Score: <output id="kappenball-score"></output></span>
<span style="float:right;">Energy: <output id="kappenball-energy"></output></span><div style="clear: both;"></div></div>
<canvas id="kappenball-canvas" width="900" height="500" style="border:1px solid black;display:inline;text-align:center "></canvas>
<div><input type="range" min="0" max="100" value="0" class="slider" id="kappenball-stochasticity" style="width:900px;"/></div>
<div><button id="kappenball-newball" style="text-align:right">New Ball</button><button id="kappenball-pause" style="text-align:right">Pause</button></div>
<output id="kappenball-count"></output>
talk-macros.gpp}cripts/includes/kappenball-js.md}
</div>}{Kappen Ball}{kappen-ball}


\endif
