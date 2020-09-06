import pytest
from trie import Node
from test_trie import montaTrie
from trie import CompactTrie
from triesearcher import TrieSearcher

class Test_TrieSearch:
    def setup_method(self, method):
        self.trie = montaTrie()
        self.texto = 'she_sells_sea_shells_by_the_sea'

    def test_findNode_found(self):
        assertList = [
            (Node(21,22), (21,22), 'by', 'by'),
            (Node(24,26), (24,26), 'the', 'the'),
            (Node(17,19), (14,19), 'shells', 'shells'),
            (Node(), (0,2), 'she', 'she'),
            (Node(6,8), (4,8), 'sells', 'sells'),
            (Node(12,12), (10,12), 'sea', 'sea'),
            (Node(12,12), (28,30), 'sea', 'sea'),
        ]
        for quad in assertList:
            node = quad[0]
            interval = quad[1]
            word = quad[2]
            label = quad[3]
            search = TrieSearcher(self.texto, self.trie, interval[0], interval[1])
            assert search.findNode() == (node, word, label), f"quad = {quad}"

    def test_findNode_not_found(self):
        assertList = [
            (Node(), (13,13), '', ''),
            (Node(), (1,2), '', ''),
            (Node(1,2), (0,3), 'she', 'she'),
            (Node(17,19), (14,20), 'shells', 'shells'),
            (Node(24,26), (24,27), 'the', 'the'),
            (Node(6,8), (4,9), 'sells', 'sells')
        ]
        for quad in assertList:
            node = quad[0]
            interval = quad[1]
            word = quad[2]
            label = quad[3]
            search = TrieSearcher(self.texto, self.trie, interval[0], interval[1])
            assert search.findNode() == (node, word, label), f"quad = {quad}"


    def test_findNode_partial_found(self):
        assertList = [
            (Node(17,19), (14,17), 'shel','shells'),
            (Node(6,8), (4,6), 'sel','sells'),
            (Node(6,8), (4,7), 'sell','sells'),
            (Node(1,2), (0,1), 'sh','she'),
            (Node(1,2), (14,15), 'sh','she'),
            (Node(5,5), (4,5), 'se','se'),
            (Node(5,5), (10,11), 'se','se'),
            (Node(5,5), (28,29), 'se','se')
        ]
        for quad in assertList:
            node = quad[0]
            interval = quad[1]
            word = quad[2]
            label = quad[3]
            search = TrieSearcher(self.texto, self.trie, interval[0], interval[1])
            assert search.findNode() == (node, word, label), f"quad = {quad}"

class Test_SimpleTrieSearch:
    @classmethod
    def setup_class(cls):
        cls.texto = 'she_sells_sea_shells_by_the_sea'
        cls.trie = CompactTrie(cls.texto)
        cls.trie.insert(0,2)
    def test_simples(self):
        search = TrieSearcher(self.texto, self.trie, 4, 8)
        node = Node(0,2)
        assert search.findNode() == (node, 's','she')
    
        