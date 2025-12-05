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

    # Helpers --------------------------------------------------

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

    # =========================================================
    #   VISIT ROOT
    # =========================================================

    def visitProgram(self, ctx):
        for scenario in ctx.scenarioDecl():
            self.visit(scenario)
        return self.report_output

    def visitScenarioDecl(self, ctx):
        name = ctx.STRING().getText()
        name = name.strip('"')
        print(f"\n--- RUNNING SCENARIO: {name} ---")

        self.visit(ctx.scenarioBody())

    def visitScenarioBody(self, ctx):
        # order matters
        self.visit(ctx.givenBlock())
        self.visit(ctx.calculateBlock())
        self.visit(ctx.reportBlock())

    # =========================================================
    #   GIVEN BLOCK
    # =========================================================

    def visitGivenBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # =========================================================
    #   CALCULATE BLOCK
    # =========================================================

    def visitCalculateBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # =========================================================
    #   STATEMENTS
    # =========================================================

    def visitStatement(self, ctx):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())

    # ---------------------------------------------------------
    #   ASSIGNMENT
    # ---------------------------------------------------------

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.set_value(name, value)
        return value

    # ---------------------------------------------------------
    #   IF STATEMENT
    # ---------------------------------------------------------

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expr())
        all_stmts = ctx.statement()

        # Temukan posisi keyword ELSE di children list
        has_else = ctx.ELSE() is not None

        if not has_else:
            if condition:
                for s in all_stmts:
                    self.visit(s)
            return

        # kalau ada ELSE, pisahkan THEN dan ELSE
        else_token = ctx.ELSE().symbol.tokenIndex
        then_stmts = []
        else_stmts = []

        for s in all_stmts:
            if s.start.tokenIndex < else_token:
                then_stmts.append(s)
            else:
                else_stmts.append(s)

        if condition:
            for s in then_stmts:
                self.visit(s)
        else:
            for s in else_stmts:
                self.visit(s)

    # =========================================================
    #   REPORT BLOCK
    # =========================================================

    def visitReportBlock(self, ctx):
        for item in ctx.reportItem():
            self.visit(item)

    def visitReportItemRule(self, ctx):
        name = ctx.ID().getText()
        label = None

        if ctx.AS():
            label = ctx.STRING().getText().strip('"')

        value = self.get_value(name)
        output_label = label if label else name

        result = f"{output_label}: {value}"
        print(result)
        self.report_output.append(result)

    # =========================================================
    #   EXPRESSIONS
    # =========================================================

    # OR
    def visitOrExprRule(self, ctx):
        left = self.eval_bool(self.visit(ctx.expr()))
        right = self.eval_bool(self.visit(ctx.expr2()))
        return left or right

    # AND
    def visitAndExprRule(self, ctx):
        left = self.eval_bool(self.visit(ctx.expr2()))
        right = self.eval_bool(self.visit(ctx.expr3()))
        return left and right

    # NOT
    def visitNotExprRule(self, ctx):
        val = self.eval_bool(self.visit(ctx.expr3()))
        return not val

    # COMPARISON
    def visitComparison(self, ctx):
        left = self.visit(ctx.arithmetic(0))

        if ctx.EQ():
            return left == self.visit(ctx.arithmetic(1))
        if ctx.NEQ():
            return left != self.visit(ctx.arithmetic(1))
        if ctx.GT():
            return left > self.visit(ctx.arithmetic(1))
        if ctx.LT():
            return left < self.visit(ctx.arithmetic(1))
        if ctx.GTE():
            return left >= self.visit(ctx.arithmetic(1))
        if ctx.LTE():
            return left <= self.visit(ctx.arithmetic(1))

        return left

    # ---------------------------
    # BASIC MATH
    # ---------------------------

    def visitAddRule(self, ctx):
        return self.visit(ctx.arithmetic()) + self.visit(ctx.term())

    def visitSubRule(self, ctx):
        return self.visit(ctx.arithmetic()) - self.visit(ctx.term())

    def visitMulRule(self, ctx):
        return self.visit(ctx.term()) * self.visit(ctx.factor())

    def visitDivRule(self, ctx):
        divisor = self.visit(ctx.factor())
        if divisor == 0:
            raise Exception("ERROR: Division by zero")
        return self.visit(ctx.term()) / divisor

    def visitPowerRule(self, ctx):
        return self.visit(ctx.primary()) ** self.visit(ctx.factor())

    # ---------------------------
    # PRIMARY VALUES
    # ---------------------------

    def visitNumberRule(self, ctx):
        text = ctx.NUMBER().getText()
        return float(text) if "." in text else int(text)

    def visitVarRefRule(self, ctx):
        return self.get_value(ctx.ID().getText())

    def visitStringRule(self, ctx):
        return ctx.STRING().getText().strip('"')

    def visitParenRule(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlusRule(self, ctx):
        return +self.visit(ctx.primary())

    def visitUnaryMinusRule(self, ctx):
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
