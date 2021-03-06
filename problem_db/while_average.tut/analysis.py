class CodeVisitor(TutorialNodeVisitor):
    def __init__(self):
        super().__init__()

        self.has_while_statement = False

    def visit_While(self, node):
        self.has_while_statement = True

class Analyser(CodeAnalyser):
    def _analyse(self):
        if not self.visitor.has_while_statement:
            self.add_error('You need to use a while statement')

ANALYSER = Analyser(CodeVisitor)
