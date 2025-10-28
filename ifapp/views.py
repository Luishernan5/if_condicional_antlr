from django.shortcuts import render
from antlr4 import *
from antlr.IfLexer import IfLexer
from antlr.IfParser import IfParser
from antlr.EvalIfVisitor import EvalIfVisitor

def index(request):
    result = None
    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            input_stream = InputStream(code)
            lexer = IfLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = IfParser(token_stream)
            tree = parser.program()

            evaluator = EvalIfVisitor()
            evaluator.visit(tree)
            result = evaluator.memory
        except Exception as e:
            result = f"Error: {e}"
    return render(request, "ifapp/index.html", {"result": result})