
###

\includeimg{../slides/diagrams/ml/pierre-simon-laplace.png}

###

\includepdf{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{16}{80%}{}

###

\includepdfclip{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{0cm 6cm 0cm 3.2cm}{16}{80%}{}

###
  
\includepdf{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{18}{80%}{}


\notes{@Laplace:essai14}

###

\includepdfclip{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{0cm 6cm 0cm 5cm}{18}{80%}{}

\notes{Daniel Bernoulli 1700-1782 Pressure from a gas is given by velocity of gas acting on sides (but constant velocity).}


###

\includeimg{../slides/diagrams/ml/daniel-bernoulli.jpg}

###

\includeimg{../slides/diagrams/ml/entropy-billiards.png}

###
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

###

\centerline{\inputdiagram{../slides/diagrams/ml/gaussian-histogram}}

\notes{James Clerk Maxwell 1831-1879 Derived distribution of velocities of particles in an ideal gas (elastic fluid).}

###

\includeimg{../slides/diagrams/ml/james-clerk-maxwell.png}{30%}{}{left}\includeimg{../slides/diagrams/ml/boltzmann2.jpg}{30%}{}{center}\includeimg{../slides/diagrams/ml/j-w-gibbs.jpg}{30%}{}{right}



\notes{Ludwig Boltzmann 1844-1906 

Josiah Willard Gibbs 1839-1903

Arthur Stanley Eddington 1882-1944}

###

\includeimg{../slides/diagrams/ml/arthur-stanley-eddington.jpg}{40%}{}{left}\includegraphics[page=7,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}}
  \centerline{\includegraphics[page=100,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}\includegraphics[page=100,height=0.5\textheight]{../slides/diagrams/ml/ChandraNobel.png}}

###

\centerline{\includegraphics[page=100,width=\textwidth,trim=0cm 3.5cm 0cm 10.4cm, clip=true]{../slides/diagrams/ml/natureofphysical00eddi.pdf}}
\notes{@Eddington:nature29}

\notes{Edwin Thompson Jaynes & Shannon (died 2001)}

###

\includeimg{../slides/diagrams/ml/claude-shannon.jpg}{40%}{}{left}\includeimg{../slides/diagrams/ml/e-t-jaynes.jpg}{40%}{}{right}

\notes{Shannon image source: http://www.gstatic.com/hostedimg/a23c741096cdf969_large}

\notes{@Jaynes:gibbs65}

###

\includeimg{../slides/diagrams/ml/bert-kappen.jpg}
<http://videolectures.net/aispds08_kappen_easop/>
  
\notes{Bert Kappen http://videolectures.net/aispds08_kappen_easop/}

###

\includeimg{../slides/diagrams/ml/kappen-ball.png}

