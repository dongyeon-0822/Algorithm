import re

regex = re.compile('^[A-F]?A+F+C+[A-F]?$')
T = int(input())
for i in range(T):
    line = input()
    print("Infected!" if regex.match(line) else "Good")
