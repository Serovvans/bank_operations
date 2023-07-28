import datetime


class Operation(object):
    """
    Класс операции. Содержит необходимые для отображения и фильтрации данные и методы доступа к ним
    """
    def __init__(self, idx: int, date: str, description: str, sender: str,
                 recipient: str, amount: dict, state: str):
        self.id = idx
        self.__sender = sender
        self.__recipient = recipient

        self.date = date
        self.amount = amount

        self.description = description
        self.state = state

    def get_date(self) -> datetime.datetime:
        """
        Переводит строковую дату в объект datetime
        :return: объект datetime с датой и временем операции
        """
        items = list(self.date.split("-"))
        year = items[0]
        month = items[1]
        day, time = items[2].split("T")

        time = list(time.split(":"))

        return datetime.datetime(int(year), int(month), int(day),
                                 int(time[0]), int(time[1]), int(float(time[2])))

    def get_amount(self) -> str:
        """
        Представляет сумму операции и валюту в виде строки для отображения
        :return: Строковое представление суммы операции
        """
        return f"{self.amount['amount']} {self.amount['currency']['name']}"

    def get_sender(self) -> str:
        """
        Возвращает информацию об отправителе в виде строки с замаскированными реквизитами
        :return: замаскированные реквизиты отправителя
        """
        if not self.__sender:
            return ""
        if self.__sender.split()[0] == "Счет":
            return self.bank_account_to_string(self.__sender)
        else:
            return self.card_number_to_string(self.__sender)

    def get_recipient(self) -> str:
        """
        Возвращает информацию об получателе в виде строки с замаскированными реквизитами
        :return: замаскированные реквизиты получателя
        """
        if self.__recipient.split()[0] == "Счет":
            return self.bank_account_to_string(self.__recipient)
        else:
            return self.card_number_to_string(self.__recipient)

    @staticmethod
    def card_number_to_string(sender: str) -> str:
        """
        Переводит номер карты в шаблонное строковое представление
        :param sender: номер карты
        :return: Строковое представление номера карты по шаблону XXXX XX** **** XXXX
        """
        if not sender:
            return ""

        sender = list(sender.split())
        card_name = " ".join(sender[:-1])
        card_number = sender[-1]
        return f"{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    @staticmethod
    def bank_account_to_string(bank_account: str) -> str:
        """
        Переводит номер счета в шаблонное строковое представление
        :param bank_account: номер счета
        :return: Номер счета в формате **XXXX
        """
        if not bank_account:
            return ""

        bank_account = list(bank_account.split())[-1]
        return f"Счет **{bank_account[-4:]}"

    def __str__(self) -> str:
        str_date = self.get_date().strftime('%d.%m.%Y')
        information = [f"{str_date} {self.description}",
                       f"{self.get_sender()} -> {self.get_recipient()}",
                       f"{self.get_amount()}"]

        return "\n".join(information)

    def __eq__(self, other) -> bool:
        return self.id == other.id
