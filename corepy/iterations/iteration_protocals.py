# Iterable:
# Can be passed to iter() to produce an iterator

# Iterator:
# Can be passed to next() to get the next value in the sequence.

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # raises StopIteration exception


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


print(first(['1st', '2nd', '3rd']))
print(first({'1st', '2nd', '3rd'}))
print(first(set()))