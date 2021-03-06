import codecs

import tweepy
from tweepy import *


import pandas as pd
import csv
import sys
from multiprocessing import Process


import re
import string
import preprocessor as p

# consumer_key = "ivtiXG3MO2jmFHY7afJIF6UhD"
# consumer_secret = "cohNK35JD05ci7BJDaM1krDMVD4LUyPQCUlf6XUSiBaTDE49j7"
# access_key = "795598438289129472-7jjuqTkYWm7U771AxFdXCFI1dWfI51g"
# access_secret = "ulU4SD2RNPkrp6iNsUJ5cYxLSsVD45BKRLio6S492U0FU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

if sys.stdout.encoding != 'u30fc':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'u30fc':
    sys.stderr.reconfigure(encoding='utf-8')

def EPL():
    csvFile = open('EPL', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("EPL Running")

    search_words = "EPL OR epl OR premier_league OR ManUtd OR ManCity OR Arsenal OR Chelsea OR spurs OR liverpool"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')], [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')], [tweet.entities["hashtags"]]])

#
def Laliga():
    csvFile = open('Laliga', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    search_words = "LaLiga OR LaLigaSantander OR FCBarcelona OR realmadrid OR FCB OR atlei "
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')], [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')], [tweet.entities["hashtags"]]])
#
def SerieA():

            csvFile = open('Italian', 'a', encoding='utf-8')
            csvWriter = csv.writer(csvFile)
            print("SerieA Running")

            search_words = "SerieA OR seriea OR juvantus OR juve OR acmilan OR napoli OR intermilan OR roma"
            new_search = search_words + " -filter:retweets"
            print(new_search)
            for tweet in tweepy.Cursor(api.search, q=new_search, count=10000,
                                       lang="en",
                                       since_id=0).items():
                # print(tweet.entities["hashtags"])
                # if "NFL" not in tweet.text.encode('utf-8'):


                csvWriter.writerow(
                    [[tweet.created_at], [tweet.text.encode('utf-8')], [tweet.user.screen_name.encode('utf-8')],
                     [tweet.user.location.encode('utf-8')], [tweet.entities["hashtags"]]])
#
def French():
                    csvFile = open('French', 'a', encoding='utf-8')
                    csvWriter = csv.writer(csvFile)
                    print("French Running")

                    search_words = "french_league OR WYN_LIGUE_1 OR psg OR lille OR monaco OR lyon"
                    new_search = search_words + " -filter:retweets"

                    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                                               lang="en",
                                               since_id=0).items():
                        # print(tweet.entities["hashtags"])
                        # if "NFL" not in tweet.text.encode('utf-8'):

                        csvWriter.writerow(
                            [[tweet.created_at], [tweet.text.encode('utf-8')], [tweet.user.screen_name.encode('utf-8')],
                             [tweet.user.location.encode('utf-8')], [tweet.entities["hashtags"]]])

def Others():
                            csvFile = open('Other_football', 'a', encoding='utf-8')
                            csvWriter = csv.writer(csvFile)
                            print("Others Running")

                            search_words = "Liga1 OR Primeira_Liga OR mls OR CSLfutbol OR EredivisieEN"
                            new_search = search_words + " -filter:retweets"

                            for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                                                       lang="en",
                                                       since_id=0).items():
                                # print(tweet.entities["hashtags"])
                                # if "NFL" not in tweet.text.encode('utf-8'):

                                csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                                                    [tweet.user.screen_name.encode('utf-8')],
                                                    [tweet.user.location.encode('utf-8')],
                                                    [tweet.entities["hashtags"]]])

def Bundesliga():
                                    csvFile = open('Budesliga', 'a', encoding='utf-8')
                                    csvWriter = csv.writer(csvFile)
                                    print("Budesliga Running")

                                    search_words = "Bundesliga_EN OR Bundesliga OR bayern OR bayern_munich"
                                    new_search = search_words + " -filter:retweets"

                                    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                                                               lang="en",
                                                               since_id=0).items():
                                        # print(tweet.entities["hashtags"])
                                        # if "NFL" not in tweet.text.encode('utf-8'):

                                        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                                                            [tweet.user.screen_name.encode('utf-8')],
                                                            [tweet.user.location.encode('utf-8')],
                                                            [tweet.entities["hashtags"]]])


def Cricket():
    csvFile = open('IPL', 'a',encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("Cricket Running")
    search_words = "ipl OR IPL OR ipl2021 OR RR OR CSK OR RCB OR MI OR SRH OR KKR OR DC"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')], [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')], [tweet.entities["hashtags"]]])


def Tennis():
    csvFile = open('TENNIS', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("Tennis Running")

    search_words = "atptour OR ATPChallenger OR usopen OR french_open OR AustralianOpen OR Wimbledon OR federer OR nadal OR rolandgarros OR rogerfederer OR RafaelNadal OR DjokerNole"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])

def IceHockey():
    csvFile = open('IceHockey', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("IH Running")

    search_words = "IIHFHockey OR usahockey OR BritIceHockey OR HockeyCanada OR hockeynight OR TSNHockey OR IceHockeyUK"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])

def FieldHockey():
    csvFile = open('FieldHockey1', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("FH Running")

    search_words = "TheHockeyIndia OR FIH_Hockey OR eurohockeyorg OR HockeyIndiaLeag"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                        ])


def NBA():
    csvFile = open('NBA', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("NBA Running")

    search_words = "nba OR NBA OR basketball OR RealABAleague OR EuroLeague"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])

def Volleyball():
    csvFile = open('Volley', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("volley Running")

    search_words = "volleyballworld OR Volleyball OR volleyball OR VNL OR FIVB OR NORCECA OR usavolleyball OR CEVolleyball"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])


def TableTennis():
    csvFile = open('TT', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("TT Running")

    search_words = "UltTableTennis OR TableTennis OR ITTF OR iitfworld"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])


def Baseball():
    csvFile = open('baseball', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    print("baseball  Running")

    search_words = "MLB OR Baseball OR MLBNetwork"
    new_search = search_words + " -filter:retweets"

    for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
                               lang="en",
                               since_id=0).items():
        # print(tweet.entities["hashtags"])
        # if "NFL" not in tweet.text.encode('utf-8'):

        csvWriter.writerow([[tweet.created_at], [tweet.text.encode('utf-8')],
                            [tweet.user.screen_name.encode('utf-8')],
                            [tweet.user.location.encode('utf-8')],
                            [tweet.entities["hashtags"]]])


if __name__ == '__main__':
    p1 = Process(target=Cricket())
    # p1.run()
    p2 = Process(target=Bundesliga())
    p2.run()
    p3 = Process(target=Others())
    p3.run()
    p4 = Process(target=Laliga())
    p4.run()
    p5 = Process(target=SerieA())
    p5.run()
    p6 = Process(target=EPL())
    p6.run()
    p7 = Process(target=French())
    p7.run()
    p8 = Process(target=Tennis())
    p8.run()
    p9 = Process(target=IceHockey())
    p9.run()
    p10 = Process(target=FieldHockey())
    p10.run()
    p11 = Process(target=NBA())
    p11.run()
    p12 = Process(target=Volleyball())
    p12.run()
    p13 = Process(target=TableTennis())
    p13.run()
    p14 = Process(target=Baseball())
    p14.run()
















