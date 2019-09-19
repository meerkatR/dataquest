## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date

## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen

decades = []
for age in final_ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)[:-1] + "0s"
    decades.append(decade)
        

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}
for age in decades:
    if age not in decade_frequency:
        decade_frequency[age] = 1
    else:
        decade_frequency[age] += 1
 

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{}'s birth year is {}"
rst = template.format(artist, birth_year)
print(rst)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1
        

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    if artist in artist_freq:
        n_works = artist_freq[artist]
        template = "There are {n} artworks by {name} in the data set"
        sentence = template.format(n = n_works, name = artist)
        print(sentence)
    else:
        print("Artist not in the data set")
        
artist_summary("Henri Matisse")
    

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {country} is {pop:,.2f} million"
for row in pop_millions:
    country = row[0]
    pop = row[1]
    sentence = template.format(country = country, pop = pop)
    print(sentence)
    
               
    
    
    
    