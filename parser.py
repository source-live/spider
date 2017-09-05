#!env/python
from sys import *

file = open(argv[1],"r")
tokens = []

def open_file(fn):
  data = open(fn,"r").read()
  data += "<EOF>"
  
def lex(cont):
  tok = ""
  state = 0
  cont = list(cont)
  string = ""
  expr = ""
  n = ""
  isexpr = 0
  
  for char in cont:
    #print(char)
    tok += char
    if tok == " ":
      if state == 0:
        tok = ""
      else:
        tok = " "
    elif tok == "\n" or tok == "<EOF>":
      if expr != "" and expr == 1:
        tokens.append("EXPR:" + expr)
        expr = ""
      elif expr != "" and expr == 0:
        tokens.append("NUM:" + expr)
        expr = ""
      tok = ""
    elif tok == "len":
      tokens.append("LEN")
    elif tok == "print":
      tokens.append("PRINT")
      tok = ""
    elif tok == "fprint":
      tokens.append("FPRINT")
      tok = ""
    elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
      expr += tok
      tok = ""
    elif tok == "+" or tok == "-" or tok == "/" or tok == "*" or tok == "(" or tok == ")":
      isexpr = 1
      expr += tok
      tok = ""
    elif tok == "\"":
      if state == 0:
        state = 1
      elif state == 1:
        tokens.append("STRING:" + string + "\"")
        state = 0
        string = ""
        tok = ""
    elif state == 1:
      string += tok
      tok = ""
  return tokens
  
def doPrint(toPrint):
  if toPrint[0:6] == "STRING":
    toPrint = toPrint[0:8]
    toPrint = toPrint[:-1]
  elif toPrint[0:3] == "NUM":
    toPrint = toPrint[0:4]
  elif toPrint[0:4] == "STRING":
    toPrint = toPrint[0:5]
  print(toPrint)
  
def parse(toks):
  i = 0
  while i < len(toks):
    if toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
      if toks[i+1][0:6] == "STRING":
        doPrint(toks[i+1])
      elif toks[i+1][0:3] == "NUM":
        doPrint(toks[i+1])
      elif toks[i+1][0:4] == "EXPR":
        doPrint(toks[i+1])
      i += 2
    elif toks[i] + " " + toks[i+1][0:6] == "FPRINT STRING":
      print("CLIENTSIDE:"toks[i+1][7:])
    elif toks[i] + " " + toks[i+1] + " " + toks[i+2][0:6] == "PRINT LEN STRING":
      print(len(toks[i+2][7:]))

def run()
  toks = lex(file)
  parse(toks)
  
run()
