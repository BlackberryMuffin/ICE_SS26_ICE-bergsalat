import ply.lex as lex

# List of token names.   This is always required
reserved = [
    "T",
    "F",
]


tokens = [
    "NUM_OP_UN",
    "NUM_OP_BI",
    "Comp_OP",
    "EQUALS",
    "BOOL_OP_UN",
    "BOOL_OP_BI",

    "INT",
    "FLOAT",
] +reserved

t_NUM_OP_BI = r"\+|\*|\^"
t_NUM_OP_UN = r"~"
t_Comp_OP = r"(<=)|(>=)|<|>|(!=)"
t_EQUALS = r"=="
t_BOOL_OP_BI = r"&|\|"
t_BOOL_OP_UN = r"!"


def t_FLOAT(t):
    r"""(\d+\.(\d?)+)|(\.\d+)"""
    t.type = "FLOAT"
    t.value = float(t.value)
    return t

def t_INT(t):
    r"""\d+"""
    t.type = "INT"
    t.value = int(t.value)
    return t

def t_variables(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]+'*"""
    if t.value.upper() in reserved:
        t.type = t.value.upper()
    else:
        print("Variables aren't implemented yet")
    #t.type = t.value.upper() if t.value.upper() in reserved else "VAR_NAME"
    return t

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()