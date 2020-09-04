
# Retorna o tamanho do maior prefixo de string que é prefixo de sub
def checkPrefixSubstring(string, sub):
    n = min([len(string),len(sub)])

    # Alguma string vazia
    if n == 0: 
        return 0
    for i in range(n):
        if string[i] != sub[i]:
            return i

    return n

class CompactTrie:
    def __init__(self, texto):
        self.root = Node()
        self.texto = texto
    
    def isEmpty(self):
        if len(self.root.children) == 0:
            return True
        return False
    
    def insert(self, inicio, fim):
        if self.isEmpty():
            newNode = Node(inicio, fim)
            self.root.children.append(newNode)
        else:
            self.find
            raise("TODO")

    
    # Procura a substring texto[a,b] na Trie
    def find(self, a, b):
        nodeAtual = self.root
        string = texto[a:b]
        padraoNode = None
        nodeProx = self.root.children[0]
        while nodeProx is not None:
            padraoNode = texto[nodeProx.inicio, nodeProx.fim]



class Node:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        self.children = []

    def setInicio(self, novoInicio):
        if novoInicio > self.fim:
            raise Exception
        self.inicio = novoInicio

    def setFim(self, novoFim):
        if novoFim < self.inicio:
            raise Exception
        self.fim = novoFim