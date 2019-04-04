# -*- coding: utf-8 -*-
"""

Compilador Main - Versao 1.0
@author: Yugo

"""
import sys 
from compiler.parser import Parser
def main(): 
    for fileName in sys.argv[1:]:
        try:
            parser = Parser( fileName ) 
            parser.syntaxAnalisys()
        except Exception as error:
            print( str(error) )

if __name__ == "__main__":
    main()