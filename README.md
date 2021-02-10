![Check updated stats](https://github.com/marco97pa/MostSubYTMusicChannels/workflows/Check%20updated%20stats/badge.svg)
![Weekly report](https://github.com/marco97pa/MostSubYTMusicChannels/workflows/Weekly%20report/badge.svg)
![Retweets daily](https://github.com/marco97pa/MostSubYTMusicChannels/workflows/Retweets%20daily/badge.svg)
![Twitter Follow](https://img.shields.io/twitter/follow/mostSubYTMusic?style=social)

![icon](https://pbs.twimg.com/profile_images/1321082040842887168/ndA1-fPV_200x200.jpg)

# Most Subscribed YouTube Music Channels

This **Python** bot checks the most subscribed music artist channels on YouTube and makes a top chart.

It runs (almost) 24/7 thanks to *GitHub Actions*.


## How to see the charts

### Web App

You see the charts on the [web app](https://marco97pa.github.io/MostSubYTMusicChannels/) in a nice Material UI.

The website can be "installed" as Web App on Android, iOS and Windows 10.

It has the benefits of the app and the advantages of the web: it takes zero space in memory but it can also work offline as a normal app would.

![Imgur](https://imgur.com/vKQvMhM.jpg)

### Using a console

Assuming that you have Python3 and pip installed on your machine:
1. `clone https://github.com/marco97pa/MostSubYTMusicChannels.git`
2. `cd MostSubYTMusicChannels`
3. `pip install rich`
4. `./show.py` 

![Imgur](https://imgur.com/8w0X2oc.jpg)

# Add a new artist
You can request a new artist (channel) to track by:
- Sending a direct message on Twitter
- [Opening a new issue](https://github.com/marco97pa/MostSubYTMusicChannels/issues/new) on Github
- Propose a change on the channels.csv file

Remember that only single **music** artist channels are approved and that it should have at least half subscribers of the most subscribed channel on YouTube.

*Example:*  
As of January 2020, Justin Bieber is the first with 60 Million subscribers.  
Only channels with at least 30 Million will be accepted.

## How it works (for developers)

The script is the **main.py**.

Data is stored in [channels.csv](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/channels.csv) and it is updated every 5 ~ 30 minutes using [GitHub Actions](https://github.com/marco97pa/MostSubYTMusicChannels/blob/master/.github/workflows/)


## Build your own
To build your own (maybe the Most subscribed YouTube Cooking channels?):
0. Clone this repository
1. Get your API Keys from [YouTube](https://developers.google.com/youtube/v3/getting-started)
2. Paste them in the **main.py** file or set them as environment variables
3. Run **main.py** to check for new updates on the subscribers of the channels listed in channels.csv 

## About the web app
The web app is written in React using the [Ionic5](https://ionicframework.com/) framework.

Source is stored in the `/webapp` directory of the **main** branch.
The site is deployed on the **gh-pages** branch instead.

To deploy the website, follow [this really helpful guide](https://github.com/gitname/react-gh-pages) and make sure that the generated index.html has the right paths to scripts, CSSes and other resources.
