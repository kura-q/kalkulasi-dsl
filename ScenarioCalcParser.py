# Generated from ScenarioCalc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,5,
        3,57,8,3,10,3,12,3,60,9,3,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,
        5,1,5,4,5,71,8,5,11,5,12,5,72,1,6,1,6,3,6,77,8,6,1,7,1,7,1,7,1,7,
        3,7,83,8,7,1,8,1,8,1,8,1,8,4,8,89,8,8,11,8,12,8,90,1,8,1,8,4,8,95,
        8,8,11,8,12,8,96,3,8,99,8,8,1,8,1,8,1,9,1,9,1,9,3,9,106,8,9,1,9,
        3,9,109,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,117,8,10,10,10,12,
        10,120,9,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,128,8,11,10,11,12,
        11,131,9,11,1,12,1,12,1,12,3,12,136,8,12,1,13,1,13,1,13,3,13,141,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,152,8,14,
        10,14,12,14,155,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        5,15,166,8,15,10,15,12,15,169,9,15,1,16,1,16,1,16,1,16,1,16,3,16,
        176,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,189,8,17,1,17,0,4,20,22,28,30,18,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,0,1,1,0,24,29,197,0,39,1,0,0,0,2,44,1,0,0,0,
        4,50,1,0,0,0,6,54,1,0,0,0,8,61,1,0,0,0,10,68,1,0,0,0,12,76,1,0,0,
        0,14,78,1,0,0,0,16,84,1,0,0,0,18,102,1,0,0,0,20,110,1,0,0,0,22,121,
        1,0,0,0,24,135,1,0,0,0,26,137,1,0,0,0,28,142,1,0,0,0,30,156,1,0,
        0,0,32,175,1,0,0,0,34,188,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,
        41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,
        0,42,43,5,0,0,1,43,1,1,0,0,0,44,45,5,1,0,0,45,46,5,33,0,0,46,47,
        5,19,0,0,47,48,3,4,2,0,48,49,5,20,0,0,49,3,1,0,0,0,50,51,3,6,3,0,
        51,52,3,8,4,0,52,53,3,10,5,0,53,5,1,0,0,0,54,58,5,2,0,0,55,57,3,
        12,6,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,
        7,1,0,0,0,60,58,1,0,0,0,61,65,5,3,0,0,62,64,3,12,6,0,63,62,1,0,0,
        0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,65,1,
        0,0,0,68,70,5,4,0,0,69,71,3,18,9,0,70,69,1,0,0,0,71,72,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,11,1,0,0,0,74,77,3,14,7,0,75,77,3,16,
        8,0,76,74,1,0,0,0,76,75,1,0,0,0,77,13,1,0,0,0,78,79,5,35,0,0,79,
        80,5,23,0,0,80,82,3,20,10,0,81,83,5,21,0,0,82,81,1,0,0,0,82,83,1,
        0,0,0,83,15,1,0,0,0,84,85,5,5,0,0,85,86,3,20,10,0,86,88,5,6,0,0,
        87,89,3,12,6,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,
        0,0,0,91,98,1,0,0,0,92,94,5,7,0,0,93,95,3,12,6,0,94,93,1,0,0,0,95,
        96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,92,1,0,0,
        0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,8,0,0,101,17,1,0,0,0,102,
        105,5,35,0,0,103,104,5,9,0,0,104,106,5,33,0,0,105,103,1,0,0,0,105,
        106,1,0,0,0,106,108,1,0,0,0,107,109,5,21,0,0,108,107,1,0,0,0,108,
        109,1,0,0,0,109,19,1,0,0,0,110,111,6,10,-1,0,111,112,3,22,11,0,112,
        118,1,0,0,0,113,114,10,2,0,0,114,115,5,31,0,0,115,117,3,22,11,0,
        116,113,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,
        119,21,1,0,0,0,120,118,1,0,0,0,121,122,6,11,-1,0,122,123,3,24,12,
        0,123,129,1,0,0,0,124,125,10,2,0,0,125,126,5,30,0,0,126,128,3,24,
        12,0,127,124,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,
        0,0,130,23,1,0,0,0,131,129,1,0,0,0,132,133,5,32,0,0,133,136,3,24,
        12,0,134,136,3,26,13,0,135,132,1,0,0,0,135,134,1,0,0,0,136,25,1,
        0,0,0,137,140,3,28,14,0,138,139,7,0,0,0,139,141,3,28,14,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,27,1,0,0,0,142,143,6,14,-1,0,143,144,
        3,30,15,0,144,153,1,0,0,0,145,146,10,3,0,0,146,147,5,12,0,0,147,
        152,3,30,15,0,148,149,10,2,0,0,149,150,5,13,0,0,150,152,3,30,15,
        0,151,145,1,0,0,0,151,148,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,
        0,153,154,1,0,0,0,154,29,1,0,0,0,155,153,1,0,0,0,156,157,6,15,-1,
        0,157,158,3,32,16,0,158,167,1,0,0,0,159,160,10,3,0,0,160,161,5,14,
        0,0,161,166,3,32,16,0,162,163,10,2,0,0,163,164,5,15,0,0,164,166,
        3,32,16,0,165,159,1,0,0,0,165,162,1,0,0,0,166,169,1,0,0,0,167,165,
        1,0,0,0,167,168,1,0,0,0,168,31,1,0,0,0,169,167,1,0,0,0,170,171,3,
        34,17,0,171,172,5,16,0,0,172,173,3,32,16,0,173,176,1,0,0,0,174,176,
        3,34,17,0,175,170,1,0,0,0,175,174,1,0,0,0,176,33,1,0,0,0,177,189,
        5,34,0,0,178,189,5,35,0,0,179,189,5,33,0,0,180,181,5,17,0,0,181,
        182,3,20,10,0,182,183,5,18,0,0,183,189,1,0,0,0,184,185,5,12,0,0,
        185,189,3,34,17,0,186,187,5,13,0,0,187,189,3,34,17,0,188,177,1,0,
        0,0,188,178,1,0,0,0,188,179,1,0,0,0,188,180,1,0,0,0,188,184,1,0,
        0,0,188,186,1,0,0,0,189,35,1,0,0,0,21,39,58,65,72,76,82,90,96,98,
        105,108,118,129,135,140,151,153,165,167,175,188
    ]

