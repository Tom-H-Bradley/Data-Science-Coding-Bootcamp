#Using a dictionary allows us to catalogue different prices for the different cities. Every city will have a different flight cost
#hotel cost and car rental rate for the tourist.
#The lists linked to each city key take this format [flight cost, hotel cost per night, car rental cost per day]

cost_dict = {"rome": [80, 50, 30],
            "paris": [40, 120, 60],
            "istanbul": [130, 70, 20],
            "madrid": [70, 80, 50],
            "stockholm": [90, 150, 90]}

#Setting the city as all lower case is defensively programming against an caps locks the user may have on

city = input("What city are you goign to be flying to? Rome, Paris, Istanbul, Madrid or Stockholm?\n")
city = city.lower()
num_nights = input("How many nights will you be staying for?\n")
rental_days = input("How many days will you need a rental car for?\n")

#In each of these functions, a is always the city, b is always the number of nights and c is the rental days. I didn't want to reuse,
#or create very similar variable names which could confuse, so I used these uniform letters with a note.

#The first function takes whichever city the user selected and multiplies it's hotel cost by the number of nights staying there.
#The second function takes the plane cost of the city selected.
#The third function takes the car rental cost per day of city selected, and multiplies it by the number of days the rental is required

def hotel_cost(a, b):
    hotel = cost_dict[a][1]*int(b)
    return hotel

def plane_cost(a):
    plane = cost_dict[a][0]
    return plane

def car_rental(a, c):
    car = cost_dict[a][2]*int(c)
    return car

#Finally, holiday cost is a simple function which sums 3 numbers. 

def holiday_cost(d, e, f):
    holiday = d + e + f
    return holiday

#When we put the functions within our sum function, this will calculate the total cost of the holiday
#Underneath is some formatting to make the result readable.

total = holiday_cost(hotel_cost(city, num_nights), plane_cost(city), car_rental(city, rental_days))
print(f"The total cost of your holiday to {city} for {num_nights} nights will be £{str(total)}")

    


