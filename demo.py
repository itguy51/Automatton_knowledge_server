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
    
}

#important note: The paramteres passed to the function is a tuple, 
#that contains the match groups, and the whole input
rules = [
    ["([Ww]hat|[Ww]hy|[Ww]hen|[Ww]ho|[Hh]ow|[Dd]id|[Ww]ill)(.*)", "question", lambda args: answerQuestion(args)],
    ["[Cc]onvert \d pounds to kilograms", "conversion", lambda args: convert(args, "Poundstokilograms")]
]

bw = BrainWise(rules, grammar)

print bw.interpret("Who killed abraham lincoln?")
