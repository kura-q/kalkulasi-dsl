# Generated from ScenarioCalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScenarioCalcParser import ScenarioCalcParser
else:
    from ScenarioCalcParser import ScenarioCalcParser

# This class defines a complete generic visitor for a parse tree produced by ScenarioCalcParser.

class ScenarioCalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScenarioCalcParser#program.
    def visitProgram(self, ctx:ScenarioCalcParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#scenarioDecl.
    def visitScenarioDecl(self, ctx:ScenarioCalcParser.ScenarioDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#scenarioBody.
    def visitScenarioBody(self, ctx:ScenarioCalcParser.ScenarioBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#givenBlock.
    def visitGivenBlock(self, ctx:ScenarioCalcParser.GivenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#calculateBlock.
    def visitCalculateBlock(self, ctx:ScenarioCalcParser.CalculateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#reportBlock.
    def visitReportBlock(self, ctx:ScenarioCalcParser.ReportBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#StAssign.
    def visitStAssign(self, ctx:ScenarioCalcParser.StAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#StIf.
    def visitStIf(self, ctx:ScenarioCalcParser.StIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Assign.
    def visitAssign(self, ctx:ScenarioCalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#IfStmt.
    def visitIfStmt(self, ctx:ScenarioCalcParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#ReportItemRule.
    def visitReportItemRule(self, ctx:ScenarioCalcParser.ReportItemRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Expr2Only.
    def visitExpr2Only(self, ctx:ScenarioCalcParser.Expr2OnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#OrExpr.
    def visitOrExpr(self, ctx:ScenarioCalcParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#AndExpr.
    def visitAndExpr(self, ctx:ScenarioCalcParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Expr3Only.
    def visitExpr3Only(self, ctx:ScenarioCalcParser.Expr3OnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#NotExpr.
    def visitNotExpr(self, ctx:ScenarioCalcParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#CompareOnly.
    def visitCompareOnly(self, ctx:ScenarioCalcParser.CompareOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#CompareExpr.
    def visitCompareExpr(self, ctx:ScenarioCalcParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Add.
    def visitAdd(self, ctx:ScenarioCalcParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Sub.
    def visitSub(self, ctx:ScenarioCalcParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#TermOnly.
    def visitTermOnly(self, ctx:ScenarioCalcParser.TermOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Div.
    def visitDiv(self, ctx:ScenarioCalcParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Mul.
    def visitMul(self, ctx:ScenarioCalcParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#FactorOnly.
    def visitFactorOnly(self, ctx:ScenarioCalcParser.FactorOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Power.
    def visitPower(self, ctx:ScenarioCalcParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#PrimaryOnly.
    def visitPrimaryOnly(self, ctx:ScenarioCalcParser.PrimaryOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#Number.
    def visitNumber(self, ctx:ScenarioCalcParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#VarRef.
    def visitVarRef(self, ctx:ScenarioCalcParser.VarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#StringLit.
    def visitStringLit(self, ctx:ScenarioCalcParser.StringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#ParenExpr.
    def visitParenExpr(self, ctx:ScenarioCalcParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#UnaryPlus.
    def visitUnaryPlus(self, ctx:ScenarioCalcParser.UnaryPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScenarioCalcParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:ScenarioCalcParser.UnaryMinusContext):
        return self.visitChildren(ctx)



del ScenarioCalcParser