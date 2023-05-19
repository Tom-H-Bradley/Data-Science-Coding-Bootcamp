import spacy
import os

#Using the more sophisticated language processing model for this task

nlp = spacy.load("en_core_web_md")

just_watched = """will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the Illuminati trick
 Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately Hulk lands on the planet 
 Sakaar where he is sold into slavery and trained as a gladiator """

#This is a piece of code that my friend, a computer scientist, helped me with. The code within the brackets returns a string that is
#the location of the current python file.
#The code outside the brackets finds the directory name of that file, and returns it as a string

base = os.path.dirname(os.path.abspath(__file__))

#This piece of code joins the string of the directory, with the text file that we wish to read from, then the readline() method
#returns a list with each line as string within that list.

file = open(base + "\movies.txt", "r")
file_by_line = file.readlines()

#As each line has \n at the end to create a new line, we have to remove those to analyse the data properly.

for line in file_by_line:
    line = line.strip("\n")

#The below function takes the text of the previously watched film, and creates a list with the values of similarity compared to
#the list of movies to watch next.
#It then selects the movie with the highest similarity and prints out the description as a suggestin with some flavour text.

def watch_next(previous_des):
    model_sentence = nlp(previous_des)
    similarities = []
    for description in file_by_line:
        similarity = nlp(description).similarity(model_sentence)
        similarities.append(float(similarity))
    recommended =  file_by_line[similarities.index(max(similarities))]
    print(f"Why not try the below film? \n{recommended}")


watch_next(just_watched)









