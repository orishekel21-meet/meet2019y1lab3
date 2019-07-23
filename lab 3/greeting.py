computer=input("whats is your name?")
print(" Hello there "+computer.capitalize())
ok="Your name is "
kj=" letters long!"
print(ok+str(len(computer))+kj)
ap="The first letter of your name is "
qw=" and the last letter is "
let1=computer[:1]
let2=computer[-1]
print(ap+str(let1)+qw+str(let2))
print("missing letters: "+str(computer[1:-1]))
