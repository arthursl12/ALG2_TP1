import pytest
from main import arquivoString, criaArvoreSufixos
from trie import CompactTrie

NOME_ARQ = 'sarscov2.fasta'

# O texto a ser processado, i.e. o genoma do Sars-Cov-2 (Corona vírus), deverá
# ser carregado para memória principal em estrutura de dados compacta, representando
# um vetor de caracteres
class Test_arquivoString:
    @classmethod
    def setup_class(cls):
        cls.string = arquivoString(NOME_ARQ)

    def test_tipo_retorno(self):
        assert type(self.string) == str
    def test_sem_espacos(self):
        string = self.string
        for i in range(len(string)):
            assert string[i].isspace() == False, f"erro na posição {i}"
    def test_sem_cabecalho(self):
        string = self.string
        for i in range(len(string)):
            assert string[i].isupper() == True, f"erro na posição {i}"

class Test_criaArvoreSufixos:
    @classmethod
    def setup_class(cls):
        cls.string = arquivoString(NOME_ARQ)
        cls.trie = criaArvoreSufixos(cls.string)
    
    def test_tipo_retorno(self):
        assert type(self.trie) == CompactTrie
    def test_nao_vazia(self):
        assert self.trie.isEmpty() == False
    def test_presenca(self):
        assert self.trie.find(0,0) != None
        assert self.trie.find(0,len(self.string)-1) != None
    def test_presenca_todos(self):
        n = len(self.string)
        for i in range(n):
            assert self.trie.find(i,n-1) != None, f"Não encontrado {sufixo}"
    def test_maior_prefixo_repetido(self):
        raise("TODO")

