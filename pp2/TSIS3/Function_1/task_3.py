#Write a program to solve a classic puzzle: 
#We count 35 heads and 94 legs among the chickens and rabbits 
#in a farm. How many rabbits and how many chickens do we have?
# Mathematical solution:
#   { 2x + 4y = 95
#   { x + y = 35    => x = 35 - y   => 2(35 - y) + 4y = 95   => 2y = 94 - 75    => y = (94 - 75) / 2

#   y = 12  => x = 35 - 12  => x = 23

def SolvingTheRiddleOfLegsAndHeads(numheads: int, numlegs: int):
    quadrupeds: int = (numlegs - (numheads * 2)) / 2
    bipeds: int = numheads - quadrupeds

    print(f"Quadrupeds: {quadrupeds}, bipeds: {bipeds}")

SolvingTheRiddleOfLegsAndHeads(35, 94)