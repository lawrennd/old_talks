---
title: The Rise of the Algorithm
venue: The Guardian Changing Media Summit
layout: slides
date: 2017-03-16
author: Neil D. Lawrence
affiliation: Amazon and University of Sheffield
---

### The Guardian Changing Media Summit
### 2017-03-16
### Neil D. Lawrence
### Amazon and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-03-16-rise-of-the-algorithm.slides.html 2017-03-16-rise-of-the-algorithm.md
-->


## 

<img src="./diagrams/alphagonature.jpg" align="center" width="50%" style="background:none; border:none; box-shadow:none;">

## {.slide: data-transition="none"}

<table width="100%" border="0" rules=none>
<tr>
<td style="text-align: center; vertical-align:middle;" width="50%">
<img src="./diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="70%"
style="background:none; border:none; box-shadow:none; text-align: center; vertical-align:middle;">
</td>
<td style="text-align: center; vertical-align:middle;" width="50%">
<table  style="border: none; rules: none">
<tr><td style="text-align: center; vertical-align:middle;">~10 gigaflops</td></tr>
<tr><td style="text-align: center; vertical-align:middle;">~1 gigbit/s</td></tr>
</table>
</td>
</tr>
<tr>
<td style="text-align: center; vertical-align:middle;" width="50%">
<img src="./diagrams/ClaudeShannon_MFO3807.jpg" width="50%"
style="background:none; border:none; box-shadow:none; text-align: center; vertical-align:middle;">
</td>
<td  style="text-align: center; vertical-align:middle;">
<table  border="0">
<tr><td style="text-align: center; vertical-align:middle;">~ 1000 teraflops?</td></tr>
<tr><td style="text-align: center; vertical-align:middle;"> ~100 bits/s?</td></tr>
</table>
</td>
</tr>
</table>

## {.slide: data-transition="none"}

<table width="100%" border="0" rules=none>
<tr>
<td style="text-align: center; vertical-align:middle;" width="50%">
<img src="./diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="70%"
style="background:none; border:none; box-shadow:none; text-align: center; vertical-align:middle;">
</td>
<td style="text-align: center; vertical-align:middle;" width="50%">
10
</td>
</tr>
<tr>
<td style="text-align: center; vertical-align:middle;" width="50%">
<img src="./diagrams/ClaudeShannon_MFO3807.jpg" width="50%"
style="background:none; border:none; box-shadow:none; text-align: center; vertical-align:middle;">
</td>
<td  style="text-align: center; vertical-align:middle;">
~ 10<sup>13</sup>
</td>
</tr>
</table>

## {.slide: data-transition="none"}

<img src="./diagrams/640px-Marcel_Renault_1903.jpg" align="center" width="70%" style="background:none; border:none; box-shadow:none;">

## {.slide: data-transition="none"}

<img src="./diagrams/Caleb_McDuff_WIX_Silence_Racing_livery.jpg" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<img src="./diagrams/George-peabody-library.jpg" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/Hilbert_InfoGrowth_neg.svg">
</object>


## {.slide: data-transition="none"}

<img src="./diagrams/20160609_132315.jpg" align="center" width="70%" style="background:none; border:none;box-shadow:none;" class="rotateimg90">

## {.slide: data-transition="none"}

<img src="./diagrams/20160609_132338.jpg" align="center" width="70%" style="background:none; border:none;box-shadow:none;" class="rotateimg90">

## {.slide: data-transition="none"}

<img src="./diagrams/rapid-diagnosis-and-consultation-save-lives.png" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg ">
</object>


## {.slide: data-transition="none"}

<img src="./diagrams/Elephantboyposter.jpg" align="center" width="50%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<img src="./diagrams/Hodder-stoughton-1918-the-new-revelation.jpg" align="center" width="50%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<p style="text-align:center;font-size: 0.5em;">Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected layers.</p>

<img src="./diagrams/deepface_neg.png" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

<p style="text-align:right; font-size: 0.5em;">Source: DeepFace</p>

## {.slide: data-transition="none"}

<p style="text-align:center;">$g(\mathbf{x})$</p>
<img src="./diagrams/deepface_neg.png" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">
<p style="text-align:center;font-size:0.7em">$f_{1}(\cdot)$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$f_{2}(\cdot)$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
$f_3(\cdot)$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$f_4(\cdot)$&nbsp;&nbsp;$f_5(\cdot)$&nbsp;&nbsp;&nbsp;&nbsp;$f_6(\cdot)$&nbsp;&nbsp;$f_7(\cdot)$&nbsp;&nbsp;
$f_8(\cdot)$&nbsp;&nbsp;$f_9(\cdot)$&nbsp;&nbsp;$f_{10}(\cdot)$</p>

<p style="text-align:center;">$$g(\mathbf{x}) = f_{10}\left(f_{9}\left(f_{8}\left(f_{7}\left(f_{6}\left(f_{5}\left(f_{4}\left(f_{3}\left(f_{2}\left(f_{1}\left(\mathbf{x}\right)\right)\right)\right)\right)\right)\right)\right)\right)\right)$$ </p>

## {.slide: data-transition="none"}

<table width="100%">
<tr><td width="10%" style="text-align:center;
vertical-align:middle">$$f_1(\mathbf{x})$$ $$f_2(\cdot)$$
$$f_3(\cdot)$$</td><td  style="text-align:center; vertical-align:middle"><object type="image/svg+xml" data="./diagrams/pinball-initial.svg">
</object>
</td></tr>
</table>

## {.slide: data-transition="none"}

<table width="100%">
<tr><td width="10%" style="text-align:center;
vertical-align:middle">$$f_1(\mathbf{x})$$ $$f_2(\cdot)$$
$$f_3(\cdot)$$</td><td  style="text-align:center; vertical-align:middle"><object type="image/svg+xml" data="./diagrams/pinball-final.svg">
</object>
</td></tr>
</table>

## {.slide: data-transition="none"}

<img src="./diagrams/16281468370_ea3702e83f_k.jpg" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<img src="./diagrams/The_hindoo_earth.jpg" align="center" width="70%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<img src="./diagrams/Steen_Doctor_and_His_Patient.jpg" align="center" width="40%" style="background:none; border:none;
box-shadow:none;">
<img src="./diagrams/Palazzo_San_Georgio_Genova_W.jpg" align="center" width="40%" style="background:none; border:none;
box-shadow:none;">

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation000.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation001.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation002.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation003.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation004.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation005.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation006.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne-bob-conversation007.svg">
</object>

## {.slide: data-transition="none"}

<a href="https://pixabay.com/en/rothenburg-of-the-deaf-1624164/"><img src="./diagrams/rothenburg-of-the-deaf-1624164_1920.jpg" align="center" width="70%" style="background:none; border:none;box-shadow:none;"></a>

## {.slide: data-transition="none"}

<a href="https://commons.wikimedia.org/wiki/File:Medievalplowingwoodcut.jpg"><img src="./diagrams/Medievalplowingwoodcut.jpg" align="center" width="90%" style="background:none; border:none;box-shadow:none;"></a>

## {.slide: data-transition="none"}

<a href="https://pixabay.com/en/elephant-watering-hole-safari-1065632/"><img src="./diagrams/elephant-1065632_1920.jpg" align="center" width="70%" style="background:none; border:none;box-shadow:none;"></a>

## Thanks!

<p style="text-align:center;"> @lawrennd</p>
<p style="text-align:center;">blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)</p>
