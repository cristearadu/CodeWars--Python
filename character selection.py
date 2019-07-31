fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
#opts = ["up","down","right","left"]
initial_position = (0,0)
moves = ['up', 'left', 'right', 'left', 'left']

def street_fighter_selection(fighters, initial_position, moves):
    chars_list = []
    cursor = initial_position
    for move in moves:

        #Y - AXIS
        #up check
        if move == 'up':
            if cursor[0] == 0:
                chars_list.append(fighters[cursor[0]][cursor[1]])
            elif cursor[0] == 1:
                cursor = (0,cursor[1])
                chars_list.append(fighters[cursor[0]][cursor[1]])
        #down check
        elif move == 'down':
            if cursor[0] == 0:
                cursor = (1,cursor[1])
                chars_list.append(fighters[cursor[0]][cursor[1]])
            elif cursor[0] == 1:
                chars_list.append(fighters[cursor[0]][cursor[1]])

        #X - AXIS
        #left check
        elif move == 'left':
            if cursor[1] == 0:
                cursor = (cursor[0], 5)
                chars_list.append(fighters[cursor[0]][cursor[1]])
            elif cursor[1] > 0 and cursor[1] <= 5:
                cursor = (cursor[0],cursor[1]-1)
                chars_list.append(fighters[cursor[0]][cursor[1]])

        elif move == 'right':
            if cursor[1] == 5:
                cursor = (cursor[0],0)
                chars_list.append(fighters[cursor[0]][cursor[1]])
            elif cursor[1] >= 0 and cursor[1] <5:
                cursor = (cursor[0],cursor[1]+1)
                chars_list.append(fighters[cursor[0]][cursor[1]])

    return chars_list

moves = ["up","left","down","right"]*2
print(street_fighter_selection(fighters,initial_position,moves))

moves = ['up','left', 'right', 'left', 'left']
moves =  ["left"]*8
moves =  ["down"]*4

#########################################

MOVES = {"up":(-1,0),
         "down":(1,0),
         "right":(0,1),
         "left":(0,-1)
         }
def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dx, dy = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])

        hovered_fighters.append(fighters[y][x])
    return hovered_fighters
moves = ["up","left","down","right"]*2
print(street_fighter_selection(fighters,initial_position,moves))