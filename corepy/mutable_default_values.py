def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ["bacon", "eggs",]
print(add_spam(breakfast))

lunch = ["baked beans"]
print(add_spam(lunch))

print(add_spam())
print(add_spam())
print(add_spam())