from AbstractOffering import AbstractOffering

class Service(AbstractOffering):
    def __init__(self, id, type, name, customer_name, price, date, duration_in_days, is_company):
        super().__init__(id, type, name, customer_name, price, date)
        self._duration_in_days = duration_in_days
        self._is_company = is_company
    
    def get_type(self):
        return "Service"
    
    def get_details(self):
        return f"Service: {self.get_name()}, Price: {self.get_price()}, Duration in days: {self._duration_in_days}, Is a campany? : {self._is_company}"
    
    def get_duration_in_days(self):
        return self._duration_in_days
    
    def get_is_company(self):
        return self._is_company
    
    def to_dict(self):
        return {
            "id": self._id,
            "type": self._type,
            "name": self._name,
            "customer_name": self._customer_name,
            "price": self._price,
            "date": self._date.__str__(),
            "duration_in_days": self._duration_in_days,
            "is_company": self._is_company
        }