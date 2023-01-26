import csv
import json

countries = {}


class CountryMedals:  # defining a class for country medals
    def __init__(self, country_name, gold_medals, silver_medals, bronze_medals, total_medals, rank, rank_by_medals):
        self.country_name = country_name
        self.gold_medals = gold_medals
        self.silver_medals = silver_medals
        self.bronze_medals = bronze_medals
        self.total_medals = total_medals
        self.rank = rank
        self.rank_by_medals = rank_by_medals

    def to_json(self):  # generates a json summary of the object
        country_json = {"gold medals": self.gold_medals,
                        "silver medals": self.silver_medals,
                        "bronze medals": self.bronze_medals,
                        "total medals": self.total_medals
                        }
        return country_json

    def get_medals(self, medal_type):  # from a user input will return the number of medals of that type
        if medal_type.lower() == "gold":  # check if input is gold
            return self.gold_medals  # return number of gold medals
        if medal_type.lower() == "silver":
            return self.silver_medals
        if medal_type.lower() == "bronze":
            return self.bronze_medals
        if medal_type.lower() == "total":
            total_medals = self.total_medals
            return total_medals
        else:
            return None

    def print_summary(self):  # prints a summary for a given country of the class
        print("{} received {} medals in total; {} gold, {} silver, and {} bronze".format(self.country_name,
                                                                                         self.total_medals,
                                                                                         self.gold_medals,
                                                                                         self.silver_medals,
                                                                                         self.bronze_medals))

    def compare(self, country2):  # to compare a second country of the same type
        print("Medals comparison between '{}' and '{}':".format(self.country_name,
                                                                country2.country_name))  # print out comparison

        """
        We create a nested list so that it is easy to iterate over and print
        The list includes the type of medal and the number of medals that each country got
        """

        compared_medals = [["gold", self.gold_medals, country2.gold_medals],
                           ["silver", self.silver_medals, country2.silver_medals],
                           ["bronze", self.bronze_medals, country2.bronze_medals],
                           ["total", self.total_medals, country2.total_medals]]
        for colour in compared_medals:
            if int(colour[1]) == int(colour[2]):  # if the number of medals were equal print something
                print("Both '{}' and '{}' received {} {} medal(s).".format(self.country_name,
                                                                           country2.country_name,
                                                                           colour[1],
                                                                           colour[0]))
            if int(colour[1]) < int(colour[2]):  # if the number of medals were not equal print something
                difference = int(colour[2]) - int(colour[1])
                print("{} received {} {} medal(s), {} fewer than {}, which received {}.".format(self.country_name,
                                                                                                colour[1],
                                                                                                colour[0],
                                                                                                difference,
                                                                                                country2.country_name,
                                                                                                colour[2]))
            if int(colour[1]) > int(colour[2]):
                difference = int(colour[1]) - int(colour[2])
                print("{} received {} {} medal(s), {} more than {}, which received {}.".format(self.country_name,
                                                                                               colour[1],
                                                                                               colour[0],
                                                                                               difference,
                                                                                               country2.country_name,
                                                                                               colour[2]))


def get_sorted_list_of_countries(countries):  # returns a sorted list of the countries in alphabetical order
    sorted_countries = sorted(dict.keys(countries))  # sort countries on their dictionary key
    return sorted_countries


def sort_country_by_medal_type_ascending(countries, medal_type):  # returns a sorted list on the medal type
    return_list = []
    for key in countries:
        return_list.append(countries[key])  # we are creating a list only with class objects which is easier to
                                            # iterate over
    if medal_type == "gold":    # depending on a given medal type complete a bubble sorting alogrithm
                                # (there are more efficient algorithms available)
        for i in range(len(return_list)):
            for j in range(0, len(return_list) - i - 1):
                if int(return_list[j].gold_medals) > int(return_list[j + 1].gold_medals):  # compare gold medal values
                    temp = return_list[j]
                    return_list[j] = return_list[j + 1]
                    return_list[j + 1] = temp
        return return_list
    if medal_type == "silver":
        for i in range(len(return_list)):
            for j in range(0, len(return_list) - i - 1):
                if int(return_list[j].silver_medals) > int(return_list[j + 1].silver_medals):
                    temp = return_list[j]
                    return_list[j] = return_list[j + 1]
                    return_list[j + 1] = temp
        return return_list
    if medal_type == "bronze":
        for i in range(len(return_list)):
            for j in range(0, len(return_list) - i - 1):
                if int(return_list[j].bronze_medals) > int(return_list[j + 1].bronze_medals):
                    temp = return_list[j]
                    return_list[j] = return_list[j + 1]
                    return_list[j + 1] = temp
        return return_list
    if medal_type == "total":
        for i in range(len(return_list)):
            for j in range(0, len(return_list) - i - 1):
                if int(return_list[j].total_medals) > int(return_list[j + 1].total_medals):
                    temp = return_list[j]
                    return_list[j] = return_list[j + 1]
                    return_list[j + 1] = temp
        return return_list


def sort_country_by_medal_type_descending(countries, medal_type):  # returns a sorted list on the medal type
    return_list = []
    sorted_list = sort_country_by_medal_type_ascending(countries, medal_type)  # sort in ascending order and then flip
    for i in range(len(sorted_list)):
        return_list.append(sorted_list[-i])  # -i wil place them in the opposite index value (1st object goes to last object etc.)
    return return_list


def read_positive_integer():  # checks that an input is a positive integer
    while True:
        integer = input("Please enter a positive integer: ")
        try:
            int(integer)
            is_int = True
        except ValueError:
            is_int = False
        if is_int:
            if int(integer) > 0:
                return int(integer)
            else:
                print("Make sure your input is positive.")
        print("Your input is not valid, please try again.")


