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

# 9.Print the first, middle and last company
middle_index = len(it_companies) // 2
last_index = len(it_companies) - 1

first_item = it_companies[0]
middle_item = it_companies[middle_index]
last_item = it_companies[last_index]

print("First company", first_item)
print("Middle company", middle_item)
print("Last company", last_item)

# 10.Print the list after modifying one of the companies
it_companies[0] = 'Instagram'
print(it_companies)

# 11.Add an IT company to it_companies
it_companies.append('SAP')
print(it_companies)

# 12.Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Sikich')
print(it_companies)

# 13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# 14.Join the it_companies with a string '#;  '
it_companies += '#;  '
print(it_companies)

# 15.Check if a certain company exists in the it_companies list.
print('APPLE' in it_companies)

# 16.Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17.Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18.Slice out the first 3 companies from the list
slice_list = it_companies[:3]
print(slice_list)
slice_list = it_companies[0:3]
print(slice_list)

# 19.Slice out the last 3 companies from the list
slice_list = it_companies[-3:]
print(slice_list)

# 20.Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
slice_list = it_companies[middle_index:middle_index+1]
print(middle_index)
print(slice_list)
print(it_companies[middle_index])

# 21.Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# 22.Remove the middle IT company or companies from the list
if len(it_companies) % 2 is not 0:
    middle_index = len(it_companies) // 2
    it_companies.remove(it_companies[middle_index])
else:
    middle_index = len(it_companies) // 2
    second_middle_index = len(it_companies) // 2 - 1
    it_companies.remove(it_companies[middle_index])
    it_companies.remove(it_companies[second_middle_index])
print(it_companies)

# 23.Remove the last IT company from the list
last_index = len(it_companies) -1
it_companies.remove(it_companies[last_index])

# 24.Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25.Destroy the IT companies list
del it_companies

# 26.Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end


front_end.extend(back_end)
new_list2 = front_end.copy()

print(new_list)
print(new_list2)

# 27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = new_list.copy()
index_redux = full_stack.index('Redux') + 1
full_stack.insert(index_redux,"Python")
full_stack.insert(index_redux + 1 ,"SQL")
print(full_stack)




