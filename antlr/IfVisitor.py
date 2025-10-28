# Generated from If.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IfParser import IfParser
else:
    from IfParser import IfParser

# This class defines a complete generic visitor for a parse tree produced by IfParser.

class IfVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IfParser#program.
    def visitProgram(self, ctx:IfParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#statement.
    def visitStatement(self, ctx:IfParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#assign.
    def visitAssign(self, ctx:IfParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#print.
    def visitPrint(self, ctx:IfParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#ifStatement.
    def visitIfStatement(self, ctx:IfParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#condition.
    def visitCondition(self, ctx:IfParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#Variable.
    def visitVariable(self, ctx:IfParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#MulDiv.
    def visitMulDiv(self, ctx:IfParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#AddSub.
    def visitAddSub(self, ctx:IfParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#Parens.
    def visitParens(self, ctx:IfParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IfParser#Int.
    def visitInt(self, ctx:IfParser.IntContext):
        return self.visitChildren(ctx)



del IfParser