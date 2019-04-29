# -*- coding: utf-8 -*-
"""

Compilador Main - Versao 1.0
@author: Yugo

"""
import sys 
from compiler.parser import Parser
from virtual_machine.isa import Isa

def main(): 
    if len(sys.argv) < 2:
        print("option required \n")
        return
    
    option = sys.argv[1]
    if option == '-compiler':   #Executar o Compilador CMP
        for fileName in sys.argv[2:]:
            try:
                parser = Parser( fileName ) 
                parser.syntaxAnalisys()
            except Exception as error:
                print( str(error) )
    elif option == '-vm':       #Executar o Emulador da Maquina Virtual 
        for fileName in sys.argv[2:]:
            try:
                isa = Isa( fileName ) 
                isa.run()
            except Exception as error:
                print( str(error) )
    else:                       #Tipo de execucao nao definida
        print("Option not defined. \n")

if __name__ == "__main__":
    main()