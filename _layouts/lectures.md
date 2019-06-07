---
layout: default
---
<div class="post">

  <talk class="post-content">
    {{ page.contact | markdownify }}
    at <b>{{ page.venue | markdownify }}</b> on {{ page.date | date: "%b %-d, %Y" }} {%if page.linkpdf %}[<a href="{{ page.linkpdf }}">pdf</a>]{% endif %}{%if page.linkpptgz %}[<a href="{{ page.linkpptgz }}">Gzipped Powerpoint</a>]{% endif %}{%if page.linkipynb %}[<a href="{{ site.nbviewer }}{{ page.linkipynb }}">jupyter</a>]{% endif %}{%if page.linkreveal %}[<a href="{{ page.linkreveal }}">reveal</a>]{% endif %}{%if page.pdf %}[<a href="{{ site.talk_files }}/{{ page.pdf }}">pdf</a>]{% endif %}{%if page.ipynb %}[<a href="{{ site.nbviewer }}{{ site.basenb }}{{ page.ipynb }}">jupyter</a>]{% endif %}{%if page.reveal %}[<a href="{{ site.talk_files }}{{ page.reveal }}">reveal</a>]{% endif %}
    {%if page.reveal %}
    <p><iframe width="{{ site.reveal.width }}" height="{{ site.reveal.height }}" src="{{ site.talk_files }}{{ page.reveal }}" frameborder="0" allowfullscreen></iframe></p>
    {% endif %}
    {% if page.youtube %}
    <p><iframe width="{{ site.youtube.width }}" height="{{ site.youtube.height }}" src="https://www.youtube.com/embed/{{ page.youtube }}" frameborder="0" allowfullscreen></iframe></p>
    {% endif %}
    {% if page.videolectures %}
    <h4>Videolectures</h4>
    <p><a href="http://videolectures.net/{{ page.videolectures }}/"><img src="http://videolectures.net/{{ page.videolectures }}/thumb.jpg" border=0></a></p>
    {% endif %}
      
    <p><b>{{ page.tagline }}</b> </p>

    {% if page.abstract %}
    <h4>Abstract</h4>
    
    <p>{{ page.abstract | markdownify }}</p>
    {% endif %}

    <h3>Links</h3>
    <div id="extras">
    <ul>
      {%if page.blog %}<li><a href="{% assign elems = page.blog | split: '-' %}{% for elem in elems %}{% if forloop.index0 < 4 %}/{% else %}-{% endif %}{% if forloop.last %}{{ elem | remove_first: '.md' }}{% else %}{{ elem }}{% endif %}{% endfor %}">Related Blog Post</a></li>{% endif %}
      {%if page.blog1 %}<li><a href="{% assign elems = page.blog1 | split: '-' %}{% for elem in elems %}{% if forloop.index0 < 4 %}/{% else %}-{% endif %}{% if forloop.last %}{{ elem | remove_first: '.md' }}{% else %}{{ elem }}{% endif %}{% endfor %}">Further Related Blog Post</a></li>{% endif %}
      {%if page.blog2 %}<li><a href="{% assign elems = page.blog2 | split: '-' %}{% for elem in elems %}{% if forloop.index0 < 4 %}/{% else %}-{% endif %}{% if forloop.last %}{{ elem | remove_first: '.md' }}{% else %}{{ elem }}{% endif %}{% endfor %}">Yet another Related Blog Post</a></li>{% endif %}
      {%if page.ppt %}<li><a href="{{ site.talk_files }}/{{ page.ppt }}">Powerpoint</a></li>{% endif %}
      {%if page.pdf %}<li><a href="{{ site.talk_files }}/{{ page.pdf }}">pdf</a></li>{% endif %}
      {%if page.linkpdf %}<li><a href="{{ page.linkpdf }}">Download PDF</a></li>{% endif %}
      {%if page.linkpsgz %}<li><a href="{{ page.linkpsgz }}">Download Gzipped Postscript</a></li>{% endif %}
      {%if page.linkps %}<li><a href="{{ page.linkps }}">Download Postscript</a></li>{% endif %}
      {%if page.linkppt %}<li><a href="{{ page.linkppt }}">Download PPT</a></li>{% endif %}
      {%if page.linkpptgz %}<li><a href="{{ page.linkpptgz }}">Download Gzipped PPT</a></li>{% endif %}
      {%if page.demo %}<li><a href="{{ site.talk_files }}/demos/{{ page.demo }}">demo code</a></li>{% endif %}
      {%if page.linksoftware %}<li><a href="{{ page.linksoftware }}">Download Software</a></li>{% endif %}
      {% for extra in page.extras %}
      <li><a href="{{ extra.link }}">{{ extra.label }}</a></li>
      {% endfor %}
    </ul>
  </div>

    {{ content | markdownify }}
  </talk>

</div>
