from summarize import summarize
import clipboard

sentence_count = input("Select number of sentences: ")
sentence_count = int(sentence_count)
# text = open('text.txt', encoding="utf8").read()
text = clipboard.paste()

summarized = summarize(text, sentence_count, language='english')

clipboard.copy(summarized)
print(summarized)