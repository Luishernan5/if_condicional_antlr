from antlr4 import *
from .IfVisitor import IfVisitor
from .IfParser import IfParser

class EvalIfVisitor(IfVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}

    # Asignación
    def visitAssign(self, ctx: IfParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    # Print
    def visitPrint(self, ctx: IfParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    # If statement
    def visitIfStatement(self, ctx: IfParser.IfStatementContext):
        left = self.visit(ctx.condition().expr(0))
        right = self.visit(ctx.condition().expr(1))
        op = ctx.condition().getChild(1).getText()

        cond = False
        if op == '>':
            cond = left > right
        elif op == '<':
            cond = left < right
        elif op == '==':
            cond = left == right
        elif op == '>=':
            cond = left >= right
        elif op == '<=':
            cond = left <= right

        if cond:
            for stmt in ctx.statement():
                self.visit(stmt)
        return None

    # Expr con suma/resta
    def visitAddSub(self, ctx: IfParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    # Expr con mul/div
    def visitMulDiv(self, ctx: IfParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            if right == 0:
                raise ValueError("División por cero")
            return left / right

    def visitInt(self, ctx: IfParser.IntContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx: IfParser.VariableContext):
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            raise NameError(f"Variable '{var_name}' no definida")
        return self.memory[var_name]

    def visitParens(self, ctx: IfParser.ParensContext):
        return self.visit(ctx.expr())