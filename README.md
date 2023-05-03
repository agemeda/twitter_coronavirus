# Coronavirus twitter analysis



**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The lambda server's `/data/Twitter dataset` folder contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

**Project Information**
For this project, I analyzed tweets from 2020 involving the word 'coronavirus'. Over the year, we can expect there to be an increase in tweets involving the word as the virus spread and became a global issue. The tweets were broken up by language and separately by country, and counted by how often they came up in each of those keys. The results were than narrowed down by the top 10 keys, so only data from the top 10 countries and languages that tweeted a certain coronavirus hashtag were recorded.

using the alternate reduce function, and the visualize file I was able to generate four graphs, Top 10 Countries that tweeted #coronavirus in 2020, Top 10 Languages that tweeted #coronavirus in 2020, Top 10 Countries that tweeted #코로나바이러스 in 2020, Top 10 languages that tweeted #코로나바이러스 in 2020.

![(src/coronavirus_lang.png)]  
