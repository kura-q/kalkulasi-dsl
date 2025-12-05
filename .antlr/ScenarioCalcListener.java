// Generated from d:/GitHub/kalkulasi-dsl/ScenarioCalc.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ScenarioCalcParser}.
 */
public interface ScenarioCalcListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ScenarioCalcParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ScenarioCalcParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#scenarioDecl}.
	 * @param ctx the parse tree
	 */
	void enterScenarioDecl(ScenarioCalcParser.ScenarioDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#scenarioDecl}.
	 * @param ctx the parse tree
	 */
	void exitScenarioDecl(ScenarioCalcParser.ScenarioDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#scenarioBody}.
	 * @param ctx the parse tree
	 */
	void enterScenarioBody(ScenarioCalcParser.ScenarioBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#scenarioBody}.
	 * @param ctx the parse tree
	 */
	void exitScenarioBody(ScenarioCalcParser.ScenarioBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#givenBlock}.
	 * @param ctx the parse tree
	 */
	void enterGivenBlock(ScenarioCalcParser.GivenBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#givenBlock}.
	 * @param ctx the parse tree
	 */
	void exitGivenBlock(ScenarioCalcParser.GivenBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#calculateBlock}.
	 * @param ctx the parse tree
	 */
	void enterCalculateBlock(ScenarioCalcParser.CalculateBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#calculateBlock}.
	 * @param ctx the parse tree
	 */
	void exitCalculateBlock(ScenarioCalcParser.CalculateBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ScenarioCalcParser#reportBlock}.
	 * @param ctx the parse tree
	 */
	void enterReportBlock(ScenarioCalcParser.ReportBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ScenarioCalcParser#reportBlock}.
	 * @param ctx the parse tree
	 */
	void exitReportBlock(ScenarioCalcParser.ReportBlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StAssign}
	 * labeled alternative in {@link ScenarioCalcParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStAssign(ScenarioCalcParser.StAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StAssign}
	 * labeled alternative in {@link ScenarioCalcParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStAssign(ScenarioCalcParser.StAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StIf}
	 * labeled alternative in {@link ScenarioCalcParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStIf(ScenarioCalcParser.StIfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StIf}
	 * labeled alternative in {@link ScenarioCalcParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStIf(ScenarioCalcParser.StIfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link ScenarioCalcParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssign(ScenarioCalcParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link ScenarioCalcParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssign(ScenarioCalcParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfStmt}
	 * labeled alternative in {@link ScenarioCalcParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(ScenarioCalcParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfStmt}
	 * labeled alternative in {@link ScenarioCalcParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(ScenarioCalcParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReportItemRule}
	 * labeled alternative in {@link ScenarioCalcParser#reportItem}.
	 * @param ctx the parse tree
	 */
	void enterReportItemRule(ScenarioCalcParser.ReportItemRuleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReportItemRule}
	 * labeled alternative in {@link ScenarioCalcParser#reportItem}.
	 * @param ctx the parse tree
	 */
	void exitReportItemRule(ScenarioCalcParser.ReportItemRuleContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Expr2Only}
	 * labeled alternative in {@link ScenarioCalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr2Only(ScenarioCalcParser.Expr2OnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Expr2Only}
	 * labeled alternative in {@link ScenarioCalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr2Only(ScenarioCalcParser.Expr2OnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code OrExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOrExpr(ScenarioCalcParser.OrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code OrExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOrExpr(ScenarioCalcParser.OrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AndExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterAndExpr(ScenarioCalcParser.AndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AndExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitAndExpr(ScenarioCalcParser.AndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Expr3Only}
	 * labeled alternative in {@link ScenarioCalcParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterExpr3Only(ScenarioCalcParser.Expr3OnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Expr3Only}
	 * labeled alternative in {@link ScenarioCalcParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitExpr3Only(ScenarioCalcParser.Expr3OnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(ScenarioCalcParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotExpr}
	 * labeled alternative in {@link ScenarioCalcParser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(ScenarioCalcParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CompareOnly}
	 * labeled alternative in {@link ScenarioCalcParser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterCompareOnly(ScenarioCalcParser.CompareOnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CompareOnly}
	 * labeled alternative in {@link ScenarioCalcParser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitCompareOnly(ScenarioCalcParser.CompareOnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CompareExpr}
	 * labeled alternative in {@link ScenarioCalcParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterCompareExpr(ScenarioCalcParser.CompareExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CompareExpr}
	 * labeled alternative in {@link ScenarioCalcParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitCompareExpr(ScenarioCalcParser.CompareExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Add}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterAdd(ScenarioCalcParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Add}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitAdd(ScenarioCalcParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterSub(ScenarioCalcParser.SubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Sub}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitSub(ScenarioCalcParser.SubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TermOnly}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterTermOnly(ScenarioCalcParser.TermOnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TermOnly}
	 * labeled alternative in {@link ScenarioCalcParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitTermOnly(ScenarioCalcParser.TermOnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Div}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void enterDiv(ScenarioCalcParser.DivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Div}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void exitDiv(ScenarioCalcParser.DivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void enterMul(ScenarioCalcParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void exitMul(ScenarioCalcParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FactorOnly}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void enterFactorOnly(ScenarioCalcParser.FactorOnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FactorOnly}
	 * labeled alternative in {@link ScenarioCalcParser#term}.
	 * @param ctx the parse tree
	 */
	void exitFactorOnly(ScenarioCalcParser.FactorOnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Power}
	 * labeled alternative in {@link ScenarioCalcParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterPower(ScenarioCalcParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Power}
	 * labeled alternative in {@link ScenarioCalcParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitPower(ScenarioCalcParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrimaryOnly}
	 * labeled alternative in {@link ScenarioCalcParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryOnly(ScenarioCalcParser.PrimaryOnlyContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrimaryOnly}
	 * labeled alternative in {@link ScenarioCalcParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryOnly(ScenarioCalcParser.PrimaryOnlyContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Number}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterNumber(ScenarioCalcParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Number}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitNumber(ScenarioCalcParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VarRef}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterVarRef(ScenarioCalcParser.VarRefContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VarRef}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitVarRef(ScenarioCalcParser.VarRefContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StringLit}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterStringLit(ScenarioCalcParser.StringLitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StringLit}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitStringLit(ScenarioCalcParser.StringLitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(ScenarioCalcParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(ScenarioCalcParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterUnaryPlus(ScenarioCalcParser.UnaryPlusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryPlus}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitUnaryPlus(ScenarioCalcParser.UnaryPlusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterUnaryMinus(ScenarioCalcParser.UnaryMinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code UnaryMinus}
	 * labeled alternative in {@link ScenarioCalcParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitUnaryMinus(ScenarioCalcParser.UnaryMinusContext ctx);
}