# -*- coding: utf-8 -*-
"""

Compilador Main - Versao 1.0
@author: Yugo

"""
from compiler.parser import Parser
def main(): 
    parser = Parser() 
    parser.syntaxAnalisys()

if __name__ == "__main__":
    main()