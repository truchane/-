import sqlite3
import datetime

correlation_db = '__HOME__/final_project/database.db'  # raw gesture data for correlation purposes
game_db = '__HOME__/final_project/game_database.db'  # contains game gestures table and game state table

# STARTING PLAYER HEALTH
health_1 = 5
health_2 = 5


def request_handler(request):
    ########## constants #############
    now = datetime.datetime.now()
<<<<<<< HEAD
    ## extracting data from post or get request##
    method = request["method"]
    # player action
    action = int(request["action"])
    # player ID
    player_ID = str(request["player_ID"])
    # game ID
    game_ID = int(request["game_ID"])
    ###################################

    ############## CONNECTING TO THE RIGHT DB ####################


if action == 0:
    conn = sqlite3.connect(correlation_db)  # connect to that database (will create if it doesn't already exist)
c = conn.cursor()
else:
conn = sqlite3.connect(game_db)  # connect to that database (will create if it doesn't already exist)
conn.row_factory = sqlite3.Row
c = conn.cursor()
##################################

if method == "POST":
## try to create table:
try:
    if action == 0:
        c.execute(
            '''CREATE TABLE raw_data_table (username text, timing timestamp, gestureID real, raw_data text);''')  # run a CREATE TABLE command
    else:
    # GESTURES TABLE
    c.execute(
        '''CREATE TABLE gestures_table (game_ID integer, player_ID text, action integer, timing timestamp, checked integer);''')
    # GAME TABLE
    c.execute(
        '''CREATE TABLE game_table (game_ID integer primary key autoincrement, player_1 text, health_1 integer, player_2 text, health_2 integer, game_state text);''')
## if already created, move to except
except:
    pass

if action == 0:  # CORRELATION
    ## get data from the body of the code #####
    data = form["data"]
    username = form["username"]
    gestureID = int(form["gestureID"])

else:
    ################# GET REQUEST ##############
    if action == 1:
        return "ERROR: this should be a get request!"
    ##############    Actions ##################
    elif action in {2, 3, 4}:  ## SLASH(2), PUSH(3) , BLOCK(4)
        ### updates gestures Table with new values ###
        add_action(game_ID, player_ID, action, now, 0)

        ### get game information using game_ID ###
        game_info_dict = extract_game_info(game_ID)
        #         EXTRACTING INFO  #

        game_state = game_info_dict["state"]  # dictionary mapping item from game table
        player_1 = game_info_dict["player_1"]
        health_1 = game_info_dict["health_1"]
        player_2 = game_info_dict["player_2"]
        health_2 = game_info_dict["health_2"]
        #####            end extraction               ####

        ## extract relevant gestures from gestures table
        player_gestures = extract_player_gestures(player_1,
                                                  player_2)  ### creates a dictionary mapping player id to gesture
        action_1 = player_gestures[player_1]
        action_2 = player_gestures[player_2]

        ## calculate score
        Score = health_update(health_1, health_2, action_1, action_2)
        health_1 = Score[0]
        health_2 = Score[1]

        ## change state = 2 (completed) when health of one person goes below 0
        if health_1 <= 0 or health_2 <= 0:
            game_state = 2

        ## update the game table
        update_game_info(game_ID, player_1, health_1, player_2, health_2, game_state)

        if player_ID == player_1:
            return "health_1,game_state,

        elif player_ID == player_2:

    """elif action == 2 : #SLASH
    elif action == 3: #PUSH
    elif action == 4: #BLOCK
    elif action == 5: #CHARGE"""

    return "ERROR: Murd shut up: this never reaches the server"
elif action == 6:  # IR_SEND
# FRANKLIN
elif action == 7:  # IR_RECEIVE
# FRANKLIN

send
stuff
to
2
elif method = "GET":
## SHANA ##

def add_action(game_ID, player_ID, action_ID, time=now, check=0):
    # Franklin
    """
    Function that updates the table: gestures table with the corresponding inputs and
    AKA add gestures to the gesture table
      returns nothing.
    """
    pass


def update_game_info(game_ID, player_1, health_1, player_2, health_2, state):
    # Franklin
    """
    Goes into the game table and will UPDATE (not make a new row) that row with these values.
    Returns game state.
    """
    pass


def extract_game_info(game_ID):
    # DONE #
    """
    Takes in the game_ID and goes into the Game Table. 
    Returns the most recent row containing the game_ID 
    as a dictionary of the game information. 
    """
    c.execute('''SELECT * FROM game_table WHERE game_ID = ?;''', (game_ID,))
    results = c.fetchone()
    return results


def extract_player_gestures(player_1, player_2):
    # BOOF NOT DONE
    """
    Looks at gesture database and finds the two most recent rows
    where one is player_1 and one is player_2. The timestamp of the rows
    must be within one second and checked for both must equal 0. If one 
    of the two rows has an action that is not block, change the check 
    value in that database row to 1. If they're not, one of the players 
    is None. Returns a dictionary of the player name and their action. 
    """
    recent_player_1 = c.execute('''SELECT * FROM gesture_table WHERE player_ID = player_1 ORDER BY timing ASC;''')
    time_delta_1 = recent_player_1['timing'] - datetime.timedelta(seconds=1)


time_delta_2 = recent_player_2['timing'] + datetime.timedelta(seconds=1)
try:
    recent_player_2 = c.execute('''SELECT * FROM gesture_table WHERE player_ID = player_2 ORDER BY timing ASC;''')


