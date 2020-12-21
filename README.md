![Check updated stats](https://github.com/marco97pa/MostSubYTMusicChannels/workflows/Check%20updated%20stats/badge.svg)
![Weekly report](https://github.com/marco97pa/MostSubYTMusicChannels/workflows/Weekly%20report/badge.svg) ![Twitter Follow](https://img.shields.io/twitter/follow/mostSubYTMusic?style=social)

![icon](https://pbs.twimg.com/profile_images/1321082040842887168/ndA1-fPV_200x200.jpg)

# Most Subscribed YouTube Music Channels

This Python bot checks the most subscribed music artist channels on YouTube and shares updates about it on Twitter.
It posts a [weekly report](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/.github/workflows/report.yml) of the top chart on Monday. Every day it [posts updates](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/.github/workflows/main.yml) such as: an artist's subscribers increased, an artist overtakes another artist and more.

You can [follow this bot on Twitter](https://twitter.com/mostSubYTMusic?s=09)

And you can also see the charts on the [web app](https://marco97pa.github.io/MostSubYTMusicChannels/)

It runs (almost) 24/7 thanks to GitHub Actions.

The script is the **main.py**.
Data is stored in [channels.csv](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/channels.csv) and it is updated every 5 ~ 30 minutes.

## Prerequisites
0. Clone this repository
1. Get your API Keys from [YouTube](https://developers.google.com/youtube/v3/getting-started) and [Twitter](https://developer.twitter.com/en/docs)
2. Paste them in the **main.py** file or set them as environment variables
3. Run `sudo pip3 install tweepy`

## How to use
Run **main.py** to check for new updates on the subscribers of the channels listed in channels.csv and eventually post on Twitter if there is any change.

If you run **main.py** with the **-report** flag, it will print (and tweet) a chart of the most subscribed channels

## The web app
A web app written in React using the [Ionic5](https://ionicframework.com/) framework is also available. You can [visit the website here](https://marco97pa.github.io/MostSubYTMusicChannels/).

Source is stored in the `/webapp` directory of the **main** branch.
The site is deployed on the **gh-pages** branch instead.
To deploy the website, follow [this really helpful guide](https://github.com/gitname/react-gh-pages)
