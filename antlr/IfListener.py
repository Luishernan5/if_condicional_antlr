# Generated from If.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IfParser import IfParser
else:
    from IfParser import IfParser

# This class defines a complete listener for a parse tree produced by IfParser.
class IfListener(ParseTreeListener):

    # Enter a parse tree produced by IfParser#program.
    def enterProgram(self, ctx:IfParser.ProgramContext):
        pass

    # Exit a parse tree produced by IfParser#program.
    def exitProgram(self, ctx:IfParser.ProgramContext):
        pass


    # Enter a parse tree produced by IfParser#statement.
    def enterStatement(self, ctx:IfParser.StatementContext):
        pass

    # Exit a parse tree produced by IfParser#statement.
    def exitStatement(self, ctx:IfParser.StatementContext):
        pass


    # Enter a parse tree produced by IfParser#assign.
    def enterAssign(self, ctx:IfParser.AssignContext):
        pass

    # Exit a parse tree produced by IfParser#assign.
    def exitAssign(self, ctx:IfParser.AssignContext):
        pass


    # Enter a parse tree produced by IfParser#print.
    def enterPrint(self, ctx:IfParser.PrintContext):
        pass

    # Exit a parse tree produced by IfParser#print.
    def exitPrint(self, ctx:IfParser.PrintContext):
        pass


    # Enter a parse tree produced by IfParser#ifStatement.
    def enterIfStatement(self, ctx:IfParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IfParser#ifStatement.
    def exitIfStatement(self, ctx:IfParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IfParser#condition.
    def enterCondition(self, ctx:IfParser.ConditionContext):
        pass

    # Exit a parse tree produced by IfParser#condition.
    def exitCondition(self, ctx:IfParser.ConditionContext):
        pass


    # Enter a parse tree produced by IfParser#Variable.
    def enterVariable(self, ctx:IfParser.VariableContext):
        pass

    # Exit a parse tree produced by IfParser#Variable.
    def exitVariable(self, ctx:IfParser.VariableContext):
        pass


    # Enter a parse tree produced by IfParser#MulDiv.
    def enterMulDiv(self, ctx:IfParser.MulDivContext):
        pass

    # Exit a parse tree produced by IfParser#MulDiv.
    def exitMulDiv(self, ctx:IfParser.MulDivContext):
        pass


    # Enter a parse tree produced by IfParser#AddSub.
    def enterAddSub(self, ctx:IfParser.AddSubContext):
        pass

    # Exit a parse tree produced by IfParser#AddSub.
    def exitAddSub(self, ctx:IfParser.AddSubContext):
        pass


    # Enter a parse tree produced by IfParser#Parens.
    def enterParens(self, ctx:IfParser.ParensContext):
        pass

    # Exit a parse tree produced by IfParser#Parens.
    def exitParens(self, ctx:IfParser.ParensContext):
        pass


    # Enter a parse tree produced by IfParser#Int.
    def enterInt(self, ctx:IfParser.IntContext):
        pass

    # Exit a parse tree produced by IfParser#Int.
    def exitInt(self, ctx:IfParser.IntContext):
        pass



del IfParser