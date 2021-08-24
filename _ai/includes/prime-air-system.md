\ifndef{primeAirSystem}
\define{primeAirSystem}

\editme

\subsection{Prime Air}

\notes{One project where the components of machine learning and the physical world come together is Amazon's Prime Air drone delivery system.}

\notes{Automating the process of moving physical goods through autonomous vehicles completes the loop between the 'bits' and the 'atoms'. In other words, the information and the 'stuff'. The idea of the drone is to complete a component of package delivery, the notion of last mile movement of goods, but in a fully autonomous way.}

\centerdiv{\gurKimchiPicture{15%}\paulViolaPicture{15%}\davidMoroPicture{15%}}

\include{_supply-chain/includes/amazon-drone-flight.md}

\notes{As Jeff Wilke (CEO of Amazon Retail)
[announced in June 2019](https://blog.aboutamazon.com/transportation/a-drone-program-taking-flight)
the technology is ready, but still needs operationalization including e.g. regulatory approval.}

\newslide{}

\figure{\includeyoutube{wa8DU-Sui8Q}{600}{450}{3767}}{Jeff Wilke (CEO Amazon Consumer) announcing the new drone at the Amazon 2019 re:MARS event alongside the scale of the Amazon supply chain.}{jeff-wilke-remars}


\notes{
> When we announced earlier this year that we were evolving our Prime
> two-day shipping offer in the U.S. to a one-day program, the
> response was terrific. But we know customers are always looking for
> something better, more convenient, and there may be times when
> one-day delivery may not be the right choice. Can we deliver
> packages to customers even faster? We think the answer is yes, and
> one way we’re pursuing that goal is by pioneering autonomous drone
> technology.
}

\notes{
> Today at Amazon’s re:MARS Conference (Machine Learning, Automation,
> Robotics and Space) in Las Vegas, we unveiled our latest Prime Air
> drone design. We’ve been hard at work building fully electric drones
> that can fly up to 15 miles and deliver packages under five pounds
> to customers in less than 30 minutes. And, with the help of our
> world-class fulfillment and delivery network, we expect to scale
> Prime Air both quickly and efficiently, delivering packages via
> drone to customers within months.
}

\notes{The 15 miles in less than 30 minutes implies air speed velocities of around 50 kilometers per hour.} 

\notes{
> Our newest drone design includes advances in efficiency, stability
> and, most importantly, in safety. It is also unique, and it advances
> the state of the art. How so? First, it’s a hybrid design. It can do
> vertical takeoffs and landings – like a helicopter. And it’s
> efficient and aerodynamic—like an airplane. It also easily
> transitions between these two modes—from vertical-mode to airplane
> mode, and back to vertical mode.
}

\notes{
> It’s fully shrouded for safety. The shrouds are also the wings,
> which makes it efficient in flight.
}

\newslide{}

\figure{\includejpg{\diagramsDir/ai/amazon-prime-air-remars-june-2019}{80%}}{Picture of the drone from Amazon Re-MARS event in 2019.}{amazon-prime-air-remars}

\comment{
> The distinctive aircraft is controlled with six degrees of freedom,
> as opposed to the standard four. This makes it more stable, and
> capable of operating safely in more gusty wind conditions.

> We know customers will only feel comfortable receiving drone
> deliveries if they know the system is incredibly safe. So we’re
> building a drone that isn’t just safe, but independently safe, using
> the latest artificial intelligence (AI) technologies.

> What does that mean? Here’s one way to think about it: Some drones
> are autonomous but not able to react to the unexpected, relying
> simply on communications systems for situational awareness. If our
> drone’s flight environment changes, or the drone‘s mission commands
> it to come into contact with an object that wasn’t there
> previously—it will refuse to do so—it is independently safe.  Let me
> explain by considering two of the drone’s main delivery stages: In
> transit to a destination, and when approaching the ground.
}

\notes{
> Our drones need to be able to identify static and moving objects
> coming from any direction. We employ diverse sensors and advanced
> algorithms, such as multi-view stereo vision, to detect static
> objects like a chimney. To detect moving objects, like a paraglider
> or helicopter, we use proprietary computer-vision and machine
> learning algorithms.
}

\comment{
> For the drone to descend for delivery, we need a small area around
> the delivery location that is clear of people, animals, or
> obstacles. We determine this using a stereo-vision based depth map in
> parallel with sophisticated AI algorithms trained to detect people
> and animals from above.
}

\notes{
> A customer’s yard may have clotheslines, telephone wires, or
> electrical wires. Wire detection is one of the hardest challenges
> for low-altitude flights. Through the use of computer-vision
> techniques we’ve invented, our drones can recognize and avoid wires
> as they descend into, and ascend out of, a customer’s yard.
}

\comment{
> We’re also thrilled about the potential environmental impact. Prime
> Air is one of many sustainability initiatives to help achieve
> Shipment Zero, the company’s vision to make all Amazon shipments net
> zero carbon, with 50% of all shipments net zero by 2030. When it
> comes to emissions and energy efficiency, an electric drone, charged
> using sustainable means, traveling to drop off a package is a vast
> improvement over a car on the road. Today, most of us run to the
> store because we need an item now. With a service like Prime Air,
> we’ll be able to order from home and stay home. This saves
> tremendously on fuel usage and reduces emissions.
}


\endif
