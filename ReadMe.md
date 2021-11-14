# COMP 598 Final Project

## Goal:

Find the favorability of the audience response for a movie. Specifically, they want to know:

1. The salient topics discussed around their film and what each topic primarily concerns
2. Relative engagement with those topics
3. How positive/negative the response to the movie has been

## Steps to be completed:

- [ ] Pick a movie
- [ ] Create Twitter API script to collect 1000 tweets over 3 days ("You should set filters such that all 1,000 posts have a very high likelihood of being related to the movie AND all are in English (ensure that thelanguage field is set to “en”… this isn’t exact, but it gets close). You can filter by hashtags or words when collecting Twitter data. You can choose the exact words, as long as they are related to the context that we mentioned before")
- [ ] Make sure to check for uniqueness when collecting tweets
- [ ] conduct an open coding on 200 tweets (approach the exercise requiring each tweet to belong to exactly one topic). You should aim for between 3-8 topics in total.
- [ ] figure out the best way to annotate these tweets
- [ ] split into thirds and annotate the tweets (also code them for positive/neutral/negative sentiment)
- [ ] Make a script that characterizes your topics by computing the 10 words in each category with the highest tf-idf scores (to compute inverse document frequency, use all 1,000 posts that you originally collected.
- [ ] make the final report ( I'll make a check list for that later if this ends up being helpful)
