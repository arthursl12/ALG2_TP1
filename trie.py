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
        else:
            string = self.texto[inicio:fim+1]
            lastNode, casParcial = self.findNode(inicio, fim)
            if casParcial == '':
                # String não casa parcialmente com nada na Trie
                newNode = Node(inicio, fim)
                self.root.children.append(newNode)
            
            raise("TODO")

    def __casamentoValido(self, match, casPrevio):
        """
        Devem ser verdadeiros:
        (1) se a string desejada tem algum prefixo em comum com o 
        casamento dos nós acima juntamente com a label do nó atual
        (2) se realmente casamos um prefixo maior (senão apenas casamos o que
        já havíamos casado)
        """
        return match >= 1 and \
               match - len(casPrevio) >= 1


    def findNode(self, a, b):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie (ou o nó que deve
        ser dividido caso desejemos inseri-la) e também a própria string 
        (ou a porção da substring casada, se não está na Trie)
        """
        nodeAtual = self.root
        string = self.texto[a:b+1]      #String de interesse
        casPrevio = ''                  #Padrão já casado nos nós acima
        labelNode = ''                  #Substring representada pelo node atual
        casParcial = ''                 #Casamento com o label do nó atual (checar)
        it = iter(nodeAtual.children)
        child = next(it, None)
        match = 0
        while child is not None:
            if (child.inicio == None and child.fim == None):
                # Chegamos num nó "vazio", indicando uma palavra inserida que 
                # termina ali
                if (casPrevio == string):
                    nodeAtual = child
                    break
                else:
                    child = next(it, None)
                    continue
            labelNode = self.texto[child.inicio:child.fim+1]
            casParcial = casPrevio + labelNode
            match = checkPrefixSubstring(string, casParcial)
            if self.__casamentoValido(match, casPrevio):
                nodeAtual = child
                it = iter(nodeAtual.children)
                child = next(it, None)
                casPrevio = string[0:match]
                if match < len(casParcial):
                    return nodeAtual, casPrevio
                continue
            casParcial = casPrevio
            child = next(it, None)
        if match == len(string):
            return nodeAtual,string
        else:
            return nodeAtual,casParcial

    def find(self, a, b):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie
        Retorna None se a substring não for encontrada 
        """
        if self.isEmpty():
            return None
        string = self.texto[a:b+1]
        nodeAtual,casParcial = self.findNode(a, b)
        if casParcial == string:
            return nodeAtual
        else: 
            return None
        


class Node:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        self.children = []

    def setInicio(self, novoInicio):
        if novoInicio > self.fim:
            raise Exception
        self.inicio = novoInicio

    def setFim(self, novoFim):
        if novoFim < self.inicio:
            raise Exception
        self.fim = novoFim
    
    def __eq__(self, other):
        if isinstance(other, Node):
            if (self.inicio == other.inicio and \
                self.fim == other.fim):
                return True
        return False

# Retorna o tamanho do maior prefixo de string que é prefixo de sub
def checkPrefixSubstring(string, sub):
    n = min([len(string),len(sub)])

    # Alguma string vazia
    if n == 0: 
        return 0
    for i in range(n):
        if string[i] != sub[i]:
            return i

    return n

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
    trie = Trie()
    trie.trie.findNode(0,1)