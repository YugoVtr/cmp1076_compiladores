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

### Prerequisites

Python 3.x


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
|ERRO              |\<NA>                    | Nenhuma das opções anteriores             |

## Tabela de Símbolos

O Lexer (ou Scanner) é responsável por criar uma tabela de símbolos para armazenar informações sobre tokens do tipo ID

| ID    |  Valor  |
|:-----:|:-------:|
|A      |0        |
|B      |0        |

### Presume-se apenas variáveis do tipo numérico.