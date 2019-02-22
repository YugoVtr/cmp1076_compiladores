# -*- coding: utf-8 -*-
"""
Spyder Editor

Analisador Léxico - Versao 1.0 
"""
import re    
from enum import Enum 
class Regex(Enum):
    ID = r'^([a-zA-Z]([a-zA-Z]|\d)*)'
    NUMBER = r'^((-?)(\d+)((\.\d+)?))'
    EQUAL = r'^(==)'
    LESSEQUAL = r'^(<=)'
    GREATEREQUAL = r'^(>=)'
    DIFFERENT = r'^(!=)'

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
              
    while len(word) > 0 : 
        char = word[0]
        
        # Verify if Start at Regex 
        foundId =           re.findall(Regex.ID.value, word)
        foundNumber =       re.findall(Regex.NUMBER.value, word)
        foundEqual =        re.findall(Regex.EQUAL.value, word)
        foundLessEqual =    re.findall(Regex.LESSEQUAL.value, word)
        foundGreaterEqual = re.findall(Regex.GREATEREQUAL.value, word)
        foundDifferent =    re.findall(Regex.DIFFERENT.value, word)

        # ============== PROCURAR ID E PALAVRAS RESERVADAS ====================
        if foundId:
            for i in foundId:
                idWord = i[0]; 
            # Verify if is reserved word 
            isReserved, reservedWordToken = isReservedWord(idWord)
            if isReserved:
                token = reservedWordToken
            else: 
                token = Token('ID', idWord)
            tokenList.append(token)
            word = re.sub(Regex.ID.value, '', word) 
            continue
        # ========================== PROCURAR NUMERO ==========================
        elif foundNumber:
            for i in foundNumber:
                token = Token('NUM', i[0])
            tokenList.append(token)
            word = re.sub(Regex.NUMBER.value, '', word) 
            continue
        # ======================= PROCURAR IGUAL ==============================
        elif foundEqual:
            token = Token('OPR_REL', 'igual')
            tokenList.append(token)
            word = re.sub(Regex.EQUAL.value, '', word) 
            continue
        # =================== PROCURAR MENOR IGUAL ============================       
        elif foundLessEqual:
            token = Token('OPR_REL', 'menor igual')
            tokenList.append(token)
            word = re.sub(Regex.LESSEQUAL.value, '', word)  
            continue
        # =================== PROCURAR MAIOR IGUAL ============================
        elif foundGreaterEqual:
            token = Token('OPR_REL', 'maior igual')
            tokenList.append(token)
            word = re.sub(Regex.GREATEREQUAL.value, '', word) 
            continue
        # =================== PROCURAR DIFERENTE IGUAL ========================
        elif foundDifferent:
            token = Token('OPR_REL', 'diferente')
            tokenList.append(token)
            word = re.sub(Regex.DIFFERENT.value, '', word) 
            continue
        
        # ================ PROCURAR CARACTERES INDIVIDUAIS ====================
        word = "".join(list(word)[1:len(word)])
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