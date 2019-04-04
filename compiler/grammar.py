# -*- coding: utf-8 -*-
"""

Gramática 
@author: Yugo

"""
from compiler.lexer import Token

# Classe para Representar a gramatica
class Grammar(object):    
    def __init__(self, tokens, ids):
        self.__tokens = list( tokens )
        self.__ids = dict( ids )
        self.__stack = list()
        self.__error = Exception()
    
    def nextToken(self):
        if self.__tokens:
            self.__tokens.pop(0)
        
    @property
    def token(self):
        if len(self.__tokens):
            return self.__tokens[0]
        else:
            return Token(None, None)
    
    @property 
    def errorHandling(self):
        return self.__error

    # ==========================  Producoes ===================================
    # programa -> lista_instrucoes
    def programa(self):
        try:
            self.listaInstrucoes()
        except ValueError:
            self.__error = Exception("Only numbers be expected")
        except Exception as error:
            self.__error = error
        finally:
            return len(self.__tokens) == 0 and len(str( self.__error )) == 0
    
    # lista_instrucoes -> instrucao ; lista_instrucoes | epsilon
    def listaInstrucoes(self): 
        self.instrucao()
        if self.token.valor == 'SEM':
            self.nextToken()
            self.listaInstrucoes()
        elif not self.token.tipo:
            self.nextToken()
            pass
        else: 
            raise Exception('; not found')
    
    # instrucao -> id = expressao
    #           -> escreva expressao
    #           -> leia id 
    def instrucao(self):
        if self.token.tipo == 'ID': 
            identificador = self.token.valor
            self.nextToken()
            if  self.token.tipo == 'ATRIB':
                self.nextToken()
                self.expressao()

                ## TRADUCAO ##
                self.__ids[identificador] = self.__stack.pop()
                ## FIM TRADUCAO ##

            else: 
                raise Exception('= expected after ID')
        elif self.token.tipo == 'ESCREVA':
            self.nextToken()
            self.expressao()

            ## TRADUCAO ##
            print('xD >> {0}'.format(self.__stack.pop()) )
            ## FIM TRADUCAO ##

        elif self.token.tipo == 'LEIA':
            self.nextToken()
            if self.token.tipo == 'ID':

                ## TRADUCAO ##
                self.__ids[self.token.valor] =  float( input('xD << ') )
                ## FIM TRADUCAO ##

                self.nextToken()
            else :
                raise Exception('ID expected after LEIA')
        else:
            pass
            
    # expressao -> termo resto1
    def expressao(self): 
        self.termo()
        self.resto1()
    
    # resto1 -> + termo resto1 | - termo resto1 | epsilon
    def resto1(self):
        if self.token.valor in ['ADD', 'SUB']:

            ## TRADUCAO ##
            op = self.token.valor
            ## FIM TRADUCAO ##

            self.nextToken()
            self.termo()
            self.resto1()

            ## TRADUCAO ##
            op2 = self.__stack.pop()
            op1 = self.__stack.pop()
            if op == 'ADD':
                self.__stack.append(op1 + op2)
            else:
                self.__stack.append(op1 - op2)
            ## FIM TRADUCAO ##

        else: 
            pass
            
    # termo -> fator resto2
    def termo(self):
        self.fator()
        self.resto2()
    
    # resto2 -> * fator resto2 | / fator resto2 | % fator resto2 | epsilon 
    def resto2(self): 
        if self.token.valor in ['MUL','DIV','MOD']:

            ## TRADUCAO ##
            op = self.token.valor
            ## FIM TRADUCAO ##

            self.nextToken()
            self.fator()
            self.resto2()

            ## TRADUCAO ##
            op2 = self.__stack.pop()
            op1 = self.__stack.pop()
            if op == 'MUL':
                self.__stack.append(op1 * op2)
            elif op2 == 0: 
                raise Exception('division by zero no way !!!')
            elif op == 'DIV':
                self.__stack.append(op1 / op2)
            else:
                self.__stack.append(op1 % op2)
            ## FIM TRADUCAO ##
        else:
            pass 
    
    # fator -> base resto3
    def fator(self): 
        self.base()
        self.resto3()
    
    # resto3 -> ^ expressao | epsilon
    def resto3(self): 
        if self.token.valor == 'POW':
            self.nextToken()
            self.expressao()

            ## TRADUCAO ##
            op2 = self.__stack.pop()
            op1 = self.__stack.pop()
            self.__stack.append(op1 ** op2)
            ## FIM TRADUCAO ##
        else:
            pass
    
    # base -> id | num | (expressao)
    def base(self): 
        if self.token.tipo in ['ID','NUM']:

            ## TRADUCAO ##
            if self.token.tipo == 'ID':
                value = self.__ids[self.token.valor]
                if value is None: 
                    raise Exception("'{0}' is not defined".format(self.token.valor))
                self.__stack.append(self.__ids[self.token.valor])
            else:
                self.__stack.append( float(self.token.valor) )
            ## FIM TRADUCAO ##

            self.nextToken()
        elif self.token.valor == 'LPA': 
            self.nextToken()
            self.expressao()
            if self.token.valor == 'RPA': 
                self.nextToken()
            else: 
                raise Exception('right parentesis was expected')
        else:
            raise Exception('ID or NUM was expected')