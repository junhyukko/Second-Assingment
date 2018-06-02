""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO

def count_lines(profiles_file: TextIO) -> int:
    """Count the total number of lines in a given file.
    
    >>> count_lines('profiles.txt')
    60
    """
    
    file = open(profiles_file)
    return len(file.readlines())

def information(profiles_file: TextIO) -> List[str]:
    """Make a new list of names that is obtained from the profiles_file without
    the \n unless there is a new line.
    
    >>> information('profiles1.txt')
    ['Pritchett, Jay']
    """
    
    file = open(profiles_file)
    l = []
    for name in file.readlines():
        if name != '\n':
            l.append(name[0:-1])
        else:
            l.append(name)
    return l

def first_line(names: List[str])-> List[str]:
    """Return only the first line of every paragraph or stanza.
    >>> first_line(['Pritchett, Jay'], 'profiles1.txt')
    ['Pritchett, Jay']
    """
    l = []
    i = 0
    l.append(names[0])
    while i < len(names):
        if names[i] == '\n':
            l.append(names[i + 1])
        i = i + 1
    return l

def remove_first(names: List[str], profiles_file: TextIO) -> List[str]:
    """Return a list that has the first line and \n removed.
    """
    
    l = []
    i = 1
    while i < len(names):
        l.append(names[i])
        if names[i] == '\n':
            i = i + 2
        else:
            i = i + 1
    return l

#def create_dict(names: List[str], network: List[str]) -> Dict[str, List[str]]:
    #"""
    #"""
    
    #d = {}
    #i = 0
    #for key in names:
        #while network[i] != '\n':
            #if key not in d:
                #d[key] = [network[i]]
            #else:
                #d[key].append(network[i])
            #if network[i] == '\n':
                #i = i + 2
            #else:
                #i = i + 1
    #return d
    
def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    
    #first section is to update person_to_friends dictionary
    #i = 0
    #total_list = information(profiles_file)
    #while i < len(total_list):
        #for list
        
    #for name in 
    #while lines != '\n':
        #if first_line not in person_to_friends:
            #person_to_friends[first_line] = [lines]
            #if first_line in person_to_friends:
                #person_to_friends[first_line].append(lines)
        #else:
            #person_to_friends[first_line].append(lines)
        #lines = file.readline()
        #print(lines)
    #for line in file:
        #if line == "\n":
            #key = line
            #while file.readline() != '\n':
                #if key not in person_to_friends:
                    #person_to_friends[key] = [file.readline()]
                #else:
                    #person_to_friends[key].append(file.readline())
                #lines = file.readline()
    #file.close()
    ##this section is updating person_to_networks
    #file = open(profiles_file)
    #for line in file:
        #if line == '\n':
            #file.readline()
            #network = file.readline()
            
            

    
def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends each person has.
    
    >>> get_average_friend_count({'Jay Pritchett': ['Claire Dunphy', 'Gloria Prit
    chett'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett']
    2.0
    """
    
    a = len(person_to_friends)
    x = 0
    for person in person_to_friends:
        x = x + len(person_to_friends[person])
    if a != 0:
        total = len(person_to_friends)
        return x/total
    else:
        return 0
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return the dictionary that has family names as keys and the family 
    member(s) in the list.
    
    >>> get_families({'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett']})
    {'Pritchett': [Jay, Gloria]}
    """
    
    d = {}
    for person in person_to_friends:
        family_name = person.split()[1]
        if person.split()[1] not in d:
            d[person.split()[1]] = [person.split()[0]]
        else:
            d[person.split()[1]].append(person.split()[0])
        for family in person_to_friends[person]:
            if family_name in family:
                d[person.split()[1]].append(family.split()[0])
            else:
                d[family.split()[1]] = [family.split()[0]]
    return d 

def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a dictionary where the keys are the networks and the list are the
    people that belong to that network.
    
    >>> invert_network({'Gloria Pritchett': ['Parent Teacher Association'], 
    'Claire Dunphy': [Parent Teacher Association]})
    {'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett']
    """
    
    d = {}
    for person in person_to_networks:
        for network in person_to_networks[person]:
            if network in person_to_networks[person]:
                if network not in d:
                    d[network] = [person]
                else:
                    d[network].append(person)
    return d

def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """Return the list that is the friends of the friends of a given person.
    >>> get_friends_of_friends({''Jay Pritchett': ['Claire Dunphy'], 'Claire Dun
    phy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy']}, 'Jay Prithett
    ')
    ['Mitchell Pritchett', 'Phil Dunphy']
    """
    
    d = person_to_friends
    l = []
    for friend in d[person]:
        if friend in person_to_friends:
            for friend2 in d[friend]:
                if friend2 != person:
                    l.append(friend2)
    return l            
        
        
def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """From the network the person in question belongs to as well as having
    mutual friends, this function returns a possible friend with a score that
    indicates the higher the score, more likely the two people can be friends.
    
    >>> make_recommendations('Jay Pritchett', person_to_friends, person_to_netwo
    rks)
    [('Mitchell Pritchett', 4), ('Alex Dunphy', 1), ('Cameron Tucker', 3), ('Hal
    ey Gwendolyn Dunphy', 2), ('Phil Dunphy', 3)]
    """
    
    l = []
    d = person_to_friends
    for population in person_to_friends:
        if population not in d[person]:
            counter = 0
            if person in get_friends_of_friends(d, population):
                counter = counter + 1
            for network in invert_network(d):
                if person and population in invert_network(d)[network]:
                    counter = counter + 1
            if population in get_families(d) and counter > 0:
                counter = counter + 1
            if counter != 0:
                l.append((population, counter))
    if len(l) > 0:
        return l
    else:
        return "There are no recommendations for this person."                


if __name__ == '__main__':
    import doctest
    doctest.testmod()
