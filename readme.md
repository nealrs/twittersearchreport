# Twitter Search Report

This is the spiritual successor to [HootSuite Extractor](http://devpost.com/software/hootsuite-extractor).

HootSuite changed their CSS (breaking HSE) and rather than refactoring a chrome extension and server-side code, I figured I could just write a better Python script and hit the Twitter API directly.

Basically, this script accepts a list of search terms (in my case, URLs, hashtags, and hackathon names) and runs an `OR` search on twitter and compiles the results in HTML and PDF reports like these: [[HTML](example/lenovo-multi-touch-multi-hack-06-17-16.html)] &middot; [[PDF](example/lenovo-multi-touch-multi-hack-06-17-16.pdf)]

## How to use TSR

1. Clone the repo

2. Install dependencies by running `pip install TwitterSearch Jinja2 pdfkit slugify` and downloading [wkhtmltopdf](http://wkhtmltopdf.org/downloads.html)

3. Rename `keys_example.py` to `keys.py`

4. [Create a new Twitter app](https://apps.twitter.com/app/new) and fill in your API keys. **Never commit API keys to git**

5. `template.html` to change the styling, layout, tags, etc.

6. Open `one.py` and change `client` to your client's name and update `keywords` with a list of keywords / urls / hashtags / etc. that you want to search for.

7. Run `python one.py` and wait patiently while the script runs the search, iterates through the items, processes a jinja template, writes HTML, and finally converts to PDF.

8. Take a nap, you deserve it.

**FYI** `all.py` lets you setup and loop through multiple clients & keyword sets all in one go. It'll also might hit up against the twitter API limits. Which it shouldn't, but IDK.
