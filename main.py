import utils
from utils import DATA_PATH


operations = utils.last_operations(DATA_PATH)

# Пять последних операций
five_last_operations = utils.correct_operations(operations)

# Экземпляры класса
Instances_of_classes = utils.list_class(five_last_operations)

# Вывод операций
for operation in Instances_of_classes:
    print(f'{operation.change_date()} {operation.description}\n'
          f'{operation.hide_number_sender()} -> {operation.hide_number_recipient()}\n'
          f'{operation.amount} {operation.currency}\n'
          f'')



