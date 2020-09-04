class CompactTrie:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return False

class Node:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
    def setInicio(self, novoInicio):
        if novoInicio > self.fim:
            raise Exception
        self.inicio = novoInicio
    def setFim(self, novoFim):
        if novoFim < self.inicio:
            raise Exception
        self.fim = novoFim