
from api import API


class SPService:
    """
    Conecta com o webservice do Detran-SP.
    """

    def __init__(self, **kwargs):
        """
        Construtor.
        """

        self.params = kwargs

    def get_json_response(self, method):

        license_plate_conv = self.get_conv_plate()
        api = API(license_plate_conv, self.params["renavam"], method)
        return api.fetch()
    
    def get_conv_plate(self):
        mercosul_letters = 'ABCDEFGHIJ'
        gray_plate = self.params["license_plate"]
        char = gray_plate[4]
        if str(char) in mercosul_letters:
            conv_char = self.get_conv_char(char)
            conv_plate = str(gray_plate[0:4]) + conv_char + str(gray_plate[5:7]) 
            return conv_plate
        else:
            return gray_plate

    def get_conv_char(self, char):

        return {
        'A':'0',       
        'B':'1',    
        'C':'2',    
        'D':'3',    
        'E':'4',    
        'F':'5',    
        'G':'6',    
        'H':'7',    
        'I':'8',    
        'J':'9',    
    }[char]
    
    def debt_search(self):

        if self.params['debt_option'] == 'consult':
            response_json_tickets = self.get_json_response("ConsultaMultas")
            response_json_ipva = self.get_json_response("ConsultaIPVA")
            response_json_dpvat = self.get_json_response("ConsultaDPVAT")
            response_json_licensing = self.get_json_response("ConsultaLicenciamento")
            
        else:
            raise Exception("opcao invalida")

        debts = {
            'IPVAs': response_json_ipva.get('IPVAs') or {},
            'DPVATs': response_json_dpvat.get('DPVATs') or {},
            'Multas': response_json_tickets.get('Multas') or {},
            'Licenciamento': response_json_licensing or {},
        }

        for debt in debts:
            if debts[debt] == {}:
                debts[debt] = None

        return debts