class ScenarioCalcParser ( Parser ):

    grammarFileName = "ScenarioCalc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'scenario'", "'given'", "'calculate'", 
                     "'report'", "'if'", "'then'", "'else'", "'end'", "'as'", 
                     "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'^'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'and'", "'or'", 
                     "'not'" ]

    symbolicNames = [ "<INVALID>", "SCENARIO", "GIVEN", "CALCULATE", "REPORT", 
                      "IF", "THEN", "ELSE", "END", "AS", "TRUE", "FALSE", 
                      "PLUS", "MINUS", "STAR", "DIV", "CARET", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMI", "COMMA", "ASSIGN", 
                      "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "AND", "OR", 
                      "NOT", "STRING", "NUMBER", "ID", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_scenarioDecl = 1
    RULE_scenarioBody = 2
    RULE_givenBlock = 3
    RULE_calculateBlock = 4
    RULE_reportBlock = 5
    RULE_statement = 6
    RULE_assignment = 7
    RULE_ifStatement = 8
    RULE_reportItem = 9
    RULE_expr = 10
    RULE_expr2 = 11
    RULE_expr3 = 12
    RULE_comparison = 13
    RULE_arithmetic = 14
    RULE_term = 15
    RULE_factor = 16
    RULE_primary = 17

    ruleNames =  [ "program", "scenarioDecl", "scenarioBody", "givenBlock", 
                   "calculateBlock", "reportBlock", "statement", "assignment", 
                   "ifStatement", "reportItem", "expr", "expr2", "expr3", 
                   "comparison", "arithmetic", "term", "factor", "primary" ]

    EOF = Token.EOF
    SCENARIO=1
    GIVEN=2
    CALCULATE=3
    REPORT=4
    IF=5
    THEN=6
    ELSE=7
    END=8
    AS=9
    TRUE=10
    FALSE=11
    PLUS=12
    MINUS=13
    STAR=14
    DIV=15
    CARET=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    SEMI=21
    COMMA=22
    ASSIGN=23
    EQ=24
    NEQ=25
    GT=26
    LT=27
    GTE=28
    LTE=29
    AND=30
    OR=31
    NOT=32
    STRING=33
    NUMBER=34
    ID=35
    WS=36
    LINE_COMMENT=37
    BLOCK_COMMENT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ScenarioCalcParser.EOF, 0)

        def scenarioDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.ScenarioDeclContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.ScenarioDeclContext,i)


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ScenarioCalcParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 36
                self.scenarioDecl()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(ScenarioCalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScenarioDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCENARIO(self):
            return self.getToken(ScenarioCalcParser.SCENARIO, 0)

        def STRING(self):
            return self.getToken(ScenarioCalcParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(ScenarioCalcParser.LBRACE, 0)

        def scenarioBody(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ScenarioBodyContext,0)


        def RBRACE(self):
            return self.getToken(ScenarioCalcParser.RBRACE, 0)

        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_scenarioDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenarioDecl" ):
                listener.enterScenarioDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenarioDecl" ):
                listener.exitScenarioDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenarioDecl" ):
                return visitor.visitScenarioDecl(self)
            else:
                return visitor.visitChildren(self)




    def scenarioDecl(self):

        localctx = ScenarioCalcParser.ScenarioDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scenarioDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ScenarioCalcParser.SCENARIO)
            self.state = 45
            self.match(ScenarioCalcParser.STRING)
            self.state = 46
            self.match(ScenarioCalcParser.LBRACE)
            self.state = 47
            self.scenarioBody()
            self.state = 48
            self.match(ScenarioCalcParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScenarioBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def givenBlock(self):
            return self.getTypedRuleContext(ScenarioCalcParser.GivenBlockContext,0)


        def calculateBlock(self):
            return self.getTypedRuleContext(ScenarioCalcParser.CalculateBlockContext,0)


        def reportBlock(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ReportBlockContext,0)


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_scenarioBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenarioBody" ):
                listener.enterScenarioBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenarioBody" ):
                listener.exitScenarioBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScenarioBody" ):
                return visitor.visitScenarioBody(self)
            else:
                return visitor.visitChildren(self)




    def scenarioBody(self):

        localctx = ScenarioCalcParser.ScenarioBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scenarioBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.givenBlock()
            self.state = 51
            self.calculateBlock()
            self.state = 52
            self.reportBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GivenBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GIVEN(self):
            return self.getToken(ScenarioCalcParser.GIVEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.StatementContext,i)


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_givenBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGivenBlock" ):
                listener.enterGivenBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGivenBlock" ):
                listener.exitGivenBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGivenBlock" ):
                return visitor.visitGivenBlock(self)
            else:
                return visitor.visitChildren(self)




    def givenBlock(self):

        localctx = ScenarioCalcParser.GivenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_givenBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ScenarioCalcParser.GIVEN)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==35:
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalculateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALCULATE(self):
            return self.getToken(ScenarioCalcParser.CALCULATE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.StatementContext,i)


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_calculateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculateBlock" ):
                listener.enterCalculateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculateBlock" ):
                listener.exitCalculateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculateBlock" ):
                return visitor.visitCalculateBlock(self)
            else:
                return visitor.visitChildren(self)




    def calculateBlock(self):

        localctx = ScenarioCalcParser.CalculateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_calculateBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ScenarioCalcParser.CALCULATE)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==35:
                self.state = 62
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReportBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPORT(self):
            return self.getToken(ScenarioCalcParser.REPORT, 0)

        def reportItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.ReportItemContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.ReportItemContext,i)


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_reportBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportBlock" ):
                listener.enterReportBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportBlock" ):
                listener.exitReportBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportBlock" ):
                return visitor.visitReportBlock(self)
            else:
                return visitor.visitChildren(self)




    def reportBlock(self):

        localctx = ScenarioCalcParser.ReportBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_reportBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ScenarioCalcParser.REPORT)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.reportItem()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StAssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(ScenarioCalcParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStAssign" ):
                listener.enterStAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStAssign" ):
                listener.exitStAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStAssign" ):
                return visitor.visitStAssign(self)
            else:
                return visitor.visitChildren(self)


    class StIfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(ScenarioCalcParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStIf" ):
                listener.enterStIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStIf" ):
                listener.exitStIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStIf" ):
                return visitor.visitStIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ScenarioCalcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                localctx = ScenarioCalcParser.StAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.assignment()
                pass
            elif token in [5]:
                localctx = ScenarioCalcParser.StIfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.ifStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ScenarioCalcParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ScenarioCalcParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(ScenarioCalcParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = ScenarioCalcParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            localctx = ScenarioCalcParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ScenarioCalcParser.ID)
            self.state = 79
            self.match(ScenarioCalcParser.ASSIGN)
            self.state = 80
            self.expr(0)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 81
                self.match(ScenarioCalcParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_ifStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStmtContext(IfStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.IfStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ScenarioCalcParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ExprContext,0)

        def THEN(self):
            return self.getToken(ScenarioCalcParser.THEN, 0)
        def END(self):
            return self.getToken(ScenarioCalcParser.END, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(ScenarioCalcParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)



    def ifStatement(self):

        localctx = ScenarioCalcParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            localctx = ScenarioCalcParser.IfStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ScenarioCalcParser.IF)
            self.state = 85
            self.expr(0)
            self.state = 86
            self.match(ScenarioCalcParser.THEN)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.statement()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==35):
                    break

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 92
                self.match(ScenarioCalcParser.ELSE)
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 93
                    self.statement()
                    self.state = 96 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5 or _la==35):
                        break



            self.state = 100
            self.match(ScenarioCalcParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReportItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_reportItem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReportItemRuleContext(ReportItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ReportItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ScenarioCalcParser.ID, 0)
        def AS(self):
            return self.getToken(ScenarioCalcParser.AS, 0)
        def STRING(self):
            return self.getToken(ScenarioCalcParser.STRING, 0)
        def SEMI(self):
            return self.getToken(ScenarioCalcParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReportItemRule" ):
                listener.enterReportItemRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReportItemRule" ):
                listener.exitReportItemRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReportItemRule" ):
                return visitor.visitReportItemRule(self)
            else:
                return visitor.visitChildren(self)



    def reportItem(self):

        localctx = ScenarioCalcParser.ReportItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_reportItem)
        self._la = 0 # Token type
        try:
            localctx = ScenarioCalcParser.ReportItemRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ScenarioCalcParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 103
                self.match(ScenarioCalcParser.AS)
                self.state = 104
                self.match(ScenarioCalcParser.STRING)


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 107
                self.match(ScenarioCalcParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Expr2OnlyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2Only" ):
                listener.enterExpr2Only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2Only" ):
                listener.exitExpr2Only(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2Only" ):
                return visitor.visitExpr2Only(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ExprContext,0)

        def OR(self):
            return self.getToken(ScenarioCalcParser.OR, 0)
        def expr2(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ScenarioCalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ScenarioCalcParser.Expr2OnlyContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 111
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ScenarioCalcParser.OrExprContext(self, ScenarioCalcParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 113
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 114
                    self.match(ScenarioCalcParser.OR)
                    self.state = 115
                    self.expr2(0) 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr2Context,0)

        def AND(self):
            return self.getToken(ScenarioCalcParser.AND, 0)
        def expr3(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class Expr3OnlyContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3Only" ):
                listener.enterExpr3Only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3Only" ):
                listener.exitExpr3Only(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3Only" ):
                return visitor.visitExpr3Only(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ScenarioCalcParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ScenarioCalcParser.Expr3OnlyContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 122
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ScenarioCalcParser.AndExprContext(self, ScenarioCalcParser.Expr2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 124
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 125
                    self.match(ScenarioCalcParser.AND)
                    self.state = 126
                    self.expr3() 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompareOnlyContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparison(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOnly" ):
                listener.enterCompareOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOnly" ):
                listener.exitCompareOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOnly" ):
                return visitor.visitCompareOnly(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ScenarioCalcParser.NOT, 0)
        def expr3(self):
            return self.getTypedRuleContext(ScenarioCalcParser.Expr3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self):

        localctx = ScenarioCalcParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr3)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                localctx = ScenarioCalcParser.NotExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(ScenarioCalcParser.NOT)
                self.state = 133
                self.expr3()
                pass
            elif token in [12, 13, 17, 33, 34, 35]:
                localctx = ScenarioCalcParser.CompareOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompareExprContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScenarioCalcParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(ScenarioCalcParser.ArithmeticContext,i)

        def EQ(self):
            return self.getToken(ScenarioCalcParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ScenarioCalcParser.NEQ, 0)
        def GT(self):
            return self.getToken(ScenarioCalcParser.GT, 0)
        def LT(self):
            return self.getToken(ScenarioCalcParser.LT, 0)
        def GTE(self):
            return self.getToken(ScenarioCalcParser.GTE, 0)
        def LTE(self):
            return self.getToken(ScenarioCalcParser.LTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self):

        localctx = ScenarioCalcParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = ScenarioCalcParser.CompareExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.arithmetic(0)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 138
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.arithmetic(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_arithmetic

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ArithmeticContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ArithmeticContext,0)

        def PLUS(self):
            return self.getToken(ScenarioCalcParser.PLUS, 0)
        def term(self):
            return self.getTypedRuleContext(ScenarioCalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ArithmeticContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ArithmeticContext,0)

        def MINUS(self):
            return self.getToken(ScenarioCalcParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(ScenarioCalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class TermOnlyContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.ArithmeticContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ScenarioCalcParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermOnly" ):
                listener.enterTermOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermOnly" ):
                listener.exitTermOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermOnly" ):
                return visitor.visitTermOnly(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ScenarioCalcParser.ArithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ScenarioCalcParser.TermOnlyContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 143
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 151
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = ScenarioCalcParser.AddContext(self, ScenarioCalcParser.ArithmeticContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 145
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 146
                        self.match(ScenarioCalcParser.PLUS)
                        self.state = 147
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ScenarioCalcParser.SubContext(self, ScenarioCalcParser.ArithmeticContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 148
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 149
                        self.match(ScenarioCalcParser.MINUS)
                        self.state = 150
                        self.term(0)
                        pass

             
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ScenarioCalcParser.TermContext,0)

        def DIV(self):
            return self.getToken(ScenarioCalcParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(ScenarioCalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ScenarioCalcParser.TermContext,0)

        def STAR(self):
            return self.getToken(ScenarioCalcParser.STAR, 0)
        def factor(self):
            return self.getTypedRuleContext(ScenarioCalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class FactorOnlyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ScenarioCalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorOnly" ):
                listener.enterFactorOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorOnly" ):
                listener.exitFactorOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorOnly" ):
                return visitor.visitFactorOnly(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ScenarioCalcParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ScenarioCalcParser.FactorOnlyContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 157
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 165
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = ScenarioCalcParser.MulContext(self, ScenarioCalcParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 159
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 160
                        self.match(ScenarioCalcParser.STAR)
                        self.state = 161
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ScenarioCalcParser.DivContext(self, ScenarioCalcParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 162
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 163
                        self.match(ScenarioCalcParser.DIV)
                        self.state = 164
                        self.factor()
                        pass

             
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PowerContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ScenarioCalcParser.PrimaryContext,0)

        def CARET(self):
            return self.getToken(ScenarioCalcParser.CARET, 0)
        def factor(self):
            return self.getTypedRuleContext(ScenarioCalcParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryOnlyContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(ScenarioCalcParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryOnly" ):
                listener.enterPrimaryOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryOnly" ):
                listener.exitPrimaryOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryOnly" ):
                return visitor.visitPrimaryOnly(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = ScenarioCalcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = ScenarioCalcParser.PowerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.primary()
                self.state = 171
                self.match(ScenarioCalcParser.CARET)
                self.state = 172
                self.factor()
                pass

            elif la_ == 2:
                localctx = ScenarioCalcParser.PrimaryOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScenarioCalcParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarRefContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ScenarioCalcParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarRef" ):
                listener.enterVarRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarRef" ):
                listener.exitVarRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRef" ):
                return visitor.visitVarRef(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ScenarioCalcParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(ScenarioCalcParser.PLUS, 0)
        def primary(self):
            return self.getTypedRuleContext(ScenarioCalcParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlus" ):
                listener.enterUnaryPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlus" ):
                listener.exitUnaryPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlus" ):
                return visitor.visitUnaryPlus(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(ScenarioCalcParser.MINUS, 0)
        def primary(self):
            return self.getTypedRuleContext(ScenarioCalcParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ScenarioCalcParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ScenarioCalcParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ScenarioCalcParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringLitContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScenarioCalcParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ScenarioCalcParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLit" ):
                listener.enterStringLit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLit" ):
                listener.exitStringLit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLit" ):
                return visitor.visitStringLit(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = ScenarioCalcParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = ScenarioCalcParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(ScenarioCalcParser.NUMBER)
                pass
            elif token in [35]:
                localctx = ScenarioCalcParser.VarRefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(ScenarioCalcParser.ID)
                pass
            elif token in [33]:
                localctx = ScenarioCalcParser.StringLitContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(ScenarioCalcParser.STRING)
                pass
            elif token in [17]:
                localctx = ScenarioCalcParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.match(ScenarioCalcParser.LPAREN)
                self.state = 181
                self.expr(0)
                self.state = 182
                self.match(ScenarioCalcParser.RPAREN)
                pass
            elif token in [12]:
                localctx = ScenarioCalcParser.UnaryPlusContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.match(ScenarioCalcParser.PLUS)
                self.state = 185
                self.primary()
                pass
            elif token in [13]:
                localctx = ScenarioCalcParser.UnaryMinusContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 186
                self.match(ScenarioCalcParser.MINUS)
                self.state = 187
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        self._predicates[11] = self.expr2_sempred
        self._predicates[14] = self.arithmetic_sempred
        self._predicates[15] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




