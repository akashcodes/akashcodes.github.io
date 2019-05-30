title: Bookmarklets 3 - Execute JS code from bookmarks
slug: bookmarklets3
category: tech
tags: web, javascript, programming, bookmark, code, 100daysofcode
date: 2019-05-28
modified: 2019-05-28
summary: Bookmarklets, and how to create one
showdate: True

# Psst... wanna execute JavaScript commands on your phone browser?
## - Enter the bookmarklets -

##### *Please note that I'm gonnna use Google Chrome on Android for this article*

I've had my share of making web-apps and writing lots of JavaScript code. It has become a habit of mine to execute javascript snippets on many websites I visit, sometimes to hide those annoying popups that distract me from the main content, sometimes to automate some boring stuff, and most of the times just for fun.

You can use TamperMonkey, or just fire up the console but that only works on PC. There are moments I wish I could execute some of those commands while browsing on my Android phone. As of writing this article, Chrome on Android has no extensions, niether does it has a console on Android. Thankfully, there's a thing called Bookmarklets that does works.

If you're unaware - Bookmarklets are, just as their name says are bookmarks but they won't open a webpage. Instead, they execute some Javascript code when you open them. Sounds fun, right?

(might wanna add wikipedia definition. we'll see...)


When you bookmark a page, URI has a protocol specified with the bookmark (like http, or ftp). Now there'se on more protocol in the URI scheme that tells browsert it parse Javascript code. The __*javascript:*__ protocol.

Normal bookmarks - https://example.com
Javascript bookmark(let)s - javascript:function() {alert("Hello, world!");} ();

#### Note to self: replace " " (space) with "%20% in the above example javascript bookmarklet.

Okay, so how do I actually create a bookmarklet, and how it works?

To create a bookmarklet, simply create a bookmark, enter any recognizable unique name (we'll come to it soon), and in the bookmark URI, start with "javascript:", and then write your javascript code. Simple, ehh? Well, there are slight complications to it.

You need follow UTF-8 encoding while making your bookmark, replace spaces " " by %20%. You can save yourself from this kinda labour by simply using any bookmarklet editor available online.

Okay, let's create a simple bookmarklet. We'll create a bookmarklet that'll let us remove any page element when we click/tap on it.

## Create your sample bookmarklet now


### Writing the Javascript

> function() {
> 
> // This a function that
> 
> var el = document.createElement("div");
> 
> el.id= "dont-remove-me";
> 
> 
> }();