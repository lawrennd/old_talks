### Fragility of AI Systems

\slides{
* They are componentwise built from ML Capabilities.
* Each capability is independently constructed and verified.
    * Pedestrian detection
    * Road line detection
* Important for verification purposes.
}

### Pigeonholing

\includeimg{../slides/diagrams/TooManyPigeons.jpg}{60%}


\notes{The way we are deploying artificial intelligence systems in practice is to build up systems of machine learning components. To build a machine learning system, we decompose the task into parts which we can emulate with ML methods. Each of these parts can be, typically, independently constructed and verified. For example, in a driverless car we can decompose the tasks into components such as "pedestrian detection" and "road line detection". Each of these components can be constructed with, for example, an independent classifier. We can then superimpose a logic on top. For example, "Follow the road line unless you detect a pedestrian in the road". 

This allows for verification of car performance, as long as we can verify the individual components. However, it also implies that the AI systems we deploy are *fragile*.}

### Rapid Reimplementation

\slides{
* Whole systems are being deployed.
* But they change their environment.
* The experience evolved adversarial behaviour.
}

### Early AI

\includeimg{../slides/diagrams/2017-10-12 16.47.34.jpg}{40%}{rotateimg90}

### Machine Learning Systems Design

\includeimg{../slides/diagrams/SteamEngine_Boulton&Watt_1784_neg.png}{50%}

### Adversaries

* Stuxnet
* Mischevious-Adversarial

### Turnaround And Update

* There is a massive need for turn around and update
* A redeploy of the entire system.
    * This involves changing the way we design and deploy.
* Interface between security engineering and machine learning.

### Peppercorns

* A new name for system failures which aren't bugs.
* Difference between finding a fly in your soup vs a peppercorn in
  your soup. 

<!--
### {.slide: data-transition="none"}

<center><video height="600" type="video/mp4"><source src="../slides/diagrams/paolo-peppercorn.mp4" height="80%"></video></center>

### {.slide: data-transition="none"}

<center><video type="video/mp4"><source src="../slides/diagrams/paolo-save.mp4"></video></center>
-->
