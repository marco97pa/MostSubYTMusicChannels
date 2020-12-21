#!/usr/bin/env python3
import sys
import csv
import requests
import json
import datetime
from operator import itemgetter
import tweepy
import os
from keys import youtube_key
from keys import twitter_keys

#Get API key for YouTube
youtube_api_key = os.environ.get('YOUTUBE_API_KEY')

#Get Twitter API keys
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_KEY')
access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')

def load_channels():
    try:
        with open("channels.csv") as file:
            channel_dict = csv.DictReader(file)
            return list(channel_dict)
    except OSError:
        print("File could not be loaded")
        return None

def write_channels(channels):
    keys = ["name", "username", "id", "subs"]
    with open("channels.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(channels)

def get_subscribers(channels):
    assert type(channels) != None, "List of channels empty or invalid"
    id_list = ""
    for channel in channels:
        id_list = id_list + channel["id"] + ","
    page = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + id_list + "&key=" + youtube_api_key)
    response = json.loads(page.content)
    return response

def update_subscribers(response, channels):
    for item in response["items"]:
        for channel in channels:
            if channel["id"] == item["id"]:
                if channel["subs"] != item["statistics"]["subscriberCount"]:
                    channel["subs"] = item["statistics"]["subscriberCount"]
                    subs_notify_change(channel)
    return channels

def subs_notify_change(channel):
    twitter_post("{} reached {} Million subscribers on YouTube\n@{} #music #youtube #stats".format(channel["name"], int(channel["subs"])/1000000, channel["username"]))
    log_message("{} reached {} Mln subs".format(channel["name"], int(channel["subs"])/1000000))

def check_if_ordered(channels):
    for i in range(len(channels) - 1):
        if channels[i]["subs"] < channels[i + 1]["subs"]:
            twitter_post("{} is now the #{} most subscribed music channel on YouTube with {} Million subs, surpassing {}\n@{} #music #youtube #stats"
            .format(channels[i+1]["name"], i+1, int(channels[i+1]["subs"])/1000000, channels[i]["name"], channels[i+1]["username"]))

def sort_channels(channels):
    return sorted(channels, key=itemgetter('subs'), reverse=True)

def report(channels):
    msg = "Weekly report top #youtube #music channels\n"
    for channel in channels:
        old_msg = msg 
        msg += "@{} {} Mln\n".format(channel["username"], int(channel["subs"])/1000000)
        if len(msg) >= 280:
            msg = old_msg
            break
    twitter_post(msg[:-1])

def twitter_post(message):
    print(message+"\n")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

def log_message(message):
    with open("message.txt", "a") as myfile:
        myfile.write(message+"\n")

channels = load_channels()
response = get_subscribers(channels)
channels = update_subscribers(response, channels)
check_if_ordered(channels)
channels = sort_channels(channels)
write_channels(channels)
if len(sys.argv) > 1:
    if sys.argv[1] == "-report" or sys.argv[1] == "-r":
        report(channels)

