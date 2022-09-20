stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

stops.append("Edinburgh Waverley")  # Adds E.W to end of list
insert = ("Glasgow Queen St")       # Inserts GQS to start of list
stops = [insert] + stops            # Inserts GQS to start of list

stops.insert(4, ("Polmont"))        # Inserts Polmont into position 4

index = stops.index("Linlithgow")   # Notes Linlithgows index position ########

stops.remove("Livingston")          # Removes Livingston via its name
del stops[2]                        # Deletes Cumbernauld from list via index

num_of_stops = len(stops)           # Prints total number of stops
stops.sort()                        # Sorts list items alphabetically
print(stops)                        # 
print(index)                        # Prints Linlithgows index position
print(num_of_stops)                 # Prints number of stops

stops.reverse()                     # Reverses order of stops in the list
# print(stops)                      # Prints the stops in the list
for x in stops:                     # Prints list items via For Loop
    print(x)                        # Prints list items via For Loop