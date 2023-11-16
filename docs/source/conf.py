# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FPGAprince'
copyright = '2023, FPGAprince'
author = 'FPGAprince'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    #"hoverxref.extension",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

#i think this is to add js configs though..
# def setup(app):
#     # (create a setup() function if you don't already have one;
#     # or add to the existing setup() ...)
#     app.add_js_file("mathjax-config.js")
#     app.add_css_file()

#html_static_path =[]
# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

#
html_theme_options = {
#    'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#    'analytics_anonymize_ip': False,
#    'logo_only': False,
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#    'style_external_links': False,
#    'vcs_pageview_mode': '',
#    'style_nav_header_background': 'white',

    # Toc options
#    'collapse_navigation': True,
#    'sticky_navigation': True,
    'navigation_depth': 5,
    'includehidden': False
#    'titles_only': False
}