print ("Write the menu method name (leave blank for menu):")
name = input() or "menu"

print ("Is static? (blank = no static, something = static)")
if len(input()) != 0:
    static = "static "
else:
    static = ""

options = []
print ("---Options---:")
inp = "y"
while len(inp) != 0:
    print ("Write the option name:")
    options.append("\t\t\tcase {0}: {1}(); break;".format(len(options)+1,input()))
    print ("Wanna add another case? (blank = no, something = yes:")
    inp = input()

menu = [
    "public " + static + "void " + name + "() {",
    "\tint op",
    "\tdo {",
    "\t\top = USERINPUT",
    "\t\tswitch(op) {",
]
for x in options:
    menu.append(x)
menu.append("\t\t}")
menu.append("\t}"+"while(op<{0});".format(len(options)+1))
menu.append("}")

print ("---Generated Menu---")
for i in menu:
    print(i)
