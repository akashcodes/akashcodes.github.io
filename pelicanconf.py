#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = 'Akash Mishra'
SITENAME = 'akash codes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Default date format: Eg: (%d %B %Y) => 28 May 2019
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Current year. might be useful
CURRENT_YEAR = time.strftime("%Y")

# Path to theme to be used
THEME = "themes/basic1"


# List of templates that are used directly to render content. 
# Typically direct templates are used to generate index pages for collections of content 
# (e.g., tags and category index pages). If the tag and category collections are not needed, 
# set DIRECT_TEMPLATES = ('index', 'archives')
# TODO: Add 'error' below after creating error.html
DIRECT_TEMPLATES = ['index','archives','categories', 'tags', 'blog']


# Auto generate slug from this source. Overridden by the Slug: property
SLUGIFY_SOURCE = 'title'


# When creating a short summary of an article, 
# this will be the default length (measured in words) of the text created. 
# This only applies if your content does not otherwise specify a summary. 
# Setting to None will cause the summary to be a copy of the original content.
SUMMARY_MAX_LENGTH = 40


# Use a different page to index blogs... but how???
# INDEX_SAVE_AS = 'blogs.html'


ARTICLE_URL = '{category}/{date:%Y}/{date:%B}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%B}/{date:%d}/{slug}/index.html'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

