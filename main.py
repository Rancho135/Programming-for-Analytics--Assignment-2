#****************************************************************
#Name: GOODNEWS AGBADU

#
#ANA1001 Lab 2
#****************************************************************

'''Q1: Think about the city you were born. Make a Python list of some of the interesting things to see.  Use your list to print a series of statements about these items, such as "Paris is wonderful in the spring because everyone is eating crepes". Print one statement for each item in your list using a fstring. Print the statements using the index position counting from the beginning, the middle, and end of the list'''

city = ["is the capital of Nigeria", "is has a beautiful landscape", "is known for unity","is a city for all cultures"]
print(f'Abuja {city[0]}')
print(f'Abuja {city[1]}')
print(f'Abuja {city[-1]}')
print(f'Abuja {city[-2]}')

'''Step 1: You just got an important call from the new president of the Intergalactic Space Force, Priyanka Chopra. She would like you to bring four friends on a mission to save humanity. Make a list of the five people going on the mission (yourself included) and print out a message to each person letting them know they are going on the mission. Print a statement using len() and an fstring showing how many people are on the mission'''

mission = ['Goodnews', 'Sharon', 'Sunday', 'Victor', 'Paddy']
print(f'{mission[0]} you am going on a mission to save humanity')
print(f'{mission[1]} you am going on a mission to save humanity')
print(f'{mission[2]} you am going on a mission to save humanity')
print(f'{mission[3]} you am going on a mission to save humanity')
print(f'{mission[4]} you am going on a mission to save humanity')
print(f'There are {len(mission)} people going for the mission')

'''Step 2: One of the members of the mission is unable to make it due to a bad case of Space Sneezing. Print a message to the person letting them know they are not able to go. Find someone else who is able to go on the mission and modify the list replacing the name of your sick space colleague with the new volunteer. Then print new messages to everyone on the team informing them of the mission and is now on the list. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence'''

print(f'{mission[1]} you are no loner going for the mission because you have covid')
mission[1] = 'Oge'
print(f'{mission[0]} you am going on a mission to save humanity')
print(f'{mission[1]} you am going on a mission to save humanity')
print(f'{mission[2]} you am going on a mission to save humanity')
print(f'{mission[3]} you am going on a mission to save humanity')
print(f'{mission[4]} you am going on a mission to save humanity')
print(f'There are {len(mission)} people going for the mission')

'''Step 3:  On short notice, a new space rocket has become available and more members of the team are able to join the mission to space. The catch is that they must all be celebrities for publicity reasons. Use insert() to add one celebrity to the beginning and middle of the list. Then use append() to add a celebrity to the end of the list. When the three celebrities have been added to the list of space adventurers, print out a message to each person on the list letting them know about the mission. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence'''

mission.insert(0, 'Ronaldo')
mission.insert(2, 'Messi')
mission.append('Rashford')
print(f'{mission[0]} you am going on a mission to save humanity')
print(f'{mission[1]} you am going on a mission to save humanity')
print(f'{mission[2]} you am going on a mission to save humanity')
print(f'{mission[3]} you am going on a mission to save humanity')
print(f'{mission[4]} you am going on a mission to save humanity')
print(f'{mission[5]} you am going on a mission to save humanity')
print(f'{mission[6]} you am going on a mission to save humanity')
print(f'{mission[7]} you am going on a mission to save humanity')
print(f'There are {len(mission)} people going for the mission')

'''Step 4: In yet another cruel twist of fate, Priyanka Chopra calls to let you know that your shuttle has been given to a mission team with a more important mission. How this could be possible you have no idea. Your new vessel, the Little Ducky, only has room for two passengers. First print a message letting everyone know only two people will be able to go on the mission. The use the pop() method to remove people one at a time from the list and print a message to them letting them know that they will not be able to attend the mission. Once the list is down to the final two people, print each of them a message letting them know they will be going on the mission. Its OK if you are not among the final two chosen to go on the mission. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence.'''

print('The mission has changed and only two people are going on the mission')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
popped_mission = mission.pop()
print(f'{popped_mission} you are not going on the mission anymore')
print(f'{mission[0]} you are not going on the mission anymore')
print(f'{mission[1]} you are not going on the mission anymore')
print(f'There are {len(mission)} people going for the mission')

'''Step 5: In a final blow to your already shaky leadership, Priyanka Chopra calls and lets you know that your now downgraded mission has been canceled entirely. Use the del() method to delete everyone from the list and print the list to show it is empty. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence.'''

del mission[0]
del mission[0]
print(mission)
print(f'There are {len(mission)} people going for the mission')

'''Q3: Brazilian football star Ronaldo has been tasked with finding locations for the next World Cup. Think of five places anywhere on earth the event could be held and store them in a list.'''

location = ['Canada', 'Nigeria', 'Usa', 'India', 'Uk']
print(location) #Printing the list as it was stored
print(sorted(location)) #Printing without modifying the original list
print(location) #Printing the list as it was stored
print(sorted(location, reverse = True)) #Printing the list using sorted() in reverse alphabetical order without modifying the original list.
print(location) #printing list at sorted.
location.reverse() #printing list using reverse.
print(location)
location.sort() #printing list for the second time to bring it back to its original form
print(location)
location.sort(reverse = True) #print the list in reverse alphabetical order
print(location)

'''Q4: Create five or more lists (for example, places, colours, types of cheese, super heroes, time, numbers, cats, cars, food, etc) and using the random package (import random at the top of your script, and use random.choice(list) and random.randint(1,5) ), write a story that uses random elements from the lists and random numbers. Your story should change each time you run it. Make sure to properly format where applicable using .title()'''

import random
people = ['Chioma','oge', 'Chika',]
food = ['Rice', 'banana', 'Bagel',]
drinks = ['water', 'coke', 'fanta']
places = ['london', 'Paris', 'toronto']
purpose = ['wedding', 'party', 'church']
print(f"{random.choice(people).title()} likes to eat {food[random.randint(0,2)].lower()} with {drinks[random.randint(0,2)]} in the winter, but would love to visit {places[random.randint(0,2)]} in the summer to attend a {purpose[random.randint(0,2)]}")

'''Q5: Make a list of your student number (for example, student = ["A",0,0,5,5,5,5,5,5]) and write a program that adds the numbers of your student number together using list index positions. Then, using the same list, print out your student number by converting numbers to strings as needed using an fstring.'''

student_id = ['A',0,0,2,3,8,2,1,9]
total = student_id[1] + student_id[2] + student_id[3] + student_id[4] + student_id[5] + student_id[6] + student_id[7] + student_id[8]
print(total)
complete_id = (f"{student_id[0]}{student_id[1]}{student_id[2]}{student_id[3]}{student_id[4]}{student_id[5]}{student_id[6]}{student_id[7]}{student_id[8]}")
print(complete_id)