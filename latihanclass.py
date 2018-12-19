class Flight:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError("Harus ada kode maskapai pada {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Kode maskapai salah {}".format(number))
        if not (number[2:].isdigit() and int(number[2:])<=999):
            raise ValueError("Nomor rute penerbangan salah {}".format(number))
        self._number = number
        #self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number

    def aircraft_model(self):
        a = Aircraft("GA123","Airbus 111",22,6)
        return a.model()

class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model