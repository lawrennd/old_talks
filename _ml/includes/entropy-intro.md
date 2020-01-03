\ifndef{entropyIntro}
\define{entropyIntro}


\include{_ml/includes/laplace-portrait.md}
\include{_ai/includes/laplaces-determinism.md}

\editme

\newslide{}

\figure{\includejpg{../slides/diagrams/ml/daniel-bernoulli}}{Daniel Bernoulli 1700-1782 Pressure from a gas is given by velocity of gas acting on sides (but constant velocity).}{daniel-bernoulli}

\newslide{}

\figure{\includepng{../slides/diagrams/ml/entropy-billiards}}{Bernoulli's simple kinetic models of gases assume that the molecules of air operate like billiard balls.}{entropy-billiards}

\newslide{}

\code{
    a = randn(10000, 1);
    [heights, centres] = hist(a, 20);
    a = bar(centres, heights/sum(heights)/(centres(2)-centres(1)));
    set(a, 'facecolor', blueColor);
    xlim = [-4 4];
    set(gca, 'xlim', xlim);
    ylim = get(gca, 'ylim');
    
    x = linspace(xlim(1), xlim(2), 200);
    y = 1/sqrt(2*pi)*exp(-1/2*x.*x);
    line(x, y, 'color', redColor, 'linewidth', 3);
    line([xlim(1) xlim(1)], ylim, 'color', blackColor);
    line(xlim, [ylim(1) ylim(1)], 'color', blackColor);
    printLatexPlot('gaussian-histogram', '../slides/diagrams/ml', 0.75*textWidth)}

\newslide{}

\figure{\inputdiagram{../slides/diagrams/ml/gaussian-histogram}}}{James Clerk Maxwell 1831-1879 Derived distribution of velocities of particles in an ideal gas (elastic fluid).}{gaussian-histogram}

\newslide{}

\figure{\includepng{../slides/diagrams/ml/james-clerk-maxwell}{30%}{}{left}\includejpg{../slides/diagrams/ml/boltzmann2}{30%}{}{center}\includejpg{../slides/diagrams/ml/j-w-gibbs}{30%}{}{right}}{James Clerk Maxwell (1831-1879), Ludwig Boltzmann (1844-1906) Josiah Willard Gibbs (1839-1903)}{maxwell-boltzmann-gibbs}

\newslide{}

\figure{\includejpg{../slides/diagrams/ml/arthur-stanley-eddington}{40%}{}{left}\includepng{../slides/diagrams/ml/natureofphysical00eddi_7}{40%}{}{right}}{Arthur Stanley Eddington () book on the Nature of the Physical World [@Eddington:nature29]}{eddington-book}

<!--\includegraphics[page=7,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}-->

\newslide{}

\figure{\includepng{../slides/diagrams/ml/natureofphysical00eddi_100}{40%}{}{left}\includepng{../slides/diagrams/ml/ChandraNobel}{40%}{}{right}}{Chandrasekhar (1910-1995)}{physical-world-chandra}

<!--\includegraphics[page=100,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}-->
\newslide{}

\figure{\includepng{../slides/diagrams/ml/natureofphysiccal00eddi_100_cropped}{60%}}{@Eddington:nature29}{deepest-humiliation-eddington-cropped}

<!--\includegraphics[page=100,width=\textwidth,trim=0cm 3.5cm 0cm 10.4cm, clip=true]{../slides/diagrams/ml/natureofphysical00eddi.pdf}-->

\newslide{}

\figure{\includejpg{../slides/diagrams/ml/claude-shannon}{40%}{}{left}\includejpg{../slides/diagrams/ml/e-t-jaynes}{40%}{}{right}}{Claude Shannon (died 2001) and Edwin Thompson Jaynes @Jaynes:gibbs65}{shannon-jaynes}

\notes{Shannon image source: http://www.gstatic.com/hostedimg/a23c741096cdf969_large}

\newslide{}

\figure{\includejpg{../slides/diagrams/ml/bert-kappen}}{Bert Kappen}{bert-kappen}
<http://videolectures.net/aispds08_kappen_easop/>
  
\newslide{}

\figure{\includepng{../slides/diagrams/ml/kappen-ball}}{Kappen Ball}{kappen-ball}

\endif

