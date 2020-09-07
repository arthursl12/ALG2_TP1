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
                if grand is not None:
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
        maior = 0
        somaNodesSub = 0
        strMaior = ''
        for child in self.children:
            qtd, string = child.maiorSubstring(texto)
            somaNodesSub += qtd
            if qtd >= 2 and len(string) > len(strMaior):
                maior = qtd
                strMaior = string
        if maior == 0 and strMaior == '':
            return (somaNodesSub, self.labelPai(texto)+self.labelNode(texto))
        return (maior, strMaior)

if __name__ == "__main__":
    texto = 'she_sells_sea_shells_by_the_sea'
    # node0 = Node()
    # node1 = Node(17,19)
    # node2 = Node(1,2)
    # node2.addChild(node1)
    # node2.addChild(node0)

    # node3 = Node(6,8)
    # node4 = Node(12,12)
    # node5 = Node(5,5)
    # node5.addChild(node3)
    # node5.addChild(node4)

    # node6 = Node(0,0)
    # node6.addChild(node2)
    # node6.addChild(node5)

    # root = Node()
    # root.addChild(node6)
    # assert node6.maiorSubstring(texto) == (2, 'she')
    # node0 = Node()
    # node1 = Node(17,19)
    # node2 = Node(0,2)
    # node2.addChild(node1)
    # node2.addChild(node0)
    # root = Node()
    # root.addChild(node2)
    # assert node2.maiorSubstring(texto) == (2, 'she')