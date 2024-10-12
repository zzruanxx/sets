frutas = {"maça", "banana", "laranja", "maça"}

print(frutas)

frutas.add("uva")
print(frutas)

frutas.remove("banana")
print(frutas)

if "laranja" in frutas:
    print("Laranja esta no set!")
    
outros_frutas = {"melancia", "pessego", "uva"}
todas_frutas = frutas.union(outros_frutas)
print(todas_frutas)

