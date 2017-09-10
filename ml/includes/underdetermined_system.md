
### Underdetermined System {data-transition="none"}

<table>
<tr><td>
What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

</tr></td>
</table>

### Underdetermined System {data-transition="none"}

<table>
<tr><td>
What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

Can compute $m$
given $c$. $$m = \frac{\dataScalar_1 -c}{\inputScalar}$$

</tr></td>
</table>

### Underdetermined System {data-transition="none"}

<table>
<tr><td>
What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

<div class="fragment" data-fragment-index="1">Can compute $m$
given $c$. $$m = \frac{\dataScalar_1 -c}{\inputScalar}$$</div>

<div class="fragment" data-fragment-index="2">Can compute $m$ given $c$.
$$c=1.75\Longrightarrow m=1.25$$</div>

</td>
<td>
<object class="svgplot" data="../ml/diagrams/under_determined_system000.svg">
</object>
</td></tr>
</table>

### Underdetermined System {data-transition="none"}

<table>
<tr><td>
What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

<div>Can compute $m$
given $c$. $$m = \frac{\dataScalar_1 -c}{\inputScalar}$$</div>

<div>Can compute $m$ given $c$.
$$c=1.75\Longrightarrow m=1.25$$</div>

</td>
<td>
<object class="svgplot" data="../ml/diagrams/under_determined_system001.svg">
</object>
</td></tr>
</table>


### Underdetermined System {data-transition="none"}

<table>
<tr><td>
What about two unknowns and *one* observation?
$$\dataScalar_1 =  m\inputScalar_1 + c$$

Can compute $m$
given $c$. $$m = \frac{\dataScalar_1 -c}{\inputScalar}$$


Can compute $m$ given $c$.
$$c=-0.777\Longrightarrow m=3.78$$

</td>
<td>
<object class="svgplot" data="../ml/diagrams/under_determined_system002.svg">
</object>
</td></tr>
</table>

###

\onslide<5> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval3.tex}c=-4.01\Longrightarrow m=7.01\PandocEndInclude{input}{45}{53}$$
\onslide<6> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval4.tex}c=-0.718\Longrightarrow m=3.72\PandocEndInclude{input}{50}{53}$$
\onslide<7> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval5.tex}c=2.45\Longrightarrow m=0.545\PandocEndInclude{input}{55}{53}$$
\onslide<8> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval6.tex}c=-0.657\Longrightarrow m=3.66\PandocEndInclude{input}{60}{53}$$
\onslide<9> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval7.tex}c=-3.13\Longrightarrow m=6.13\PandocEndInclude{input}{65}{53}$$
\onslide<10> Can compute $m$ given $c$.
$$\PandocStartInclude{../../../ml/tex/diagrams/onePointCval8.tex}c=-1.47\Longrightarrow m=4.47\PandocEndInclude{input}{70}{53}$$
\onslide<11> Can compute $m$ given $c$.\
Assume $$c\sim \gaussianSamp{0}{4},$$ we find a distribution of
solutions.
</td>
<td>
\onslide<1-2> ![](../../../ml/tex/diagrams/one_point.png) \onslide<3>
![](../../../ml/tex/diagrams/one_point1.png) \onslide<4>
![](../../../ml/tex/diagrams/one_point2.png) \onslide<5>
![](../../../ml/tex/diagrams/one_point3.png) \onslide<6>
![](../../../ml/tex/diagrams/one_point4.png) \onslide<7>
![](../../../ml/tex/diagrams/one_point5.png) \onslide<8>
![](../../../ml/tex/diagrams/one_point6.png) \onslide<9>
![](../../../ml/tex/diagrams/one_point7.png) \onslide<10>
![](../../../ml/tex/diagrams/one_point8.png) \onslide<11>
![](../../../ml/tex/diagrams/one_point100.png)
</td>
</tr>
</table>
