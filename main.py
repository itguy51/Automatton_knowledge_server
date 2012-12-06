from classes import *

#EXAMPLE FUNCTIONS_______________________________________
def convert(args, rule):
    
    #args[0][0] is the first match in the groups argument
    conversion_table = {
        "Poundstokilograms": args[0][0] * 0.453592  
    }
    
    return conversion_table[rule]
    
def answerQuestion(args):
    dt = DeepThought()
    #args[1] is the whole input
    return dt.answer(args[1])
#________________________________________________________

grammar = {
    "NUMBER" : "([0-9\.\*\ ]*)"
}

#important note: The paramteres passed to the function is a tuple, 
#that contains the match groups, and the whole input
rules = [
    ["[Cc]onvert /NUMBER/ pounds to kilograms", "conversion", lambda args: convert(args, "Poundstokilograms")],
    #For some reason, interpretation won't work unless this rule, is at the bottom
    ["([Ww]hat|[Ww]hy|[Ww]hen|[Ww]ho|[Hh]ow|[Dd]id|[Ww]ill)(.*)", "question", lambda args: answerQuestion(args)]
]

bw = BrainWise(rules, grammar)

