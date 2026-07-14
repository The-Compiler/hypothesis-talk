import lark
import hypothesis
import hypothesis.extra.lark

GRAMMAR = r"""
    program : ( class )*
    class : "class" " " identifier [ ":" identifier ] "{" ( classmember )* "}"
    classmember : variable | method
    variable : type " " identifier ";"
    method : methodhead methodbody
    methodhead : type " " identifier "(" parameterlist ")"
    parameterlist : [ parameter ( "," parameter )* ]
    parameter : type " " identifier
    methodbody : statementblock
    type : identifier | arraytype
    arraytype : type "[" "]"
    statementblock : "{" ( statement )* "}"
    statement : ";" | variable | assignment | ifstatement | whilestatement | callstatement | returnstatement
    assignment : designator "=" expression ";"
    ifstatement : "if" "(" expression ")" statementblock [ "else" statementblock ]
    whilestatement : "while" "(" expression ")" statementblock
    callstatement : methodcall ";"
    returnstatement : "return" " " [ expression ] ";"
    expression : logicterm ( "||" logicterm )*
    logicterm : logicfactor ( "&&" logicfactor )*
    logicfactor : typeexpression ( compareoperator typeexpression  )*
    typeexpression : simpleexpression " " [ ( "cast" | "is" ) " " type ]
    compareoperator : "==" | "!=" | "<" | "<=" | ">" | ">="
    simpleexpression : term ( ( "+" | "-" ) term )*
    term : factor ( ( "*" | "/" | "%" ) factor )*
    factor : operand | unaryexpression | "(" expression ")"
    unaryexpression : ( "!" | "+" | "-" ) factor
    operand : literal | designator | objectcreation | arraycreation | methodcall
    literal : number | character | string
    designator : identifier | designator "." identifier | designator "[" expression "]"
    objectcreation : "new" " " identifier "(" ")"
    arraycreation : "new" " " identifier "[" expression "]" ( "[" "]" )*
    methodcall : designator "(" argumentlist ")"
    argumentlist : [ expression ( "," expression )* ]
    identifier : letter ( letter | digit )*
    number : digit ~ 1..9 | "0x" (hexdigit) ~ 1..8
    character : "'" ( charcontent | charesc ) "'"
    charcontent : (" " .. "&" | "(" .. "[" | "]" .. "~")  // no \ or '
    charesc : "\\0" | "\\\\" | "\\n" | "\\'"
    string : "\"" ( stringcontent | stringesc )* "\""
    stringcontent : (" " | "!" | "#" .. "[" | "]" .. "~")  // no \ or "
    stringesc : "\\\\" | "\\n" "\\\""
    // letters chosen to avoid keywords like cast/if/is
    letter : "A" .. "Z" | "a" .. "h" | "j" .. "r" | "t" .. "z"
    digit : "0" .. "9"
    hexdigit : digit | "a" .. "f"

    // %import common.WS
    // %ignore WS
"""

PARSER = lark.Lark(GRAMMAR, start="program")


@hypothesis.given(hypothesis.extra.lark.from_lark(PARSER, start="ifstatement"))
def test_programs(code: str):
    print(code)
