\ifndef{connectionistRevival}
\define{connectionistRevival}

\editme

\subsection{The Connectionists}

\notes{By the early 1980s, some disillusionment was creeping into the artificial intelligence agenda that stemmed from the Dartmouth Meeting. At the same time, an emerging group was re-examining the ideas of the Cyberneticists. This group became known as the connectionists, because of their focus on neural network models with their myriad of connections.}

\notes{By the second half of the decade, some of their principles had come together to form a movement. Meetings including the Snowbird Workshop, Neural Informaton Processing Systems and the connectionist summer school provided a venue for these researchers to come together.}

\figure{\includejpg{\diagramsDir/ml/connectionist-summer-school}{100%}}{Group photo from the 1986 Connectionists' Summer School, held at CMU in July. Included in the photo are Richard Durbin, Terry Sejnowski, Geoff Hinton, Yann LeCun, Michael I. Jordan.}

\notes{This was also the era of cheap(er) computing. Connectionists were able to implement *simulators* of neural networks in *minicomputers* such as DEC's PDP-11 series. These allowed new architectures to be tried. Among them was backpropagation, popularised by the "Parallel Distributed Processing" books [Rumelhart:book86], these books formed the canonical ideas on which the connectionists based their research.}

\notes{
> What makes people smarter than machines? They certainly are not
> quicker or more precise. Yet people are far better at perceiving
> objects in natural scenes and noting their relations, at understanding
> language and retrieving contextually appropriate information from
> memory, at making plans and carrying out contextually appropriate
> actions, and at a wide range of other natural cognitive tasks. People
> are also far better at learning to do these things more accurately and
> fluently through processing experience.
>
> What is the basis for these differences? One answer, perhaps the
> classic one we might expect from artificial intelligence, is
> "software." If we only had the right computer program, the argument
> goes, we might be able to capture the fluidity and adaptability of
> human information processing.
>
> Certainly this answer is partially correct. There have been great
> breakthroughs in our understanding of cognition as a result of the
> development of expressive high-level computer languages and powerful
> algorithms. No doubt there will be more such breakthroughs in the
> future. However, we do not think that software is the whole story.
>
> In our view, people are smarter than today's computers because the
> brain employs a basic computational architecture that is more suited
> to deal with a central aspect of the natural information processing
> tasks that people are so good at.
>
> J. L. McClelland, David E. Rumelhart and Geoffrey E. Hinton in
> *Parallel Distributed Processing,* @Rumelhart:book86
}

\newslide{}

\figure{\includejpg{\diagramsDir/ml/pdp_cover}{40%}}{Cover of the Parallel Distributed Processing edited volume [@Rumelhart:book86].}{pdp-volume-1}

\speakernotes{What makes people smarter than computers? These volumes by a pioneering neurocomputing group suggest that the answer lies in the massively parallel architecture of the human mind. They describe a new theory of cognition called connectionism that is challenging the idea of symbolic computation that has traditionally been at the center of debate in theoretical discussions about the mind.}

\notes{This led to the second wave of neural network architectures. A new journal, *Neural Computation* was launched in 1989 to cater for this new field. It's first volume contained a new architecture: the convolutional neural networks [@LeCun:zip89], developed for recognising hand written digits. It made the cover.}

\newslide{}

\figure{\includejpg{\diagramsDir/ml/nc_cover}{40%}}{Cover of *Neural Computation*, Volume 1, Issue 4 containing @LeCun:zip89. The cover shows examples from the U.S. Postal Service data set of handwritten digits.}{nc-cover-lecun}

\speakernotes{The first several stages of processing in our previous system (described in Denker et al. 1989) involved convolutions in which the coefficients had been laboriously hand designed. In the present system, the first two layers of the network are constrained to be convolutional, but the system automatically learns the coefficients that make up the kernels. }

\notes{It's worth noting what compute and data that LeCun and collaborators had avaialble. Experiments were run on a SUN-4/260, with a CPU running at 16.67 MHz and 128 MB of RAM. It's an impressive machine for the day. The neural network had just under 10,000 parameters and the training data consisted of 7,291 digitized training images on a 16 x 16 grid, 2007 images were retained for testing. The model had a 5% error rate on the test data.}

\notes{
> The first several stages of processing in our previous system (described in Denker et al. 1989) involved convolutions in which the coefficients had been laboriously hand designed. In the present system, the first two layers of the network are constrained to be convolutional, but the system automatically learns the coefficients that make up the kernels. 
>
> Section 5.1 in @LeCun:zip89
}

\notes{The second half of the 1980s and the 1990s were a period of growth and innovation for the community. Recurrent neural networks that operated through time were produced including in 1997, the Long Short-Term Memory architecture [@Hochreiter-lstm97], a form of recurrent neural network that can deal with sequence data.}

\endif
