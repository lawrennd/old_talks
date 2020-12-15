\ifndef{kappenball}
\define{kappenball}

\editme 

\newslide{}

\figure{<div>
<canvas id="kappenballCanvas" width="900" height="500" style="border:1px solid black;display: block; "></canvas>
<input type="range" min="0" max="100" value="0" class="slider" id="stochasticityRange"/>
<output id="scoreBox"></output>
<output id="ballCountBox"></output>
<output id="energyBox"></output>

<script src="\scriptsDir/ballworld/constructors.js"></script>
<script src="\scriptsDir/ballworld/script2.js"></script>
<script src="\scriptsDir/ballworld/ballworld.js"></script>
<script src="\scriptsDir/ballworld/kappenball.js"></script>
</div>}{Kappen Ball}{kappen-ball}

<!--\includepng{\diagramsDir/ml/kappen-ball}-->

\endif
