from triesearcher import TrieSearcher

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
            # string = self.texto[inicio:fim+1]
            # lastNode, casParcial = self.findNode(inicio, fim)
            # if casParcial == '':
            #     # String não casa parcialmente com nada na Trie
            #     newNode = Node(inicio, fim)
            #     self.root.children.append(newNode)
            
            raise("TODO")

    def find(self, a, b):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie
        Retorna None se a substring não for encontrada 
        """
        if self.isEmpty():
            return None
        string = self.texto[a:b+1]
        finder = TrieSearcher(self.texto, self, a, b)
        nodeAtual,casParcial = finder.findNode()
        if casParcial == string:
            return nodeAtual
        else: 
            return None
        
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
    
    def __eq__(self, other):
        if isinstance(other, Node):
            if (self.inicio == other.inicio and \
                self.fim == other.fim):
                return True
        return False

class Trie:
    def __init__(self):
        self.texto = 'she_sells_sea_shells_by_the_sea'
        self.trie = None
        self.trie = CompactTrie(self.texto)

        n1 = Node(17,19)
        n2 = Node()
        n3 = Node(1,2)
        n3.children.append(n1)
        n3.children.append(n2)

        n4 = Node(6,8)
        n5 = Node(12,12)
        n6 = Node(5,5)
        n6.children.append(n4)
        n6.children.append(n5)
        
        n7 = Node(0,0)
        n7.children.append(n3)
        n7.children.append(n6)

        n8 = Node(24,26)
        n9 = Node(21,22)

        self.trie.root.children.append(n8)
        self.trie.root.children.append(n9)
        self.trie.root.children.append(n7)

if __name__ == "__main__":
    trie = Trie()
    trie.trie.findNode(0,1)