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
\figure{\includepng{\diagramsDir/ceres/ceres-optimized}{60%}}{A blurry image of Ceres taken from the Hubble space telescope. Piazzi first observed the planet while constructing a star catalogue. He was confirming the position of the stars in a second night of observation when he noted one of them was moving. The name planet is originally from the Greek for 'wanderer'.}{ceres-optimized}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/giuseppe-piazzi}{50%}}{Giuseppe Piazzi (1746-1826) was an Italian Catholic priest and an astronomer. Jesuits had been closely involved in education, following their surpression in the Kingdom of Naples and Sicily, Piazzi was recruited as part of a drive to revitalize the University of Palermo. His funding was from King Ferdinand I and enabled him to buy high quality instruments from London.}{giuseppe-piazzi}

\newslide{}

\figure{\includegooglebook{XG43AQAAMAAJ}{PA88}}{Announcement of Giuseppe Piazzi's discovery in the "Monthly Magazine" (also known as the British Register). This announcement is made in August 1801, 7 months after Giuseppe Piazzi first observed Ceres.}{monthly-magazine-ceres-piazzi}

\newslide{Titius-Bode Law}

\notes{The planet's location was a prediction. It was a missing planet, other planets had been found through a formula, a law, that represented their distance from the sun:
$$
a = 0.4 + 0.3 \times 2^m
$$
where $m=-\infty, 0, 1, 2, \dots$.}

\setupcode{import numpy as np}

\code{m = np.asarray([-np.inf, 0, 1, 2, 3, 4, 5, 6])
index = np.asarray(range(len(m)))
planets = ['Mercury', 'Venus', 'Earth', 'Mars', '*', 'Jupiter', 'Saturn', 'Uranus']
a = 0.5 + 0.3*2**m}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(index+1, a, 'rx-', markersize=10, linewidth=2)
for x,y in zip(index, a):
  ax.text(x+1, y+0.5, planets[x], fontsize=18)
ax.set_xlabel('Planets', fontsize=14)
ax.set_ylabel('Distance from Sun in Astronimical Units', fontsize=14)
mlai.write_figure('bodes-law.svg', directory='\writeDiagramsDir/physics')}


\figure{\includediagram{\diagramsDir/physics/bodes-law}{80%}}{The Titius-Bode law was a relatively obscure empirical observation about how the planets are distributed across the solar system. It became well known after the discovery of Uranus by Herschel in 1781 which was found at the location the law predicts for the 8th planet.}{titius-bode-law}

