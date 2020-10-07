\ifndef{ceresDiscovery}
\define{ceresDiscovery}

\editme

\notes{\subsection{Discovery of Ceres}

On New Year's Eve in 1800, Giuseppe Piazzi, an Italian Priest, born in Lombardy, but installed in a new Observatory at the University viewed a faint smudge through his telescope.

Piazzi was building a star catalogue. 

Unbeknownst to him, Piazzi was also participating in an international search. One that he'd been volunteered for by the Hungarian astronomer Franz von Zach. But without even knowing that he'd joined the search party, Piazzi had discovered their target a new planet.}


\slides{
\newslide{} 

\figure{\includepng{\diagramsDir/ceres/ceres-optimized-totally-faint}{60%}}{}{ceres-optimized-totally-faint}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/ceres-optimized-extremely-faint}{60%}}{}{ceres-optimized-extremely-faint}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/ceres-optimized-very-faint}{60%}}{}{ceres-optimized-very-faint}

\newslide{}

\figure{}{\includepng{\diagramsDir/ceres/ceres-optimized-faint}{60%}}{}{ceres-optimized-faint}

\newslide{}
}
\figure{\includepng{\diagramsDir/ceres/ceres-optimized}{60%}}{}{ceres-optimized}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/giuseppe-piazzi}{60%}}{}{giuseppe-piazzi}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/monthly-magazine-ceres-piazzi}}{}{monthly-magazine-ceres-piazzi}

\newslide{}

\notes{The planet's location was a prediction. It was a missing planet, other planets had been found through a formula, a law, that represented their distance from the sun:
$$
a = 0.4 + 0.3 \times 2^m
$$
where $m=-\infty, 0, 1, 2, \dots$.

When this law was published it fitted all known planets: Mercury, Venus, Earth, Mars, Jupiter and Saturn. Although there was a gap between the fourth and fifth planets (between Mars and Jupiter). In 1781 William Herschel discovered Uranus. It was located in the position predicted by the formula. One of the originators of the formula, Johann Elert Bode urged astronomers to search for the missing planet, to be situated between Mars and Jupiter. Franz Xaver von Zach formed the United Astronomical Society, also known as the Celestial Police. But before this celestial police managed to start their search, Piazzi, without even knowing he was a member completed the search. Piazzi first observed the new planet in the early hours of January 1st 1801. He continued to observe it over the next .. days. Initially he thought it may be a comet, but as he watched it he became convinced he'd found a planet. The international search was over before it started, only there was a problem. Once he'd found the planet, Piazzi promptly lost it.}

\figure{\includegooglebook{JBw4AAAAMAAJ}{PA280}}{Page from the publication *Monatliche Correspondenz* that shows Piazzi's observations of the new planet @Piazzi:monatliche1801
.}{monatliche-corresondez-piazzi}


<!--[\includepng{\diagramsDir/ceres/ceres-beobachtung-von-piazzi}{100%}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA280)-->

\speakernotes{Image data ```wget http://server3.sky-map.org/imgcut?survey=DSS2&img_id=all&angle=4&ra=3.5&de=17.25&width=1600&height=1600&projection=tan&interpolation=bicubic&jpeg_quality=0.8&output_type=png```}

