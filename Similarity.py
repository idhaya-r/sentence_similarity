import spacy
nlp = spacy.load("en_core_web_lg")


def sentence_similarity(sentence_1,sentence_2):
    doc1 = nlp(sentence_1)
    doc2 = nlp(sentence_2)
    return doc1.similarity(doc2)