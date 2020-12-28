\ifndef{kappenball}
\define{kappenball}

\editme 

\newslide{}

\figure{  <div><div style="width:900px;text-align:center;display:inline"><span style="float:left;">Score: <output id="scoreBox"></output></span>
<span style="float:right;">Energy: <output id="energyBox"></output></span><div style="clear: both;"></div></div>
<canvas id="kappenballCanvas" width="900" height="500" style="border:1px solid black;display:inline;text-align:center "></canvas>
<input type="range" min="0" max="100" value="0" class="slider" id="stochasticityRange" style="width:900px;"/>
<div><button id="newballButton" style="text-align:right">New Ball</button><button id="pauseButton" style="text-align:right">Pause</button></div>
<output id="ballCountBox"></output>
<script src="\scriptsDir/ballworld/constructors.js"></script>
<script src="\scriptsDir/ballworld/script2.js"></script>
<script src="\scriptsDir/ballworld/ballworld.js"></script>
<script src="\scriptsDir/ballworld/kappenball.js"></script>
<script src="\scriptsDir/ballworld/ballbuttons.js"></script>
</div>}{Kappen Ball}{kappen-ball}


\endif
