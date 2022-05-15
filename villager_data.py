"""Functions to parse a file containing villager data."""
species_data = open("villagers.csv")


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

   
    species_data = open(filename)

    unique_species = []
    for line in species_data:
        data = ("name", "species","motto", "hobby")
        data = line.split('|')
        species = data[1]
        unique_species.append(species)
    village_species = set(unique_species)


    return village_species
    #unique_species = set(species)

    # return data


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    species_data = open(filename)
    villagers = []
    for line in species_data:
        data = line.split('|')
        name = data[0]
        species = data[1]
        if search_string == 'All':
            villagers.append(name)
        elif search_string == species:
            villagers.append(name)
    return sorted(villagers)




def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    species_data = open(filename)

    hobby_by_name = []
    hobbies_list = []
    for line in species_data:
        data = ("name", "species","motto", "hobby")
        data = line.split('|')
        name = data[0]
        hobby = data[3]
        if hobby not in hobbies_list:
            hobbies_list.append(hobby)
        hobbies_list_len = len(hobbies_list)
        for index in range(hobbies_list_len):
            if hobbies_list[index] == hobby:
                hobby_by_name.append(hobby)
                #hobby_by_name.append(name)
    print(hobbies_list)
            
       # new_hobbiest_list= hobbies_list.append(hobby)+hobbies_list.append(name)
'''        
    village_hobby = set(unique_hobby)

    return village_hobby
'''

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
#print(all_species("villagers.csv"))
#print(get_villagers_by_species("villagers.csv",))
print(all_names_by_hobby("villagers.csv"))
