# Twitter Search Report

This is the spiritual successor to [HootSuite Extractor](http://devpost.com/software/hootsuite-extractor).

HootSuite changed their CSS (breaking HSE) and rather than refactoring a chrome extension and server-side code, I figured I could just write a better Python script and hit the Twitter API directly.

Basically, this script accepts a list of search terms (in my case, URLs, hashtags, and hackathon names) and runs an `OR` search on twitter and compiles the results in HTML and PDF reports like these: [[HTML](example/lenovo-multi-touch-multi-hack-06-17-16.html)] & middot; [[PDF](example/lenovo-multi-touch-multi-hack-06-17-16.pdf)]

## Installation

Hope you're got pip and homebrew installed. You'll need to run: `pip install TwitterSearch Jinja2 pdfkit slugify` and install [wkhtmltopdf](http://wkhtmltopdf.org/downloads.html)

## Configuration

After you clone the repo, rename `keys_example.py` to `keys.py`. Then, [create a new Twitter app](https://apps.twitter.com/app/new) and fill in your API keys. And for the love of god, don't ever commit them to git.

Edit `template.html` to change the styling, layout, tags, etc.

Once that's done, open up `one.py` and change `client` to your client's name / title of the report and update `keywords` with a list of keywords / urls / hashtags / etc. that you want to search for.

Finally, run the file and wait patiently while the script runs the search, iterates through the items, processes a jinja template, writes HTML, and converts it to a PDF.

`all.py` lets you setup and loop through multiple clients / keyword sets in one go. It'll also might hit up against the twitter API limits. Which it shouldn't, but IDK.
