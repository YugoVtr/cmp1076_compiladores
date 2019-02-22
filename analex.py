# -*- coding: utf-8 -*-
"""
Spyder Editor

Analisador Léxico - Versao 1.0 
"""
import re    

class Token:
    def __init__(self, tipo, valor): 
        self.tipo = tipo
        self.valor = valor 
        
def isReservedWord( identifier ):
    
    reservedWords = {
            'and': 'OPR_LOG',
            'or': 'OPR_LOG',
            'not': 'OPR_LOG',
            'if': 'IF',
            'else':'ELSE',
            'while':'WHILE',
            }
    
    if identifier in list(reservedWords.keys()):    
        return True, Token(reservedWords[identifier], None)
    return False, Token(None, None)

def analyzeWord( word ): 
    tokenList = []
    idList = []
    numberList = []
    
    for i in re.findall(r'([a-zA-Z]([a-zA-Z]|\d)*)', word):
        idList.append(i[0])
    
    for i in re.findall(r'([-]*\d+[.\d]+)', word):
        numberList.append(i)
    
    word = re.sub(r'([a-zA-Z]([a-zA-Z]|\d)*)', chr(1), word)
    word = re.sub(r'([-]*\d+[.\d]+)', chr(2), word)
    word = re.sub(r'==', chr(3), word) 
    word = re.sub(r'<=', chr(4), word) 
    word = re.sub(r'>=', chr(5), word) 
    word = re.sub(r'!=', chr(6), word) 
    
    for char in word :
        # Single char
        if char == '<':
            token = Token('OPR_REL', 'menor')
            tokenList.append(token)
            continue
        elif char == '>':
            token = Token('OPR_REL', 'maior')
            tokenList.append(token)
            continue
        elif char == '+':
            token = Token('OPR_AR', 'adicao')
            tokenList.append(token)
            continue
        elif char == '-':
            token = Token('OPR_AR', 'subtracao')
            tokenList.append(token)
            continue
        elif char == '*':
            token = Token('OPR_AR', 'multiplicacao')
            tokenList.append(token)
            continue
        elif char == '%':
            token = Token('OPR_AR', 'resto')
            tokenList.append(token)
            continue
        elif char == '/':
            token = Token('OPR_AR', 'divisao')
            tokenList.append(token)
            continue
        elif char == '^':
            token = Token('OPR_AR', 'potenciacao')
            tokenList.append(token)
            continue
        elif char == '(':
            token = Token('DELIM', 'parentesis esq')
            tokenList.append(token)
            continue
        elif char == ')':
            token = Token('DELIM', 'parentesis dir')
            tokenList.append(token)
            continue
        elif char == ',':
            token = Token('DELIM', 'virgula')
            tokenList.append(token)
            continue
        elif char == ';':
            token = Token('DELIM', 'ponto e virtula')
            tokenList.append(token)
            continue
        elif char == '.':
            token = Token('DELIM', 'ponto')
            tokenList.append(token) 
            continue
        elif char == '=':
            token = Token('ATRIB', None)
            tokenList.append(token) 
            continue
        elif char == chr(1):
            idWord = idList.pop(); 
            flag, reservedWordToken = isReservedWord(idWord)
            if flag:
                token = reservedWordToken
            else: 
                token = Token('ID', idWord)
            tokenList.append(token) 
            continue
        elif char == chr(2):
            token = Token('NUM', numberList.pop())
            tokenList.append(token) 
            continue
        elif char == chr(3):
            token = Token('OPR_REL', 'igual')
            tokenList.append(token) 
            continue
        elif char == chr(4):
            token = Token('OPR_REL', 'menor igual')
            tokenList.append(token) 
            continue
        elif char == chr(5):
            token = Token('OPR_REL', 'maior igual')
            tokenList.append(token) 
            continue
        elif char == chr(6):
            token = Token('OPR_REL', 'diferente')
            tokenList.append(token) 
            continue
        else:
            token = Token('ERRO', None)
            tokenList.append(token) 
        
    return tokenList
    
def anaLex(content):    
    # Dividir o conteudo por espaco 
    contentSplittingBySpace = content.split()
        
    # Percorrer Conteudo
    tokenList = []
    for strSplitting in contentSplittingBySpace:
        tokenList = tokenList + analyzeWord( strSplitting )
        
    return tokenList;     
            
def main(): 
    # Ler Conteudo do Arquivo 
    fileName = "exemp.txt"
    file = open(fileName, "r")
    content = file.read()
    
    # Analise Lexica 
    tokenList = anaLex(content)
    [print("Token ->\n\tTipo: {},\tValor: {}".format(token.tipo, token.valor)) for token in tokenList]

            
if __name__ == "__main__":
    main()