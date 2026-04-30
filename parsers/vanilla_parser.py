from ply.yacc import yacc
from lexers.lexer import tokens

def err(ptype:str):
    return lambda e: print(f"no implemented behaviour for {ptype} '{e}'")
    

def num_op_un(p, error):
    match p[2]:
        case "~":
            return -p[1]
        case e:
            error(e)
            return None

def num_op_bi(p, error):
    match p[3]:
        case "+":
            return p[2] + p[1]
        case "*":
            return p[2] * p[1]
        case "^":
            return p[2] ** p[1]
        case e:
            error(e)
            return None



def p_expression_int(p):
    """int : INT"""
    p[0] = p[1]
def p_expression_float(p):
    """float : FLOAT"""
    p[0] = p[1]
def p_expression_e(p):
    """expression : int
    | float"""
    p[0] = p[1]

def p_expression_int_op_un(p):
    """int : INT NUM_OP_UN"""
    p[0] = num_op_un(p, err("unary int operator"))

def p_expression_float_op_un(p):
    """float : float NUM_OP_UN"""
    p[0] = num_op_un(p, err("unary float operator"))


def p_expression_int_op_bi(p):
    """int : int int NUM_OP_BI"""
    p[0] = num_op_bi(p, err("binary int operator"))

def p_expression_float_op_bi(p):
    """float : float float NUM_OP_BI
    | int float NUM_OP_BI
    | float int NUM_OP_BI"""
    p[0] = num_op_bi(p, err("binary float operator"))

def p_error(p):
    print("Syntax error in input!")



parser = yacc()



while True:
    try:
        s = input('> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)






