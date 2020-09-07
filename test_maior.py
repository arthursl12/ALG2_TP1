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
        node2 = Node(0,2)
        node2.addChild(node1)
        node2.addChild(node0)
        root = Node()
        root.addChild(node2)
        assert node2.maiorSubstring(self.texto) == (2, 'she')

    def test_tres_niveis(self):
        node0 = Node()
        node1 = Node(17,19)
        node2 = Node(1,2)
        node2.addChild(node1)
        node2.addChild(node0)

        node3 = Node(6,8)
        node4 = Node(12,12)
        node5 = Node(5,5)
        node5.addChild(node3)
        node5.addChild(node4)

        node6 = Node(0,0)
        node6.addChild(node2)
        node6.addChild(node5)

        root = Node()
        root.addChild(node6)
        assert node6.maiorSubstring(self.texto) == (2, 'she')
    

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

class Test_MaiorSubstringTrie02:
    def test_case01(self):
        texto = 'GEEKSFORGEEKS'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'GEEKS')

    def test_case02(self):
        texto = 'AAAAAAAAAA'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'AAAAAAAAA')
    
    def test_case03(self):
        texto = 'ABABABA'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'ABABA')
    
    def test_case04(self):
        texto = 'ATCGATCGA'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'ATCGA')
    
    def test_case05(self):
        texto = 'banana'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'ana')

    def test_case06(self):
        texto = 'abcpqrabpqpq'
        trie = CompactTrie(texto)
        for i in range(len(texto)):
            trie.insert(i,len(texto))
        assert trie.maiorSubstring() == (2,'ab')




