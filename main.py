# -*- coding: utf-8 -*-
"""

Compiladore Main - Versao 1.0

"""
from analex import AnaLex
import pprint                                                    

def main(): 
    
    # Analise Lexica 
    objAnaLex = AnaLex()
    tokenList, idList = objAnaLex.run()
    
    # Imprimir no console 
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint({'TOKEN': tokenList})
    pp.pprint({'ID': idList})
    
if __name__ == "__main__":
    main()