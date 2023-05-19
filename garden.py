import spacy

#Assigning the English language model to the variable NLP

nlp = spacy.load('en_core_web_sm')

#Setting the list as garden path sentences sourced on the internet and the 3 given in the task.

gardenpathSentences = ["The complex houses married and single soldiers and their families.", 
                       "The old man the boat.",
                       "Mary gave the child a Band-Aid", 
                       "That Jill is never here hurts", 
                       "The cotton clothing is made of grows in Mississipi"]

#Using a for loop to iterate through the list applying tokenisation and name entity recognition to each sentence.
#Name entity recognition will go through the sentence and locate tokens which are recognised as being entities such as a place, or a
#name, or a currency.

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([token.orth_ for token in doc])
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

#This returned Mississipi as GPE which I was unsure of, so I used spacy.explain and it clarified that GPE is countries, cities or states


print(spacy.explain("GPE"))  
print(spacy.explain("PERSON"))     
print(spacy.explain("ORG"))    

#Person is explained as being people fictional and real and ORG is explained as being any company agency or institution.
#This makes sense based on the label
