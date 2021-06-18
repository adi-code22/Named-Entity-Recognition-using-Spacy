import spacy
import spacy.displacy as displacy
from scrape import text

nlp = spacy.load("en_core_web_lg")

doc = nlp(text)

for ents in doc.ents:
    print(ents.text, ents.start_char, ents.end_char, ents.label_)
displacy.serve(doc, style='ent')
# python -m spacy download en_core_web_lg
