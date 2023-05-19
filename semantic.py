import spacy

#Assinging the weaker model to nlp_compare to test the differences between the two

nlp = spacy.load("en_core_web_md")
nlp_compare = spacy.load("en_core_web_sm")

#Applying the advanced model notices similarities between the actual words - monkey and banana are more closely related than monkey
#and apple

tokens1 = nlp("cat apple monkey banana")

for token1 in tokens1:
    for token2 in tokens1:
        print(token1.text, token2.text, token1.similarity(token2))

#Trying the less advanced model yields results which are based on similarities of the words themselves rather than their definitions.

tokens2 = nlp_compare("cat apple monkey banana")

for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))
