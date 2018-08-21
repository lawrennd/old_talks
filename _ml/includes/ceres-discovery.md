\notes{### Discovery of Ceres

Year is 1801 Planet Ceres discovered in January by Giuseppe Piazzi, an italian priest, born in Lombardy, but working in Palermo, where he founded the observatory. He was later to die in Naples.}


\slides{
###  {data-transition="none"} 

\includeimg{../slides/diagrams/ceres/ceres-optimized-totally-faint.png}

###  {data-transition="none"}

\includeimg{../slides/diagrams/ceres/ceres-optimized-extremely-faint.png}

###  {data-transition="none"}

\includeimg{../slides/diagrams/ceres/ceres-optimized-very-faint.png}

###  {data-transition="none"}

\includeimg{../slides/diagrams/ceres/ceres-optimized-faint.png}

###  {data-transition="none"}
}
\includeimg{../slides/diagrams/ceres/ceres-optimized.png}

###

\includeimg{../slides/diagrams/ceres/giuseppe-piazzi.png}

###

\includeimg{../slides/diagrams/ceres/monthly-magazine-ceres-piazzi.png}

###

\includegooglebook{JBw4AAAAMAAJ}{PA280}
@Piazzi:monatliche1801

<!--[\includeimg{../slides/diagrams/ceres/ceres-beobachtung-von-piazzi.png}{100%}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA280)-->

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

###

\includesvg{../slides/diagrams/ceres/ceres-data.svg}

###

\includeimg{../slides/diagrams/ceres/godfrey-kneller-isaac-newton-1689.png}

\notes{@Gauss:monatliche1801,@Gauss:astronomische02}

\speakernotes{Named ceres because Ceres is strongly associated with Sicily}


###

\includegooglebook{JBw4AAAAMAAJ}{PA647}

<!--[\includeimg{../slides/diagrams/ceres/gauss-ceres-prediction-monatliche.png}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA647)-->

###
trim=0cm 9cm 0cm 12cm, clip=true
\includegooglebook{JBw4AAAAMAAJ}{PA647}
[\includeimg{../slides/diagrams/ceres/gauss-ceres-prediction-monatliche.png}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA647)

###

<!---

\includeimg{../slides/diagrams/ceres/ceres-orbit-gauss.png}
-->

###

\includeimg{../slides/diagrams/ceres/bendixen-carl-friedrich-gauss-1828.png}


<!--

\include{_ml/includes/overdetermined-inaugural.md}

-->

###

\includeimg{../slides/diagrams/ceres/piazzi-cerere.png}

\speakernotes{Use image of the earth to introduce the unpredictability of the weather. 

http://www.astropa.unipa.it/HISTORY/history.htm

Surface area Ceres 2,850,000 sq km (a little bigger than Greenland, but a lot colder)
Radius Ceres 487.3 (at equator)
Radius 1,738.14
Radius  6,378.1
Moon is 0.273 earths wide.
Ceres is 0.0764 earths wide.
}

###
  
\includeimg{../slides/diagrams/ceres/ceres-optimized.png}{3.82%}
\includeimg{../slides/diagrams/ceres/full-moon-2010.png}{13.65%}
\includeimg{../slides/diagrams/ceres/the-earth-seen-from-apollo-17.png}{50%}

###
  
\notes{This image from http://upload.wikimedia.org/wikipedia/commons/c/c4/Planets2008.jpg}

\includeimg{../slides/diagrams/ceres/planets-2008.jpg}
  
###

\notes{This image from http://www.popsci.com/sites/popsci.com/files/styles/large_1x_/public/dawn-two-bright-spots.jpg?itok=P5oeSRrc}

\includeimg{../slides/diagrams/ceres/ceres.jpg}



