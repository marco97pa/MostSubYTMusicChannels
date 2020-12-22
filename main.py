#!/usr/bin/env python3
import sys
import csv
import requests
import json
import datetime
from operator import itemgetter
import tweepy
import os

# Get API key for YouTube
youtube_api_key = os.environ.get('YOUTUBE_API_KEY')

# Get Twitter API keys
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_KEY')
access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')

def load_channels():
    """ Loads channels list from file

    Opens the channels.csv file, reads it and returns a dictionary from that file

    Returns:
        list: representing the list of channels
    """
    try:
        with open("channels.csv") as file:
            channel_dict = csv.DictReader(file)
            return list(channel_dict)
    except OSError:
        print("File could not be loaded")
        return None


def write_channels(channels):
    """ Writes channels list to file

    Opens the channels.csv file and writes to it the dictonary of the channels

    Args:
        channels (dict): the list of channels, each one with name, username, id and subs properties
    """
    keys = ["name", "username", "id", "subs","img"]
    with open("channels.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(channels)

def get_subscribers(channels):
    """ Gets the number of subscribers of one or more channels

    From the list of channels provided as argument, it takes the channel id and queries YouTube to get more info about the statistics of that channel(s)

    Args:
        channels (dict): the list of channels, each one with id property

    Returns:
        response: a list containing the statistics about the channels provided
    """
    assert type(channels) != None, "List of channels empty or invalid"
    print("Getting statistics from YouTube...")
    id_list = ""
    for channel in channels:
        id_list = id_list + channel["id"] + ","
    page = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + id_list + "&key=" + youtube_api_key)
    response = json.loads(page.content)
    return response

def update_subscribers(response, channels):
    """ Updates the number of subscribers of the channels and takes actions based on the changes

    It merges changes from the list of channels and the response provided as arguments.
    It checks if there is any change and takes the according actions such as invoke subs_notify_change().

    Args:
        channels (dict): the list of channels, each one with id and subs property
        response (response): the response provided from YouTube, containing the statistics of the channels above

    Returns:
        list: a list containing the channels, updated with new values
    """ 
    print("Updating subscribers...")
    for item in response["items"]:
        for channel in channels:
            if channel["id"] == item["id"]:
                if channel["subs"] != item["statistics"]["subscriberCount"]:
                    channel["subs"] = item["statistics"]["subscriberCount"]
                    subs_notify_change(channel)
    return channels

def subs_notify_change(channel):
    """ Takes actions on change of the number of subscriber of a channel

    It invokes a post on Twitter and adds this change to the log

    Args:
        channels (dict): a single channel
    """ 
    twitter_post("{} reached {} Million subscribers on YouTube\n@{} #music #youtube #stats".format(channel["name"], int(channel["subs"])/1000000, channel["username"]))
    log_message("{} reached {} Mln subs".format(channel["name"], int(channel["subs"])/1000000))

def check_if_ordered(channels):
    """ Checks if the list of channels is ordered
    
    If it is not, it invokes a Twitter post about this change: a channel "surpassed" another based on its subscribers count

    Args:
        channels (list): a list containing the channels
    """
    for i in range(len(channels) - 1):
        if channels[i]["subs"] < channels[i + 1]["subs"]:
            twitter_post("{} is now the #{} most subscribed music channel on YouTube with {} Million subs, surpassing {}\n@{} #music #youtube #stats"
            .format(channels[i+1]["name"], i+1, int(channels[i+1]["subs"])/1000000, channels[i]["name"], channels[i+1]["username"]))

def sort_channels(channels):
    """ Orders the list of channels based on the subscribers count, from the highest to the lowest

    Args:
        channels (list): a list containing the channels

    Returns:
        list: a list containing the channels sorted
    """
    return sorted(channels, key=itemgetter('subs'), reverse=True)

def report(channels):
    """ Setups a the report: a message containing the top channels based on the subs count.
    
    If the message exceeds the 280 chars limit, it is trimmed nicely to the last entry.

    Args:
        channels (list): a list containing the channels
    """
    msg = "Weekly report top #youtube #music channels\n"
    for channel in channels:
        old_msg = msg 
        msg += "@{} {} Mln\n".format(channel["username"], int(channel["subs"])/1000000)
        if len(msg) >= 280:
            msg = old_msg
            break
    twitter_post(msg[:-1])

def twitter_post(message):
    """ Post a message on Twitter (uses the Tweepy module)
    
    Args:
        message (str): a string containing the message to be posted
    """
    print(message+"\n")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)

def log_message(message):
    """ Appends a message in the log (the message.txt file)

    This file's contents will be used as text of the commit of changes on GitHub
    
    Args:
        message (str): a string containing the message to be logged
    """
    with open("message.txt", "a") as myfile:
        myfile.write(message+"\n")


def get_images(channels):
    """ Gets the images of one or more channels

    From the list of channels provided as argument, it takes the channel id and queries YouTube to get the image of that channel(s)

    Args:
        channels (dict): the list of channels, each one with id property

    Returns:
        response: a list containing the images of the channels provided, in many sizes
    """
    assert type(channels) != None, "List of channels empty or invalid"
    print("Getting images from YouTube...")
    id_list = ""
    for channel in channels:
        id_list = id_list + channel["id"] + ","
    page = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet&id=" + id_list + "&fields=items(id%2Csnippet%2Fthumbnails)&key=" + youtube_api_key)
    response = json.loads(page.content)
    return response

def update_images(response, channels):
    """ Updates the images of the channels

    Args:
        channels (dict): the list of channels, each one with id and img property
        response (response): the response provided from YouTube, containing the images of the channels above

    Returns:
        list: a list containing the channels, updated with new images
    """ 
    print("Updating images...")
    for item in response["items"]:
        for channel in channels:
            if channel["id"] == item["id"]:
                if channel["img"] != item["snippet"]["thumbnails"]["medium"]["url"]:
                    channel["img"] == item["snippet"]["thumbnails"]["medium"]["url"]
                    log_message("Image of {} updated".format(channel["name"]))
    return channels

# Main
channels = load_channels()
response = get_subscribers(channels)
channels = update_subscribers(response, channels)
check_if_ordered(channels)
channels = sort_channels(channels)
response = get_images(channels)
channels = update_images(response, channels)
write_channels(channels)

# If the -report argument is passed on script launch, generate the report
if len(sys.argv) > 1:
    if sys.argv[1] == "-report" or sys.argv[1] == "-r":
        report(channels)

