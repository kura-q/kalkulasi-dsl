/*
  ScenarioCalc.g4
  - DSL for scenario-based calculations:
      scenario "Name" {
        given
          x = 10;
        calculate
          y = x * 2;
          if y > 15 then
            z = y + 5;
          else
            z = y - 1;
          end
        report
          y as "Result Y";
          z;
      }
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
  : GIVEN statement*    // assignments only recommended
  ;

calculateBlock
  : CALCULATE statement*   // assignments and ifStatements
  ;

reportBlock
  : REPORT reportItem+ 
  ;

statement
  : assignment
  | ifStatement
  ;

assignment
  : ID ASSIGN expr SEMI?
  ;

ifStatement
  : IF expr THEN statement+ (ELSE statement+)? END
  ;

reportItem
  : ID (AS STRING)? SEMI?
  ;

/* expressions with precedence */
expr
  : expr OR expr2             # OrExpr
  | expr2
  ;

expr2
  : expr2 AND expr3           # AndExpr
  | expr3
  ;

expr3
  : NOT expr3                 # NotExpr
  | comparison
  ;

comparison
  : arithmetic ((EQ | NEQ | GT | LT | GTE | LTE) arithmetic)?
  ;

arithmetic
  : arithmetic PLUS term      # Add
  | arithmetic MINUS term     # Sub
  | term
  ;

term
  : term STAR factor          # Mul
  | term DIV factor           # Div
  | factor
  ;

factor
  : primary CARET factor      # Power
  | primary
  ;

primary
  : NUMBER                    # Number
  | ID                        # VarRef
  | STRING                    # StringLit
  | LPAREN expr RPAREN        # ParenExpr
  | PLUS primary              # UnaryPlus
  | MINUS primary             # UnaryMinus
  ;

/* ---------------------------
   LEXER RULES (tokens)
   Order matters: keywords before ID
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

/* boolean operators as keywords */
AND : 'and';
OR  : 'or';
NOT : 'not';

/* literals */
STRING
  : '"' (~["\\] | '\\' .)* '"'
  ;

NUMBER
  : DIGIT+ ('.' DIGIT+)?      // integer or float
  ;

/* identifier (variable names) */
ID
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;

/* skip whitespace and comments */
WS
  : [ \t\r\n]+ -> skip
  ;

LINE_COMMENT
  : '//' ~[\r\n]* -> skip
  ;

BLOCK_COMMENT
  : '/*' .*? '*/' -> skip
  ;

/* fragments */
fragment DIGIT : [0-9] ;
