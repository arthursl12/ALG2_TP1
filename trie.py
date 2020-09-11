from node import Node
from triesearcher import TrieSearcher
from trieinserter import TrieInserter
from helper import checkPrefixSubstring

class CompactTrie:
    def __init__(self, texto):
        self.root = Node()
        self.texto = texto
    
    def isEmpty(self):
        if len(self.root.children) == 0:
            return True
        return False       

    def insert(self, inicio, fim):
        """
        Insere a string [inicio:fim+1] na trie
        """
        if self.isEmpty():
            newNode = Node(inicio, fim)
            self.root.addChild(newNode)
            return
        
        string = self.texto[inicio:fim+1]
        searcher = TrieSearcher(self.texto, self, inicio, fim)
        nodeAtual,casParcial,casNode = searcher.findNode()
        inserter = TrieInserter(self.texto, self, nodeAtual, casParcial, casNode, string)
        inserter.insertNode(inicio, fim)

    def find(self, a, b):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie
        Retorna None se a substring não for encontrada 
        """
        if self.isEmpty():
            return None
        string = self.texto[a:b+1]
        nodeAtual,casParcial,casNode = TrieSearcher(self.texto, self, a, b).findNode()
        if casParcial == string:
            return nodeAtual
        else: 
            return None
        
    def maiorSubstring(self):
        """
        Retorna a maior substring que se repete na árvore de sufixos e a 
        quantidade de repetições, i.e., retorna a substring cuja subárvore
        possui mais folhas, sendo que cada folha representa uma ocorrência
        dessa substring
        """
        if self.isEmpty():
            return (1,'')
        maior = 0
        somaNodesSub = 0
        strMaior = ''
        for child in self.root.children:
            qtd, string = child.maiorSubstring(self.texto)
            somaNodesSub += qtd
            if qtd >= 2 and len(string) > len(strMaior) and len(string) > 1:
                maior = qtd
                strMaior = string
        return maior, strMaior