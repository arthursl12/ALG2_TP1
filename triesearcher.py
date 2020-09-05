from helper import checkPrefixSubstring

class TrieSearcher:
    """
    Procura a substring texto[a,b] na Trie
    Retorna último nó que representa a substring na Trie (ou o nó que deve
    ser dividido caso desejemos inseri-la) e também a própria string 
    (ou a porção da substring casada, se não está na Trie)
    """
    def __init__(self, texto, trie, a, b):
        self.texto = texto
        self.trie = trie

        self.string = self.texto[a:b+1]   #String de interesse
        self.casPrevio = ''               #Padrão já casado nos nós acima
        self.labelNode = ''               #Substring representada pelo node atual
        self.casParcial = ''              #Casamento com o label do nó atual
        self.nodeAtual = self.trie.root   #Node inicial da busca

        self.it = iter(self.nodeAtual.children)
        self.child = next(self.it, None)
        self.match = 0                    #Qtd de caracteres casados

    def __casamentoValido(self):
        """
        Devem ser verdadeiros:
        (1) se a string desejada tem algum prefixo em comum com o 
        casamento dos nós acima juntamente com a label do nó atual
        (2) se realmente casamos um prefixo maior (senão apenas casamos o que
        já havíamos casado)
        """
        return self.match >= 1 and \
               self.match - len(self.casPrevio) >= 1

    def __nodeFimPalavra(self):
        """
        Chegamos num nó vazio que simboliza uma palavra que termina ali e 
        que está na Trie.
        Verificamos se esse nó vazio representa a string de interesse. Se sim
        podemos terminar a busca. Se não, seguimos para o próximo filho.
        """
        if (self.casPrevio == self.string):
            self.nodeAtual = self.child
            self.child = None
        else:
            self.child = next(self.it, None)
    
    def __searchChildren(self):
        """
        Faz uma busca pela string nos filhos do nó atual e desce um nível para
        algum filho, se o casamento for com sucesso
        """
        labelNode = self.texto[self.child.inicio:self.child.fim+1]
        self.casParcial = self.casPrevio + labelNode
        self.match = checkPrefixSubstring(self.string, self.casParcial)
        if self.__casamentoValido():
            self.nodeAtual = self.child
            self.it = iter(self.nodeAtual.children)
            self.child = next(self.it, None)
            self.casPrevio = self.string[0:self.match]
            if self.match < len(self.casParcial):
                # O casamento não foi com o label do nó inteiro, a string não
                # está presente, podemos parar a busca. Nota: se quisermos 
                # inseri-la, temos que dividir o nó atual. 
                self.child = None
        else:
            self.casParcial = self.casPrevio
            self.child = next(self.it, None)
    
    def findNode(self):
        """
        Faz a procura em si, criando os retornos
        """
        while self.child is not None:
            if (self.child.inicio == None and self.child.fim == None):
                self.__nodeFimPalavra()
            else:
                self.__searchChildren()
        
        if self.match == len(self.string):
            return self.nodeAtual,self.string
        else:
            return self.nodeAtual,self.casParcial
