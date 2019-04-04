# Linguagem CMPUC v.2.0

## extensão 

* .cmp

## executar arquivos 

1. git clone https://github.com/YugoVtr/cmp1076_compiladores.git <path_name>
2. python <path_name> <file_name_1.cmp> <file_name_2.cmp>...

### Prerequisites

Python 3.x

# Analisador Léxico

Analisador Léxico (Lexer) para ler sequência de caracteres de um arquivo de texto e retorna uma lista de Token reconhecidos.

## Token

Um token e representado como um Objeto:

```
Class Token { 
    Tipo    --> Tipo de Token reconhecido. 
    Valor   --> Valor específico do token (Se aplicavel).
}
```

## Descricao Lexica

| Tipos de Tokens  |         Valor           |          Padrão de reconhecimento         |
|:----------------:|:-----------------------:|:-----------------------------------------:|
|ID                |String com "Nome"        | letra(letra|digito)*                      |
|NUM               |Valor numérico da string | [-]digito<sup>+</sup>[.digito<sup>+</sup>]|
|OPR_AR            |Tipo de operação         | "+", "*", "%", "-", "/", "^"              |
|OPR_REL           |Tipo de operação         | "<", ">", "==", "<=", ">=", "!="          |
|OPR_LOG           |Tipo de operação         | "and", "or", "not"                        |
|DELIM             |Tipo                     | "(", ")", ",", ";", "."                   |
|IF                |\<NA>                    | "if"                                      |
|ELSE              |\<NA>                    | "else"                                    |
|WHILE             |\<NA>                    | "while"                                   |
|ATRIB             |\<NA>                    | "="                                       |
|LEIA              |\<NA>                    | "leia"                                    |
|ESCREVA           |\<NA>                    | "escreva"                                 |
|ERRO              |\<NA>                    | Nenhuma das opções anteriores             |

## Tabela de Símbolos

O Lexer (ou Scanner) é responsável por criar uma tabela de símbolos para armazenar informações sobre tokens do tipo ID

| ID    |  Valor  |
|:-----:|:-------:|
|A      |0        |
|B      |0        |

### Presume-se apenas variáveis do tipo numérico.

# Analisador Semântico

## Gramática

```
programa            -> lista_instrucoes
lista_instrucoes    -> instrucao ; lista_instrucoes | ε
instrucao           -> id = expressao
                    -> escreva expressao
                    -> leia id
expressao           -> termo resto1
resto1              -> + termo resto1 | - termo resto1 | ε
termo               -> fator resto2
resto2              -> * fator resto2 | / fator resto2 | % fator resto2 | ε
fator               -> base resto3
resto3              -> ^ expressao | ε
base                -> id | num | (expressao)
```

# Interpretador

Durante o processo de analise sematica da linguagem CMPUC, 
cada instrução e interpretada em python; 
