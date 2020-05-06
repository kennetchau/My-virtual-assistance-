"""Description: This is a self-learning chatbot"""

#import libraries
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

#Ignore any warning messages
warnings.filterwarnings('ignore')

#Download the packages from NLTK
#nltk.download('punkt')
#nltk.download('wordnet', quiet = True)

#Get the article URL
article = Article('https://www.cbc.ca/radio/asithappens/vancouver-doctor-s-portraits-show-the-two-different-lives-of-health-care-workers-1.5549297')
article.download()
article.parse()
article.nlp()
corpus = article.text

#print the corpus/text
#print(corpus)

#Tokenization
text = corpus
sent_tokens = nltk.sent_tokenize(text) #Convert the text into a list of sentences

#Print the list of sentences
##print(sent_tokens)

#Create
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

#Create a function to return a list of lematized lower case words after removing punctuations
def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

#print the tokenization text
# print(LemNormalize(text))

#Keyword Matching
#Greeting Inputs
GREETING_INPUT = ["hi","hello","hola","Greeting","hey"]

#Greeting responses back to the user
GREETING_RESPONSE = ["howdy", "hi", "hey", "what's good", "Hey there"]

def greeting(sentence):
    #if the user's input is a greeting, the return a randomly chosen greeting response
    for word in sentence.split():
        if word.lower() in GREETING_INPUT:
            return random.choice(GREETING_RESPONSE)

# Generate the response
def response(user_response):

    #The User response
    #user_response = 'What is the first step'
    user_response = user_response.lower() #Make the response lower case

    #Print the user query/ response
    #print(user_response)

    #Set the chatbot response to an empty string
    robo_response = ''

    #Append the user response to the sentence list
    sent_tokens.append(user_response)

    #Print the sentence list after appending the users response
    #print(sent_tokens)

    #Create a TfidfVectorizer Object
    TfidfVec = TfidfVectorizer(tokenizer= LemNormalize , stop_words='english')

    #Convert the text to a matrix of TF-IDF features
    tfidf = TfidfVec.fit_transform(sent_tokens)

    #Print the TFIDF features
    #print(tfidf)

    #Get the measure of similarity (similarity scores)
    vals = cosine_similarity(tfidf[-1],tfidf)
    #print(vals)

    #Get the index of the most similar text/ sentence to the users response
    idx = vals.argsort()[0][-2]

    #Reduce the dimensionality of vals
    flat = vals.flatten()

    #sort the list in ascending order
    flat.sort()

    #get the most similar score to the users response
    score = flat[-2]

    #Print the similarity score
    #print(score)

    #If the variable 'score' is 0 then there is no text similar to the users response
    if (score ==0):
        robo_response = robo_response + "I apologize, I don't understand."
    else:
        robo_response = robo_response + sent_tokens[idx]

    #Print the chat bot response
    #print(robo_response)
    #remove the users response from tokens list
    sent_tokens.remove(user_response)
    return robo_response


flag = True
print("Hi, I am your first chatbot. I will try to answer your answer about alberta first step to open the economy. If you want to exit, type bye")
while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("You're welcome!")
        else:
            if(greeting(user_response)!= None):
                print(greeting(user_response))
            else:
                print(response(user_response))
    else:
        flag = False
        print("Chat Later!")