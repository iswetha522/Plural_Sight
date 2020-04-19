# SET ALGEBRA
# Union 
# difference 
# intersection 
# subset 
# superset 
# disjoint 

blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia',}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua',}
smell_hcn = {'Harry', 'Amelia',}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Oivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# Union
print(blue_eyes.union(blond_hair))
# {'Lily', 'Jack', 'Olivia', 'Harry', 'Amelia', 'Joshua', 'Mia'}
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
# True

# Intersection
print(blue_eyes.intersection(blond_hair))
# {'Jack', 'Amelia', 'Harry'}
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))
# True

#Difference
print(blond_hair.difference(blue_eyes))
# {'Joshua', 'Mia'}
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))
# False

# Symmetric difference
print(blond_hair.symmetric_difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

# issubset
print(smell_hcn.issubset(blond_hair))

# issuperset
print(taste_ptc.issuperset(smell_hcn))

# isdisjoint
print(a_blood.isdisjoint(o_blood))