import sys
from antlr4 import *
from ScenarioCalcLexer import ScenarioCalcLexer
from ScenarioCalcParser import ScenarioCalcParser
from ScenarioCalcVisitor import ScenarioCalcVisitor


# ============================================================
#  Runtime / Interpreter
# ============================================================

class ScenarioRuntime(ScenarioCalcVisitor):
    def __init__(self):
        self.variables = {}   # store variables values
        self.report_output = []

    # ===================== Helpers =====================

    def get_value(self, name):
        if name not in self.variables:
            raise Exception(f"ERROR: variable '{name}' not defined")
        return self.variables[name]

    def set_value(self, name, value):
        self.variables[name] = value

    def eval_bool(self, val):
        if isinstance(val, bool):
            return val
        raise Exception(f"Boolean expected, got: {val}")

    # ===================== ROOT ========================

    def visitProgram(self, ctx):
        for scenario in ctx.scenarioDecl():
            self.visit(scenario)
        return self.report_output

    def visitScenarioDecl(self, ctx):
        name = ctx.STRING().getText().strip('"')
        print(f"\n--- RUNNING SCENARIO: {name} ---")
        self.visit(ctx.scenarioBody())

    def visitScenarioBody(self, ctx):
        self.visit(ctx.givenBlock())
        self.visit(ctx.calculateBlock())
        self.visit(ctx.reportBlock())

    # ===================== BLOCKS ======================

    def visitGivenBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitCalculateBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitReportBlock(self, ctx):
        for item in ctx.reportItem():
            self.visit(item)

    # ===================== STATEMENTS ==================

    # statement: assignment #StAssign | ifStatement #StIf
    # kita tidak perlu visitStAssign/visitStIf eksplisit;
    # cukup handle di level Assign & IfStmt

    # assignment: ID ASSIGN expr SEMI? #Assign
    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_value(name, value)
        return value

    # ifStatement: IF expr THEN statement+ (ELSE statement+)? END #IfStmt
    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expr())
        stmts = ctx.statement()

        if ctx.ELSE():
            else_token = ctx.ELSE().symbol.tokenIndex
            then_stmts = []
            else_stmts = []

            for s in stmts:
                if s.start.tokenIndex < else_token:
                    then_stmts.append(s)
                else:
                    else_stmts.append(s)

            if self.eval_bool(condition):
                for s in then_stmts:
                    self.visit(s)
            else:
                for s in else_stmts:
                    self.visit(s)
        else:
            if self.eval_bool(condition):
                for s in stmts:
                    self.visit(s)

    # ===================== REPORT ======================

    # reportItem: ID (AS STRING)? SEMI? #ReportItemRule
    def visitReportItemRule(self, ctx):
        name = ctx.ID().getText()
        label = ctx.STRING().getText().strip('"') if ctx.AS() else None

        value = self.get_value(name)
        output_label = label if label else name

        result = f"{output_label}: {value}"
        print(result)
        self.report_output.append(result)

    # ===================== EXPRESSIONS =================
    # expr: expr OR expr2 #OrExpr | expr2 #Expr2Only

    def visitOrExpr(self, ctx):
        left = self.eval_bool(self.visit(ctx.expr()))
        right = self.eval_bool(self.visit(ctx.expr2()))
        return left or right

    def visitExpr2Only(self, ctx):
        return self.visit(ctx.expr2())

    # expr2: expr2 AND expr3 #AndExpr | expr3 #Expr3Only

    def visitAndExpr(self, ctx):
        left = self.eval_bool(self.visit(ctx.expr2()))
        right = self.eval_bool(self.visit(ctx.expr3()))
        return left and right

    def visitExpr3Only(self, ctx):
        return self.visit(ctx.expr3())

    # expr3: NOT expr3 #NotExpr | comparison #CompareOnly

    def visitNotExpr(self, ctx):
        val = self.eval_bool(self.visit(ctx.expr3()))
        return not val

    def visitCompareOnly(self, ctx):
        return self.visit(ctx.comparison())

    # comparison: arithmetic ((EQ|NEQ|GT|LT|GTE|LTE) arithmetic)? #CompareExpr

    def visitCompareExpr(self, ctx):
        left = self.visit(ctx.arithmetic(0))
        if ctx.arithmetic(1) is None:
            return left

        right = self.visit(ctx.arithmetic(1))

        if ctx.EQ():
            return left == right
        if ctx.NEQ():
            return left != right
        if ctx.GT():
            return left > right
        if ctx.LT():
            return left < right
        if ctx.GTE():
            return left >= right
        if ctx.LTE():
            return left <= right

        return left

    # arithmetic: arithmetic PLUS term #Add
    #           | arithmetic MINUS term #Sub
    #           | term #TermOnly

    def visitAdd(self, ctx):
        return self.visit(ctx.arithmetic()) + self.visit(ctx.term())

    def visitSub(self, ctx):
        return self.visit(ctx.arithmetic()) - self.visit(ctx.term())

    def visitTermOnly(self, ctx):
        return self.visit(ctx.term())

    # term: term STAR factor #Mul
    #     | term DIV factor #Div
    #     | factor #FactorOnly

    def visitMul(self, ctx):
        return self.visit(ctx.term()) * self.visit(ctx.factor())

    def visitDiv(self, ctx):
        divisor = self.visit(ctx.factor())
        if divisor == 0:
            raise Exception("ERROR: Division by zero")
        return self.visit(ctx.term()) / divisor

    def visitFactorOnly(self, ctx):
        return self.visit(ctx.factor())

    # factor: primary CARET factor #Power
    #       | primary #PrimaryOnly

    def visitPower(self, ctx):
        return self.visit(ctx.primary()) ** self.visit(ctx.factor())

    def visitPrimaryOnly(self, ctx):
        return self.visit(ctx.primary())

    # primary:
    #   NUMBER #Number
    # | ID     #VarRef
    # | STRING #StringLit
    # | LPAREN expr RPAREN #ParenExpr
    # | PLUS primary #UnaryPlus
    # | MINUS primary #UnaryMinus

    def visitNumber(self, ctx):
        text = ctx.NUMBER().getText()
        return float(text) if "." in text else int(text)

    def visitVarRef(self, ctx):
        return self.get_value(ctx.ID().getText())

    def visitStringLit(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.primary())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.primary())


# ============================================================
#  MAIN ENTRY
# ============================================================

def run_file(path):
    input_stream = FileStream(path, encoding='utf-8')
    lexer = ScenarioCalcLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ScenarioCalcParser(tokens)

    tree = parser.program()
    visitor = ScenarioRuntime()

    try:
        result = visitor.visit(tree)
    except Exception as e:
        print(f"\nRuntime Error: {e}")
        return

    print("\n--- FINAL REPORT ---")
    for line in result:
        print(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_calc.py <file.dsl>")
    else:
        run_file(sys.argv[1])
