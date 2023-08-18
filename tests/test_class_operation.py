import class_operation


def test_repr():
    assert type(
        class_operation.Operation('date', 'description', 'to_op', 'amount', 'currency')) is class_operation.Operation


def test_change_date():
    check_class = class_operation.Operation("2018-12-22T02:02:49.564873", "Перевод с карты на карту",
                                          "Visa Gold 8326537236216459", "56516.63", "USD",
                                          "MasterCard 6783917276771847")
    assert check_class.change_date() == "22.12.2018"


def test_hide_number_sender():
    check_class = class_operation.Operation("2018-12-22T02:02:49.564873", "Перевод с карты на карту",
                                          "Visa Gold 8326537236216459", "56516.63", "USD",
                                          "MasterCard 6783917276771847")
    assert check_class.hide_number_sender() == "MasterCard 6783 91** **** 1847"

def test_hide_number_recipient():
    fix_class = class_operation.Operation("2019-11-19T09:22:25.899614", "Перевод организации",
                                          "Счет 43241152692663622869", "30153.72", "RUB",
                                          "Maestro 7810846596785568")
    assert fix_class.hide_number_recipient() == 'Счет **2869'