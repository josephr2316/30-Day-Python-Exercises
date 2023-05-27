# 1.Declare an empty list
lst = list()
list1 = []

# 2.Declare a list with more than 5 items
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3.Find the length of your list
print("Length of the list: ", len(list2))

# 4.Get the first item, the middle item and the last item of the list
first_item = list2[0]
middle_index = len(list2) // 2
last_index = len(list2) - 1
middle_item = list2[middle_index]
last_item = list2[last_index]

print("The first item of the list is: ", first_item)
print("The middle item of the list is: ", middle_item)
print("The last item of the list is : ", last_item)

# 5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Joseph", 29, 1.85, "single", "Villa Olga"]

# 6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7.Print the list using print()
print(mixed_data_types)
print(it_companies)

# 8.Print the number of companies in the list
print(len(it_companies))

