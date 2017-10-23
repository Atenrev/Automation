print ("Write the menu method name (leave blank for menu):")
name = input() or "menu"

print ("Is static? (blank = no static, something = static)")
if len(input()) != 0:
    static = "static "
else:
    static = ""

options = []
print ("---Options---:")
inp = ""
while len(inp) == 0:
    print ("Write the option name:")
    options.append("\t\t\tcase {0}: {1}(); break;".format(len(options),input()))
    print ("Wanna add another case? (blank = yes, something = no:")
    inp = input()

print ("Write the text (with the format you want) you want to appear on the menu:")
text = input()

menu = [
    "public " + static + "void " + name + "() {",
    "\tint op;",
    "\tdo {",
     "\t\tSystem.out.println('{0}');".format(text),
    "\t\top = USERINPUT;",
    "\t\tswitch(op) {",
]
for x in options:
    menu.append(x)
menu.append("\t\t}")
menu.append("\t}"+"while(op<{0});".format(len(options)))
menu.append("}")

print ("---Generated Menu---")
for i in menu:
    print(i)
