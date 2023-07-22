import json
import os
from deep_translator import MyMemoryTranslator

#import pandas
#from pandas import json_normalize

load_dotenv()
apikey=os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

def english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation

def french_to_english(text):
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation

print(englishtofrench(''))
print(frenchtoenglish('Bonjour'))