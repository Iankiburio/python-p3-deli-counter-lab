def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_text = "The line is currently:"
        for index, name in enumerate(katz_deli, start=1):
            line_text += " " + str(index) + ". " + name
        print(line_text)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print("Welcome, {}. You are number {} in line.".format(name, position))

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print("Currently serving {}.".format(serving))
