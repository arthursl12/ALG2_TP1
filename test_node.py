import pytest
from node import Node

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

class Test_NodePai:
    @classmethod
    def setup_class(cls):
        cls.node0 = Node(1,2)
        cls.node1 = Node(3,4)
        cls.node2 = Node(8,8)

    def test_sem_filhos(self):
        assert self.node0.getChildren() == []
        assert len(self.node0.getChildren()) == 0
        assert self.node0.getParent() == None
    
    def test_filho(self):
        self.node0.addChild(self.node1)
        assert self.node0.getChildren()[0] == self.node1
        assert self.node0.getChildren()[0].getParent() == self.node0

    def test_filhos(self):
        self.node0.addChild(self.node2)
        assert len(self.node0.getChildren()) == 2
        for node in self.node0.getChildren():
            assert node.getParent() == self.node0
    
        
