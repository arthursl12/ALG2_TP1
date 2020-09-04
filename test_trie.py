import pytest
from trie import CompactTrie, Node, EmptyNodeException

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
    def test_init(self):
        with pytest.raises(EmptyNodeException):
            node = Node()
        node = Node(0,7)
    def test_modificacao(self):
        raise("TODO")

class Test_CompactTrie:
    @pytest.mark.run(order=1)
    def test_init(self):
        trie = CompactTrie()
    
    @pytest.mark.run(order=2)
    def test_vazia(self):
        trie = CompactTrie()
        assert trie.isEmpty() == True

    @pytest.mark.run(order=3)
    def test_insercao(self):
        trie = CompactTrie()
        trie.insert('she')
        assert trie.isEmpty() == False
    
    @pytest.mark.run(order=4)
    def test_remocao(self):
        trie = CompactTrie()
        trie.insert('she')
        trie.remove('she')
        assert self.trie.isEmpty() == True


