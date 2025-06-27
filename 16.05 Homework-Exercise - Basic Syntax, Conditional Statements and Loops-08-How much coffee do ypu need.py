# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake. Until you receive the command "END",
# you need to read commands on different lines. According to the commands, calculate the number of coffees
# you need to drink to stay awake during the daytime.
# The list of events can contain the following:
# •	You have homework to do ("coding").
# •	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# •	You watch a movie ("movie").
# •	If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# •	If it is lowercase, you need 1 coffee by an event.
# •	If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".

coffee_count = 0

while True:
    event = input()
    if event == "END":
        break

    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffee_count += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffee_count += 2

    if coffee_count > 5:
        print("You need extra sleep")
        exit()

print(coffee_count)