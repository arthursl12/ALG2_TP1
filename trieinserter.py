from node import Node
from helper import checkPrefixSubstring

class TrieInserter:
    """
    
    """
    def __init__(self, texto, trie, nodeAtual, casParcial, casNode, string):
        self.texto = texto
        self.trie = trie
        self.string = string

        self.match = checkPrefixSubstring(casParcial,string)
        self.nodeAtual = nodeAtual
        self.casParcial = casParcial
        self.casNode = casNode

        

    def __divideNode(self, newNode):
        """
        Divide o nodeAtual, sendo que a parte dele que não casa com a palavra
        nova a ser inserida virará um filho (que herdará todos os filhos do 
        nó original). O outro filho desse nó divisor é o nó 'newNode' que 
        representa a palavra nova (ou a parte dela que não casou) 
        """
        labelNode = self.texto[self.nodeAtual.inicio : self.nodeAtual.fim+1]
        # Match normalizado = qtd de caracteres casada apenas com o nó atual,
        #sem considerar os nós acima
        matchNormalizado = self.match - (len(self.casNode) - len(labelNode))
        newNodeParent = Node(self.nodeAtual.inicio, 
                             self.nodeAtual.inicio + matchNormalizado - 1)
        newNodeParent.parent = self.nodeAtual.parent
        newNodeParent.addChild(newNode)

        grandNode = self.nodeAtual.parent
        grandNode.children.remove(self.nodeAtual)
        grandNode.addChild(newNodeParent)

        #Filho: label que sobrou do pai
        newNodeSon = Node(self.nodeAtual.inicio + matchNormalizado,
                          self.nodeAtual.fim)
        newNodeSon.children = self.nodeAtual.children
        newNodeParent.addChild(newNodeSon)

    def insertNode(self, inicio, fim):
        """
        Insere a string [inicio:fim+1] na trie
        """
        if self.casParcial == '':
            # String não casa parcialmente com nada na Trie
            newNode = Node(inicio, fim)
            self.trie.root.addChild(newNode)
            return 

        if self.__jaPresenteTrie():
            pass
        elif self.__nodePrefix():
            #Filho1: marcador de fim de palavra (palavra que já estava no nó)
            newNodeSon = Node()
            self.nodeAtual.addChild(newNodeSon)

            #Filho2: palavra nova que engloba uma que já existe na Trie
            newNode = Node(inicio+self.match, fim)
            self.nodeAtual.addChild(newNode)
        elif self.__stringPrefix():
            #Filho1: novo (fim de palavra)
            newNode = Node()
            self.__divideNode(newNode)
        else:
            # String casa parcialmente com o node atual
            #Filho1: novo nó
            newNode = Node(inicio+self.match, fim)
            self.__divideNode(newNode)

    def __jaPresenteTrie(self):
        """
        String já está na trie, nada precisamos fazer
        """
        return self.casParcial == self.string and \
               self.casNode == self.string
    
    def __stringPrefix(self):
        """
        A string inteira é prefixo do nó
        (String representada pelo nó é maior que a string desejada,
        temos que quebrar o nó e adicionar um vazio como filho)
        Ex.: nó 'GEEKSFORGEEKS', adicionar 'GEEKS'
        """
        return self.casParcial == self.string and \
               self.casNode != self.string
    
    def __nodePrefix(self):
        """
        O nó inteiro é prefixo da string
        Ex.: nó 'she', adicionar 'shells'
        """
        return self.casParcial == self.casNode and \
               self.casNode != self.string

    