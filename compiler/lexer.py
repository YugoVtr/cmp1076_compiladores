# -*- coding: utf-8 -*-
"""

Analisador Léxico - Versao 1.0
@author: Yugo

"""
import re                                                         # Regex
import pprint                                                     # Impressao
from enum import Enum                                             # Enumeracao

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
    AND =     'OPR_LOG'
    OR =      'OPR_LOG'
    NOT =     'OPR_LOG'
    IF =      'IF'
    ELSE =    'ELSE'
    WHILE=    'WHILE'
    LEIA =    'LEIA'
    ESCREVA = 'ESCREVA'
    
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
class Lexer(object):

    def __init__(self, fileName):
        if not fileName: 
            raise Exception('arquivo nao informado')
            
        # Ler Conteudo do Arquivo 
        file = open(fileName, "r")
        
        if not file: 
            raise Exception('arquivo nao encontrado')
            
        self.__content = file.read()
        file.close()
        
    @property
    def content(self):
        return self.__content
    
    def lexicalAnalysis(self):    
        # Dividir o conteudo por espaco para analisar cada String separadamente
        contentSplittingBySpace = str(self.__content).split()
            
        # Percorrer Conteudo
        tokenList = []; idList = {}
        for strSplitting in contentSplittingBySpace:
            token = []; identifier = {}
            token, identifier = self.analyzeWord( strSplitting )
            tokenList = tokenList + token
            idList = {**idList, **identifier}
           
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
                token = Token('OPR_REL', 'EQU')
                tokenList.append(token)
                word = re.sub(Regex.EQUAL.value, '', word) 
                continue
            # =================== PROCURAR MENOR IGUAL ============================       
            elif foundLessEqual:
                token = Token('OPR_REL', 'LEQ')
                tokenList.append(token)
                word = re.sub(Regex.LESSEQUAL.value, '', word)  
                continue
            # =================== PROCURAR MAIOR IGUAL ============================
            elif foundGreaterEqual:
                token = Token('OPR_REL', 'GEQ')
                tokenList.append(token)
                word = re.sub(Regex.GREATEREQUAL.value, '', word) 
                continue
            # =================== PROCURAR DIFERENTE IGUAL ========================
            elif foundDifferent:
                token = Token('OPR_REL', 'INE')
                tokenList.append(token)
                word = re.sub(Regex.DIFFERENT.value, '', word) 
                continue
            
            # ================ PROCURAR CARACTERES INDIVIDUAIS ====================
            word = "".join(list(word)[1:len(word)])
            if char == '<':
                token = Token('OPR_REL', 'LES')
                tokenList.append(token)
                continue
            elif char == '>':
                token = Token('OPR_REL', 'GRE')
                tokenList.append(token)
                continue
            elif char == '+':
                token = Token('OPR_AR', 'ADD')
                tokenList.append(token)
                continue
            elif char == '-':
                token = Token('OPR_AR', 'SUB')
                tokenList.append(token)
                continue
            elif char == '*':
                token = Token('OPR_AR', 'MUL')
                tokenList.append(token)
                continue
            elif char == '%':
                token = Token('OPR_AR', 'MOD')
                tokenList.append(token)
                continue
            elif char == '/':
                token = Token('OPR_AR', 'DIV')
                tokenList.append(token)
                continue
            elif char == '^':
                token = Token('OPR_AR', 'POW')
                tokenList.append(token)
                continue
            elif char == '(':
                token = Token('DELIM', 'LPA')
                tokenList.append(token)
                continue
            elif char == ')':
                token = Token('DELIM', 'RPA')
                tokenList.append(token)
                continue
            elif char == ',':
                token = Token('DELIM', 'COM')
                tokenList.append(token)
                continue
            elif char == ';':
                token = Token('DELIM', 'SEM')
                tokenList.append(token)
                continue
            elif char == '.':
                token = Token('DELIM', 'DOT')
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
            