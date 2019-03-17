# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account

#Attempting to fix credentials problem
credentials = service_account.Credentials.from_service_account_file(
    '/home/parul/rare_use/hackpsu/mood-songs/creds.json')

# Instantiates a client
client = language.LanguageServiceClient(credentials=credentials)

# The text to analyze
text = u'I want nicotine.'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude)) 
