# Question 1
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
    solutions = []
    while arrivals["red"] or arrivals["yellow"] or arrivals["green"] or arrivals["blue"]:
        key = "red"
        if min(arrivals["yellow"], default=2147483647) < min(arrivals[key], default=2147483647):
            key = "yellow"
        if min(arrivals["green"], default=2147483647) < min(arrivals[key], default=2147483647):
            key = "green"
        if min(arrivals["blue"], default=2147483647) < min(arrivals[key], default=2147483647):
            key = "blue"
        solutions.append(key)
        arrivals[key].pop(0)
        
    return solutions

# Question 3
def rail_yard(width: int) -> list[str]:
    solutions = []
    rail_yard_helper(solutions, "", width)

    return solutions

def rail_yard_helper(arr: list[str], word: str, spots_left: int):
    if spots_left >= 1:
        rail_yard_helper(arr, word + "r", spots_left - 1)
    if spots_left >= 2:
        rail_yard_helper(arr, word + "y", spots_left - 2)
    if spots_left >= 3:
        rail_yard_helper(arr, word + "g", spots_left - 3)
    if spots_left >= 4:
        rail_yard_helper(arr, word + "b", spots_left - 4)
    if spots_left == 0:
        arr.append(word)   

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
    solutions = []
    for i in range(1,9):
        part_codes_helper(solutions, n - 1, str(i))
    solutions = solutions[0: k]
    return solutions

def part_codes_helper(solutions: list[str], digitsleft: int, solution: str):
    if digitsleft == 0:
        solutions.append(solution)
        return
    num1 = int(solution[-1]) - 2
    num2 = int(solution[-1]) + 2
    if num1 >= 0:
        part_codes_helper(solutions, digitsleft - 1, solution + str(num1))
    if num2 <= 9:
        part_codes_helper(solutions, digitsleft - 1, solution + str(num2))
    
# Question 6
def race_against_bay(n: int, times: list[int]) -> int:
    mini = [2147483647]
    if not list:
        return 0
    race_against_bay_helper([], [], times, mini)
    return mini[0]

def race_against_bay_helper(a: list[int], b: list[int], left: list[int], mini: list[int]):
    if not left:
        solution = max(sum(a), sum(b))
        if solution < mini[0]:
            mini[0] = solution
    else:
        race_against_bay_helper(a + [left[-1]], b, left[:-1], mini)
        race_against_bay_helper(a, b + [left[-1]], left[:-1], mini)
