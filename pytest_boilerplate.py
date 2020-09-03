import pytest

class TestClass01:
    def test_case01(self):
        assert 'python'.upper() == 'PYTHON'
    def test_case02(self):
        assert 'PYTHON'.lower() == 'python'

class TestClass02:
    @classmethod
    def setup_class(cls):
        print ("\nIn setup_class()...") 

    @classmethod
    def teardown_class(cls):
        print ("\nIn teardown_class()...")  

    def setup_method(self, method):
        print ("\nIn setup_method()...")

    def teardown_method(self, method):
        print ("\nIn teardown_method()...")

    def test_case03(self):
        print("\nIn test_case03()...")  

    def test_case04(self):
        print("\nIn test_case04()...")

@pytest.fixture() 
def fixture01(request):
    print("\nIn fixture...")

    def fin():
        print("\nFinalized...")
    request.addfinalizer(fin)

@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")