\code{
    ceresData = load('ceresData.txt');
    rightAscension = ceresData(:, 3);
    declination = ceresData(:, 5);
    clf
    A = imread('../diagrams/ceresSkyBackground.png');
    image([3.5-4/15 3.5+4/15], [15.25 19.25], A)
    hold on
    a = plot(rightAscension, declination, 'x');
    dayPrev = -2;
    for i = 1:size(ceresData, 1)
      day = ceresData(i, 1);
      if day - dayPrev>2
        if ~isnan(rightAscension(i)) && ~isnan(declination(i))
          text(rightAscension(i)+0.025, declination(i), datestr(day, '1801/mm/dd'));
          dayPrev = day;
        end
      end
    end
    set(a, 'color', blueColor, 'markersize', 12)
    set(gca, 'xlim', [3.25 3.75])
    set(gca, 'ylim', [15.5 19])
    xlim = get(gca, 'xlim');
    ylim = get(gca, 'ylim');
    set(gca, 'xtick', [3.25 3.5 3.75])
    set(gca, 'xticklabel', {'$3$h$15^\\prime$', '$3$h$30^\\prime$', '$3$h$45^\\prime$'})
    set(gca, 'ytick', [15.5 16 16.5 17 17.5 18 18.5 19])
    set(gca, 'yticklabel', {'$15^\\circ 30^\\prime$', '$16^\\circ$', '$16^\\circ 30^\\prime$', '$17^\\circ$', '$17^\\circ 30^\\prime$', '$18^\\circ$', '$18^\\circ 30^\\prime$', '$19^\\circ$'})
    set(gca, 'box', 'off')
    validData = find(~isnan(declination));
    times = ceresData(validData, 1);
    axis off
    printLatexPlot('ceresData', '../../../ceres/tex/diagrams', 0.9*textWidth)
}

\newslide{}

\figure{\includediagram{\diagramsDir/ceres/ceres-data}{80%}}{}{ceres-data}

\newslide{}

\figure{\includepng{\diagramsDir/ml/godfrey-kneller-isaac-newton-1689}}{}{Godfrey Kneller portrait of Isaac Newton}{godfrey-kneller-isaac-newton}

\notes{@Gauss:monatliche1801,@Gauss:astronomische02}

\speakernotes{Named ceres because Ceres is strongly associated with Sicily}


\newslide{}

\includegooglebook{JBw4AAAAMAAJ}{PA647}

<!--[\includepng{\diagramsDir/ceres/gauss-ceres-prediction-monatliche}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA647)-->

\newslide{}
<!--trim=0cm 9cm 0cm 12cm, clip=true-->
\includegooglebook{JBw4AAAAMAAJ}{PA647}

<!--[\includepng{\diagramsDir/ceres/gauss-ceres-prediction-monatliche}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA647)-->

\newslide{}

<!---

\includepng{\diagramsDir/ceres/ceres-orbit-gauss}
-->

\newslide{}

\figure{\includepng{\diagramsDir/ceres/bendixen-carl-friedrich-gauss-1828}}{}{bendixen-carl-friedrich-gauss-1828}


<!--

\include{_ml/includes/overdetermined-inaugural.md}

-->

\newslide{}

\figure{\includepng{\diagramsDir/ceres/piazzi-cerere}{60%}}{}{piazzi-cerere}

\speakernotes{Use image of the earth to introduce the unpredictability of the weather. 

http://www.astropa.unipa.it/HISTORY/history.htm

Surface area Ceres 2,850,000 sq km (a little bigger than Greenland, but a lot colder)
Radius Ceres 487.3 (at equator)
Radius 1,738.14
Radius  6,378.1
Moon is 0.273 earths wide.
Ceres is 0.0764 earths wide.
}

\newslide{}
  
\figure{\centerdiv{\includeimg{\diagramsDir/ceres/ceres-optimized.png}{3.82%}{}{left}
\includeimg{\diagramsDir/ceres/full-moon-2010.png}{13.65%}{}{left}
\includeimg{\diagramsDir/ceres/the-earth-seen-from-apollo-17.png}{50%}{}{left}}}{The surface area of Ceres is 2,850,000 square kilometers, it's a little bigger than Greenland, but quite a lot colder. The moone is about 27% of the width of the Earth. Ceres is 7% of the width of the Earth.}{ceres-moon-earth}

\newslide{}
  

\figure{\includejpg{\diagramsDir/ceres/planets-2008}{}}{This image from http://upload.wikimedia.org/wikipedia/commons/c/c4/Planets2008.jpg}{planets-2008}
  
\newslide{}


\figure{\includejpg{\diagramsDir/ceres/ceres}{60%}}{This image from http://www.popsci.com/sites/popsci.com/files/styles/large_1x_/public/dawn-two-bright-spots.jpg?itok=P5oeSRrc}{ceres}


\endif
