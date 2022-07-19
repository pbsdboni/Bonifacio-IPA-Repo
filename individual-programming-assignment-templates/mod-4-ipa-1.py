'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if to_member not in social_graph:
        if to_member in social_graph[from_member]["following"]:
            return "follower"
        else:
            return "no relationship"
        
    elif to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            return "friends"
        else:
            return "follower"
        
    else:
        if from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # diagonal 1 is up-left to down-right
    # diagonal 2 is down-left to up-right
    
    by = len(board)
    horz = [x for x in board]
    vert = [x for x in zip(*board)]
    diagonal1 = [board[i][i] for i in range(by)]
    diagonal2 = [board[by-1-i][i] for i in range(by)]
      
    if by == 3:
        if ['O','O','O'] in horz:
            return 'O'
        elif ['X','X','X'] in horz:
            return 'X'
        else:
            if ('O','O','O') in vert:
                return 'O'
            elif ('X','X','X') in vert:
                return 'X'
            else:
                if diagonal1 == ['O','O','O']:
                    return 'O'
                elif diagonal1 == ['X','X','X']:
                    return 'X'
                else:
                    if diagonal2 == ['O','O','O']:
                        return 'O'
                    elif diagonal2 == ['X','X','X']:
                        return 'X'
                    else:
                        return 'NO WINNER'                  
   
    elif by == 4:
        if ['O','O','O','O'] in horz:
            return 'O'
        elif ['X','X','X','X'] in horz:
            return 'X'
        else:
            if ('O','O','O','O') in vert:
                return 'O'
            elif ('X','X','X','X') in vert:
                return 'X'
            else:
                if diagonal1 == ['O','O','O','O']:
                    return 'O'
                elif diagonal1 == ['X','X','X','X']:
                    return 'X'
                else:
                    if diagonal2 == ['O','O','O','O']:
                        return 'O'
                    elif diagonal2 == ['X','X','X','X']:
                        return 'X'
                    else:
                        return 'NO WINNER'
    
    elif by == 5:
        if ['O','O','O','O','O'] in horz:
            return 'O'
        elif ['X','X','X','X','X'] in horz:
            return 'X'
        else:
            if ('O','O','O','O','O') in vert:
                return 'O'
            elif ('X','X','X','X','X') in vert:
                return 'X'
            else:
                if diagonal1 == ['O','O','O','O','O']:
                    return 'O'
                elif diagonal1 == ['X','X','X','X','X']:
                    return 'X'
                else:
                    if diagonal2 == ['O','O','O','O','O']:
                        return 'O'
                    elif diagonal2 == ['X','X','X','X','X']:
                        return 'X'
                    else:
                        return 'NO WINNER'
    
    elif by == 6:
        if ['O','O','O','O','O','O'] in horz:
            return 'O'
        elif ['X','X','X','X','X','X'] in horz:
            return 'X'
        else:
            if ('O','O','O','O','O','O') in vert:
                return 'O'
            elif ('X','X','X','X','X','X') in vert:
                return 'X'
            else:
                if diagonal1 == ['O','O','O','O','O','O']:
                    return 'O'
                elif diagonal1 == ['X','X','X','X','X','X']:
                    return 'X'
                else:
                    if diagonal2 == ['O','O','O','O','O','O']:
                        return 'O'
                    elif diagonal2 == ['X','X','X','X','X','X']:
                        return 'X'
                    else:
                        return 'NO WINNER'
    
    
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    arrive = 0
    leave = 0
    minutes = 0
    
    legs = len(route_map)
    stop = list(route_map.keys())
    
    for x in range(legs):
        if first_stop == stop[x][0]:
            arrive = x
            
    for x in range(legs):
        if second_stop == stop[x][1]:
            leave = x
    
    if arrive <= leave:
        for y in range(legs):
            if y >= arrive and y <= leave:
                if (arrive < leave or arrive == leave):
                    new_dict = route_map[stop[y]]
                    minutes += new_dict['travel_time_mins']
                    
    if arrive > leave:
        for z in range(legs):
            if z <= leave or z >= arrive:
                new_dict = route_map[stop[z]]
                minutes += new_dict['travel_time_mins']
                
    return(minutes)
