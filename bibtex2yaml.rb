#!/usr/bin/env ruby

require 'rubygems'
require 'bibtex'
require 'yaml'
require 'facets'
require 'pandoc-ruby'
require 'pry'

bibdir = '/Users/neil/SheffieldML/publications/bib'
pubdir = '/Users/neil/lawrennd/'
talkdir = '/Users/neil/lawrennd/'
projdir = '/Users/neil/sods/'
url = 'http://inverseprobability.com'
email = ''
twitter = 'lawrennd'

def detex(text)
  # Returning up to second end character is to deal with new line
  return PandocRuby.convert(text, {:from => :latex, :to => :markdown}, 'no-wrap')[0..-2]
end
def bibtohash(obj, bib, researchers)
  # Takes an bib file object and returns a cleaned up hash.
  # Params:
  # +obj+:: Object to clean up
  # +bib+:: +BibTeX+ object that contains strings etc
  # +errhandler+:: +Proc+ object that takes a pipe object as first and only param (may be nil)
  ha = obj.to_hash(:quotes=>'').rekey!(&:to_s)
  if ha.has_key?('crossref')
    hac = bibtohash(bib[ha['crossref']], bib, researchers)
    hac.each do |key, array|
      unless ha.has_key?(key)
        ha[key]=array
      end
    end
  end
  ha['layout'] = ha['bibtex_type'].to_s
  ha.tap { |hs| hs.delete('bibtex_type') }

  ha['key'] = ha['bibtex_key'].to_s.tr(":", "-")
  ha.tap { |hs| hs.delete('bibtex_key') }

  ha['categories'] = Array.new(1)
  ha['categories'][0] = ha['key']

  ha['month'] = ha['month_numeric'].to_i
  ha.tap { |hs| hs.delete('month_numeric') }

  ha.delete_if {|key, value| key[0..2] == "opt" }

  if ha.has_key?('title')
    ha['title'] = detex(ha['title'])
  end

  if ha['abstract'] == ''
    ha.tap { |hs| hs.delete('abstract') }
  else
    ha['abstract'] = detex(ha['abstract'])
  end


  if ha.has_key?('pages')
    pages = ha['pages'].split('-')
    ha['firstpage'] = pages[0].to_i
    ha['lastpage'] = pages[-1].to_i
    ha.tap { |hs| hs.delete('pages') }
  end

  if ha.has_key?('comments')
    if ha['comments'].downcase == 'yes' or ha['comments'].downcase == 'true'
      ha['comments'] = true
    end
  end
  
  if ha.has_key?('sections')
    if ha['sections']
      sections = ha['sections'].split('|')
      hasections = Array.new(sections.length)
      sections.each.with_index do |section, index|
        name_title = section.split('=')
        hasections[index] = {'name' => name_title[0], 'title' => name_title[-1]}
      end
    end
    ha['sections'] = hasections
  end
  if ha.has_key?('editor')    
    ha['editors'] = splitauthors(ha, obj, researchers, type=:editor)
    ha.tap { |hs| hs.delete('editor') }
  end
  
  if ha.has_key?('author')
    ha['authors'] = splitauthors(ha, obj, researchers)
    ha.tap { |hs| hs.delete('author') }
  end
  if ha.has_key?('published')
    ha['published'] = Date.parse ha['published'].to_s
  else
    if ha.has_key?('year')
      year = ha['year'].to_s
    else
      year = '0001'
    end
    if ha.has_key?('month')
      month = ha['month'].to_s
      if month=='0'
        month='01'
      end
    else
      month = '01'
    end
    if ha.has_key?('day')
      day = ha['day'].to_s
    else
      day = '01'
    end
    date = year + '-' + month + '-' + day
    ha['published'] = Date.parse date
  end
  if ha.has_key?('start')
    ha['start'] = Date.parse ha['start']
  end
  if ha.has_key?('end')
    ha['end'] = Date.parse ha['end']
  end
  ha['extras'] = []
  max_labels=10
  for i in 1..max_labels
    label = 'label' << i.to_s
    link = 'link' << i.to_s
    if ha.has_key?(label) and ha.has_key?(link)
      ha['extras'] << {'label' => ha[label], 'link' => ha[link]}
      ha.tap { |hs| hs.delete(label) }
      ha.tap { |hs| hs.delete(link) }
    end
  end
  ha['errata'] = []
  max_errata = 10
  for i in 1..max_errata
    errata = 'errata' << i.to_s
    errata_credit = 'erratacredit' << i.to_s
    if ha.has_key?(errata)
      if ha.has_key?(errata_credit)
        ha['errata'] << {'text' => ha[errata], 'credit' => ha[errata_credit]}
        ha.tap { |hs| hs.delete(errata) }
        ha.tap { |hs| hs.delete(errata_credit) }
      else
        ha['errata'] << {'text' => ha[errata]}
        ha.tap { |hs| hs.delete(errata) }
      end
    end
  end
  return ha
