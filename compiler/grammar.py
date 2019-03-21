# -*- coding: utf-8 -*-
"""

Gramática 
@author: Yugo

"""
from compiler.lexer import Token

# Classe para Representar a gramatica
class Grammar(object):    
    def __init__(self):
        self.__space = 0
    
    def nextToken(self):
        self.__tokens.pop(0)
        
    @property
    def token(self):
        if len(self.__tokens):
            return self.__tokens[0]
        else:
            return Token(None, None)
    
    # ==========================  Producoes ===================================
    # programa -> lista_instrucoes
    def programa(self, tokens):
        self.__tokens = list( tokens )
        self.listaInstrucoes()
        return len(self.__tokens) == 0
    
    # lista_instrucoes -> instrucao ; lista_instrucoes | epsilon
    def listaInstrucoes(self): 
        if not self.token.tipo:
            pass
        else:
            self.instrucao()
            if self.token.valor == 'SEM':
                self.nextToken()
                self.listaInstrucoes()
            else: 
                raise Exception('; not found')
    
    # instrucao -> id = expressao
    #           -> escreva ( expressao )
    #           -> leia ( id )
    def instrucao(self):
        if self.token.tipo == 'ID': 
            self.nextToken()
            if  self.token.tipo == 'ATRIB':
                self.nextToken()
                self.expressao()
            else: 
                raise Exception('= not found')
        elif self.token.tipo == 'ESCREVA':
            self.nextToken()
            if self.token.valor == 'LPA':
                self.nextToken()
                self.expressao()
                if self.token.valor == 'RPA':
                    self.nextToken()
                else:
                    raise Exception(') not found')
            else:
                raise Exception('( not found')
        elif self.token.tipo == 'LEIA':
            self.nextToken()
            if self.token.valor == 'LPA':
                self.nextToken()
                self.token.tipo == 'ID'
                self.nextToken()
                if self.token.valor == 'RPA':
                    self.nextToken()
                else:
                    raise Exception(') not found')
            else:
                raise Exception('( not found')
        else:
            pass
            
    # expressao -> termo resto1
    def expressao(self): 
        self.termo()
        self.resto1()
    
    # resto1 -> + termo resto1 | - termo resto1 | epsilon
    def resto1(self):
        if self.token.valor in ['ADD', 'SUB']:
            self.nextToken()
            self.termo()
            self.resto1()
        else: 
            pass
            
    # termo -> fator resto2
    def termo(self):
        self.fator()
        self.resto2()
    
    # resto2 -> * fator resto2 | / fator resto2 | % fator resto2 | epsilon 
    def resto2(self): 
        if self.token.valor in ['MUL','DIV','MOD']:
            self.nextToken()
            self.fator()
            self.resto2()
        else:
            pass 
    
    # fator -> base resto3 | ( expressao )
    def fator(self): 
        if self.token.valor == 'LPA':
            self.nextToken()
            self.expressao()
            if self.token.valor == 'RPA':
                self.nextToken()
            else:
                raise Exception(') not found')
        else:
            self.base()
            self.resto3()
    
    # resto3 -> ^ expoente | epsilon
    def resto3(self): 
        if self.token.valor == 'POW':
            self.nextToken()
            self.expoente()
        else:
            pass
    
    # base -> id | num 
    def base(self): 
        if self.token.tipo == 'ID' or self.token.tipo == 'NUM':
            self.nextToken()
        else:
            raise Exception('ID or NUM was expected')
    
    # expoente -> id | num 
    def expoente(self): 
        if self.token.tipo == 'ID' or self.token.tipo == 'NUM':
            self.nextToken()
        else:
            raise Exception('ID or NUM was expected')
    