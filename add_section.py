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

    for key,val in replacements:
        if val not in post.keys() and key in post.keys():
            post.metadata[val] = post.metadata[key]
            del post.metadata[key]
    for name_field in name_fields:
        if name_field in post.keys():
            for author in post.metadata[name_field]:
                for key,val in name_replacements:
                    if val not in post.keys() and key in post.keys():
                        post.metadata[val] = post.metadata[key]
                        del post.metadata[key]

                    
    if 'editor' not in post.keys() and 'editors' in post.keys():
        post.metadata['editor'] = post.metadata['editors']
        del post.metadata['editors']

    if 'id' not in post.keys() and 'key' in post.keys():
        post.metadata['id'] = post.metadata['key']
        del post.metadata['editors']
        
    if 'editor' in post.keys():
        for editor in post.metadata['editor']:
            if 'given' not in editor.keys() and 'firstname' in editor.keys():
                editor['given'] = editor['firstname']
                del editor['firstname']
            if 'family' not in editor.keys() and 'lastname' in editor.keys():
                editor['family'] = editor['lastname']
                del editor['lastname']

    print(frontmatter.dumps(post))
    stream = file(filename, 'w')
    frontmatter.dump(post, stream, encoding='utf-8')
    f.close()

