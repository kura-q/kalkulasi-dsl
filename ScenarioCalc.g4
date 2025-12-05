grammar ScenarioCalc;

/*
  ScenarioCalc DSL — FIXED VERSION (visitor-safe)
*/

/* ---------------------------
   PARSER RULES
   --------------------------- */

program
  : scenarioDecl* EOF
  ;

scenarioDecl
  : SCENARIO STRING LBRACE scenarioBody RBRACE
  ;

scenarioBody
  : givenBlock calculateBlock reportBlock
  ;

givenBlock
  : GIVEN statement*
  ;

calculateBlock
  : CALCULATE statement*
  ;

reportBlock
  : REPORT reportItem+
  ;

statement
  : assignment                     # StAssign
  | ifStatement                    # StIf
  ;

assignment
  : ID ASSIGN expr SEMI?           # Assign
  ;

ifStatement
  : IF expr THEN statement+ (ELSE statement+)? END   # IfStmt
  ;

reportItem
  : ID (AS STRING)? SEMI?          # ReportItemRule
  ;

/* expressions (all labeled) */
expr
  : expr OR expr2                  # OrExpr
  | expr2                          # Expr2Only
  ;

expr2
  : expr2 AND expr3                # AndExpr
  | expr3                          # Expr3Only
  ;

expr3
  : NOT expr3                      # NotExpr
  | comparison                     # CompareOnly
  ;

comparison
  : arithmetic ((EQ | NEQ | GT | LT | GTE | LTE) arithmetic)?  # CompareExpr
  ;

/* arithmetic */
arithmetic
  : arithmetic PLUS term           # Add
  | arithmetic MINUS term          # Sub
  | term                           # TermOnly
  ;

term
  : term STAR factor               # Mul
  | term DIV factor                # Div
  | factor                         # FactorOnly
  ;

factor
  : primary CARET factor           # Power
  | primary                        # PrimaryOnly
  ;

primary
  : NUMBER                         # Number
  | ID                             # VarRef
  | STRING                         # StringLit
  | LPAREN expr RPAREN             # ParenExpr
  | PLUS primary                   # UnaryPlus
  | MINUS primary                  # UnaryMinus
  ;

/* ---------------------------
   LEXER RULES
   --------------------------- */

/* keywords */
SCENARIO : 'scenario';
GIVEN    : 'given';
CALCULATE: 'calculate';
REPORT   : 'report';
IF       : 'if';
THEN     : 'then';
ELSE     : 'else';
END      : 'end';
AS       : 'as';
TRUE     : 'true';
FALSE    : 'false';

/* operators / punctuation */
PLUS  : '+';
MINUS : '-';
STAR  : '*';
DIV   : '/';
CARET : '^';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
SEMI   : ';';
COMMA  : ',';

ASSIGN : '=';
EQ     : '==';
NEQ    : '!=';
GT     : '>';
LT     : '<';
GTE    : '>=';
LTE    : '<=';

AND : 'and';
OR  : 'or';
NOT : 'not';

/* literals */
STRING
  : '"' (~["\\] | '\\' .)* '"'
  ;

NUMBER
  : DIGIT+ ('.' DIGIT+)?
  ;

ID
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

WS
  : [ \t\r\n]+ -> skip
  ;

LINE_COMMENT
  : '//' ~[\r\n]* -> skip
  ;

BLOCK_COMMENT
  : '/*' .*? '*/' -> skip
  ;

fragment DIGIT : [0-9] ;
