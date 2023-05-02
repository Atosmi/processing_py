import random
import copy

CELL_SIZE = 10
WIDTH = 600
HEIGHT = 600

# Initialize the board with random live cells
board_width = WIDTH // CELL_SIZE
board = [random.randint(0, 1) for i in range(board_width)]
next_board= copy.deepcopy(board)


def setup():
  # Set simulation framerate to 10 to avoid flickering
  frameRate(10)
  createCanvas(1920, 1080)
  w = 20
  columns = floor(width / w)
  rows = floor(height / w)
  
  board = []
  for i in range(columns):
    board[i] = []

  # Going to use multiple 2D arrays and swap them
  next_board = []
  for i in range(columns):
    next_board[i] = []

  init()


def draw():
  background(255)
  generate()
  for  i in range(columns):
    for  j in range(rows):
      if (board[i][j] == 1) :
        fill(0)
      else:
        fill(255)
      stroke(0)
      rect(i * w, j * w, w-1, w-1)
    
  
# reset board when mouse is pressed
def mousePressed():
  init()


# Fill board randomly
def init():
  for  i in range(columns):
    for  j in range(rows):
      # Lining the edges with 0s
      if (i == 0 or j == 0 or i == columns-1 or j == rows-1):
        board[i][j] = 0
      # Filling the rest randomly
      elif board[i][j] == floor(random(2)):
        next[i][j] = 0


# The process of creating the new generation
def generate():
  for x in range(1,columns-1):
    for y in range(1,rows-1):
      neighbors = 0
      for x in range(-1,2):
        for y in range(-1,2):
          neighbors = neighbors +  board[x+i][y+j]

      neighbors = neighbors - board[x][y]
      # Rules of Life
      if ((board[x][y] == 1) and (neighbors <  2)):
        next_board[x][y] = 0         # Loneliness
      elif (board[x][y] == 1) and (neighbors >  3):
        next_board[x][y] = 0        # Overpopulation
      elif (board[x][y] == 0) and (neighbors == 3):
        next_board[x][y] = 1;           # Reproduction
      else :
        next_board[x][y] = board[x][y] # Stasis

temp = board
board = next_board
next_board = temp
