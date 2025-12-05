# Generated from ScenarioCalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScenarioCalcParser import ScenarioCalcParser
else:
    from ScenarioCalcParser import ScenarioCalcParser

# This class defines a complete listener for a parse tree produced by ScenarioCalcParser.
class ScenarioCalcListener(ParseTreeListener):

    # Enter a parse tree produced by ScenarioCalcParser#program.
    def enterProgram(self, ctx:ScenarioCalcParser.ProgramContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#program.
    def exitProgram(self, ctx:ScenarioCalcParser.ProgramContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#scenarioDecl.
    def enterScenarioDecl(self, ctx:ScenarioCalcParser.ScenarioDeclContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#scenarioDecl.
    def exitScenarioDecl(self, ctx:ScenarioCalcParser.ScenarioDeclContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#scenarioBody.
    def enterScenarioBody(self, ctx:ScenarioCalcParser.ScenarioBodyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#scenarioBody.
    def exitScenarioBody(self, ctx:ScenarioCalcParser.ScenarioBodyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#givenBlock.
    def enterGivenBlock(self, ctx:ScenarioCalcParser.GivenBlockContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#givenBlock.
    def exitGivenBlock(self, ctx:ScenarioCalcParser.GivenBlockContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#calculateBlock.
    def enterCalculateBlock(self, ctx:ScenarioCalcParser.CalculateBlockContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#calculateBlock.
    def exitCalculateBlock(self, ctx:ScenarioCalcParser.CalculateBlockContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#reportBlock.
    def enterReportBlock(self, ctx:ScenarioCalcParser.ReportBlockContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#reportBlock.
    def exitReportBlock(self, ctx:ScenarioCalcParser.ReportBlockContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#StAssign.
    def enterStAssign(self, ctx:ScenarioCalcParser.StAssignContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#StAssign.
    def exitStAssign(self, ctx:ScenarioCalcParser.StAssignContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#StIf.
    def enterStIf(self, ctx:ScenarioCalcParser.StIfContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#StIf.
    def exitStIf(self, ctx:ScenarioCalcParser.StIfContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Assign.
    def enterAssign(self, ctx:ScenarioCalcParser.AssignContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Assign.
    def exitAssign(self, ctx:ScenarioCalcParser.AssignContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#IfStmt.
    def enterIfStmt(self, ctx:ScenarioCalcParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#IfStmt.
    def exitIfStmt(self, ctx:ScenarioCalcParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#ReportItemRule.
    def enterReportItemRule(self, ctx:ScenarioCalcParser.ReportItemRuleContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#ReportItemRule.
    def exitReportItemRule(self, ctx:ScenarioCalcParser.ReportItemRuleContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Expr2Only.
    def enterExpr2Only(self, ctx:ScenarioCalcParser.Expr2OnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Expr2Only.
    def exitExpr2Only(self, ctx:ScenarioCalcParser.Expr2OnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#OrExpr.
    def enterOrExpr(self, ctx:ScenarioCalcParser.OrExprContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#OrExpr.
    def exitOrExpr(self, ctx:ScenarioCalcParser.OrExprContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#AndExpr.
    def enterAndExpr(self, ctx:ScenarioCalcParser.AndExprContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#AndExpr.
    def exitAndExpr(self, ctx:ScenarioCalcParser.AndExprContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Expr3Only.
    def enterExpr3Only(self, ctx:ScenarioCalcParser.Expr3OnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Expr3Only.
    def exitExpr3Only(self, ctx:ScenarioCalcParser.Expr3OnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#NotExpr.
    def enterNotExpr(self, ctx:ScenarioCalcParser.NotExprContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#NotExpr.
    def exitNotExpr(self, ctx:ScenarioCalcParser.NotExprContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#CompareOnly.
    def enterCompareOnly(self, ctx:ScenarioCalcParser.CompareOnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#CompareOnly.
    def exitCompareOnly(self, ctx:ScenarioCalcParser.CompareOnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#CompareExpr.
    def enterCompareExpr(self, ctx:ScenarioCalcParser.CompareExprContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#CompareExpr.
    def exitCompareExpr(self, ctx:ScenarioCalcParser.CompareExprContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Add.
    def enterAdd(self, ctx:ScenarioCalcParser.AddContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Add.
    def exitAdd(self, ctx:ScenarioCalcParser.AddContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Sub.
    def enterSub(self, ctx:ScenarioCalcParser.SubContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Sub.
    def exitSub(self, ctx:ScenarioCalcParser.SubContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#TermOnly.
    def enterTermOnly(self, ctx:ScenarioCalcParser.TermOnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#TermOnly.
    def exitTermOnly(self, ctx:ScenarioCalcParser.TermOnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Div.
    def enterDiv(self, ctx:ScenarioCalcParser.DivContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Div.
    def exitDiv(self, ctx:ScenarioCalcParser.DivContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Mul.
    def enterMul(self, ctx:ScenarioCalcParser.MulContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Mul.
    def exitMul(self, ctx:ScenarioCalcParser.MulContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#FactorOnly.
    def enterFactorOnly(self, ctx:ScenarioCalcParser.FactorOnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#FactorOnly.
    def exitFactorOnly(self, ctx:ScenarioCalcParser.FactorOnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Power.
    def enterPower(self, ctx:ScenarioCalcParser.PowerContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Power.
    def exitPower(self, ctx:ScenarioCalcParser.PowerContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#PrimaryOnly.
    def enterPrimaryOnly(self, ctx:ScenarioCalcParser.PrimaryOnlyContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#PrimaryOnly.
    def exitPrimaryOnly(self, ctx:ScenarioCalcParser.PrimaryOnlyContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#Number.
    def enterNumber(self, ctx:ScenarioCalcParser.NumberContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#Number.
    def exitNumber(self, ctx:ScenarioCalcParser.NumberContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#VarRef.
    def enterVarRef(self, ctx:ScenarioCalcParser.VarRefContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#VarRef.
    def exitVarRef(self, ctx:ScenarioCalcParser.VarRefContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#StringLit.
    def enterStringLit(self, ctx:ScenarioCalcParser.StringLitContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#StringLit.
    def exitStringLit(self, ctx:ScenarioCalcParser.StringLitContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#ParenExpr.
    def enterParenExpr(self, ctx:ScenarioCalcParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#ParenExpr.
    def exitParenExpr(self, ctx:ScenarioCalcParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#UnaryPlus.
    def enterUnaryPlus(self, ctx:ScenarioCalcParser.UnaryPlusContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#UnaryPlus.
    def exitUnaryPlus(self, ctx:ScenarioCalcParser.UnaryPlusContext):
        pass


    # Enter a parse tree produced by ScenarioCalcParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:ScenarioCalcParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by ScenarioCalcParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:ScenarioCalcParser.UnaryMinusContext):
        pass



del ScenarioCalcParser