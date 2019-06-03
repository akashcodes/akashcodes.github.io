title: Setting up a static blog with Pelican and Netlify
slug: pelican-python
category: tech
tags: web, javascript, programming, web_development, python, pelican
date: 2018-10-20
modified: 2019-05-27
summary: Creating a static site with Pelican on Python



Have you ever wanted to start your own blog? Are you too lazy to create the whole website from scratch? Or, are you just too busy? Or maybe you haven't found the right kinda motivation yet...

&nbsp;

Well, I have similar problems, and lucky for me, I found some motivation recently. A couple of days ago, I was reading an article on [Full Stack Python](https://www.fullstackpython.com/), and I found out that it was made using something called Pelican. Now, I knew what Pelican was but I never thought to give it a try until then...

&nbsp;

So... I finally decided to set-up my own blog using Pelican. Before this, I had my single-page website parked on AWS's free tier but then I decided to move on to Github Pages and Netlify. (Well, my free tier expired too :p)

&nbsp; 

<img alt="Pelican" src='https://media.giphy.com/media/xUA7aX3WnLn91k2DeM/giphy.gif' style="display: block; margin-left:auto; margin-right:auto; width: auto;" />

&nbsp; 

Assuming you have Python3 and pip installed, start by downloading and installing __Pelican__. Hit up the console and run:

&nbsp;

<pre><code class="bash para"># download pelican library
pip install pelican
</code></pre>

&nbsp;

###### Note: it's good to use virtual environments but that's for you to decide.

&nbsp;

Now that Pelican is installed, create a new folder, and in that folder run&nbsp;`pelican-quickstart` command in terminal. This will create a new Pelican project. After answering to the prompts, a pelican project will be created with all the basic settings in __pelicanconf.py__ file.

&nbsp;

<img alt="pelican-quickstart screenshot" src='https://i.imgur.com/FUckQkj.png' style="display: block; margin-left:auto; margin-right:auto; max-width: 90%;" />

&nbsp;

Type `make` in the terminal to see the commands you can use to run development server, publish your blog, etc. Alternatively, you can open the __Makefile__ in the project folder, to read, and edit commands.

&nbsp;

<img alt="pelican make commands" src='https://i.imgur.com/r5Sy9HQ.png' style="display: block; margin-left:auto; margin-right:auto; max-width: 90%;" />

&nbsp;

Use `make devserver` command to launch development server on port 8000 (default). After launching the devserver, check out the website at __*localhost:8000*__. It uses default theme for the site, you can [create](http://docs.getpelican.com/en/3.6.3/themes.html) your own theme, or you use [this site's theme](https://github.com/akashcodes/pelican-themes) if you want.

&nbsp;

<img alt="pelican demo on localhost:8000" src='https://i.imgur.com/mqI6FnV.png' style="display: block; margin-left:auto; margin-right:auto; max-width: 90%;" />

&nbsp;

&nbsp;

&nbsp;

#### Okay! Now let's write a blog post

&nbsp;

Create a file with __.md__ extension in __[project's root]/content/posts__. Add details about the blog post in the header of the markdown file and then write your content.

&nbsp;

<img alt="pelican blog example" src='https://i.imgur.com/y9DSgPo.png' style="display: block; margin-left:auto; margin-right:auto; max-width: 90%;" />

&nbsp;

Here: __slug__ is the name of your html file generated, __pelican-python.html__ in this case. Save the file and reload __localhost:8000__ to find the new blog post there. [no screenshot. see it for yourself :p]

&nbsp;

&nbsp;

Okay! Now let's make some changes to __pelicanconf.py__.

&nbsp;

<pre><code class="python"># Add following to your pelicanconf.py
# Default date format to use: Eg: (%d %B %Y) => 28 May 2019
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Current year. might be useful
CURRENT_YEAR = time.strftime("%Y")

# Path to theme to be used. I've named my theme basic1
THEME = "themes/basic1"

# List of templates that are used directly to render content. 
# Typically direct templates are used to generate index pages for collections of content 
# (e.g., tags and category index pages). If the tag and category collections are not needed, 
# set DIRECT_TEMPLATES = ('index', 'archives')
# I've add 'blog' here to create a separate page for blog indexing
DIRECT_TEMPLATES = ['index','archives','categories', 'tags', 'blog']

# Auto generate slug from this title, if not specified [Overridden by the Slug: property]
SLUGIFY_SOURCE = 'title'

# How URLs will be created for a blog post. eg - {root}/category/year/month/date/{slug}
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'

# How/where to generate HTML file for the blog post. eg - {root}/category/year/month/date/{slug}
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
</code></pre>

&nbsp;

Now create `blog.html` in __themes/{theme_name}/templates__. This is where you blogs will be indexed. Now you can remove blog indexing from `index.html`, and make it your landing page. Blogs can now accessed from __SITE_URL/blog/__. You can refer to theme files for [this website's theme]() to see how I did it.

&nbsp;

Okay! So now we need to publish our site. We'll use Github Pages and Netlify so host our site. [Rasor's Tech Blog has a nice article](https://rasor.github.io/using-pelican-blog-on-github-pages.html) on how to publish your blog on Github Pages. After you're done with that, we'll link our github pages repository to Netlify. 

&nbsp;

Publishing on Netlify is pretty simple. Signup on Netlify using your Github account and follow the steps. When asked which repository you want to use to serve the pages, select the repository for your blog. __Note:__ if you followed steps from Rasor's Tech Blog article, then when selecting the branch to publish use the __pelican branch__ (or whatever you named it). Done! Netlify will generate a link to your website, and your website must also be published at __username.github.io__ (again if you followed Rasor's Tech Blog). __To use your custom domain:__ It's pretty easy on Netlify. Just follow this link - [Netlify - Custom Domains](https://www.netlify.com/docs/custom-domains/).

&nbsp;

So, that's it. I hope you liked this post. If I made any mistakes, please let me know in the comments below. Also, if you have any queries, feel free to ask. Have a great day!

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

