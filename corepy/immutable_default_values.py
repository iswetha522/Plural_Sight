# Always use immutable objects for default values.
def add_spam(menu = None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


breakfast = ["bacon", "eggs"]
print(add_spam(breakfast))
print(add_spam())
print(add_spam())