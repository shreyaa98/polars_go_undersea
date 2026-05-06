
# Project: pandas-to-polars

## Goal

Convert the pandas-go-to-space tutorial to polars:

## Timeline

I would plan with 2 hours per chapter and 3 chapters per week, including the translation, tests and double-checking the test. Please git push each chapter separately. I would reserve 2h / week for review and communicating and creative ideas. I expect that you communicate a) when things move according to plan b) slower c) faster. All three are ok, I just want to know.

### Week March 02-06:

Chapters:

* Preparations (short but requires Sphinx setup) - Under Review
* Read and Write Data - Under Review
* Inspect DataFrames - Under Review

### Week March 09-13:

Chapters:

* Select Rows and Columns
* Data Wrangling
* High-Quality Plots

### Week March 16-20:

Chapters:

* Descriptive Statistics
* Pivot Tables
* Edit columns

### Week March 23-27:

Chapters:

* String Handling
* Time Series
* Plotting Maps

### Later

Chapters:

* Create DataFrames and Series
* Long vs Wide Format
* Aggregation

### Not sure

The challenges might need some heavy restructuring, as they do not fit the theme at all. I have to think about it.

## Things to do:

1. copy the repository: https://github.com/krother/pandas_go_to_space
2. build the HTML using Sphinx (let me know if you need help)
3. write into the README how to build it
4. create a new repo `polars_go_to_space` and put everything there
5. add yourself as an author in index.rst and README.md, update the year
6. go through the chapters one by one
   6.1 rewrite the code using polars. Some code might look very different after or disappear completely. Adjust the text accordingly.
   6.2 try out the code yourself
   6.3 commit and push the changes after each chapter
7. remove the "Hall of Fame" and "Page Rank" chapters
8. CREATIVE: if you like, replace the oldschool AI images by better ones
9. CREATIVE: I honestly have no idea what to do with the panda cover story. Rewriting it with polar bears is a lot less cute... if you have a good story, write it.
10. some of the stuff is not of superb quality. Change whatever you feel necessary. Some chapters might be dropped. I feel the animated gif exercise is interesting on the data side, but the animation itself could be replaced by a one-liner in plotly.
11. people have repeatedly said they like the tutorial because it is concise. It should stay that way. So no long theory or adding lots of things.
12. BONUS: change the installation to uv. it is much better. Use the pyproject.toml and .github/workflows/.. from https://github.com/krother/rest-api-tutorial/
13. edit the conf.py to update metadata.
14. ask me when you feel stuck for more than 20 minutes.
15. use LLMs to speed up things as you find reasonable
16. feel free to post as much about it as you like in any number of channels (make yourself visible on the market) 
17. if you find other ideas on the way, let's talk about them


## Other projects

- clean up the homepage at https://blueberry-py-staging.netlify.app/
(the files are too convoluted and it is too hard for me to announce
courses there).
clone). Try out everything.
- announce courses (Python Basics + Data Analytics Basics)
- create some social media postings to advertise the courses
- help me make the office space nicer
- as soon as someone signs up, run the courses

## Pay stuff

I can offer 20,- EUR/h plus health insurance (19% or something similar).

With the courses, I'd like to negotiate a sum for the room and 10% for
branding and you keep the rest
