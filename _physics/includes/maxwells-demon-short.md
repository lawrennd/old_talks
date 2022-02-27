\ifndef{maxwellsDemonShort}
\define{maxwellsDemonShort}

\editme

\subsection{Maxwell's Demon}

\figure{\includediagramclass{\diagramsDir/physics/maxwells-demon}{100%}}{Maxwell's demon opens and closes a door which allows fast particles to pass from left to right and slow particles to pass from right to left. This makes the left hand side colder than the right.}{maxwells-demon}

\newslide{}

\figure{
<div>
<div style="width:68%;float:left">
  <canvas id="maxwell-canvas" width="700" height="500" style="border:1px solid black;display:inline;text-align:left"></canvas>
</div>
<div style="width:28%;float:right;margin:auto">
  <div style="float:right;width:100%;margin:auto">Entropy: <output id="maxwell-entropy"></output></div>
  <div id="maxwell-histogram-canvas" style="width:300px;height:250px;display:inline-block;text-align:right;margin:auto">
  </div>
</div>
</div>
<div>
<button id="maxwell-newball" style="text-align:right">New Ball</button>
<button id="maxwell-pause" style="text-align:right">Pause</button>
<button id="maxwell-skip" style="text-align:right">Skip 1000s</button>
<button id="maxwell-histogram" style="text-align:right">Histogram</button>
</div>

talk-macros.gpp}cripts/includes/maxwell-js.md}
}{Maxwell's Demon. The demon decides balls are either cold (blue) or hot (red) according to their velocity. Balls are allowed to pass the green membrane from right to left only if they are cold, and from left to right, only if they are hot.}{maxwells-demon}

\endif