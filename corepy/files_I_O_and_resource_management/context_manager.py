# files are context managers which close files on exit.
# Context managers aren't restricted to file-like objects.


"""Demonstrate raiding a refridgerator."""
#Use closing:

from contextlib import closing

# A class for raiding the fridge
class RefridgeratorRaider:
    """Raid a refridgerator"""

    # Open the refridgerator door
    def open(self):
        print("Open fridge door.")

    # Take some food
    def take(self, food):
        print(f"Finding {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print(f"Taking {food}")

    # Close the refridgerator
    def close(self):
        print("Close fridge door.")

# Raid for some food!   
def raid(food):
        # r = RefridgeratorRaider()
        with closing(RefridgeratorRaider()) as r: # By using this we get the closing of fridge door. when we call deep fried pizza
            r.open()
            r.take(food)
            # r.close() # Removed explicit call to close()


# print(raid('becon'))
# print(raid('deep fried pizza')) # Here we have a problem the fridge door is not closing so we rectify it
print(raid('spam')) # We get two times of close fridge door.