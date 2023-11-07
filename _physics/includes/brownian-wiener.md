\ifndef{brownianWiener}
\define{brownianWiener}

\editme


\subsection{Brownian Motion and Wiener}

\notes{Robert Brown was a botanist who was studying plant pollen in 1827 when he noticed a trembling motion of very small particles contained within cavities within the pollen. He worked hard to eliminate the potential source of the movement by exploring other materials where he found it to be continuously present. Thus, the movement was not associated, as he originally thought, with life.}

\notes{In 1905 Albert Einstein produced the first mathematical explanation of the phenomenon. This can be seen as our first model of a ‘curve of a simple molecule of air’. To model the phenomenon Einstein introduced stochasticity to a differential equation. The particles were being peppered with high-speed water molecules, that was triggering the motion. Einstein modelled this as a stochastic process.}


\figure{\includejpg{\diagramsDir/physics/Albert_Einstein_photo_1921}{40%}}{Albert Einstein’s 1905 paper on Brownian motion introduced stochastic differential equations which can be used to model the ‘curve of a simple molecule of air’.}{albert-einstein-photo}

\newslide{}

\notes{Norbert Wiener was a child prodigy, whose father had schooled him in philosophy. He was keen to have his son work with the leading philosophers of the age, so at the age of 18 Wiener arrived in Cambridge (already with a PhD). He was despatched to study with Bertrand Russell but Wiener and Russell didn’t get along. Wiener wasn’t persuaded by Russell’s ideas for theories of knowledge through logic. He was more aligned with Laplace and his desire for a theory of ignorance. In is autobiography he relates it as the first thing he could see his father was proud of (at around the age of 10 or 11) [@Wiener-exprodigy64].}


\figure{\threeColumns{\aligncenter{\includejpg{\diagramsDir/philosophy/Bertrand_Russell_1957}{100%}}\slides{\aligncenter{*Betrand Russell*}}}{\aligncenter{\includejpg{\diagramsDir/physics/Albert_Einstein_photo_1921}{85%}}\slides{\aligncenter{*Albert Einstein*}}}{\aligncenter{\includejpg{\diagramsDir/physics/Norbert_wiener}{100%}}\slides{\aligncenter{*Norbert Wiener*}}}{30%}{30%}{30%}}{Bertrand Russell (1872-1970), Albert Einstein (1879-1955), Norbert Wiener, (1894-1964)}{russell-wiener-russell}

\speakernotes{Wiener came to Cambridge in 1913. Russell showed him Einstein's 1905 paper on Brownian motion (@Einstein-brownian05)}

\notes{But Russell (despite also not getting along well with Wiener) introduced Wiener to Einstein’s works, and Wiener also met G. H. Hardy. He left Cambridge for Göttingen where he studied with Hilbert. He developed the underlying mathematics for proving the existence of the solutions to Einstein’s equation, which are now known as Wiener processes.}

\newslide{Brownian Motion}

\figure{\includegif{\diagramsDir/physics/brownian-motion}{40%}}{Brownian motion of a large particle in a group of smaller particles. The movement is known as a *Wiener process* after Norbert Wiener.}{brownian-motion}

\newslide{Stochasticity and Control}

\figure{\columns{\includejpg{\diagramsDir/physics/Norbert_wiener}{100%}{}{left}}{\includepng{\diagramsDir/books/wiener-yellow-peril}{100%}{}{right}}{45%}{45%}}{Norbert Wiener (1894 - 1964). Founder of cybernetics and the information era. He used Gibbs’s ideas to develop a “theory of ignorance” that he deployed in early communication. On the right is Wiener's wartime report that used stochastic processes in forecasting with applications in radar control (image from @Coales-yellow14).}{norbert-wiener-yellow-peril}

\notes{Wiener himself used the processes in his work. He was focused on mathematical theories of communication. Between the world wars he was based at Massachusetts Institute of Technology where the burgeoning theory of electrical engineering was emerging, with a particular focus on communication lines. Winer developed theories of communication that used Gibbs’s entropy to encode information. He also used the ideas behind the Wiener process for developing tracking methods for radar systems in the second world war. These processes are what we know of now as Gaussian processes (@Wiener:yellow49).}


\endif
