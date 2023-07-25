import datetime

from typing import Dict


class Operation(object):
    def __init__(self, date: Dict, description: str, sender: str,  recipient: str, amount: str):
        self.date = datetime.datetime(date["year"], date["month"], date["day"])
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self) -> str:
        str_date = self.date.strftime('%d.%m.%Y')
        information = [f"{str_date} {self.description}",
                       f"{self.sender} -> {self.recipient}",
                       f"{self.amount}"]

        return "\n".join(information)
