class Smartphone:
    def __init__(self, brand, model, phone_number):
        
        if not phone_number.startswith("+79"):
            raise ValueError("Некорректный номер телефона. Номер должен начинаться с +79...")

        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"Телефон: {self.brand} {self.model}, Номер: {self.phone_number}"