import pytest
from trie import CompactTrie, Node
from triesearcher import TrieSearcher

# Deve-se implementar também o algoritmo que identifica a maior substring que se 
# repete no texto. Isso é, o algoritmo deve localizar e retornar a maior substring
# w no genoma do Sars-cov-2 que ocorre em pelo menos duas posições distintas do
# texto

# Sua implementação deve retornar essa string e o número de ocorrências no
# texto. Poderão ser introduzidas modificações na estrutura de dados para facilitar
# a implementação dessa funcionalidade.

  
# A árvore de sufixos deverá ser implementada através de uma Trie compacta
# A árvore pode ser construída com um algoritmo quadrático, inserindo os sufixos
# um a um. 
class Test_CompactTrie:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she'

    def test_init(self):
        trie = CompactTrie(self.texto)
    
    def test_vazia(self):
        trie = CompactTrie(self.texto)
        assert trie.isEmpty() == True

    def test_insercao_simples(self):
        trie = CompactTrie(self.texto)
        trie.insert(0,2)
        assert trie.isEmpty() == False

    def test_busca_simples(self):
        trie = CompactTrie(self.texto)
        assert trie.find(1,2) == None
        trie.insert(0,2)
        node = Node(0,2)
        assert trie.find(0,2) == node
    
class Test_CompactTrieBusca:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
        cls.trie = montaTrie()

    def test_busca_complexa(self):
        assertList = [
            (Node(21,22), (21,22)),
            (Node(24,26), (24,26)),
            (Node(17,19), (14,19)),
            (Node(), (0,2)),
            (Node(6,8), (4,8)),
            (Node(12,12), (10,12)),
            (Node(12,12), (28,30))
        ]
        for pair in assertList:
            node = pair[0]
            interval = pair[1]
            assert self.trie.find(interval[0], interval[1]) == node
    
    def test_busca_vazia(self):
        assert self.trie.find(13,13) == None
        assert self.trie.find(0,3) == None
        assert self.trie.find(14,20) == None
        assert self.trie.find(24,27) == None
        assert self.trie.find(4,9) == None
        assert self.trie.find(1,2) == None

class Test_CompactTrieInsercaoCompleta:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
    
    def setup_method(self, method):
        self.trie = CompactTrie(self.texto)
        self.trie.insert(0,2)
        self.trie.insert(4,8)
        self.trie.insert(10,12)
        self.trie.insert(14,19)
        self.trie.insert(21,22)
        self.trie.insert(24,26)
        self.trie.insert(28,30)

    def test_insercao_complexa(self):
        assertList = [
            (Node(21,22), (21,22)),
            (Node(24,26), (24,26)),
            (Node(17,19), (14,19)),
            (Node(), (0,2)),
            (Node(6,8), (4,8)),
            (Node(12,12), (10,12)),
            (Node(12,12), (28,30))
        ]
        for pair in assertList:
            node = pair[0]
            interval = pair[1]
            assert self.trie.find(interval[0], interval[1]) == node, \
            f"{interval[0]},{interval[1]} != {node.inicio},{node.fim}"

    def test_insercao_complexa_nodes_falsos(self):
        assert self.trie.find(13,13) == None
        assert self.trie.find(0,3) == None
        assert self.trie.find(14,20) == None
        assert self.trie.find(24,27) == None
        assert self.trie.find(4,9) == None

class Test_CompactTrieInsertCase1:
    @classmethod
    def setup_class(cls):
        cls.trie = CompactTrie('she_sells_sea_shells_by_the_sea')
    
    def test_case01(self):
        assert len(self.trie.root.children) == 0
    
    def test_case02(self):
        self.trie.insert(0,2)
        node = Node(0,2)
        assert len(self.trie.root.children) == 1
        assert self.trie.root.children[0] == node

    def test_case03(self):
        self.trie.insert(0,3)
        node = Node(0,2)
        node1 = Node(3,3)
        assert len(self.trie.root.children) == 1
        assert self.trie.root.children[0] == node
        assert len(self.trie.root.children[0].children) == 2
        assert self.trie.find(0,3) == node1
        assert self.trie.find(0,2) == Node()

class Test_CompactTrieInsertCase2:
    @classmethod
    def setup_class(cls):
        cls.trie = CompactTrie('she_sells_sea_shells_by_the_sea')
    def test_case01(self):
        assert len(self.trie.root.children) == 0
    def test_case02(self):
        self.trie.insert(0,2)
        self.trie.insert(4,8)
        assert len(self.trie.root.children) == 1
        node0 = Node(0,0)
        assert self.trie.root.children[0] == node0
        assert len(self.trie.root.children[0].children) == 2
        assert self.trie.find(0,2) == Node(1,2)
        assert self.trie.find(4,8) == Node(5,8)


    def test_case03(self):
        self.trie.insert(0,2)
        self.trie.insert(4,8)
        self.trie.insert(10,12)
        assert len(self.trie.root.children) == 1
        node0 = Node(0,0)
        assert self.trie.root.children[0] == node0
        assert len(self.trie.root.children[0].children) == 2
        assert self.trie.find(0,2) == Node(1,2)
        assert self.trie.find(4,8) == Node(6,8)
        assert self.trie.find(10,12) == Node(12,12)

def montaTrie():
    texto = 'she_sells_sea_shells_by_the_sea'
    trie = CompactTrie(texto)

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

    trie.root.children.append(n8)
    trie.root.children.append(n9)
    trie.root.children.append(n7)
    return trie