\notes{When [this law](https://en.wikipedia.org/wiki/Titius%E2%80%93Bode_law) was published it fitted all known planets: Mercury, Venus, Earth, Mars, Jupiter and Saturn. Although there was a gap between the fourth and fifth planets (between Mars and Jupiter). In 1781 William Herschel discovered Uranus. It was in the position predicted by the formula. One of the originators of the formula, Johann Elert Bode urged astronomers to search for the missing planet, to be situated between Mars and Jupiter. Franz Xaver von Zach formed the United Astronomical Society, also known as the Celestial Police. But before the celestial police managed to start their search, Piazzi, without even knowing he was a member completed the search. Piazzi first observed the new planet in the early hours of January 1st 1801. He continued to observe it over the next 42 days. Initially he thought it may be a comet, but as he watched it he became convinced he'd found a planet. The international search was over before it started.}

\notes{Unfortunately, there was a problem. Once he'd found the planet, Piazzi promptly lost it. Piazzi was keen not just to discover the planet, but to to be known as the determiner of its orbit. He took observations across the months of January and February, working to find the orbit. Unfortunately, he was unable to pin it down. He became ill, and by the time the dat awas revealed to the wider community through von Zach's journal, Monatlicher Correspondenz, the new planet had been lost behind the sun.}

\newslide{}

\figure{\includegooglebook{JBw4AAAAMAAJ}{PA280}}{Page from the publication *Monatliche Correspondenz* that shows Piazzi's observations of the new planet @Piazzi:monatliche1801
.}{monatliche-correspondenz-piazzi}


<!--[\includepng{\diagramsDir/ceres/ceres-beobachtung-von-piazzi}{100%}](https://play.google.com/books/reader?printsec=frontcover&output=reader&id=JBw4AAAAMAAJ&pg=GBS.PA280)-->

\newslide{}

\speakernotes{Image data ```wget http://server3.sky-map.org/imgcut?survey=DSS2&img_id=all&angle=4&ra=3.5&de=17.25&width=1600&height=1600&projection=tan&interpolation=bicubic&jpeg_quality=0.8&output_type=png```}

\installcode{pods}

\downloadfile{http://server3.sky-map.org/imgcut?survey=DSS2&img_id=all&angle=4&ra=3.5&de=17.25&width=1600&height=1600&projection=tan&interpolation=bicubic&jpeg_quality=0.8&output_type=png,ceresSkyBackground.png}{ceres-sky-background.png}

\setupcode{import pods}

\code{data = pods.datasets.ceres()
right_ascension = data['data']['Gerade Aufstig in Zeit']
declination = data['data']['Nordlich Abweich']}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
A = plt.imread('ceres-sky-background.png')
ax.imshow(image([3.5-4/15 3.5+4/15], [15.25 19.25], A)
ax.plot(right_ascension, declination, 'rx')
ax.set_xlabel('right ascension')
ax.set_ylabel('declination')
ax.set_title('Procession of Ceres through Sky')
mlai.write_figure('ceres-data.svg', directory='\writeDiagramsDir/ceres')}

\notes{<!--dayPrev = -2;
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
    printLatexPlot('ceresData', '../../../ceres/tex/diagrams', 0.9*textWidth)-->
}


\figure{\includediagram{\diagramsDir/ceres/ceres-data}{60%}}{Plot of the declination and right ascension that Piazzi recorded as Ceres passed through the sky in 1800. Gaps are evenings where Piazzi was unable to make an observation.}{ceres-data}

\newslide{}

\notes{Piazzi was able to attempt to predict the orbit because of Kepler's laws of planetary motion. Johannes Kepler had outlined the way in which planets move according to elliptical shapes, and comets move according to parabolic shapes.}

\figure{\includepng{\diagramsDir/ml/godfrey-kneller-isaac-newton-1689}{40%}}{Godfrey Kneller portrait of Isaac Newton}{godfrey-kneller-isaac-newton}

\notes{Later Isaac Newton was able to describe the underlying laws of motion that underpinned Kepler's laws. This was the enlightenment. An age of science and reason driven by reductionist approaches to the natural world. The enlightenment scientists were able to read and understand each other's work through the invention of the printing press. Kepler died in 1630, 12 years before Newton was born in 1642. But Kepler's ideas were able to influence Newton and his peers, and the understanding of gravity became an objective of the nascent Royal Society.}

\notes{The sharing of information in printed form had evolved by the time of Piazzi, and the collected discoveries of the astronomic world were being shared in Franz von Zach's monthly journal. It was here that Piazzi's observations were eventually published, some 7 months after the planet was lost.}

\notes{It was also here that a young German mathematician read about the international hunt for the lost planet. Carl Friedrich Gauss was a 23-year-old mathematician working from Göttingen. He combined Kepler's laws with Piazzi's data to make predictions about where the planet would be found. In doing so, he also developed the method of least squares, and incredibly was able to fit the relatively complex model to the data with a high enough degree of accuracy that astronomers were able to look to the skies to try to recover the planet.}

\notes{Almost exactly one year after it was lost, Ceres was recovered by Franz von Zach. Gauss had combined model with data to make a prediction and in doing so a new planet was discovered [@Gauss:monatliche1801,@Gauss:astronomische02].}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/bendixen-carl-friedrich-gauss-1828}{40%}}{Carl Friedrich Gauss in 1828. He became internationally famous 27 years earlier for recovering the planet Ceres with a mathematical prediction.}{bendixen-carl-friedrich-gauss-1828}


\notes{It is this combination of *model* and *data* that underpins machine learning but notice that here it has also been delivered through a mechanistic understanding of the way the planets move. This understanding is derived from natural laws that are explicitly incorporated into the model. Kepler's laws derive from Newton's mathematical representation of gravity.}

\notes{But there was a problem. The laws don't precisely fit the data.}
\speakernotes{Named ceres because Ceres is strongly associated with Sicily}


\newslide{}

\figure{\includegooglebook{JBw4AAAAMAAJ}{PA647}}{Gauss's prediction of Ceres's orbit as published in Franz von Zach's Monatliche Correspondenz. He gives the location where the planet may be found, and then some mathematics for making other predictions. He doesn't share his method, and this later leads to a priority dispute with Legendre around least-squares, which Gauss used to form the fit}{gauss-ceres-prediction}

\newslide{}

\figure{\includepng{\diagramsDir/ceres/piazzi-cerere}{40%}}{Piazzi achieved his glory after the planet was discovered. Ceres is an agricultural god (in Greek tradition Demeter). She was associated with Sicily, where Piazzi was working when he made the discovery.}{piazzi-cerere}

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

\notes{Unfortunately, the story doesn't end so well for the Titsius-Bode law. In 1846 Neptune was discovered, not in the place predicted by the law (it should be closer to where Pluto was eventually found). And Ceres was found to be merely the largest object in the asteroid belt. It was recategorized as a Dwarf planet.}

\figure{\threeColumns{\includepng{\diagramsDir/ceres/ceres-optimized}{7%}{}{left}}{\includepng{\diagramsDir/ceres/full-moon-2010}{27%}{}{left}}{\includepng{\diagramsDir/ceres/the-earth-seen-from-apollo-17}{100%}{}{left}}}{The surface area of Ceres is 2,850,000 square kilometers, it's a little bigger than Greenland, but quite a lot colder. The moon is about 27% of the width of the Earth. Ceres is 7% of the width of the Earth.}{ceres-moon-earth}

\newslide{}
  
\notes{}
\figure{\includejpg{\diagramsDir/ceres/planets-2008}{80%}}{The location of Ceres as ordered in the solar system. While no longer a planet, Ceres is the unique Dwarf Planet in the inner solar system. This image from http://upload.wikimedia.org/wikipedia/commons/c/c4/Planets2008.jpg}{planets-2008}
  
\newslide{}


\figure{\includejpg{\diagramsDir/ceres/ceres}{60%}}{Ceres as photographed by the Dawn Mission. The photo highlights Ceres's 'bright spots' which are thought to be a material with a high level of reflection (perhaps ice or salt). This image from http://www.popsci.com/sites/popsci.com/files/styles/large_1x_/public/dawn-two-bright-spots.jpg?itok=P5oeSRrc}{ceres}


\endif
