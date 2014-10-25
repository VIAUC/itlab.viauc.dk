#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = u'ITLab'
SITEURL = 'http://localhost:8000/'
TAGLINE = 'Playground for all ICT student at VIA University'

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Facebook Group', 'https://www.facebook.com/groups/1479179769018998/'),
    ('Via Web Society', 'http://viawebsociety.github.io/'),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
STATIC_PATHS = ['images', 'files']

# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'gravatar', 'pelican_youtube']
PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}

# Theme
THEME = 'theme/'
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_SHOW_TAGS = False
FOUNDATION_FOOTER_TEXT = ' '
FOUNDATION_PYGMENT_THEME = 'monokai'

DISPLAY_PAGES_ON_MENU = True

RELATIVE_URLS = True
