import pytest
from trie import CompactTrie, Node, checkPrefixSubstring

# A árvore de sufixos deverá ser implementada através de uma Trie compacta

# Dessa forma, os nós da árvore serão rotulados por pares de índices, identificando 
# início e fim da substring no texto. 

# A árvore pode ser construída com um algoritmo quadrático, inserindo os sufixos
# um a um. 

# Deve-se implementar também o algoritmo que identifica a maior substring que se 
# repete no texto. Isso é, o algoritmo deve localizar e retornar a maior substring
# w no genoma do Sars-cov-2 que ocorre em pelo menos duas posições distintas do
# texto

# Sua implementação deve retornar essa string e o número de ocorrências no
# texto. Poderão ser introduzidas modificações na estrutura de dados para facilitar
# a implementação dessa funcionalidade.
class Test_Node:
    def test_init_raiz(self):
        node = Node()
        assert node.inicio == None
        assert node.fim == None

    def test_init(self):
        node = Node(0,7)
        assert node.inicio == 0
        assert node.fim == 7

    def test_modificacao_inicio(self):
        node1 = Node(0,7)
        node1.setInicio(2)
        assert node1.inicio == 2
        assert node1.fim == 7

    def test_modificacao_fim(self):
        node2 = Node(0,7)
        node2.setFim(4)
        assert node2.inicio == 0
        assert node2.fim == 4

    def test_sets_invalidos(self):
        node1 = Node(0,7)
        node2 = Node(3,7)
        with pytest.raises(Exception):
            node1.setInicio(10)
        with pytest.raises(Exception):
            node2.setFim(1)
    
    def test_no_um_caractere(self):
        node = Node(0,0)
        node1 = Node(1,1)
        node2 = Node(45,45)


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
    
    def test_no_prefix_match(self):
        assert checkPrefixSubstring('sell','mysells') == 0
    

class Test_CompactTrie:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she'

    def test_init(self):
        trie = CompactTrie(self.texto)
    
    def test_vazia(self):
        trie = CompactTrie(self.texto)
        assert trie.isEmpty() == True

    def test_insercao(self):
        trie = CompactTrie(self.texto)
        trie.insert('she')
        assert trie.isEmpty() == False

    def test_busca(self):
        trie = CompactTrie(self.texto)
        assert trie.find('A') == False
        trie.insert('she')
        assert trie.find('she') == True


