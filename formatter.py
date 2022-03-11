tokens = [x.strip() for x in open('tokens.txt', 'r', encoding="utf8").readlines()]
output = open("output.txt", "a+")
class funcs:
 def f1():
    for i in tokens:
        t = i.split(":")
        output.write(f"{t[1]}:{t[0]}:{t[2]}\n")

 def f2():
    for i in tokens:
        t = i.split(":")
        output.write(f"{t[1]}:{t[2]}:{t[0]}\n")

 def f3():
    for i in tokens:
        t = i.split(":")
        output.write(f"{t[1]}\n")
 def f4():
    for i in tokens:
        t = i.split(":")
        output.write(f"{t[0]}:{t[2]}:{t[1]}\n")
fr = funcs()
modes = {'1': fr.f1, '2': fr.f2, '3': fr.f3,'4':fr.f4}

print("""
YOU NEED TO HAVE EMAIL:TOKEN:PASS TOKENS TO USE THAT FORMATTER

-----------------------

AVAILABLE FORMATS:

1 > TOKEN:MAIL:PASS
2 > TOKEN:PASS:MAIL
3 > TOKEN
4 > MAIL:PASS:TOKEN

-----------------------
""")

FORMAT = input(">> ")

try:
    modes[FORMAT]()
except Exception as e:
    print(f"""
An error occured, please check that you're
using a good input, and that you have a tokens.txt
file with EMAIL:TOKEN:PASS tokens inside. ({e})   
""")
