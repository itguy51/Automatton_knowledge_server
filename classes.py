import re
import cosmeasure
from bs4 import BeautifulSoup
import urllib

#BrainWise - Query interpretation using regex
#v1

class BrainWise:
    #Store rules and grammar
    def __init__(self, rules, grammar):
        self.rules = rules
        self.grammar = grammar
        
    def interpret(self, input):
        #Iterate of rules and check each one
        for rule in self.rules:
            pattern = rule[0]
            #Replace each grammar value in the pattern with the grammar pattern
            for grammar in re.findall("\/([a-zA-z\-\_]*)\/", rule[0]):
                pattern = pattern.replace("/" + grammar + "/", self.grammar[grammar])
            
            #Check if pattern matches
            match = re.match(pattern, input)
            if match:
                #Ok yay it does match, do the function call back
                #Pass the paramters and return the value
                
                #Values that are passed are the matched values
                #Passes a tuple
                output = rule[2]([match.groups(), input])
                return [rule[1], output]
            else:
                return "No interpretation"

#DeepThought module - Question Answering
#v1

class DeepThought:
    def answer(self, question):
        #Don't forget to encode the question!
        question = urllib.quote_plus(question)
        
        #Scrape results from ask.com
        #NOTE: This is only temporary, I'm going to build a database of questions instead of using ask
        soup = BeautifulSoup(urllib.urlopen("http://www.ask.com/web?q=" + question + "&search=&qsrc=0&o=0&l=dir"))
        
        i = 0
        similarity = {}
        
        #iterate over each div in ask results and put together list of similarity between questions
        for div in soup.find_all("div", class_="ptbs"):
            if div.find("span", class_="ofh txt_lg") is not None:
                ask_question = div.find("span", class_="ofh txt_lg").get_text()
                div_similarity = self.similarity(str(ask_question), str(question))
                similarity[div_similarity] = i
            i = i + 1
        
        #sort similarity list in descending order
        similarity = self.krsort(similarity)
        
        for (measurement, i) in similarity.iteritems():
            if measurement > 0.85:
                #if the similarity between the question is above threshold
                #then get the answer text and source link then return them
                answer_div = soup.find_all("div", class_="ptbs")[i]
                answer = answer_div.find("div", class_="txt3 abstract").get_text()
                source = answer_div.find("div", class_="attrib txt3").get_text()
                
                return [answer, source]
        
    def similarity(self, s, p):
        #We want a percentage of the similarity
        return cosmeasure.compare(s, p)
        
    def krsort(self, dic):
        #Sort a dictionary by key (similarity measurement) in descending order
        newdict = {}
        for key in sorted(dic.iterkeys()):
            newdict[key] = dic[key]
        return newdict