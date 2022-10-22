#Colab Code
!pip install --upgrade spacy
import spacy

# Refer to the sizes of the models
# en_core_web_lg (large)
# en_core_web_md (medium)
# en_core_web_sm (small)
nlp = spacy.load('en_core_web_sm')
sentences = "Model differences are mostly statistical. In general, we do expect larger models to be better and more accurate overall. Ultimately, it depends on your use case and requirements. We recommend starting with the default models (marked with a star below)."
doc = nlp(sentences)
tokenized = list(doc)
print(tokenized)

# Part-of-Speech(POS)
# Text : The original word text
# Lemma : The base form of the word
# POS : The simple part-of-speech tag
# Tag : The detailed part-ofspeech tag
# Dep : Syntactic dependecy, i.e. the relation between tokens
# Shape : The word shape - capitalisation, punctuation, digits
# is alpha : Is the token an alpha character?
# is stop : Is the token part of a stop list, i.e. the most common words of the language?
str_format = "{:>20}" * 8
print(str_format.format('Text', 'Lemma', 'POS', 'Tag', 'Dep', 'Shape', 'is alpha', 'is stop'))
print("=" * 160)
for token in doc:
  print(str_format.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, str(token.is_alpha), str(token.is_stop)))

stopwords = spacy.lang.en.stop_words.STOP_WORDS
print(stopwords)

filtered = []
for word in doc:
  if not word.is_stop:
    filtered.append(word)
print(filtered)

# Dependecy Parsing
# Noun Chunking
# Text : The Original noun chunk text
# Root Text : The original text of the word connectiong the noun chunk to the rest of the parse
# Root Dep : Dependency relation connecting the root to its head
# Root Head Text : The text of the root token's head
noun_chunks_ = doc.noun_chunks
print("=" * 80)
str_format = "{:>20}{:>20}{:>20}{:>20}"
print(str_format.format('Text', 'Root Text', 'Root Dep', 'Root Head Text'))
print("=" * 80)

for chunk in noun_chunks_:
  print(str_format.format(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text))


# Navigating Parse Tree
for tok in doc:
  print(tok.text)
  children = list(tok.children)
  print("children : ", children, "head : ", tok.head if tok.head != tok else "Root Node")
  print("=" * 60)

# Name Entity Recognition(NER)
doc = nlp(sentences)
print('=' * 40)
str_format = "{:>20}" * 2
print(str_format.format('Text', 'NER'))
print('=' * 40)
for ent in doc.ents:
  print(str_format.format(ent.text, ent.label_))

# Reference : https://ungodly-hour.tistory.com/37