def check_game_start():
    # DONE#
    """
    Looks at gesture database and finds the last time itself sent action 6.
    Checks everything after that row and sees if it finds action 7. If it 
    finds it, returns True. Otherwise, returns False. 
    """
    last_6_time = c.execute(
        '''SELECT timing FROM game_table WHERE (action = 6 AND checked = 0) ORDER BY timing ASC LIMIT 1;''').fetchone()
    last_7_time = c.execute(
        '''SELECT timing FROM game_table WHERE (action = 7 AND checked = 0) ORDER BY timing ASC LIMIT 1;''').fetchone()
    return last_6_time < last_7_time


def start_game():
    # BOOF
    """
    Goes into game table and finds the last entry. Returns a list of that game_ID 
      and the other player's name.
    """
    last_entry = c.execute('''SELECT * FROM game_table ORDER BY timing ASC;''').fetchone()
    game_ID = last_entry['game_ID']
    if last_entry['player_1'] == player_ID:
        other_player = last_entry['player_2']
    else:
        other_player = last_entry['player_1']
    return [game_ID, other_player]


def health_update(cur_health_1, cur_health_2, action_1, action_2):
=======
    if request["method"] == "POST": #puts encrypted response in database
        form = request["form"]
        try:
            action = int(form["action"])
            if action == 0:
                data = form["data"]
                username = form["username"]
                gestureID = int(form["gestureID"])

                conn = sqlite3.connect(db)  # connect to that database (will create if it doesn't already exist)
                c = conn.cursor()  # make cursor into database (allows us to execute commands)
            elif action == 1:
                user1 = form["user1"]
                user2 = form["user2"]

                conn = sqlite3.connect(game_db)  # connect to that database (will create if it doesn't already exist)
                c = conn.cursor()  # make cursor into database (allows us to execute commands)
            elif action == 2:
                user = form["user"]
                data = form["data"]

                conn = sqlite3.connect(game_db)  # connect to that database (will create if it doesn't already exist)
                c = conn.cursor()  # make cursor into database (allows us to execute commands)

        except Exception:
            return "-1"

        try:
            if action == 0:
                c.execute('''CREATE TABLE raw_data_table (username text, timing timestamp, gestureID real, raw_data text);''')  # run a CREATE TABLE command
            elif action == 1:
                c.execute('''CREATE TABLE game_stats_table (gameID integer primary key autoincrement, user1 text, user2 text, user1Score integer, user2Score integer, game_status text, start_time timestamp);''')  # run a CREATE TABLE command
            elif action == 2:
                c.execute('''CREATE TABLE game_gestures_table (gameID integer primary key, user, gestureID real, time timestamp);''')  # run a CREATE TABLE command
        except:
            pass

        if action == 0:
            c.execute('''INSERT into raw_data_table VALUES (?,?,?,?);''', (username, now, gestureID, data))
        elif action == 1:
            c.execute('''INSERT into game_stats_table VALUES (?,?,?,?,?,?);''', (user1, user2, 0, 0, 'ongoing', now))
        elif action == 2:
            gestureID = analyze_gesture(data)
            gameID = c.execute('''SELECT gameID FROM game_stats_table WHERE game_status = 'ongoing' AND (user1 = ? OR user2 = ?);''', (user,)).fetchone()[0] #check if returns right data type
            c.execute('''INSERT into game_gestures_table VALUES (?,?,?,?);''', (gameID, user, gestureID, now))
        conn.commit()  # commit commands
        conn.close()  # close connection to database
        return data

    elif request['method'] == 'GET': #is a GET request

        args = request["args"]
        if 'table' not in args:
            return '-1'

        try:
            table = int(request["values"]['table'])

        except Exception:
            return '-1'

        all = []
        #twenty_seconds_ago = timestamp - datetime.timedelta(seconds=20)  # create time for 20 seconds ago!
        things = c.execute('''SELECT * FROM ?;''', (table,)).fetchall()
        for x in things:
            all.append(x[0])

        return str(all)

def health_update(cur_health_1,cur_health_2,action_1,action_2):
    """
    Takes in the current healths of both players and the last action each of them made.
    Returns the updated healths of both players.
    """
    #Both None
    if action_1 == None and action_2 == None:
        return [cur_health_1,cur_health_2]
    #One slash and one None
    if action_1 == 2 and action_2 == None:
        return [cur_health_1,cur_health_2-1]
    if action_1 == None and action_2 == 2:
        return [cur_health_1-1,cur_health_2]
    #One push and one None
    if action_1 == 3 and action_2 == None:
        if cur_health_2 > 1:
            return [cur_health_1,cur_health_2-2]
        else:
            return [cur_health_1,0]
    if action_1 == None and action_2 == 3:
        if cur_health_1 > 1:
            return [cur_health_1-2,cur_health_2]
        else:
            return [0,cur_health_2]
    #Any block
    if (action_1 == 2 and action_2 == 4) or (action_1 == 4 and action_2 == 2) or (action_1 == 3 and action_2 == 4) or (action_1 == 4 and action_2 == 3) or (action_1 == 4 and action_2 == 4):
        return [cur_health_1,cur_health_2]
    #one slash and one slash
    if action_1 == 2 and action_2 == 2:
        return [cur_health_1-1,cur_health_2-1]
    #one push and one push
    if action_1 == 3 and action_2 == 3:
        if cur_health_1 > 1 and cur_health_2 > 1:
            return [cur_health_1-2,cur_health_2-2]
        elif cur_health_1 > 1:
            return [cur_health_1-2,0]
        elif cur_health_2 > 1:
            return [0,cur_health_2-2]
        else:
            return [0,0]