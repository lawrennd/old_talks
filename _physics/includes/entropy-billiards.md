\ifndef{entropyBilliards}
\define{entropyBilliards}

\editme

\subsection{Entropy Billiards}

\figure{
<div>
<div style="width:68%;float:left">
  <canvas id="multiball-canvas" width="700" height="500" style="border:1px solid black;display:inline;text-align:left "></canvas>
</div>
<div style="width:28%;float:right;margin:auto">
  <div style="float:right;width:100%;margin:auto">Entropy: <output id="multiball-entropy"></output></div>
  <div id="multiball-histogram-canvas" style="width:300px;height:250px;display:inline-block;text-align:right;margin:auto">
  </div>
</div>
</div>
<div>
<button id="multiball-newball" style="text-align:right">New Ball</button>
<button id="multiball-pause" style="text-align:right">Pause</button>
<button id="multiball-skip" style="text-align:right">Skip 1000s</button>
<button id="multiball-histogram" style="text-align:right">Histogram</button>
</div>

\include{_scripts/includes/multiball-js.md}}{Bernoulli's simple kinetic models of gases assume that the molecules of air operate like billiard balls.}{entropy-billiards-js}


\endif
