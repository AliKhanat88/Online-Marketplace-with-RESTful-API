
class Seller:
    def __init__(self):
        self._offerings = []
        self._next_id = 0
    
    def add(self, offering):
        offering.set_id(self._next_id)
        self._offerings.append(offering)
        self._next_id += 1
        return self._next_id -1

    
    def get(self, id):
        for offering in self._offerings:
            if offering.get_id() == id:
                return offering
        return None
    
    def get_all(self):
        return self._offerings
    
    def get_all_by_type(self, type):
        return [offering for offering in self._offerings if offering.get_type() == type]
    
    def update(self, offering):
        for i in range(len(self._offerings)):
            if self._offerings[i].get_id() == offering.get_id():
                self._offerings[i] = offering
                return
        raise Exception("Offering with ID {} does not exist".format(offering.get_id()))
    
    def delete(self, id):
        for offering in self._offerings:
            if offering.get_id() == id:
                self._offerings.remove(offering)
                return
        raise Exception("Offering with ID {} does not exist".format(id))