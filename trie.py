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
            self.root.children.append(newNode)
            print('caso0')
        else:
            string = self.texto[inicio:fim+1]
            searcher = TrieSearcher(self.texto, self, inicio, fim)
            nodeAtual,casParcial = searcher.findNode()
            match = checkPrefixSubstring(casParcial,string)
            if casParcial == '':
                # String não casa parcialmente com nada na Trie
                newNode = Node(inicio, fim)
                self.root.children.append(newNode)
                print('caso1')
            elif casParcial == string:
                # String já está na Trie
                print('caso2')
                pass
            elif match == len(casParcial):
                # String casa totalmente com o nó atual
                print('caso3')
                newNode = Node(inicio+match, fim)
                nodeAtual.children.append(newNode)
            else:
                # String casa parcialmente com o node atual
                #Divide o nó atual
                newNodeParent = Node(nodeAtual.inicio, nodeAtual.inicio+match)
                nodeAtual.parent = grandNode
                grandNode.children.remove(nodeAtual)
                newNodeParent.parent = nodeAtual.parent

                #Filho2: label que sobrou do pai
                newNodeSon = Node(nodeAtual.inicio+match+1,nodeAtual.fim)
                newNodeSon.children = nodeAtual.children
                newNodeSon.parent = newNodeParent

                #Filho1: novo (fim de palavra)
                newNode = Node()
                newNode.parent = newNodeParent
                newNodeParent.children.append(newNode)

                #Arruma o parent do newNodeParent
                grandNode.children.append(newNodeParent)
                print('caso4')
                pass

    def find(self, a, b):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie
        Retorna None se a substring não for encontrada 
        """
        if self.isEmpty():
            return None
        string = self.texto[a:b+1]
        nodeAtual,casParcial = TrieSearcher(self.texto, self, a, b).findNode()
        if casParcial == string:
            return nodeAtual
        else: 
            return None
        


class Trie:
    def __init__(self):
        self.texto = 'she_sells_sea_shells_by_the_sea'
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

if __name__ == "__main__":
    trie = CompactTrie('she_sells_sea_shells_by_the_sea')
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

    trie.root.children.append(n8)
    trie.root.children.append(n9)
    trie.root.children.append(n7)
    # trie = CompactTrie('she_sells_sea_shells_by_the_sea')
    trie.find(4,5)
