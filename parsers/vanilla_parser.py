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
            return p[1] + p[2]
        case "*":
            return p[1] * p[2]
        case "^":
            return p[1] ** p[2]
        case "%":
            return p[1] % p[2]
        case e:
            error(e)
            return None



def p_expression_num(p):
    """expr : num"""
    p[0] = p[1]
def p_expression_bool(p):
    """expr : bool"""
    p[0] = "T" if p[1] else "F"
def p_expression_to_num(p):
    """num : int
    | float"""
    p[0] = p[1]
def p_expression_int(p):
    """int : INT"""
    p[0] = p[1]
def p_expression_float(p):
    """float : FLOAT"""
    p[0] = p[1]
def p_expression_true_false(p):
    """bool : T
    | F"""
    p[0] = p[1] == "T"



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


def p_expression_comp_op(p):
    """bool : int int COMP_OP"""
    """bool : int float COMP_OP"""
    """bool : float int COMP_OP"""
    """bool : float float COMP_OP"""
    match p[2]:
        case "<":
            p[0] = p[1] < p[2]
        case ">":
            p[0] =  p[1] > p[2]
        case "<=":
            p[0] =  p[1] <= p[2]
        case ">=":
            p[0] =  p[1] >= p[2]
        case e:
            err("comparator")
            p[0] = None

def p_expression_equality(p):
    """bool : expr expr EQUALITY
    | int int EQUALITY
    | int float EQUALITY
    | float int EQUALITY
    | float float EQUALITY"""
    match p[2]:
        case "==":
            p[0] = p[1] == p[2]
        case "!=":
            p[0] =  p[1] != p[2]
        case e:
            err("equality operator")
            p[0] = None

def p_expression_bool_op_un(p):
    """bool : bool BOOL_OP_UN"""
    match p[2]:
        case "!":
            p[0] = not p[1]
        case e:
            err(e)
            p[0] = None

def p_expression_bool_op_bi(p):
    """bool : bool bool BOOL_OP_BI"""
    match p[3]:
        case "|":
            p[0] = p[1] or p[2]
        case "&":
            p[0] = p[1] and p[2]
        case e:
            err(e)
            p[0] = None

def p_expression_if_then_else(p):
    """bool : bool expr expr IF_THEN_ELSE"""
    p[0] = p[2] if p[1] else p[3]





def p_error(p):
    print("Syntax error in input!",(p))



parser = yacc()