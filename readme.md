# CTech Projects
Hi. This repo is a blog to share projects from CTechis for CTechis. You can visit the website here: [https://ctechfilmuniversity.github.io/](https://ctechfilmuniversity.github.io/)

# How to create a new post
In order to create a new post or entry on the github io pages site, please have a look at this [readme.md](__content/readme.md).

# About
Hi. This repo is a Jekyll-Blog-System to share projects from CTechis for CTechis. 

> The project forked and has been modified from [Millennial](https://github.com/LeNPaul/Millennial). Please find some more information about Millenial in the info directory. 

## Structure 
```
.../
├── __content                  # All posts are stored here, see the readme.md in this folder
|  ├── new-post                # A new post can be created here
├── __scripts                  # Python scripts for the automated post publishing process  
├── _data                      # Data files
|  └── settings.yml            # Theme settings and custom text
├── _includes                  # Theme includes (Header, Footer...)
├── _layouts                   # Theme layouts (for pages, posts ...)
├── _posts                     # Where all submission markdowns are
├── assets                     # Style sheets, images and js logic are found here
|  ├── css                     # Style sheets go here
|  |  └── _sass                # Folder containing SCSS files
|  |  └── main.scss            # Main SCSS file
|  |  └── syntax.css           # Style sheet for code syntax highlighting
|  └── img                     # Images go here
|  └── js                      # Logic go here (for example for the search)
├── info                       # contains additional information
├── pages                      # 1st, 2nd, 3rd, 4th, Other (all tabs)
├── _config.yml                # Site build settings
├── Gemfile                    # Ruby Gemfile for managing Jekyll plugins
├── index.md                   # Home page
├── LICENSE.md                 # License for this theme
├── README.md                  # Includes all of the documentation for this theme
└── rss-feed.xml               # Generates RSS 2.0 file which Jekyll points to
```

## Some notes

- Github pages + Jekyll ctechfilmuni webpage prototype
- themes for Jekyll:
    - https://jekyllthemes.io/theme/millennial
    - https://jekyllthemes.io/theme/flexible-jekyll

- Jekyll uses Liquid language, documentation: https://shopify.github.io/liquid/basics/introduction/
- Jekyll tutorials : https://learn.cloudcannon.com/tutorials/
- Using Sass (CSS tool)
- Search: https://lunrjs.com/


Getting started:
- clone repo
- run ```bundle exec jekyll serve```


### MathJax Library deactivated
The millenial theme comes packed with the MathJax library. It enables to display mathematical formulas in a Latex-Style manner. Because it has not been used, I deactivated it for now. If there is the need for it, I would recommend, hosting it on the server instead of CloudFlare: http://docs.mathjax.org/en/latest/web/hosting.html
