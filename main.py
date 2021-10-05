import sys
import json
from service import SPService
from parser import SPParser

if __name__ == "__main__":

    try:
        debt_option = sys.argv[1]
        license_plate = sys.argv[2]
        renavam = sys.argv[3]
        assert len(sys.argv) == 4
    except (AssertionError, IndexError):
        print("Argumentos inválidos")
        sys.exit(1)

    service = SPService(
        license_plate=license_plate,
        renavam=renavam,
        debt_option=debt_option
    )
    try:
        search_result = service.debt_search()
    except Exception as exc:
        print(exc)
        sys.exit(1)

    parser = SPParser(search_result)

    if debt_option == "consult":
        result = parser.collect_ticket_debts()
        result1 = parser.collect_ipva_debts()
        result2 = parser.collect_insurance_debts()
        result3 = parser.collect_licensing_debts()
    else:
        print("Opção inválida")
        sys.exit(1)

    print(
        json.dumps(result, indent=4, ensure_ascii=False)
        + json.dumps(result1, indent=4, ensure_ascii=False)
        + json.dumps(result2, indent=4, ensure_ascii=False)
        + json.dumps(result3, indent=4, ensure_ascii=False)
    )
    sys.exit(0)