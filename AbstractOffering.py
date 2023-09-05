from abc import ABC, abstractmethod

class AbstractOffering(ABC):
    def __init__(self, id, type, name, customer_name, price, date):
        self._id = id
        self._type = type
        self._name = name
        self._customer_name = customer_name
        self._price = price
        self._date = date
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_name(self):
        return self._name
    
    def get_customer_name(self):
        return self._customer_name
    
    def get_price(self):
        return self._price
    
    def get_date(self):
        return self._date
    
    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass