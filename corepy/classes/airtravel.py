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


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    
    def _passenger_seats(self):
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

# Removed after using polymorphism:
# class Aircraft:
#     def __init__(self, registration, model, num_rows, num_seats_per_row):
#         self._registration = registration
#         self._model = model
#         self._num_rows = num_rows
#         self._num_seats_per_row = num_seats_per_row


#     def registration(self):
#         return self._registration
    

#     def model(self):
#         return self._model


#     def seating_plan(self):
#         return(range(1, self._num_rows + 1),
#                 "ABCDEFGHJK"[:self._num_seats_per_row])


# Using Inheritance:
class Aircraft:
    
    # pylint: disable=no-member
    # pylint: disable=E1101
    def __init__(self,registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

# "Using Polymorphism"
# Using objects of different types through a uniform interface.
# It applies to both functions as well as more complex types.
class AirbusA319(Aircraft):
    
    def model(self):
        return "Airbus A319"


    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    
    def model(self):
        return "Boeing 777"


    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}" \
             f" Flight: {flight_number}" \
             f" Seat : {seat}" \
             f" Aircraft: {aircraft}" \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA758", AirbusA319("G-Eupt"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders, Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D","Rich Hickey")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("55K", "LArry Wall")
    g.allocate_seat("33G", "Yukihiro Matsumoto")
    g.allocate_seat("4B", "Brain Kernighan")
    g.allocate_seat("4A", "Dennis Ritchie")

    return f, g
    
    
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
f, g = make_flights()
# pp(f._seating)
# f.relocate_passenger("12A", "15D")
# pp(f._seating)
# print(f.num_available_seats())
# print(f.make_boarding_cards(console_card_printer))
print(f.aircraft_model())
print(g.aircraft_model())
print(f.num_available_seats)
print(g.num_available_seats)
g.relocate_passenger("55K", "13G")
g.make_boarding_cards(console_card_printer)

a = AirbusA319("G-EZBT")
print(a.num_seats())

b = Boeing777("N717AN")
print(b.num_seats())