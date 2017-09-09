from pyparsing import *

class Spider:
  def __init__(f):
    # Open file:
    f = open(f,"r").read()
    
    # Define variables
    LBRACE,RBRACE,LPAREN,RPAREN,SEMI,COL,AT,DOT,EQ = map(Suppress,"{}();:@.=")
    real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
    integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
    string = QuotedString('"')
    
    # Keywords
    REAL = Keyword("real")
    INTEGER = Keyword("integer")
    
    # Parser
    con = Forward()
    con >> Group(LBRACE + ZeroOrMore((norm | num | f)) + RBRACE)
    
    norm = Group(word(alphas) + EQ + string("norm") + SEMI)
    num = Group(word(alphas) + EQ + integer + SEMI)
    f = Group(word(alphas) + EQ + real + SEMI)
    comment = Literal('~').suppress() + Optional(restOfLine)
    
    con.ignore(comment)

    result = tree.parseString(data)
    
    print(result.asList())
