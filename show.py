#!/usr/bin/env python3
import csv
from rich.console import Console
from rich.table import Table

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

def show(channels):

    console = Console()

    table = Table(show_header=True, header_style="bold red")
    table.add_column("Name")
    table.add_column("Twitter", style="dim")
    table.add_column("YouTube Subscribers", justify="right")

    for channel in channels:
        table.add_row(channel["name"], "@"+channel["username"], str(int(channel["subs"])/1000000)+" Mln")

    console.print(table)
    print()
    console.print(":globe_with_meridians: You can see this chart in a fresh web app by visiting:")
    console.print(":link: https://marco97pa.github.io/MostSubYTMusicChannels/")
    print()

channels = load_channels()
show(channels)