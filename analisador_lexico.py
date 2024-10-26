import ply.lex as lex

# Palavras reservadas
reserved_words = {
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'for': 'FOR',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'void': 'VOID',
    'static': 'STATIC',
    'const': 'CONST',
    'struct': 'STRUCT',
    'typedef': 'TYPEDEF',
    'sizeof': 'SIZEOF',
    'union': 'UNION',
    'enum': 'ENUM',
    'goto': 'GOTO',
    'volatile': 'VOLATILE',
    'extern': 'EXTERN',
    'register': 'REGISTER',
    'signed': 'SIGNED',
    'unsigned': 'UNSIGNED',
}

# Lista de tokens, incluindo as palavras reservadas
tokens = [
    'NUMBER',       # Números inteiros
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'DIVIDE',       # /
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'SEMICOLON',    # ;
    'COMMA',        # ,
    'ID',           # Identificadores (nomes de variáveis)
    'ATRIBUITION',  # Atribuição =
    'EQUALS',       # ==
    'NOT_EQUALS',   # !=
    'LESS_THAN',    # <
    'GREATER_THAN', # >
    'LESS_EQUAL',   # <=
    'GREATER_EQUAL',# >=
    'AND',          # &&
    'OR',           # ||
    'NOT',          # !
    'INCREMENT',    # ++
    'DECREMENT',    # --
    'DOTS',         # :
    'BREAKLINE',    # \n
    'BREAKLINE_2',  # \r
] + list(reserved_words.values())

# Expressões regulares para tokens simples
t_PLUS           = r'\+'
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_LBRACE         = r'\{'
t_RBRACE         = r'\}'
t_SEMICOLON      = r';'
t_COMMA          = r','
t_ATRIBUITION    = r'='
t_EQUALS         = r'=='
t_NOT_EQUALS     = r'!='
t_LESS_THAN      = r'<'
t_GREATER_THAN   = r'>'
t_LESS_EQUAL     = r'<='
t_GREATER_EQUAL  = r'>='
t_AND            = r'&&'
t_OR             = r'\|\|'
t_NOT            = r'!'
t_INCREMENT      = r'\+\+'
t_DECREMENT      = r'--'
t_DOTS           = r':'

# Função para capturar quebra de linha \n
def t_BREAKLINE(t):
    r'\n'
    t.lexer.lineno += 1  # Atualiza a contagem de linhas
    return t

# Função para capturar quebra de linha \r (carriage return)
def t_BREAKLINE_2(t):
    r'\r'
    return t

# Expressão regular para um identificador (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Expressão regular para um número (NUMBER)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte o número para inteiro
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Definição de regras para lidar com erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na posição {t.lexpos}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Função para ler o arquivo e analisar o código
def analyze_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Analisando o arquivo de entrada
analyze_file('./exemplo1.sp')
