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
        if self.isEmpty():
            return None

        # Iteração inicial pela raiz
        nodeAtual = self.root
        string = self.texto[a:b+1]
        padraoAtual = ''
        print('1.1',nodeAtual,nodeAtual.inicio,nodeAtual.fim)
        for child in nodeAtual.children:
            print('2.1.0',nodeAtual,nodeAtual.inicio,nodeAtual.fim)
            print('2.1.1',child,child.inicio,child.fim)
            padraoNode = self.texto[child.inicio:child.fim+1]
            print('PN',padraoNode)
            print('PA',padraoAtual)
            match = checkPrefixSubstring(string, padraoAtual+padraoNode)
            if match >= 1:
                print('M',match)
                nodeAtual = child
                padraoAtual += string[0:match+1]

        # Iterações para os nós seguintes
        print('1.2',nodeAtual,nodeAtual.inicio,nodeAtual.fim)
        print(padraoAtual)
        for child in nodeAtual.children:
            print('2.2.0',nodeAtual,nodeAtual.inicio,nodeAtual.fim)
            print('2.2.1',child,child.inicio,child.fim)
            padraoNode = self.texto[child.inicio, child.fim+1]
            match = checkPrefixSubstring(string, padraoAtual+padraoNode)
            if match >= 1:
                nodeAtual = child
                padraoAtual += string[0:match+1]
        print('3',nodeAtual,nodeAtual.inicio,nodeAtual.fim)
        return nodeAtual

        


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