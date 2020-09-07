from node import Node
from triesearcher import TrieSearcher
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
        if self.isEmpty():
            newNode = Node(inicio, fim)
            self.root.addChild(newNode)
        else:
            string = self.texto[inicio:fim+1]
            searcher = TrieSearcher(self.texto, self, inicio, fim)
            nodeAtual,casParcial,casNode = searcher.findNode()
            match = checkPrefixSubstring(casParcial,string)
            if casParcial == '':
                # String não casa parcialmente com nada na Trie
                newNode = Node(inicio, fim)
                self.root.addChild(newNode)
            elif casParcial == string and casNode == string:
                pass
            elif casParcial == string and casNode != string:
                # String casa parcialmente com o node atual
                #Divide o nó atual
                labelNode = self.texto[nodeAtual.inicio:nodeAtual.fim+1]
                # n = checkPrefixSubstring(casNode,labelNode)
                # labelParent = casNode[0:n+1]
                matchNormalizado = match - (len(casNode) - len(labelNode))
                newNodeParent = Node(nodeAtual.inicio, nodeAtual.inicio+matchNormalizado-1)
                grandNode = nodeAtual.parent
                grandNode.children.remove(nodeAtual)
                newNodeParent.parent = nodeAtual.parent

                #Filho2: label que sobrou do pai
                newNodeSon = Node(nodeAtual.inicio+matchNormalizado,nodeAtual.fim)
                newNodeSon.children = nodeAtual.children
                newNodeParent.addChild(newNodeSon)

                #Filho1: novo (fim de palavra)
                newNode = Node()
                newNode.parent = newNodeParent
                newNodeParent.addChild(newNode)

                #Arruma o parent do newNodeParent
                grandNode.addChild(newNodeParent)
            elif casParcial == casNode and casNode != string:
                # String casa perfeitamente com o nó atual
                #Filho1: marcador de fim de palavra
                newNodeSon = Node()
                nodeAtual.addChild(newNodeSon)

                #Filho2: palavra nova que engloba uma que já existe na Trie
                newNode = Node(inicio+match, fim)
                nodeAtual.addChild(newNode)
            else:
                # String casa parcialmente com o node atual
                #Divide o nó atual
                labelNode = self.texto[nodeAtual.inicio:nodeAtual.fim+1]
                # n = checkPrefixSubstring(casNode,labelNode)
                # labelParent = casNode[0:n+1]
                matchNormalizado = match - (len(casNode) - len(labelNode))
                newNodeParent = Node(nodeAtual.inicio, nodeAtual.inicio+matchNormalizado-1)
                grandNode = nodeAtual.parent
                grandNode.children.remove(nodeAtual)
                newNodeParent.parent = nodeAtual.parent

                #Filho2: label que sobrou do pai
                newNodeSon = Node(nodeAtual.inicio+matchNormalizado,nodeAtual.fim)
                newNodeSon.children = nodeAtual.children
                newNodeParent.addChild(newNodeSon)

                #Filho1: novo (fim de palavra)
                newNode = Node(inicio+match, fim)
                newNode.parent = newNodeParent
                newNodeParent.addChild(newNode)

                #Arruma o parent do newNodeParent
                grandNode.addChild(newNodeParent)

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
        return (maior, strMaior)