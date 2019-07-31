#https://www.codewars.com/kata/street-fighter-2-character-selection-part-2/train/python
#TODO

fighters = [
	[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],
	[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],
	[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]
]

position = (0,0)

MOVES = {"up" : (-1,0),
          "down" : (1, 0),
          "left" : (0,-1),
          "right" : (0,1)
            }
def super_street_fighter_selection(fighters, position, moves):
  y, x = position
  hovered_fighters = []
  for move in moves:
      dy, dx = MOVES[move]
      y += dy
      if not 0 <= y < len(fighters):
          y -= dy
      x = (x + dx) % len(fighters[y])
      if fighters[y][x] != '':
          hovered_fighters.append(fighters[y][x])
  return hovered_fighters


#moves =  ["right","up"]
moves =  ["right"]*8
print(super_street_fighter_selection(fighters,position,moves))