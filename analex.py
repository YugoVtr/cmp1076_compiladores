# -*- coding: utf-8 -*-
"""
Spyder Editor

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
    
    """ Verifica se e uma palavra reservada 

    Keyword arguments:
    identifier -- palavra identificada (default "")
    
    Return: (2 Parametros de retorno)
    TRUE caso a palavra seja reservada, FALSE caso Contrario 
    TOKEN associado a palavra reservada, NONE caso nao seja reservada 
    """
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

""" Realiza a analise lexica em uma palavra (string)

Keyword arguments:
word -- palavra a ser analisada (default "")

Return: (2 Parametros de retorno)
Lista de Tokens associados a cada String
Dict de Identificadores associados a cada token ID (formato {nome:conteudo})
"""
def analyzeWord( word="" ): 
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

""" Manipula o codigo fonte para analise lexica 

Keyword arguments:
content -- codigo fonte como String

Return: (2 Parametros de retorno)
Lista de Tokens associados a todo o Codigo
Dict de Identificadores associados a cada token ID (formato {nome:conteudo})
"""
def anaLex(content):    
    # Dividir o conteudo por espaco para analisar cada String separadamente
    contentSplittingBySpace = content.split()
        
    # Percorrer Conteudo
    tokenList = []; idList = {}
    for strSplitting in contentSplittingBySpace:
        token = []; identifier = {}
        token, identifier = analyzeWord( strSplitting )
        tokenList = tokenList + token
        idList = {**idList, **identifier}
        
    return tokenList, idList;     

""" Escreve em um arquivo o conteudo formatado  

Keyword arguments:
name -- nome do arquivo
obj  -- objeto a ser escrito 

Return: None
"""
def saveInFile(name, obj):
    with open(name, "w") as outputFile:
        pprint.pprint(obj, outputFile)
            
def main(): 
    # Ler Conteudo do Arquivo 
    fileName = "exemp.txt"
    file = open(fileName, "r")
    content = file.read()
    
    # Analise Lexica 
    tokenList, idList = anaLex(content)
    
    # Imprimir no console 
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint({'TOKEN': tokenList})
    pp.pprint({'ID': idList})
    
    # Salvar Tokens em Arquivo 
    saveInFile("tokenList.txt", tokenList)
    
    # Salvar Id's em Arquivo 
    saveInFile("idList.txt", idList)
    
if __name__ == "__main__":
    main()