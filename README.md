# Most Subscribed YouTube Music Channels
This Python bot checks the most subscribed music artist channels on YouTube and shares updates about it on Twitter.
It posts a weekly report of the top chart on Monday. Every day it posts updates such as: an artist's subscribers increased, an artist overtakes another artist and more.

You can [follow this bot on Twitter](https://twitter.com/mostSubYTMusic?s=09)

And you can also see the charts on the [web app](https://marco97pa.github.io/MostSubYTMusicChannels/)


It runs (almost) 24/7 on a Raspberry Pi and it also updates the data on this repository.

The script is the **main.py** and data are stored in [channels.csv](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/channels.csv)

## Prerequisites
1. Get your API Keys from [Youtube](https://developers.google.com/youtube/v3/getting-started) and [Twitter](https://developer.twitter.com/en/docs)
2. Paste them in the **main.py** file
3. Run `sudo pip3 install tweepy`

## How to use
Run **main.py** to check for new updates on the subscribers of the channels listed in channels.csv and eventually post on Twitter if there is any change

BONUS: If you run **main.py** with the **-report** flag, it will print (and tweet) a chart of the most subscribed channels

## The web app
A web app written in React using the Ionic5 framework is also available. You can [visit the website here](https://marco97pa.github.io/MostSubYTMusicChannels/).

Source is stored in the `/webapp` directory of the main branch.
The site is deployed on the gh-pages branch instead.
To deploy the website, follow [this really helpful guide](https://github.com/gitname/react-gh-pages)
