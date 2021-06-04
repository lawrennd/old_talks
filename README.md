# talks

Talks from Neil Lawrence

To create talks from these files you need to access the python package `makemd`. This package includes a macro language implemented in the generic preprocessor, `gpp` for interpeting the markdown.

You can install with

```
apt-get install gpp
pip install makemd
```

The talks folder is organized as follows.

Each general subject or lecture series comes under a sub-directory 

```
_subject/
```

Under that subject, there are a series of talks. Each as a markdown file. These files include various talk files from different parts of the site. They are also allocated to different subject files, under the includes subdirectory.

```
_subject/includes/
```

Different subjects have their own configuration files that are found in

```
_subject/_config.yml
```

