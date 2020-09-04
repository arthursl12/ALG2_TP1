import pytest
from main import arquivoString

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


