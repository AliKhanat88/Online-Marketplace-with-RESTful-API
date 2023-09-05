from AbstractOffering import AbstractOffering

class Product(AbstractOffering):
    def __init__(self, id, type, name, customer_name, price, date, unit_price, quantity):
        super().__init__(id, type, name, customer_name, price, date)
        self._unit_price = unit_price
        self._quantity = quantity
    
    def get_type(self):
        return "Product"
    
    def get_details(self):
        return f"Product: {self.get_name()}, Price: {self.get_price()}, Unit Price: {self._unit_price}, Quantity: {self._quantity}, "
    
    def get_unit_price(self):
        return self._unit_price
    
    def get_quantity(self):
        return self._quantity
    
    def to_dict(self):
        return {
            "id": self._id,
            "type": self._type,
            "name": self._name,
            "customer_name": self._customer_name,
            "price": self._price,
            "date": self._date.__str__(),
            "unit_price": self._unit_price,
            "quantity": self._quantity
        }