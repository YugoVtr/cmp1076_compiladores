# -*- coding: utf-8 -*-
"""

ISA - Instruction Set Architecture
@author: Yugo

"""

class Isa(object):

    def __init__(self, fileName):
        if not fileName: 
            raise Exception('arquivo nao informado')
            
        # Ler Conteudo do Arquivo 
        file = open(fileName, "r")
        
        if not file: 
            raise Exception('arquivo nao encontrado')
            
        self.__content = file.read()
        file.close()
    
    def run(self):   
        num_instruction = 0 
        for line in self.__content.split('\n'):
            num_instruction += 1
            token = line.split()
            instruction = token[0].upper()
            if   instruction == 'MOVE':
                pass
            elif instruction == 'MOVEV': 
                pass
            elif instruction == 'LOAD': 
                pass  
            elif instruction == 'STORE': 
                pass  
            elif instruction == 'JUMP': 
                pass  
            elif instruction == 'BEQ': 
                pass  
            elif instruction == 'BNE': 
                pass  
            elif instruction == 'BLT': 
                pass  
            elif instruction == 'BLE': 
                pass  
            elif instruction == 'BGT': 
                pass  
            elif instruction == 'BGE': 
                pass  
            elif instruction == 'READ': 
                pass  
            elif instruction == 'WRITE': 
                pass  
            elif instruction == 'PUSH': 
                pass  
            elif instruction == 'POP': 
                pass  
            elif instruction == 'ADD': 
                pass  
            elif instruction == 'SUB': 
                pass  
            elif instruction == 'MUL': 
                pass  
            elif instruction == 'DIV': 
                pass  
            elif instruction == 'MOD': 
                pass  
            elif instruction == 'POT': 
                pass  
            elif instruction == 'AND': 
                pass  
            elif instruction == 'OR': 
                pass  
            elif instruction == 'NOT': 
                pass              
            else: 
                raise Exception('instruction not found in line {0}'.format( num_instruction ))         

    def isRegister( self, name ): 
        pass
    
    def isNumber( self, name ): 
        pass
                 