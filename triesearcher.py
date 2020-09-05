class TrieSearcher:
    def __init__(self, texto, trie, a, b):
        self.texto = texto
        self.trie = trie

        self.string = self.texto[a:b+1]   #String de interesse
        self.casPrevio = ''               #Padrão já casado nos nós acima
        self.labelNode = ''               #Substring representada pelo node atual
        self.casParcial = ''              #Casamento com o label do nó atual
        self.nodeAtual = self.trie.root

        self.it = iter(self.nodeAtual.children)
        self.child = next(self.it, None)
        self.match = 0

    def __checkPrefixSubstring(self, string, sub):
        """
        Retorna o tamanho do maior prefixo de string que é prefixo de sub
        """
        n = min([len(string),len(sub)])
        if n == 0: 
            # Alguma string vazia
            return 0
        for i in range(n):
            if string[i] != sub[i]:
                return i
        return n

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

    def findNode(self):
        """
        Procura a substring texto[a,b] na Trie
        Retorna último nó que representa a substring na Trie (ou o nó que deve
        ser dividido caso desejemos inseri-la) e também a própria string 
        (ou a porção da substring casada, se não está na Trie)
        """
        while self.child is not None:
            if (self.child.inicio == None and self.child.fim == None):
                # Chegamos num nó "vazio", indicando uma palavra inserida que 
                # termina ali
                if (self.casPrevio == self.string):
                    self.nodeAtual = self.child
                    self.child = None
                else:
                    self.child = next(self.it, None)
            else:
                labelNode = self.texto[self.child.inicio:self.child.fim+1]
                self.casParcial = self.casPrevio + labelNode
                self.match = self.__checkPrefixSubstring(self.string, self.casParcial)
                if self.__casamentoValido(self.match, self.casPrevio):
                    self.nodeAtual = self.child
                    self.it = iter(self.nodeAtual.children)
                    self.child = next(self.it, None)
                    self.casPrevio = self.string[0:self.match]
                    if self.match < len(self.casParcial):
                        return self.nodeAtual, self.casPrevio
                else:
                    self.casParcial = self.casPrevio
                    self.child = next(self.it, None)
        
        if self.match == len(self.string):
            return self.nodeAtual,self.string
        else:
            return self.nodeAtual,self.casParcial
