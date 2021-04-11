#!/usr/bin/env python
# Format taken from: http://blog.martinfenner.org/2013/07/30/citeproc-yaml-for-bibliographies/
import frontmatter
import glob

replacements = {'key' : 'id', 'editors' : 'editor', 'authors' : 'author', 'number' : 'issue', 'booktitle' : 'container-title', 'doi' : 'DOI', 'url': 'URL'}

name_replacements = {'firstname' : 'given', 'lastname' : 'family'}
name_fields = ['author', 'editor']
section = False
section_name = 'neil'

for filename in glob.glob('./_posts/*.md'):
    post = frontmatter.load(filename)
    if section:
        if 'section' not in post.keys():
            post.metadata['section'] = section_name

    for key,val in replacements.items():
        if val not in post.keys() and key in post.keys():
            post.metadata[val] = post.metadata[key]
            del post.metadata[key]
    for name_field in name_fields:
        if name_field in post.keys():
            for author in post.metadata[name_field]:
                for key,val in name_replacements.items():
                    if val not in post.keys() and key in post.keys():
                        post.metadata[val] = post.metadata[key]
                        del post.metadata[key]                    

    print(frontmatter.dumps(post))
    stream = file(filename, 'w')
    frontmatter.dump(post, stream, encoding='utf-8')
    f.close()

