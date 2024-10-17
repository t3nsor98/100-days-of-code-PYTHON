# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question1 = int(
    input(
        """Q1) Do you like Dawn or Dusk? 
1) Dawn 
2) Dusk
"""
    )
)


question2 = int(input("""Q2) When I’m dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold
"""
)
)

question3 = int(input("""Q3) Which kind of instrument most pleases your ear?
1) The violin
2) The trumpet
3) The piano
4) The drum
"""))


if question1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif question1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("error!!!! Wrong Input")

if question2 == 1:
    Hufflepuff += 2
elif question2 == 2:
    Slytherin += 2
elif question2 == 3:
    Ravenclaw += 2
elif question2 == 4:
    Gryffindor += 2
else:
    print("error!!!! Wrong Input")
    
if question3 == 1:
    Hufflepuff += 2
elif question3 == 2:
    Slytherin += 2
elif question3 == 3:
    Ravenclaw += 2
elif question3 == 4:
    Gryffindor += 2
else:
    print("error!!!! Wrong Input")
    
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)


print("You are going to the House with maximum points: ", max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin))
