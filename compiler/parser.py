# -*- coding: utf-8 -*-
"""

Analisador Sintático 
@author: Yugo

"""

from compiler.lexer import Lexer
from compiler.grammar import Grammar
import pprint                                                    


# Classe para Analise Sintatica 
class Parser(object):
    
    def __init__(self, fileName):
        self.__lexer = Lexer(fileName)
        self.__grammar = None
        
    def syntaxAnalisys(self):
        # Analise Lexica 
        tokenList, idList = self.__lexer.lexicalAnalysis()
        self.__grammar = Grammar(tokenList, idList)
        
        if self.__grammar.programa():
            pass 
            # Imprimir no console 
            # pp = pprint.PrettyPrinter(indent=2)
            # pp.pprint({'TOKEN': tokenList})
            # pp.pprint({'ID': idList})
        else:
            print(self.__grammar.errorHandling)