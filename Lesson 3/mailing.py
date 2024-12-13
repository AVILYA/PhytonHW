from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        if not isinstance(to_address, Address) or not isinstance(from_address, Address):
            raise TypeError("to_address and from_address must be Address objects")
        if not isinstance(cost, (int, float)):
            raise TypeError("cost must be a number")
        if not isinstance(track, str):
            raise TypeError("track must be a string")

        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправитель: {self.from_address}\n"
                f"Получатель: {self.to_address}\n"
                f"Стоимость: {self.cost}\n"
                f"Трек-номер: {self.track}")