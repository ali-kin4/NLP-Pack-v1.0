from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = input("Please enter your desired text: ")

from googletrans import Translator
translator = Translator()

mytext = translator.translate(text, dest = 'en').text

sentences = [] 
sentences.append(mytext) 
sid = SentimentIntensityAnalyzer()

for sentence in sentences:
	ss = sid.polarity_scores(sentence)

if (ss['neg'] > ss['pos']):
        print("This text is negative. | Negative value: " + str(ss['neg']) + " | Positive value: " + str(ss['pos']))
else:
        print("This text is positive. | Negative value: " + str(ss['neg']) + " | Positive value: " + str(ss['pos']))
        
