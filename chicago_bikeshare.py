
# coding: utf-8
#Student: R

# Here goes the imports
import csv
import numpy as np
import pandas
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
   reader = csv.reader(file_read)
   data_list = list(reader)
file_read.close()

print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

for index in range(len(data_list[0:20])):
    print(data_list[index])

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")


aux = []
for i in range(len(data_list[0:20])):
    for j in range(len(data_list[i])):
        aux = data_list[i]
    print(aux[-2])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order

"""
      Example function to add the columns(features) of a list in another list in the same order.
      def column_to_list(data_list: list, index: int) -> column_list:
      Args:
          data_list: all the data read from the csv file as a list
          index: the index of the data
      Returns:
          column_list: a list with all the values from the column specified by the index

      """
def column_to_list(data_list, index):
    column_list = []
    aux = []
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            aux = data_list[i]
        column_list.append(aux[index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])


# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
aux = []
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        aux = data_list[i]
    #print(aux[-2])
    if aux[-2] == "Male":
        male = male + 1
    elif aux[-2] == "Female":
        female = female + 1



# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)

"""
      Example function to count the genders. Return a list
      def count_gender(data_list: list) -> [male: int, female: int]:
      Args:
          data_list: all the data read from the csv file as a matrix
      Returns:
          [male , female]: the int variables responsible to count the number of males and females
"""

def count_gender(data_list):
    male = 0
    female = 0
    aux = []
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            aux = data_list[i]
        if aux[-2] == "Male":
            male = male + 1
        elif aux[-2] == "Female":
            female = female + 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.

"""
      Example function tto get the most popular gender and print the gender as string
      def count_gender(data_list: list) -> answer: str
      Args:
          data_list: all the data read from the csv file as a matrix
      Returns:
          answer: depending on the result of the auxiliars variables from the function the result can be "Male" or "Female"
"""

def most_popular_gender(data_list):
    answer = ""
    male = 0
    female = 0
    aux = []
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            aux = data_list[i]

        if aux[-2] == "Male":
            male = male + 1
        elif aux[-2] == "Female":
            female = female + 1

    if male > female:
        answer = "Male"
    else:
        answer = "Female"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

"""
      Example function to check the type of the user that is very similar to the count_gender() function
      def count_user_type(data_list: list) -> answer: str
      Args:
          data_list: all the data read from the csv file as a matrix
      Returns:
         [customer, subscriber]: the int variables responsible to count the number of customers and subscribers
"""

def count_user_type(data_list):
    customer = 0
    subscriber = 0
    aux = []
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            aux = data_list[i]
        if aux[5] == "Customer":
            customer = customer + 1
        elif aux[5] == "Subscriber":
            subscriber = subscriber + 1
    return [customer, subscriber]

user_type_list = column_to_list(data_list, 5)
types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
print(male + female)
print(len(data_list))
answer = "Because there are some data with a blank space"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
#print (trip_duration_list)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

"""
      Example function to ordenate the values of a list using the quicksort algorithm
      def quicksort(l: list) -> []: list
      Args:
          l: list of values not ordenated
      Returns:
         []: list ordenated
"""

def quicksort(l):
    if l:
        left = [x for x in l if x < l[0]]
        right = [x for x in l if x > l[0]]

        if len(left) > 1:
            left = quicksort(left)
            right = quicksort(right)

        return left + [l[0]] * l.count(l[0]) + right

    return []

"""
      Example function to calculate the mean of a list of float values
      def mean(data_list: list) -> mean: float
      Args:
          data_list: list of float values
      Returns:
         mean: the mean of the values
"""

def mean(data_list):
    total = 0
    mean = 0
    for i in range(len(data_list)):
        total = int(data_list[i]) + total

    mean = total/len(data_list)
    return mean

"""
      Example function to get the median of a list of float values
      def median(data_list: list) -> data_list[half]: float
      Args:
          data_list: list of float values
      Returns:
         median: the median of the data_list
"""

def median(data_list):
    half = len(data_list) // 2
    data_list.quicksort()
    if not len(data_list) % 2:
        return (data_list[half - 1] + data_list[half]) / 2.0
    return data_list[half]

sorted_list = quicksort(trip_duration_list)
min_trip = sorted_list[0]
max_trip = sorted_list[-1]
mean_trip = mean(trip_duration_list)
median_trip = median(trip_duration_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
#assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
#assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
#assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
#assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...\n")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
start_stations_list =  column_to_list(data_list, 3)
user_types = set(start_stations_list)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

      """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
