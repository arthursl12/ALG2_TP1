from helper import checkPrefixSubstring

class TrieSearcher:
    """
    Procura a substring texto[a,b] na Trie
    Retorna:
        - O último nó que representa a substring na Trie (ou o nó que deve ser 
        dividido caso desejemos inseri-la)
        - A própria string (ou a porção da string casada, se não está na Trie)
        - Que palavra representa esse último nó (se a busca teve sucesso, 
        essa palavra é a própria string)
    """
    def __init__(self, texto, trie, a, b):
        self.texto = texto
        self.trie = trie

        self.string = self.texto[a:b+1]   #String de interesse
        self.casParent = ''               #Padrão já casado nos nós acima
        self.casNode = ''                 #Padrão casado com o nó atual (esperado)
        self.casParcial = ''              #Padrão casado com o nó atual (de fato)
        self.labelNode = ''               #Substring representada pelo node atual
        self.nodeAtual = self.trie.root   #Node inicial da busca (raiz)

        self.it = iter(self.nodeAtual.children)
        self.child = next(self.it, None)
        self.match = 0                    #Qtd de caracteres casados
    
    def findNode(self):
        """
        Inicia a busca pela string, procurando nos filhos da raiz, inicialmente,
        e avançando nesse filho caso haja um casamento.
        Faz os retornos descritos na docstring da classe
        """
        while self.child is not None:
            if (self.child.inicio == None and self.child.fim == None):
                self.__nodeFimPalavra()
            else:
                self.__searchChildren()
        
        if self.match == len(self.string) and self.casParcial == self.casNode:
            # Busca com sucesso
            return self.nodeAtual, self.string, self.casParcial
        elif self.match == 0:
            # Busca sem sucesso, exigindo nó totalmente novo na raiz
            return self.nodeAtual, self.casParcial, self.casParcial
        else:
            # Busca sem sucesso, exigindo divisão de nós para inserção
            return self.nodeAtual, self.casParcial, self.casParent
    
    def __nodeFimPalavra(self):
        """
        Chegamos num nó vazio que simboliza uma palavra que termina ali e 
        que está na Trie.
        Verificamos se esse nó vazio representa a string de interesse. Se sim
        podemos terminar a busca. Se não, seguimos para o próximo filho.
        """
        if (self.casParent == self.string):
            self.nodeAtual = self.child
            self.child = None
        else:
            self.child = next(self.it, None)

    def __searchChildren(self):
        """
        Faz uma busca pela string nos filhos do nó atual e desce um nível para
        algum filho, se o casamento for com sucesso
        """
        self.labelNode = self.texto[self.child.inicio:self.child.fim+1]
        self.casNode = self.casParent + self.labelNode
        self.match = checkPrefixSubstring(self.string, self.casNode)
        if self.__casamentoValido():
            self.nodeAtual = self.child
            self.it = iter(self.nodeAtual.children)
            self.child = next(self.it, None)
            self.casParent = self.casNode
            self.casParcial = self.string[0:self.match]

            if len(self.casParcial) < len(self.casNode):
                # O casamento não foi com o label do nó inteiro, a string não
                # está presente, podemos parar a busca. Nota: se quisermos 
                # inseri-la, temos que dividir o nó atual. 
                self.child = None
                self.casParcial = self.string[0:self.match]
                self.casParent = self.casNode
        else:
            self.child = next(self.it, None)

    def __casamentoValido(self):
        """
        Devem ser verdadeiros:
        (1) se a string desejada tem algum prefixo em comum com o 
        casamento dos nós acima juntamente com a label do nó atual
        (2) se realmente casamos um prefixo maior (senão apenas casamos o que
        já havíamos casado nos nós acima)
        """
        return self.match >= 1 and \
               self.match - len(self.casParent) >= 1


    

