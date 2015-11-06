#!/usr/bin/env ruby

require 'rubygems'
require 'bibtex'
require 'yaml'
require 'facets'
require 'pandoc-ruby'


def mindigit(str, num=2)
  str.gsub(/-[0-9]+/, '')
  while str.length < num
    str = '0' + str
  end
  return str
end

def filename(obj)
  
  f = mindigit(obj['year'].to_s,4) \
         + '-' + mindigit(obj['month_numeric'].to_s) \
         + '-' + mindigit(obj['day'].to_s) \
         + '-' + obj['title'].convert(:latex).to_s.downcase.gsub(/\W+/, ' ').gsub(/\s+/, '-') \
      + '.md'
  if f.length > 100
    f = f[0..97] + '.md'
  end
  return f
end

if ARGV.length < 1
  puts "Usage: #{$0} <bib> [<yml>]"
else
  out = ARGV.length == 2 ? File.open(ARGV[1], 'w') : STDOUT
  b = BibTeX.open ARGV[0]
  b['@talk'].each do |obj|
    obj.replace(b.q('@string'))
    obj.join
    ha = obj.to_hash(:quotes=>'').rekey!(&:to_s)
    ha['layout'] = 'talk'
    ha['key'] = ha['bibtex_key']
    ha['month'] = ha['month_numeric']
    ha.tap { |hs| hs.delete('month_numeric') }
    ha.tap { |hs| hs.delete('bibtex_type') }
    ha.tap { |hs| hs.delete('bibtex_key') }
    ha.delete_if {|key, value| key[0..2] == "opt" }
    if ha['abstract'] == ''
      ha.tap { |hs| hs.delete('abstract') }
    end
    if ha.has_key?('abstract')
      ha['abstract'] = PandocRuby.convert(ha['abstract'], :from => :latex, :to => :markdown)
    end
    ha.each do |key, value|
      ha[key] = LaTeX.decode(value)
    end
      
    ya = ha.to_yaml
    out = File.open('/Users/neil/lawrennd/talks/_posts/' + filename(obj), 'w')    
    out.puts ya
    out.puts "---"
  end  

  b['@article'].each do |obj|
    obj.replace(b.q('@string'))
    obj.join
    ha = obj.to_hash(:quotes=>'').rekey!(&:to_s)
    ha['layout'] = 'article'
    ha['key'] = ha['bibtex_key']
    if ha.has_key?('month')
      ha['month'] = ha['month_numeric']
      ha.tap { |hs| hs.delete('month_numeric') }
    else
      ha['month'] = 1
    end
    unless ha.has_key?('day')
      ha['day'] = 1
    end
    ha.tap { |hs| hs.delete('bibtex_type') }
    ha.tap { |hs| hs.delete('bibtex_key') }
    ha.delete_if {|key, value| key[0..2] == "opt" }
    if ha['abstract'] == ''
      ha.tap { |hs| hs.delete('abstract') }
    end
    if ha.has_key?('abstract')
      ha['abstract'] = PandocRuby.convert(ha['abstract'], :from => :latex, :to => :markdown)
    end
    ha.each do |key, value|
      ha[key] = LaTeX.decode(value)
    end
      
    ya = ha.to_yaml
    out = File.open('/Users/neil/lawrennd/publications/_posts/' + filename(obj), 'w')    
    out.puts ya
    out.puts "---"
  end  
end