end

def mindigit(str, num=2)
  str.gsub(/-[0-9]+/, '')
  while str.length < num
    str = '0' + str
  end
  return str
end

def filename(date, title)
  f = date.to_s + '-' + title.to_s.downcase.gsub(/\W+/, ' ').gsub(/\s+/, '-') + '.md'
  if f.length > 100
    f = f[0..97] + '.md'
  end
  return f
end

def splitauthors(ha, obj, researchers, type=:author)
  a = Array.new(obj[type].length)       #=> [nil, nil, nil]
  obj[type].each.with_index(0) do |name, index|
    first = detex(name.first)
    last = detex(name.last)
    a[index] = {'firstname' => first, 'lastname' => last}
    for researcher in researchers
      if researcher['firstname'] == first and researcher['lastname']==last
        for key in ['url', 'institute', 'twitter', 'gscholar']
          if researcher.has_key?(key)
            a[index][key] = researcher[key]
          end
        end
        break
      end
    end
  end
  return a
end

if ARGV.length < 1
  puts "Usage: #{$0} <bib>"
else

  researchers = YAML.load_file('../data/researchers.yml')
  
  txt = ''
  ARGV.each do |obj|
    txt += Kernel.open(obj).read
  end
  b = BibTeX::Bibliography.new
  b.add BibTeX::Element.parse txt
  #c = BibTeX.open ARGV[1]
  #b.add(c)
  reponame = 'talks'

  b.each do |obj|
    obj.replace(b.q('@string'))
    obj.join
  end

  # Process talks
  reponame = 'talks'
  b['@talk'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['title'])
    out = File.open(talkdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  
  
  # Process journals
  reponame = 'publications'
  b['@article'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  

  b['@inproceedings'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  

  b['@techreport'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  

  b['@incollection'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  


  
  b['@misc'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  

  b['@proceedings'].each do |obj|
    ha = bibtohash(obj, b, researchers)
    output = false
    for author in ha['authors']
      if author.firstname == 'Neil D.' and author.lastname = 'Lawrence'
        output = true
      end
    end
    for editor in ha['editors']
      if editor.firstname == 'Neil D.' and editor.lastname = 'Lawrence'
        output = true
      end
    end
    if not output
      next
    end
    ya = ha.to_yaml(:ExplicitTypes => true)
    fname = filename(ha['published'], ha['key'])
    out = File.open(pubdir + reponame + '/_posts/' + fname, 'w')
    out.puts ya
    out.puts "---"
  end  
  
  # # Process projects
  # reponame = 'dsiprojects'
  # b['@bscproject'].each do |obj|
  #   ha = bibtohash(obj, b)
  #   ya = ha.to_yaml(:ExplicitTypes => true)
  #   fname = filename(ha['published'], ha['key'])
  #   out = File.open(projdir + reponame + '/_posts/' + fname, 'w')
  #   out.puts ya
  #   out.puts "---"
  # end  

  # b['@phdproject'].each do |obj|
  #   ha = bibtohash(obj, b)
  #   ya = ha.to_yaml(:ExplicitTypes => true)
  #   fname = filename(ha['published'], ha['key'])
  #   out = File.open(projdir + reponame + '/_posts/' + fname, 'w')
  #   out.puts ya
  #   out.puts "---"
  # end  

end
