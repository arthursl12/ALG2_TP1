class Node:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        self.children = []
        self.parent = None

    def setInicio(self, novoInicio):
        if novoInicio > self.fim:
            raise Exception
        self.inicio = novoInicio

    def setFim(self, novoFim):
        if novoFim < self.inicio:
            raise Exception
        self.fim = novoFim
    
    def __eq__(self, other):
        if isinstance(other, Node):
            if (self.inicio == other.inicio and \
                self.fim == other.fim):
                return True
        return False
    
    def getChildren(self):
        return self.children
    
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def getParent(self):
        return self.parent