import re

#BrainWise Module - Interpretation
#Copyright (C) 2012 Timothy Pogue
#www.timothypogue.com
#me@timothypogue.com

#Important notice: This is only v1, and is still rudimentary. 
#This is not the finished product!

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
                output = rule[2](match.groups())
                return [rule[1], output]
            else:
                return "No interpretation"

