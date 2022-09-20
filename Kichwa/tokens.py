from enum import(
    auto,
    Enum,
    unique
)
from typing import (
    Dict,
    NamedTuple
)


@unique
class TokenType(Enum):
    AND = auto()
    ASSIGN = auto()
    COMMA = auto()
    CLASSNAME = auto()
    DIVISION = auto()
    ELSE = auto()
    EQ = auto()
    EOF = auto()
    EXPONENTIATION = auto()
    FALSE = auto()
    FLOAT = auto()
    FUNCTION = auto()
    G_OR_EQ_T = auto()
    GT = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LBRAKET = auto()
    L_OR_EQ_T = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MODULUS = auto()
    MULTIPLICATION = auto()
    NOT_EQ = auto()
    PLUS = auto()
    RETURN = auto()
    RBRAKET = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    STRING = auto()
    THEN = auto()
    TRUE = auto()
    TYPEASSIGN = auto()
    OR = auto()
    OUTPUTFUNTION = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'fn': TokenType.FUNCTION,
        'mushuk': TokenType.LET,
        'panta': TokenType.FALSE,
        'kikin': TokenType.TRUE,
        'ari': TokenType.IF,
        'shinapi': TokenType.THEN,
        'arimana': TokenType.ELSE,
        'bool': TokenType.CLASSNAME,
        'int': TokenType.CLASSNAME,
        'shimi': TokenType.CLASSNAME,
        'float': TokenType.CLASSNAME,
        'fshukcion': TokenType.CLASSNAME,
        'list': TokenType.CLASSNAME,
        'tuple': TokenType.CLASSNAME,
        'chusak': TokenType.CLASSNAME,
    }

    return keywords.get(literal, TokenType.IDENT)