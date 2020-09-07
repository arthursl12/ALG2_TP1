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

    def labelPai(self, texto):
        parent = self.parent
        label = ''
        if parent is not None:
            grand = parent.parent
            while grand is not None:
                label = parent.labelNode(texto) + label
                parent = grand
                grand = grand.parent
        return label
    
    def labelNode(self, texto):
        if self.inicio == None or self.fim == None:
            raise Exception
        else:
            return texto[self.inicio:self.fim+1] 


    
    def maiorSubstring(self, texto):
        if self.inicio == None and self.fim == None:
            return (1, self.labelPai(texto))
        if len(self.children) == 0:
            return (1,self.labelNode(texto))