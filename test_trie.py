import pytest
from trie import CompactTrie, Node, checkPrefixSubstring


# Deve-se implementar também o algoritmo que identifica a maior substring que se 
# repete no texto. Isso é, o algoritmo deve localizar e retornar a maior substring
# w no genoma do Sars-cov-2 que ocorre em pelo menos duas posições distintas do
# texto

# Sua implementação deve retornar essa string e o número de ocorrências no
# texto. Poderão ser introduzidas modificações na estrutura de dados para facilitar
# a implementação dessa funcionalidade.

class Test_checkPrefix:
    def test_no_match(self):
        assert checkPrefixSubstring('','') == 0
        assert checkPrefixSubstring('','as') == 0
        assert checkPrefixSubstring('as','') == 0
    
    def test_symmetry(self):
        assert checkPrefixSubstring('ab','cd') == checkPrefixSubstring('cd','ab')
        assert checkPrefixSubstring('she','sells') == \
                    checkPrefixSubstring('sells','she')
        assert checkPrefixSubstring('sell','sells') == \
                    checkPrefixSubstring('sells','sell')

    def test_one_match(self):
        assert checkPrefixSubstring('she','sells') == 1
        assert checkPrefixSubstring('s','s') == 1
        
    def test_more_match_prefix(self):
        assert checkPrefixSubstring('sell','sells') == 4
    
    def test_equals(self):
        assert checkPrefixSubstring('sell','sell') == 4
        assert checkPrefixSubstring('she','she') == 3

    def test_no_prefix_match(self):
        assert checkPrefixSubstring('sell','mysells') == 0
    
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
    
class Test_ComplexaCompactTrie:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
    
    def setup_method(self, method):
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

    def test_busca_complexa(self):
        node = Node(21,22)
        assert self.trie.find(21,22) == node
        node = Node(24,26)
        assert self.trie.find(24,26) == node
        node = Node(17,19)
        assert self.trie.find(14,19) == node
        node = Node()
        assert self.trie.find(0,2) == node
        node = Node(6,8)
        assert self.trie.find(4,8) == node
        node = Node(12,12)
        assert self.trie.find(10,12) == node
        assert self.trie.find(28,30) == node
    
    def test_busca_vazia(self):
        assert self.trie.find(13,13) == None
        assert self.trie.find(0,3) == None
        assert self.trie.find(14,20) == None
        assert self.trie.find(24,27) == None
        assert self.trie.find(4,9) == None
        assert self.trie.find(1,2) == None
    
    def test_findNode_found(self):
        node = Node(21,22)
        assert self.trie.findNode(21,22) == (node,'by')
        node = Node(24,26)
        assert self.trie.findNode(24,26) == (node,'the')
        node = Node(17,19)
        assert self.trie.findNode(14,19) == (node,'shells')
        node = Node()
        assert self.trie.findNode(0,2) == (node,'she')
        node = Node(6,8)
        assert self.trie.findNode(4,8) == (node,'sells')
        node = Node(12,12)
        assert self.trie.findNode(10,12) == (node,'sea')
        assert self.trie.findNode(28,30) == (node,'sea')

    def test_findNode_not_found(self):
        raiz = Node() 
        assert self.trie.findNode(13,13) == (raiz,'')
        assert self.trie.findNode(1,2) == (raiz,'')
        node = Node(1,2)
        assert self.trie.findNode(0,3) == (node,'she')
        node = Node(17,19)
        assert self.trie.findNode(14,20) == (node,'shells')
        node = Node(24,26)
        assert self.trie.findNode(24,27) == (node,'the')
        node = Node(6,8)
        assert self.trie.findNode(4,9) == (node,'sells')
    
    def test_findNode_partial_found(self):
        node = Node(17,19)
        assert self.trie.findNode(14,17) == (node,'shel')
        node = Node(6,8)
        assert self.trie.findNode(4,6) == (node,'sel')
        assert self.trie.findNode(4,7) == (node,'sell')
        node = Node(1,2)
        assert self.trie.findNode(0,1) == (node,'sh')
        assert self.trie.findNode(14,15) == (node,'sh')
        node = Node(5,5)
        assert self.trie.findNode(4,5) == (node,'se')
        assert self.trie.findNode(10,11) == (node,'se')
        assert self.trie.findNode(28,29) == (node,'se')

    
    
    





class Test_InsercaoCompactTrie:
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
        node = Node(21,22)
        assert self.trie.find(21,22) == node
        node = Node(24,26)
        assert self.trie.find(24,26) == node
        node = Node(17,19)
        assert self.trie.find(14,19) == node
        node = Node()
        assert self.trie.find(0,2) == node
        node = Node(6,8)
        assert self.trie.find(4,8) == node
        node = Node(12,12)
        assert self.trie.find(10,12) == node
        assert self.trie.find(28,30) == node

    def test_insercao_complexa_nodes_falsos(self):
        assert self.trie.find(13,13) == None
        assert self.trie.find(0,3) == None
        assert self.trie.find(14,20) == None
        assert self.trie.find(24,27) == None
        assert self.trie.find(4,9) == None
    
    



