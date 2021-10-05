from unittest.mock import patch,MagicMock, Mock
from service import SPService
import api
from parser import SPParser
import unittest

# Sinta-se livre para deletar o teste abaixo, caso queira.
class Teste(unittest.TestCase):

    @patch('service.SPService.get_json_response', MagicMock(return_value={}))
    def test_search_debt_when_there_is_no_debt(mocker):
        service = SPService(
            license_plate="license_plate",
            renavam="renavam",
            debt_option="consult"
        )
        result = service.debt_search()
        assert result == {'DPVATs': None, 'IPVAs': None, 'Licenciamento': None, 'Multas': None}
    
    @patch('service.SPService.get_conv_plate', MagicMock(return_value='TES9385'))
    def test_get_conv_plate(mocker):
        service = SPService(
            license_plate= SPService.get_conv_plate(),
            renavam="renavam",
            debt_option="consult"
        )
        result = service.get_conv_plate()
        assert result == 'TES9385'

    @patch('service.SPService.get_conv_plate', MagicMock(return_value='ABC1234'))
    def test_get_json_response(mocker):
        service = SPService(
            license_plate= SPService.get_conv_plate(),
            renavam="11111111111",
            debt_option="consult"
        )
        result = service.get_json_response("ConsultaLicenciamento")
        assert result == {'Servico': 'Licenciamento', 'Veiculo': {'UF': 'SP', 'Placa': 'ABC1234', 'CPFCNPJ': '000.000.000-00', 'Renavam': '11111111111', 'Proprietario': 'JOHN'}, 'Exercicio': 2021, 'TaxaLicenciamento': 9891}
