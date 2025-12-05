// Generated from c:/KEHIDUPAN KODINGAN KU/003 plp/kalkulasi-dsl/ScenarioCalc.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ScenarioCalcParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SCENARIO=1, GIVEN=2, CALCULATE=3, REPORT=4, IF=5, THEN=6, ELSE=7, END=8, 
		AS=9, TRUE=10, FALSE=11, PLUS=12, MINUS=13, STAR=14, DIV=15, CARET=16, 
		LPAREN=17, RPAREN=18, LBRACE=19, RBRACE=20, SEMI=21, COMMA=22, ASSIGN=23, 
		EQ=24, NEQ=25, GT=26, LT=27, GTE=28, LTE=29, AND=30, OR=31, NOT=32, STRING=33, 
		NUMBER=34, ID=35, WS=36, LINE_COMMENT=37, BLOCK_COMMENT=38;
	public static final int
		RULE_program = 0, RULE_scenarioDecl = 1, RULE_scenarioBody = 2, RULE_givenBlock = 3, 
		RULE_calculateBlock = 4, RULE_reportBlock = 5, RULE_statement = 6, RULE_assignment = 7, 
		RULE_ifStatement = 8, RULE_reportItem = 9, RULE_expr = 10, RULE_expr2 = 11, 
		RULE_expr3 = 12, RULE_comparison = 13, RULE_arithmetic = 14, RULE_term = 15, 
		RULE_factor = 16, RULE_primary = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "scenarioDecl", "scenarioBody", "givenBlock", "calculateBlock", 
			"reportBlock", "statement", "assignment", "ifStatement", "reportItem", 
			"expr", "expr2", "expr3", "comparison", "arithmetic", "term", "factor", 
			"primary"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'scenario'", "'given'", "'calculate'", "'report'", "'if'", "'then'", 
			"'else'", "'end'", "'as'", "'true'", "'false'", "'+'", "'-'", "'*'", 
			"'/'", "'^'", "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'=='", 
			"'!='", "'>'", "'<'", "'>='", "'<='", "'and'", "'or'", "'not'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SCENARIO", "GIVEN", "CALCULATE", "REPORT", "IF", "THEN", "ELSE", 
			"END", "AS", "TRUE", "FALSE", "PLUS", "MINUS", "STAR", "DIV", "CARET", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "COMMA", "ASSIGN", "EQ", 
			"NEQ", "GT", "LT", "GTE", "LTE", "AND", "OR", "NOT", "STRING", "NUMBER", 
			"ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ScenarioCalc.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ScenarioCalcParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ScenarioCalcParser.EOF, 0); }
		public List<ScenarioDeclContext> scenarioDecl() {
			return getRuleContexts(ScenarioDeclContext.class);
		}
		public ScenarioDeclContext scenarioDecl(int i) {
			return getRuleContext(ScenarioDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SCENARIO) {
				{
				{
				setState(36);
				scenarioDecl();
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(42);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScenarioDeclContext extends ParserRuleContext {
		public TerminalNode SCENARIO() { return getToken(ScenarioCalcParser.SCENARIO, 0); }
		public TerminalNode STRING() { return getToken(ScenarioCalcParser.STRING, 0); }
		public TerminalNode LBRACE() { return getToken(ScenarioCalcParser.LBRACE, 0); }
		public ScenarioBodyContext scenarioBody() {
			return getRuleContext(ScenarioBodyContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ScenarioCalcParser.RBRACE, 0); }
		public ScenarioDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scenarioDecl; }
	}

	public final ScenarioDeclContext scenarioDecl() throws RecognitionException {
		ScenarioDeclContext _localctx = new ScenarioDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_scenarioDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(SCENARIO);
			setState(45);
			match(STRING);
			setState(46);
			match(LBRACE);
			setState(47);
			scenarioBody();
			setState(48);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScenarioBodyContext extends ParserRuleContext {
		public GivenBlockContext givenBlock() {
			return getRuleContext(GivenBlockContext.class,0);
		}
		public CalculateBlockContext calculateBlock() {
			return getRuleContext(CalculateBlockContext.class,0);
		}
		public ReportBlockContext reportBlock() {
			return getRuleContext(ReportBlockContext.class,0);
		}
		public ScenarioBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scenarioBody; }
	}

	public final ScenarioBodyContext scenarioBody() throws RecognitionException {
		ScenarioBodyContext _localctx = new ScenarioBodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_scenarioBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			givenBlock();
			setState(51);
			calculateBlock();
			setState(52);
			reportBlock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GivenBlockContext extends ParserRuleContext {
		public TerminalNode GIVEN() { return getToken(ScenarioCalcParser.GIVEN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public GivenBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_givenBlock; }
	}

	public final GivenBlockContext givenBlock() throws RecognitionException {
		GivenBlockContext _localctx = new GivenBlockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_givenBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(GIVEN);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IF || _la==ID) {
				{
				{
				setState(55);
				statement();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CalculateBlockContext extends ParserRuleContext {
		public TerminalNode CALCULATE() { return getToken(ScenarioCalcParser.CALCULATE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CalculateBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_calculateBlock; }
	}

	public final CalculateBlockContext calculateBlock() throws RecognitionException {
		CalculateBlockContext _localctx = new CalculateBlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_calculateBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(CALCULATE);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IF || _la==ID) {
				{
				{
				setState(62);
				statement();
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReportBlockContext extends ParserRuleContext {
		public TerminalNode REPORT() { return getToken(ScenarioCalcParser.REPORT, 0); }
		public List<ReportItemContext> reportItem() {
			return getRuleContexts(ReportItemContext.class);
		}
		public ReportItemContext reportItem(int i) {
			return getRuleContext(ReportItemContext.class,i);
		}
		public ReportBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reportBlock; }
	}

	public final ReportBlockContext reportBlock() throws RecognitionException {
		ReportBlockContext _localctx = new ReportBlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_reportBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(REPORT);
			setState(70); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(69);
				reportItem();
				}
				}
				setState(72); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StAssignContext extends StatementContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public StAssignContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StIfContext extends StatementContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public StIfContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				_localctx = new StAssignContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				assignment();
				}
				break;
			case IF:
				_localctx = new StIfContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(75);
				ifStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	 
		public AssignmentContext() { }
		public void copyFrom(AssignmentContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends AssignmentContext {
		public TerminalNode ID() { return getToken(ScenarioCalcParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(ScenarioCalcParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ScenarioCalcParser.SEMI, 0); }
		public AssignContext(AssignmentContext ctx) { copyFrom(ctx); }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assignment);
		int _la;
		try {
			_localctx = new AssignContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(ID);
			setState(79);
			match(ASSIGN);
			setState(80);
			expr(0);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(81);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	 
		public IfStatementContext() { }
		public void copyFrom(IfStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends IfStatementContext {
		public TerminalNode IF() { return getToken(ScenarioCalcParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode THEN() { return getToken(ScenarioCalcParser.THEN, 0); }
		public TerminalNode END() { return getToken(ScenarioCalcParser.END, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ScenarioCalcParser.ELSE, 0); }
		public IfStmtContext(IfStatementContext ctx) { copyFrom(ctx); }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifStatement);
		int _la;
		try {
			_localctx = new IfStmtContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(IF);
			setState(85);
			expr(0);
			setState(86);
			match(THEN);
			setState(88); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(87);
				statement();
				}
				}
				setState(90); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IF || _la==ID );
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(92);
				match(ELSE);
				setState(94); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(93);
					statement();
					}
					}
					setState(96); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==IF || _la==ID );
				}
			}

			setState(100);
			match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReportItemContext extends ParserRuleContext {
		public ReportItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reportItem; }
	 
		public ReportItemContext() { }
		public void copyFrom(ReportItemContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ReportItemRuleContext extends ReportItemContext {
		public TerminalNode ID() { return getToken(ScenarioCalcParser.ID, 0); }
		public TerminalNode AS() { return getToken(ScenarioCalcParser.AS, 0); }
		public TerminalNode STRING() { return getToken(ScenarioCalcParser.STRING, 0); }
		public TerminalNode SEMI() { return getToken(ScenarioCalcParser.SEMI, 0); }
		public ReportItemRuleContext(ReportItemContext ctx) { copyFrom(ctx); }
	}

	public final ReportItemContext reportItem() throws RecognitionException {
		ReportItemContext _localctx = new ReportItemContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_reportItem);
		int _la;
		try {
			_localctx = new ReportItemRuleContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(ID);
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(103);
				match(AS);
				setState(104);
				match(STRING);
				}
			}

			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(107);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr2OnlyContext extends ExprContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Expr2OnlyContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OrExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode OR() { return getToken(ScenarioCalcParser.OR, 0); }
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public OrExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Expr2OnlyContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(111);
			expr2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(118);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new OrExprContext(new ExprContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(113);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(114);
					match(OR);
					setState(115);
					expr2(0);
					}
					} 
				}
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr2Context extends ParserRuleContext {
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	 
		public Expr2Context() { }
		public void copyFrom(Expr2Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends Expr2Context {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode AND() { return getToken(ScenarioCalcParser.AND, 0); }
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public AndExprContext(Expr2Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr3OnlyContext extends Expr2Context {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr3OnlyContext(Expr2Context ctx) { copyFrom(ctx); }
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expr2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Expr3OnlyContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(122);
			expr3();
			}
			_ctx.stop = _input.LT(-1);
			setState(129);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AndExprContext(new Expr2Context(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_expr2);
					setState(124);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(125);
					match(AND);
					setState(126);
					expr3();
					}
					} 
				}
				setState(131);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr3Context extends ParserRuleContext {
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
	 
		public Expr3Context() { }
		public void copyFrom(Expr3Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompareOnlyContext extends Expr3Context {
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public CompareOnlyContext(Expr3Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NotExprContext extends Expr3Context {
		public TerminalNode NOT() { return getToken(ScenarioCalcParser.NOT, 0); }
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public NotExprContext(Expr3Context ctx) { copyFrom(ctx); }
	}

	public final Expr3Context expr3() throws RecognitionException {
		Expr3Context _localctx = new Expr3Context(_ctx, getState());
		enterRule(_localctx, 24, RULE_expr3);
		try {
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				_localctx = new NotExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(132);
				match(NOT);
				setState(133);
				expr3();
				}
				break;
			case PLUS:
			case MINUS:
			case LPAREN:
			case STRING:
			case NUMBER:
			case ID:
				_localctx = new CompareOnlyContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				comparison();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ParserRuleContext {
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	 
		public ComparisonContext() { }
		public void copyFrom(ComparisonContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CompareExprContext extends ComparisonContext {
		public List<ArithmeticContext> arithmetic() {
			return getRuleContexts(ArithmeticContext.class);
		}
		public ArithmeticContext arithmetic(int i) {
			return getRuleContext(ArithmeticContext.class,i);
		}
		public TerminalNode EQ() { return getToken(ScenarioCalcParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(ScenarioCalcParser.NEQ, 0); }
		public TerminalNode GT() { return getToken(ScenarioCalcParser.GT, 0); }
		public TerminalNode LT() { return getToken(ScenarioCalcParser.LT, 0); }
		public TerminalNode GTE() { return getToken(ScenarioCalcParser.GTE, 0); }
		public TerminalNode LTE() { return getToken(ScenarioCalcParser.LTE, 0); }
		public CompareExprContext(ComparisonContext ctx) { copyFrom(ctx); }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_comparison);
		int _la;
		try {
			_localctx = new CompareExprContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			arithmetic(0);
			setState(140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(138);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056964608L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(139);
				arithmetic(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArithmeticContext extends ParserRuleContext {
		public ArithmeticContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic; }
	 
		public ArithmeticContext() { }
		public void copyFrom(ArithmeticContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddContext extends ArithmeticContext {
		public ArithmeticContext arithmetic() {
			return getRuleContext(ArithmeticContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(ScenarioCalcParser.PLUS, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public AddContext(ArithmeticContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SubContext extends ArithmeticContext {
		public ArithmeticContext arithmetic() {
			return getRuleContext(ArithmeticContext.class,0);
		}
		public TerminalNode MINUS() { return getToken(ScenarioCalcParser.MINUS, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public SubContext(ArithmeticContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TermOnlyContext extends ArithmeticContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TermOnlyContext(ArithmeticContext ctx) { copyFrom(ctx); }
	}

	public final ArithmeticContext arithmetic() throws RecognitionException {
		return arithmetic(0);
	}

	private ArithmeticContext arithmetic(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ArithmeticContext _localctx = new ArithmeticContext(_ctx, _parentState);
		ArithmeticContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_arithmetic, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new TermOnlyContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(143);
			term(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(153);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(151);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new AddContext(new ArithmeticContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic);
						setState(145);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(146);
						match(PLUS);
						setState(147);
						term(0);
						}
						break;
					case 2:
						{
						_localctx = new SubContext(new ArithmeticContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic);
						setState(148);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(149);
						match(MINUS);
						setState(150);
						term(0);
						}
						break;
					}
					} 
				}
				setState(155);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	 
		public TermContext() { }
		public void copyFrom(TermContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DivContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode DIV() { return getToken(ScenarioCalcParser.DIV, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public DivContext(TermContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode STAR() { return getToken(ScenarioCalcParser.STAR, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public MulContext(TermContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FactorOnlyContext extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public FactorOnlyContext(TermContext ctx) { copyFrom(ctx); }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new FactorOnlyContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(157);
			factor();
			}
			_ctx.stop = _input.LT(-1);
			setState(167);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(165);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new MulContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(159);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(160);
						match(STAR);
						setState(161);
						factor();
						}
						break;
					case 2:
						{
						_localctx = new DivContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(162);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(163);
						match(DIV);
						setState(164);
						factor();
						}
						break;
					}
					} 
				}
				setState(169);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	 
		public FactorContext() { }
		public void copyFrom(FactorContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PowerContext extends FactorContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public TerminalNode CARET() { return getToken(ScenarioCalcParser.CARET, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public PowerContext(FactorContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryOnlyContext extends FactorContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public PrimaryOnlyContext(FactorContext ctx) { copyFrom(ctx); }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_factor);
		try {
			setState(175);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				_localctx = new PowerContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				primary();
				setState(171);
				match(CARET);
				setState(172);
				factor();
				}
				break;
			case 2:
				_localctx = new PrimaryOnlyContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(174);
				primary();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	 
		public PrimaryContext() { }
		public void copyFrom(PrimaryContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarRefContext extends PrimaryContext {
		public TerminalNode ID() { return getToken(ScenarioCalcParser.ID, 0); }
		public VarRefContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends PrimaryContext {
		public TerminalNode NUMBER() { return getToken(ScenarioCalcParser.NUMBER, 0); }
		public NumberContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryPlusContext extends PrimaryContext {
		public TerminalNode PLUS() { return getToken(ScenarioCalcParser.PLUS, 0); }
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryPlusContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryMinusContext extends PrimaryContext {
		public TerminalNode MINUS() { return getToken(ScenarioCalcParser.MINUS, 0); }
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryMinusContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenExprContext extends PrimaryContext {
		public TerminalNode LPAREN() { return getToken(ScenarioCalcParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ScenarioCalcParser.RPAREN, 0); }
		public ParenExprContext(PrimaryContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringLitContext extends PrimaryContext {
		public TerminalNode STRING() { return getToken(ScenarioCalcParser.STRING, 0); }
		public StringLitContext(PrimaryContext ctx) { copyFrom(ctx); }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primary);
		try {
			setState(188);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				_localctx = new NumberContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(NUMBER);
				}
				break;
			case ID:
				_localctx = new VarRefContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(178);
				match(ID);
				}
				break;
			case STRING:
				_localctx = new StringLitContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(179);
				match(STRING);
				}
				break;
			case LPAREN:
				_localctx = new ParenExprContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(180);
				match(LPAREN);
				setState(181);
				expr(0);
				setState(182);
				match(RPAREN);
				}
				break;
			case PLUS:
				_localctx = new UnaryPlusContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(184);
				match(PLUS);
				setState(185);
				primary();
				}
				break;
			case MINUS:
				_localctx = new UnaryMinusContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(186);
				match(MINUS);
				setState(187);
				primary();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 11:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		case 14:
			return arithmetic_sempred((ArithmeticContext)_localctx, predIndex);
		case 15:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean arithmetic_sempred(ArithmeticContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u00bf\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0005\u0000"+
		"&\b\u0000\n\u0000\f\u0000)\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0005\u0003"+
		"9\b\u0003\n\u0003\f\u0003<\t\u0003\u0001\u0004\u0001\u0004\u0005\u0004"+
		"@\b\u0004\n\u0004\f\u0004C\t\u0004\u0001\u0005\u0001\u0005\u0004\u0005"+
		"G\b\u0005\u000b\u0005\f\u0005H\u0001\u0006\u0001\u0006\u0003\u0006M\b"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007S\b"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0004\bY\b\b\u000b\b\f\bZ\u0001"+
		"\b\u0001\b\u0004\b_\b\b\u000b\b\f\b`\u0003\bc\b\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0003\tj\b\t\u0001\t\u0003\tm\b\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\nu\b\n\n\n\f\nx\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0080"+
		"\b\u000b\n\u000b\f\u000b\u0083\t\u000b\u0001\f\u0001\f\u0001\f\u0003\f"+
		"\u0088\b\f\u0001\r\u0001\r\u0001\r\u0003\r\u008d\b\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0005\u000e\u0098\b\u000e\n\u000e\f\u000e\u009b\t\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00a6\b\u000f\n\u000f"+
		"\f\u000f\u00a9\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0003\u0010\u00b0\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0003\u0011\u00bd\b\u0011\u0001\u0011\u0000\u0004"+
		"\u0014\u0016\u001c\u001e\u0012\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"\u0000\u0001\u0001\u0000"+
		"\u0018\u001d\u00c5\u0000\'\u0001\u0000\u0000\u0000\u0002,\u0001\u0000"+
		"\u0000\u0000\u00042\u0001\u0000\u0000\u0000\u00066\u0001\u0000\u0000\u0000"+
		"\b=\u0001\u0000\u0000\u0000\nD\u0001\u0000\u0000\u0000\fL\u0001\u0000"+
		"\u0000\u0000\u000eN\u0001\u0000\u0000\u0000\u0010T\u0001\u0000\u0000\u0000"+
		"\u0012f\u0001\u0000\u0000\u0000\u0014n\u0001\u0000\u0000\u0000\u0016y"+
		"\u0001\u0000\u0000\u0000\u0018\u0087\u0001\u0000\u0000\u0000\u001a\u0089"+
		"\u0001\u0000\u0000\u0000\u001c\u008e\u0001\u0000\u0000\u0000\u001e\u009c"+
		"\u0001\u0000\u0000\u0000 \u00af\u0001\u0000\u0000\u0000\"\u00bc\u0001"+
		"\u0000\u0000\u0000$&\u0003\u0002\u0001\u0000%$\u0001\u0000\u0000\u0000"+
		"&)\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000"+
		"\u0000(*\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000*+\u0005\u0000"+
		"\u0000\u0001+\u0001\u0001\u0000\u0000\u0000,-\u0005\u0001\u0000\u0000"+
		"-.\u0005!\u0000\u0000./\u0005\u0013\u0000\u0000/0\u0003\u0004\u0002\u0000"+
		"01\u0005\u0014\u0000\u00001\u0003\u0001\u0000\u0000\u000023\u0003\u0006"+
		"\u0003\u000034\u0003\b\u0004\u000045\u0003\n\u0005\u00005\u0005\u0001"+
		"\u0000\u0000\u00006:\u0005\u0002\u0000\u000079\u0003\f\u0006\u000087\u0001"+
		"\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000"+
		":;\u0001\u0000\u0000\u0000;\u0007\u0001\u0000\u0000\u0000<:\u0001\u0000"+
		"\u0000\u0000=A\u0005\u0003\u0000\u0000>@\u0003\f\u0006\u0000?>\u0001\u0000"+
		"\u0000\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000B\t\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000"+
		"DF\u0005\u0004\u0000\u0000EG\u0003\u0012\t\u0000FE\u0001\u0000\u0000\u0000"+
		"GH\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000"+
		"\u0000I\u000b\u0001\u0000\u0000\u0000JM\u0003\u000e\u0007\u0000KM\u0003"+
		"\u0010\b\u0000LJ\u0001\u0000\u0000\u0000LK\u0001\u0000\u0000\u0000M\r"+
		"\u0001\u0000\u0000\u0000NO\u0005#\u0000\u0000OP\u0005\u0017\u0000\u0000"+
		"PR\u0003\u0014\n\u0000QS\u0005\u0015\u0000\u0000RQ\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000S\u000f\u0001\u0000\u0000\u0000TU\u0005\u0005"+
		"\u0000\u0000UV\u0003\u0014\n\u0000VX\u0005\u0006\u0000\u0000WY\u0003\f"+
		"\u0006\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000ZX\u0001"+
		"\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[b\u0001\u0000\u0000\u0000"+
		"\\^\u0005\u0007\u0000\u0000]_\u0003\f\u0006\u0000^]\u0001\u0000\u0000"+
		"\u0000_`\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000ac\u0001\u0000\u0000\u0000b\\\u0001\u0000\u0000\u0000bc\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0005\b\u0000\u0000e\u0011"+
		"\u0001\u0000\u0000\u0000fi\u0005#\u0000\u0000gh\u0005\t\u0000\u0000hj"+
		"\u0005!\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000"+
		"jl\u0001\u0000\u0000\u0000km\u0005\u0015\u0000\u0000lk\u0001\u0000\u0000"+
		"\u0000lm\u0001\u0000\u0000\u0000m\u0013\u0001\u0000\u0000\u0000no\u0006"+
		"\n\uffff\uffff\u0000op\u0003\u0016\u000b\u0000pv\u0001\u0000\u0000\u0000"+
		"qr\n\u0002\u0000\u0000rs\u0005\u001f\u0000\u0000su\u0003\u0016\u000b\u0000"+
		"tq\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000vw\u0001\u0000\u0000\u0000w\u0015\u0001\u0000\u0000\u0000xv\u0001"+
		"\u0000\u0000\u0000yz\u0006\u000b\uffff\uffff\u0000z{\u0003\u0018\f\u0000"+
		"{\u0081\u0001\u0000\u0000\u0000|}\n\u0002\u0000\u0000}~\u0005\u001e\u0000"+
		"\u0000~\u0080\u0003\u0018\f\u0000\u007f|\u0001\u0000\u0000\u0000\u0080"+
		"\u0083\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0017\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0084\u0085\u0005 \u0000\u0000\u0085\u0088"+
		"\u0003\u0018\f\u0000\u0086\u0088\u0003\u001a\r\u0000\u0087\u0084\u0001"+
		"\u0000\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0088\u0019\u0001"+
		"\u0000\u0000\u0000\u0089\u008c\u0003\u001c\u000e\u0000\u008a\u008b\u0007"+
		"\u0000\u0000\u0000\u008b\u008d\u0003\u001c\u000e\u0000\u008c\u008a\u0001"+
		"\u0000\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d\u001b\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0006\u000e\uffff\uffff\u0000\u008f\u0090"+
		"\u0003\u001e\u000f\u0000\u0090\u0099\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\n\u0003\u0000\u0000\u0092\u0093\u0005\f\u0000\u0000\u0093\u0098\u0003"+
		"\u001e\u000f\u0000\u0094\u0095\n\u0002\u0000\u0000\u0095\u0096\u0005\r"+
		"\u0000\u0000\u0096\u0098\u0003\u001e\u000f\u0000\u0097\u0091\u0001\u0000"+
		"\u0000\u0000\u0097\u0094\u0001\u0000\u0000\u0000\u0098\u009b\u0001\u0000"+
		"\u0000\u0000\u0099\u0097\u0001\u0000\u0000\u0000\u0099\u009a\u0001\u0000"+
		"\u0000\u0000\u009a\u001d\u0001\u0000\u0000\u0000\u009b\u0099\u0001\u0000"+
		"\u0000\u0000\u009c\u009d\u0006\u000f\uffff\uffff\u0000\u009d\u009e\u0003"+
		" \u0010\u0000\u009e\u00a7\u0001\u0000\u0000\u0000\u009f\u00a0\n\u0003"+
		"\u0000\u0000\u00a0\u00a1\u0005\u000e\u0000\u0000\u00a1\u00a6\u0003 \u0010"+
		"\u0000\u00a2\u00a3\n\u0002\u0000\u0000\u00a3\u00a4\u0005\u000f\u0000\u0000"+
		"\u00a4\u00a6\u0003 \u0010\u0000\u00a5\u009f\u0001\u0000\u0000\u0000\u00a5"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8"+
		"\u001f\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa"+
		"\u00ab\u0003\"\u0011\u0000\u00ab\u00ac\u0005\u0010\u0000\u0000\u00ac\u00ad"+
		"\u0003 \u0010\u0000\u00ad\u00b0\u0001\u0000\u0000\u0000\u00ae\u00b0\u0003"+
		"\"\u0011\u0000\u00af\u00aa\u0001\u0000\u0000\u0000\u00af\u00ae\u0001\u0000"+
		"\u0000\u0000\u00b0!\u0001\u0000\u0000\u0000\u00b1\u00bd\u0005\"\u0000"+
		"\u0000\u00b2\u00bd\u0005#\u0000\u0000\u00b3\u00bd\u0005!\u0000\u0000\u00b4"+
		"\u00b5\u0005\u0011\u0000\u0000\u00b5\u00b6\u0003\u0014\n\u0000\u00b6\u00b7"+
		"\u0005\u0012\u0000\u0000\u00b7\u00bd\u0001\u0000\u0000\u0000\u00b8\u00b9"+
		"\u0005\f\u0000\u0000\u00b9\u00bd\u0003\"\u0011\u0000\u00ba\u00bb\u0005"+
		"\r\u0000\u0000\u00bb\u00bd\u0003\"\u0011\u0000\u00bc\u00b1\u0001\u0000"+
		"\u0000\u0000\u00bc\u00b2\u0001\u0000\u0000\u0000\u00bc\u00b3\u0001\u0000"+
		"\u0000\u0000\u00bc\u00b4\u0001\u0000\u0000\u0000\u00bc\u00b8\u0001\u0000"+
		"\u0000\u0000\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bd#\u0001\u0000\u0000"+
		"\u0000\u0015\':AHLRZ`bilv\u0081\u0087\u008c\u0097\u0099\u00a5\u00a7\u00af"+
		"\u00bc";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}