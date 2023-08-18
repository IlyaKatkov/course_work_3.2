from datetime import datetime



class Operation:
    def __init__(self, date, description, operation_to, amount, currency, operation_from=None):
        self.date = date
        self.description = description
        self.operation_to = operation_to
        self.amount = amount
        self.currency = currency
        self.operation_from = operation_from




    def __repr__(self):
        return f'Operation: дата перевода - {self.date}\n' \
               f'описание перевода - {self.description}\n' \
               f'откуда - {self.operation_from}\n' \
               f'куда - {self.operation_to}\n' \
               f'сумма перевода - {self.amount}\n' \
               f'валюта - {self.currency}\n'

    def change_date(self):
        """Преобразует дату в удобный вид"""
        old_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        new_date = old_date.strftime('%d.%m.%Y')
        return new_date

    def hide_number_sender(self):
        """Скрывает номер карты или счёта отправителя"""
        name = ""
        numbers = ""
        if self.operation_from is not None:
            for letter in self.operation_from:
                if letter.isdigit():
                    numbers += letter
                elif letter.isalpha():
                    name += letter

            if len(numbers) == 16:
                return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
            elif len(numbers) > 16:
                return f'{name} **{numbers[-4:]}'
        else:
            return ''

    def hide_number_recipient(self):
        """Прячет номер карты или счёта получателя"""
        name = ''
        numbers = ''
        for letter in self.operation_to:
            if letter.isdigit():
                numbers += letter
            elif letter.isalpha():
                name += letter

        if len(numbers) == 16:
            return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
        elif len(numbers) > 16:
            return f'{name} **{numbers[-4:]}'

