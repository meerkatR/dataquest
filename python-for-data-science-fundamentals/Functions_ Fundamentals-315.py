## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
sum_manual = 0
for element in a_list:
    sum_manual += element
print(sum_manual, sum(a_list))

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for element in ratings:
    if element in content_ratings:
        content_ratings[element] += 1
    else:
        content_ratings[element] =1
print(content_ratings)

## 3. Creating Our Own Functions ##

def square(x):
    x2 = x*x
    return(x2)
squared_10 = square(10)
squared_16 = square(16)

## 4. The Structure of a Function ##

def add_10(num):
    num10 = num +10
    return(num10)
add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##

def square(x):
    return x*x
squared_6 = square(6)
squared_11 = square(11)

## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    alist = []
    for row in apps_data[1:]:
        value = row[index]
        alist.append(value)
    return alist
genres = extract(11)
    

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(alist):
    alist_ct = {}
    for element in alist:
        if element in alist_ct:
            alist_ct[element] += 1
        else:
            alist_ct[element] = 1
    return alist_ct
genres_ft = freq_table(genres)

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
def freq_table(idx):
    freq_tbl = {}
    for row in apps_data[1:]:
        value = row[idx]
        if value in freq_tbl:
            freq_tbl[value] += 1
        else:
            freq_tbl[value] = 1
    return freq_tbl

ratings_ft = freq_table(7)

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index, data_set):
    frequency_table = {}
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft = freq_table(7, apps_data)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set = apps_data, index = 7)
genres_ft = freq_table(index = 11, data_set = apps_data)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    data_list = extract(data_set, index)
    return find_sum(data_list)/find_length(data_list)

avg_price = mean(apps_data, 4)

## 12. Debugging Functions ##

# INITIAL CODE
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)