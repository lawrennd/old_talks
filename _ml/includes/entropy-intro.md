\ifndef{entropyIntro}
\define{entropyIntro}


\include{_ml/includes/laplace-portrait.md}

\editme

\newslide{}

\includepdf{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{16}{80%}{}

\newslide{}

\includepdfclip{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{0cm 6cm 0cm 3.2cm}{16}{80%}{}

\newslide{}
  
\includepdf{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{18}{80%}{}

\notes{@Laplace:essai14}

\newslide{}

\includepdfclip{../slides/diagrams/ml/philosophicaless00lapliala.pdf}{0cm 6cm 0cm 5cm}{18}{80%}{}

\notes{Daniel Bernoulli 1700-1782 Pressure from a gas is given by velocity of gas acting on sides (but constant velocity).}

\newslide{}

\includejpg{../slides/diagrams/ml/daniel-bernoulli}

\newslide{}

\includepng{../slides/diagrams/ml/entropy-billiards}

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

\centerline{\inputdiagram{../slides/diagrams/ml/gaussian-histogram}}

\notes{James Clerk Maxwell 1831-1879 Derived distribution of velocities of particles in an ideal gas (elastic fluid).}

\newslide{}

\includepng{../slides/diagrams/ml/james-clerk-maxwell}{30%}{}{left}\includejpg{../slides/diagrams/ml/boltzmann2}{30%}{}{center}\includejpg{../slides/diagrams/ml/j-w-gibbs}{30%}{}{right}

\notes{Ludwig Boltzmann 1844-1906 

Josiah Willard Gibbs 1839-1903

Arthur Stanley Eddington 1882-1944}

\newslide{}

\includejpg{../slides/diagrams/ml/arthur-stanley-eddington}{40%}{}{left}\includegraphics[page=7,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}}
  \centerline{\includegraphics[page=100,height=0.5\textheight]{../slides/diagrams/ml/natureofphysical00eddi.pdf}\includegraphics[page=100,height=0.5\textheight]{../slides/diagrams/ml/ChandraNobel.png}}

\newslide{}

\centerline{\includegraphics[page=100,width=\textwidth,trim=0cm 3.5cm 0cm 10.4cm, clip=true]{../slides/diagrams/ml/natureofphysical00eddi.pdf}}
\notes{@Eddington:nature29}

\notes{Edwin Thompson Jaynes & Shannon (died 2001)}

\newslide{}

\includejpg{../slides/diagrams/ml/claude-shannon}{40%}{}{left}\includejpg{../slides/diagrams/ml/e-t-jaynes}{40%}{}{right}

\notes{Shannon image source: http://www.gstatic.com/hostedimg/a23c741096cdf969_large}

\notes{@Jaynes:gibbs65}

\newslide{}

\includejpg{../slides/diagrams/ml/bert-kappen}
<http://videolectures.net/aispds08_kappen_easop/>
  
\notes{Bert Kappen http://videolectures.net/aispds08_kappen_easop/}

\newslide{}

\includepng{../slides/diagrams/ml/kappen-ball}

\endif
