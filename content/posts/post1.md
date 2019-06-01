title: Setting up a static blog with Pelican and Netlify
slug: pelican-python
category: tech
tags: web, javascript, programming, web_development, python, pelican
date: 2019-05-26
modified: 2019-05-26
summary: Creating a static site with Pelican on Python



Have you ever wanted to start your own blog? Are you too lazy to create the whole website from scratch? Or, are you just too busy? Or maybe you haven't found the right kinda motivation yet...

&nbsp;

Well, I have similar problems, and lucky for me, I found some motivation recently. A couple of days ago, I was reading an article on [Full Stack Python](https://www.fullstackpython.com/), and I found out that it was made using something called Pelican. Now, I knew what Pelican was but I never thought to give it a try until then...

&nbsp;

So... I finally decided to set-up my own blog using Pelican. Before this, I had my single-page website parked on AWS's free tier but then I decided to move on to Github Pages and Netlify. (Well, my free tier expired too :p)

&nbsp; 

Okay! Okay! Okay! You may not be interested in my story so let's jump to the main content now.

&nbsp;

<img alt="Pelican" src='https://media.giphy.com/media/xUA7aX3WnLn91k2DeM/giphy.gif' style="display: block; margin-left:auto; margin-right:auto; width: auto;" />

&nbsp; 

Assuming you have Python3 and pip installed, start by downloading and installing __Pelican__. Hit up the console and type

&nbsp;

>pip install pelican

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

Use `make devserver` command to launch development server on port 8000 (default). After launching the devserver, check out the website at __*localhost:8000*__. It uses default theme for the site, you can [create]() your own theme, or you use [this site's theme]() if you want.

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

&nbsp;

&nbsp;

### To be continued...