import pytest
from trie import CompactTrie
from node import Node

class Test_MaiorSubstringNode:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
    
    def test_node_vazio(self):
        node = Node()
        assert node.maiorSubstring(self.texto) == (1, '')
    def test_node_sem_filhos(self):
        node = Node(17,19)
        assert node.maiorSubstring(self.texto) == (1, 'lls')
    def test_node_dois_filhos(self):
        node0 = Node()
        node1 = Node(17,19)
        node2 = Node(1,2)
        node2.addChild(node1)
        node2.addChild(node0)
        assert node2.maiorSubstring(self.texto) == (2, 'she')

class Test_MaiorSubstringTrie:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
        cls.trie = CompactTrie(cls.texto)
        cls.trie.insert(0,2)
        cls.trie.insert(4,8)
        cls.trie.insert(10,12)
        cls.trie.insert(14,19)
        cls.trie.insert(21,22)
        cls.trie.insert(24,26)
        cls.trie.insert(28,30)
    
    def test_case01(self):
        assert self.trie.maiorSubstring() == (2,'she')



