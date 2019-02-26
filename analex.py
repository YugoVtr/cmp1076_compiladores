# -*- coding: utf-8 -*-
"""

Analisador Léxico - Versao 1.0

"""
import re                                                         # Regex
from enum import Enum                                             # Enumeracao
import pprint                                                     # Impressao

# Enum para as Expressoes Regulares 
class Regex(Enum):
    ID = r'^([a-zA-Z]([a-zA-Z]|\d)*)'
    NUMBER = r'^((-?)(\d+)((\.\d+)?))'
    EQUAL = r'^(==)'
    LESSEQUAL = r'^(<=)'
    GREATEREQUAL = r'^(>=)'
    DIFFERENT = r'^(!=)'

# Enum para Palavras Reservadas 
class ReserverdWord(Enum):
    AND = 'OPR_LOG'
    OR = 'OPR_LOG'
    NOT = 'OPR_LOG'
    IF = 'IF'
    ELSE = 'ELSE'
    WHILE ='WHILE'
    
    @classmethod
    def isReservedWord(self, identifier="" ):
        for i, j in ReserverdWord.__members__.items():
            if i.lower() == identifier: 
                return True, Token(j.value, None)
        return False, None
            
# Classe para Manipular o Token
class Token:
    def __init__(self, tipo, valor): 
        self.tipo = tipo
        self.valor = valor 
    def __repr__(self):
        return str(self.__dict__)

# Classe para Analise Lexica
class AnaLex(object):

    def __init__(self, fileName='main.c'):
        # Ler Conteudo do Arquivo 
        file = open(fileName, "r")
        self.__content = file.read()
        file.close()
        
    @property
    def content(self):
        return self.__content
    
    def run(self, log=False):    
        # Dividir o conteudo por espaco para analisar cada String separadamente
        contentSplittingBySpace = str(self.__content).split()
            
        # Percorrer Conteudo
        tokenList = []; idList = {}
        for strSplitting in contentSplittingBySpace:
            token = []; identifier = {}
            token, identifier = self.analyzeWord( strSplitting )
            tokenList = tokenList + token
            idList = {**idList, **identifier}
           
        if log:
            # Salvar Tokens em Arquivo 
            self.saveInFile("tokenList.txt", tokenList)
    
            # Salvar Id's em Arquivo 
            self.saveInFile("idList.txt", idList)
        return tokenList, idList; 
    
    def analyzeWord(self, word="" ): 
        tokenList = []
        idList = {}
                
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
                idWord = foundId.pop()[0]; 
                # Verify if is reserved word 
                isReserved, reservedWordToken = ReserverdWord.isReservedWord( idWord )
                if isReserved:
                    token = reservedWordToken
                else: 
                    idList[idWord] = None
                    token = Token('ID', idWord)
                tokenList.append(token)
                word = re.sub(Regex.ID.value, '', word) 
                continue
            # ========================== PROCURAR NUMERO ==========================
            elif foundNumber:
                token = Token('NUM', foundNumber.pop()[0])
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
            
        return tokenList, idList   

    def saveInFile(self, name, obj):
        with open(name, "w") as outputFile:
            pprint.pprint(obj, outputFile)
            