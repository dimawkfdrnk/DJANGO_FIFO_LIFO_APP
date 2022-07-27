import json


def writing_reading(data_base):
    if data_base == "open":
        with open('E:\Python\Учеба\home works\hw_20\data.json', 'r') as data:
            data_base = json.load(data)
            return data_base
    elif data_base == data_base:
        with open('E:\Python\Учеба\home works\hw_20\data.json', 'w') as data:
            json.dump(data_base, data, indent=2)


data_base = writing_reading("open")


class Stock:
    def __init__(self, strategy):
        self.strategy = strategy

    def donation(self, name, amount):

        presence_in_database = list(filter(lambda x: x.get("name") == name, data_base))
        if presence_in_database:
            presence_in_database[0].update(amount=presence_in_database[0].get("amount") + amount)

        elif self.strategy == "lifo":
            data_base.append({"name": name, "amount": amount})

        elif self.strategy == "fifo":
            data_base.insert(0, {"name": name, "amount": amount})

        writing_reading(data_base)

    def gift(self):
        if data_base == []:
            answer = "Склад пуст, зайдите позже"

        elif data_base[-1].get("amount") == 1:
            answer = f'Вот вам {data_base[-1].get("name")} 1 шт'
            data_base.pop()


        elif data_base[-1].get("amount") > 1:
            answer = f'Вот вам {data_base[-1].get("name")} 1 шт'
            data_base[-1].update(amount=data_base[-1].get("amount") - 1)

        writing_reading(data_base)
        return answer
