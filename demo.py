from brainwise import *

#Our little demo function
def convertkilotopounds(g):
    #g is a tuple of the matched values, in this case it would be whatever number you put in:
    #convert * kilograms to pounds
    #The value returned in this function is the second value in the return object of BrainWise
    return int(g[0]) * 2.20462
    
    
#First define a grammar ditionary object
#The grammar object consists of a grammar value,
#and grammar pattern
grammar = {
    "NUMBER" : "([0-9\.\^\*]*)"
}

#Now define a rules object
#The rules object consists of a regex pattern,
#the name of the interpretation, and
#a call back lambda function

#*Note: grammar value must be wrapped in /
#Example: /NUMBER/
#Example: /ADDRESS/
rules = [
    ["convert /NUMBER/ kilograms to pounds", "conversion", lambda g: convertkilotopounds(g)] 
]

#Tell BrainWise to learn the rules and grammar
bw = BrainWise(rules, grammar)

#Have BrainWise do all of the hard work
#It will return a tuple that looks like:
#[conversion name, return value from the call back function]
print bw.interpret("convert 6 kilograms to pounds")