def read_country_name():  # returns a country name as long as the country name is in our dictionary
    while True:
        country_name = input("Please enter a country name ('q' for quit): ")
        country_name = country_name.strip()
        if country_name.lower() == "q":
            return
        for key in dict.keys(countries):
            if country_name.lower() == key.lower():
                return key
        print("Your input is not valid, pleas try again.")
        print("You can select the following countries: ")
        sorted = get_sorted_list_of_countries(countries)
        for country in sorted:
            print(country)


def read_medal_type():  # get a valid metal type as input
    medals = ["gold", "silver", "bronze", "total"]
    while True:
        medal_input = input("Please enter a medal type: ")
        medal_input = medal_input.lower()
        medal_input = medal_input.strip()
        if medal_input in medals:
            return medal_input
        print("That is not a valid medal type")
        print("Valid medal types are [gold, silver, bronze, total]")


def print_help():  # prints help for the user
    print("List of commands:")
    print("- (H)elp shows the list of commands;")
    print("- (L)ist shows the list of countries present in the dataset;")
    print("- (S)ummary prints out a summary of the medals won by a single country;")
    print("- (C)ompare allows for a comparison of the medals won by two countries;")
    print("- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;")
    print("- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;")
    print("- (E)xport, save the medals table as '.json' file;")
    print("- (Q)uit.")


with open('medals.csv', newline='') as csvfile:  # the medals file is in the same folder as the script
    parse = csv.reader(csvfile, delimiter=',', quotechar='"')  # parse the csv file (handle "" exception)
    iteration = 0
    for row in parse: # for each row, add an item to dictionary with name as the key and class CountryMedal object as value
        if iteration > 0:  # this is to avoid the first row in the csv file
            countries["{}".format(row[1])] = CountryMedals(row[1], row[2], row[3], row[4], row[5], row[0], row[6])
        iteration = iteration + 1

# start of our main loop

terminated = False
while not terminated:  # continue running as long as user hasn't quit
    c = input("\nInsert a command (H for help): ")
    c = c.upper() # get input and format for comparison

    if c == "H": # print help
        print_help()

    elif c == "L":  # get the sorted list of countries from the above function
        sorted_countries = get_sorted_list_of_countries(countries)
        print("\nThe dataset includes the following {} countries: ".format(len(dict.keys(countries))))
        for country in sorted_countries:
            print(country, end=", ")  # print the countries from the list

    elif c == "S":  # summarize the country
        key = read_country_name()  # get country
        country_to_sum = countries[key]  # get the class object for the country from the ditionary
        country_to_sum.print_summary()  # print the summary from method the class object

    elif c == "C":  # compare two countries
        print("\nCompare two Countries")
        key1 = read_country_name()
        country1 = countries[key1]  # get the class object for the country from the ditionary

        print("\nInsert the name of the country you want to compare: ")
        key2 = read_country_name()
        country2 = countries[key2]  # get the class object for the country from the ditionary

        country1.compare(country2)  # compare using the method that is within the class

    elif c == "M":  # more than a certain number of medals
        print("Given a medal type, lists all the countries that received more medals than a threshold")
        medal_type = read_medal_type()  # get medal type
        print("Enter a threshold")
        threshold = read_positive_integer()  # get integer
        print("Countries that have more than {} {} models".format(medal_type, threshold))
        sorted_list = sort_country_by_medal_type_descending(countries, medal_type)
        for country in sorted_list:  # get the sorted list and iterate over it
            if medal_type == "gold":  # depending on the medal type we will branch in different directions
                if int(country.gold_medals) > threshold:    # if the number of medals a country got is more than a
                                                            # threshold, print out the country and number of medals
                    print(" - {} received {} medals".format(country.country_name, country.gold_medals))
            if medal_type == "silver":
                if int(country.silver_medals) > threshold:
                    print(" - {} received {} medals".format(country.country_name, country.silver_medals))
            if medal_type == "bronze":
                if int(country.bronze_medals) > threshold:
                    print(" - {} received {} medals".format(country.country_name, country.bronze_medals))
            if medal_type == "total":
                if int(country.total_medals) > threshold:
                    print(" - {} received {} medals".format(country.country_name, country.total_medals))

    elif c == "F":  # fewer medals work similarly to above but comparison has been switched
        print("Given a medal type, lists all the countries that received fewer medals than a threshold")
        medal_type = read_medal_type()
        print("Enter a threshold")
        threshold = read_positive_integer()
        print("Countries that have fewer than {} {} models".format(medal_type, threshold))
        sorted_list = sort_country_by_medal_type_ascending(countries, medal_type)
        for country in sorted_list:
            if medal_type == "gold":
                if int(country.gold_medals) < threshold:
                    print(" - {} received {} medals".format(country.country_name, country.gold_medals))
            if medal_type == "silver":
                if int(country.silver_medals) < threshold:
                    print(" - {} received {} medals".format(country.country_name, country.silver_medals))
            if medal_type == "bronze":
                if int(country.bronze_medals) < threshold:
                    print(" - {} received {} medals".format(country.country_name, country.bronze_medals))
            if medal_type == "total":
                if int(country.total_medals) < threshold:
                    print(" - {} received {} medals".format(country.country_name, country.total_medals))

    elif c == "E":  # exporting a json file
        file_name = input("Please enter a file name: ")
        json_file = {}
        for key in countries:
            json_file[key] = json.dumps(countries[key].to_json()) # save dumps to data

        data = json.dumps(json_file)
        with open("{}.json".format(file_name), "w") as f:
            f.write(data)  # write file with data

    elif c == "Q":  # if user wants to quit then stop the loop
        terminated = True
    else:
        print("That is not a valid input")

# end of our main loop