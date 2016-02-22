operacije = ["mnozenje", "deljenje", "odstevanje", "sestevanje", "potenciranje", "korenjenje"]

def sestevanje (x, y):
    return (x + y);
def odstevanje (x, y):
    return (x - y);
def mnozenje (x, y):
    return (x * y);
def deljenje (x, y):
    return (x / y)
def potenciranje (x, y):
    return (x ** y)
def korenjenje (x, y):
    return (x ** (1/y))

def vnos():
    while True:
        try:
            number = int(raw_input("Stevilo: "))
            break
        except ValueError:
            print("Error")
    return number


def operacija():
    while True:
        operacija = raw_input("Katero operacijo bi zeleli (mnozenje, deljenje, odstevanje, potenciranje, korenjenje)? ")
        if operacija in operacije:
            break
        else:
            print("Ta operacija ni na izbiro.")
    return operacija;

def ponovi():
    while True:
        again = raw_input("Znova? Da/Ne: ").lower()
        if again == "da":
            return True
        elif again == "ne":
            return False
        else:
            print("Error!")

while True:
    nacin = operacija()
    s1 = vnos()
    s2 = vnos()
    if nacin == "mnozenje":
        print (mnozenje(s1,s2))
    elif nacin == "sestevanje":
        print (sestevanje(s1,s2))
    elif nacin == "odstevanje":
        print (odstevanje(s1,s2))
    elif nacin == "deljenje":
        print (deljenje(s1,s2))
    elif nacin == "potenciranje":
        print (potenciranje(s1, s2))
    elif nacin == "korenjenje":
        print (korenjenje(s1,s2))

    ponovi()
