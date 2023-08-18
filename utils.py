import json
import os
from operator import itemgetter
from class_operation import Operation

DATA_PATH = os.path.join("operations.json")
def last_operations(DATA_PATH):
    """Создаём словарь операций из json-файла и создаём словарь без пустых элементов"""
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        operations = json.load(f)

    list_nonempty = []
    for i in operations:
        if i:
            list_nonempty .append(i)
    return list_nonempty

def correct_operations(opertions):
    """Создаём список из 5 последних выполненных клиентом операций"""
    correct_list = []
    for operation in opertions:
        if operation['state'] == 'EXECUTED':
            correct_list.append(operation)

    list_reverse = sorted(correct_list, key=itemgetter("date"), reverse=True)
    return list_reverse[:5]




def list_class(correct_list):
    """Создаём массив экземпляров класса"""
    last_operations = []
    for operation in correct_list:
        if 'from' in operation.keys():
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['code']
            operation_from = operation['from']
            last_operations.append(Operation(date, description, operation_to, amount, currency, operation_from))
        else:
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['code']
            last_operations.append(Operation(date, description, operation_to, amount, currency))
    return last_operations


