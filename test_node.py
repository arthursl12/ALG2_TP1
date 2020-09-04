import pytest
from trie import Node

# Dessa forma, os nós da árvore serão rotulados por pares de índices, identificando 
# início e fim da substring no texto. 
class Test_Node:
    def test_init_raiz(self):
        node = Node()
        assert node.inicio == None
        assert node.fim == None

    def test_init(self):
        node = Node(0,7)
        assert node.inicio == 0
        assert node.fim == 7

    def test_tipos(self):
        node = Node(0,7)
        assert type(node.inicio) == int
        assert type(node.fim) == int

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
    
    def test_node_um_caractere(self):
        node = Node(0,0)
        node1 = Node(1,1)
        node2 = Node(45,45)
    
    def test_equality(self):
        node = Node(0,1)
        node1 = Node(2,5)
        node2 = Node(0,1)
        assert node != node1
        assert node1 != node
        assert node == node2
