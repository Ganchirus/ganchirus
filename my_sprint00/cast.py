a = 3
b = 10
c = -14.8
d = True
print("Avalible variables:")
print("a = {}".format(a))
print("b = {}".format(b))
print("c = {}".format(c))
print(('d = {}'.format(d)), "\n")

print("a({}) + b({}) = {}".format(a, b, float(a+b)))
print("c({}) - b({}) = {}".format(c, b,int(c-b)))
print("c({}) + b({}) = {}".format(c, b, (str(c)+str(b))))
print("a({}) - a({}) = {}".format(a, a,bool(a-a)))
print("b({}) - d({}) = {}".format(b, d,(b-d)))