"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
from pygame import mixer
import random
import time

#Attempting to fix credentials problem
credentials = service_account.Credentials.from_service_account_file(
    '/home/parul/rare_use/hackpsu/mood-songs/creds.json')


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient(credentials=credentials)

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
    print(content)

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    sentiment = annotations.document_sentiment

    # Print the results
    print(sentiment.score, sentiment.magnitude)
    print_result(annotations)

    return sentiment


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()
    #movie_review_filename = 'reviews/bladerunner-neg.txt'
    sentiment = analyze(args.movie_review_filename)
    #print(sentiment.score, sentiment.magnitude)
    r = random.randint(1,4)
    print(r)
    if sentiment.score<0:
    	print('Its sad!')
    	song = "songs/sad/"+str(r)+".mp3"
    else:
    	print('Its happy!')
    	song = "songs/happy/"+str(r)+".mp3"
    mixer.init()
    mixer.music.load(song)
    print('Playing music')
    mixer.music.play()
    time.sleep(120)
    print('Exiting...')