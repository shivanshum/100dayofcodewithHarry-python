# strings are immutable
a = "SHIVA!"
print(len(a))
print(a.lower())
b = "AmksAcScmLcKk"
c = "Hakuna Matata"
print(b.upper())
print(len(b))
print(a.rstrip("!"))
print(b.replace("A","S"))
print(c.split(" "))
d= "sHIVA"
print(d.capitalize())
print(c.center(69))
print(b.count("k"))
print(a.endswith("!"))
# 
print(b.find("Sc")) #gives the index of the given value
# print(b.index("v"))  gives the error when value is not found.
print(c.isalnum())
print(b.isalnum())
print(b.isalpha())
print(c.islower())
print(c.isprintable())
e = "  "
print(e.isspace())
print(c.istitle())
print(c.isupper())
print(c.startswith("H"))
print(b.swapcase())
s = "hello i am the shiva"
print(s.title())