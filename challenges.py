"""
Pioneers in Engineering Spring 2026 Take-Home Coding Challenges Starter Code
"""


# Question 1
stops = {"SL": "San Leandro", "COL": "Coliseum", "FR":  "Fruitvale", "LM": "Lake Merrit",
          "OAK": "Oakland", "RICH": "Richmond", "EC": "El Cerrito", "NB": "North Berkeley",
            "DB": "Downtown Berkeley", "ASH": "Ashby", "WC": "Walnut Creek", "ORI": "Orinda",
              "LAF": "Lafayette", "PH": "Pleasant Hill", "MAC": "MacArthur", "PIT": "Pittsburg"}
def berkeley_bound(grid: list[list[str]]) -> list[str]:
    def berkeley_bound(grid: list[list[str]]) -> list[str]:
    results = []
    for i in grid:
        index = -1
        for j in range(len(i)):
            if i[j] == "NB" or i[j] == "DB":
                index = j
                break
        if index < 0:
            results.append("Lost")
        else:
            results.append(index)
    return results


# Question 2
def train_schedule(arrivals: dict) -> list[str]:
    ''' Return a list of all the trains arriving, in order, 
    represented by a list of strings “red,” “yellow,” “green,” “blue.”

    >>> schedule = {“red” : [1], “yellow” : [2], “green” : [3], “blue” : [4]}
    >>> train_schedule(schedule)
    [“red”, “yellow”, “green”, “blue”]   
    >>> schedule = {“red” : [2, 32], “yellow” : [10, 80], “green” : [22], “blue” : [45, 50, 90]}
    >>> train_schedule(schedule)
    [“red”, “yellow”, “green”, “red”, “blue”, “blue”, “yellow”, “blue”]
    >>> schedule = {“red” : [109], “yellow” : [190], “green” : [80], “blue” : [20]}
    >>> train_schedule(schedule)
    [“blue”, “green”, “red”, “yellow”]
    >>> schedule = {“red” : [], “yellow”: [20, 200], “green” : [], “blue” : [30]}
    >>> train_schedule(schedule)
    [“yellow”, “blue”, “yellow”]

    '''
    # Write Your Code Here #


# Question 3
def rail_yard(width: int) -> list[str]:
    """
    >>> rail_yard(1)
   ['r'] 
   >>> rail_yard(2)
   ['y','rr']
   >>> rail_yard(3)
   ['rrr', 'ry', 'yr', 'g']
   >>> rail_yard(4)
   ['rrrr','rry','ryr','gr','yrr','rg','b']

    """
    # Write Your Code Here #


# Question 4
def paths(start: str, destination: str, startingLine: str, PARTLines: list[list[str]]) -> list[list[str]]:
    """
    >>> start1 = “Daly City”
    >>> destination1 = “Downtown Berkeley”
    >>> startingLine1 = “RED”
    >>> paths(start1, destination1, startingLine1, PARTLines)
    [
    [RED, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, Oakland City Center, Oakland, MacArthur, Ashby, Downtown Berkeley], 
    [YELLOW, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, Oakland City Center, Oakland, MacArthur, RED, Ashby, Downtown Berkeley], 
    [YELLOW, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, Oakland City Center, Oakland, MacArthur, ORANGE, Ashby, Downtown Berkeley], 
    [BLUE, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, RED, Oakland City Center, Oakland, MacArthur, Ashby, Downtown Berkeley],
    [BLUE, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, YELLOW, Oakland City Center, Oakland, MacArthur, ORANGE, Ashby, Downtown Berkeley],

    [GREEN, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, RED, Oakland City Center, Oakland, MacArthur, Ashby, Downtown Berkeley],
    [GREEN, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, YELLOW, Oakland City Center, Oakland, MacArthur, RED, Ashby, Downtown Berkeley],
    [GREEN, Daly City, Balboa Park, Glen Park, 24th St Mission, 16th St Mission, Civic Center, Powell, Montgomery, Embarcadero, West Oakland, YELLOW, Oakland City Center, Oakland, MacArthur, ORANGE, Ashby, Downtown Berkeley]
    ]

    >>> start2 = “Antioch”
    >>> destination2 = “Millbrae”
    >>> startingLine2 = “YELLOW”
    >>> paths(start2, destination2, startingLine2, PARTLines)
    [
    [YELLOW, Pittsburg Center, Pittsburg, North Concord, Concord, Pleasant Hill, Walnut Creek, Lafayette, Orinda, Rockridge, MacArthur, Oakland, Oakland City Center, West Oakland, Embarcadero, Montgomery, Powell, Civic Center, 16th St Mission, 24th St Mission, Glen Park, Balboa Park, Daly City, Colma, South San Francisco, San Bruno, SFO, Millbrae]
    ] 

    >>> start3 = “Berryessa”
    >>> destination3 = “Millbrae”
    >>> startingLine3 = “BLUE”
    >>> paths(start3, destination3, startingLine3, PARTLines)
    [[]] 
    """
    # Write Your Code Here #


# Question 5
def part_codes(n: int, k: int) -> list[str]:
    """Return all possible bark codes
    
    >>> part_codes(1, 1)
    ['1']

    >>> part_codes(1, 5)
    ['1', '2', '3', '4', '5']

    >>> part_codes(2, 10)
    ['13', '20', '24', '31', '35', '42', '46', '53', '57', '64']

    """
    # Write Your Code Here #


# Question 6
def race_against_bay(n: int, times: list[int]) -> int:
    """
    >>> race_against_bay(2, [10, 8])
    10
    >>> race_against_bay(0, [])    
    0
    >>> race_against_bay(3, [8, 9, 12])
    17
    >>> race_against_bay(5, [10, 13, 9, 10, 11])
    29

    """
    # Write Your Code Here #
