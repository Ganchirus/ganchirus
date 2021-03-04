one_var = 1000
two_var = 1000
magic_var = 999
print("one_var =", one_var, ", address is", id(one_var))
print("two_var =", two_var, ", address is", id(two_var))
print("magic_var =", magic_var, ", address is", id(magic_var))
print(one_var, "=", two_var, "is", (id(one_var) == id(two_var)))
print(one_var, "=", magic_var, "is", (id(one_var) == id(magic_var)))