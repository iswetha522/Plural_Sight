"""Model for aircraft flights."""
"""Instance methods are called on objects or instances of our class."""
"""Instance methods must accept a reference to the actual
instance on which the method was called as the first argument.
By convention, this argument is always called "self"."""

"""Why _number?"""
"""Avoids name clash with number() function."""
"""By convention, implementation details start with underscore."""
    
"""__init__"""
"""Instance method for initializing new objects."""
"""It is an initializer not a constructor."""
"""'self' is simialr to 'this' in Java, C# or C++."""

# Class Invariants:
# Truths about an object that endure for its lifetime.
from pprint import pprint as pp 
class Flight:
    """A flight with a particular passenger aircraft."""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not number[2:].isdigit():
            raise ValueError(f"Invalid route number '{number}'")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter : None for letter in seats} for _ in rows]

    
    def aircraft_model(self):
        return self._aircraft.model()
    
    def number(self):
        return self._number

    
    def airline(self):
        return self._number[:2]

    
    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
        
        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger : The passenger name.

        Raises:
            ValueError : If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger


    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid seat number {row}")
        
        return row, letter
    
    
    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.
        
        Args:
            from_seat : The existing seat designator for the
                        passenger to be moved.
            
            to_seat : The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passengers to relocate in seat {from_seat}")
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return self._registration
    

    def model(self):
        return self._model


    def seating_plan(self):
        return(range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def make_flight():
    # f = Flight("BA758", Aircraft=("G-Eupt", "Airbus A319", num_rows=22, num_seats_per_row = 6))
    # f.allocate_seat("12A", "Guido van Rossum")
    pass
    
# f = Flight("SN060")
# print(f.number())
# print(Flight.number(f))

# a = Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row = 6)
# print(a.registration()) # G-EUPT
# print(a.model()) # Airbus A319
# print(a.seating_plan()) # (range(1, 23), 'ABCDEF')

# f = Flight("BA758", Aircraft("G-EUPT", 'Airbus A319',
#             num_rows = 22, num_seats_per_row = 6))
# # print(f.aircraft_model()) # Airbus A319
# # print(f._seating)
# f.allocate_seat("12A", 'Guido Van Rossum')
# f.allocate_seat("22A", 'Guido Van Rossum')
# # f.allocate_seat("12A", 'Rasmus Rossum') # ValueError: Seat 12A already occupied
# # f.allocate_seat("E27", 'Yukihiro Matsumoto') # ValueError: Invalid seat letter 7
# f.allocate_seat("DD", 'swetha') # ValueError: Invalid seat row D
# pp(f._seating)
