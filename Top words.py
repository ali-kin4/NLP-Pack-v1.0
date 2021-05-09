from rake_nltk import Rake
import clipboard
# text = open('text.txt', encoding="utf8").read()
text = clipboard.paste()
# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

r.extract_keywords_from_text(text)

# Extraction given the list of strings where each string is a sentence.
# r.extract_keywords_from_sentences(text)

# To get keyword phrases ranked highest to lowest.
r.get_ranked_phrases()

# To get keyword phrases ranked highest to lowest with scores.
bb = r.get_ranked_phrases_with_scores()

for p in bb:
	print(p)