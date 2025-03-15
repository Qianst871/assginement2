class game 
    def__init__(self):
       self.map = [[" ", " ", " "]],
                   [" ", " ", " "],
                   [" ", " ", " "]
                   ]
       self.player_position = [0, 0]
       self.current_room = None

  def move(self, direction):
      if direction == "up":
          if self.player_position[1] > 0:
              self.player_position[1] -= 1
      elif direction == "down":
          if self.player_position[1] < len(self.map) - 1:
              self.player_position[1] += 1
      elif direction == "left":
          if self.player_position[0] > 0:
              self.player_position[0] -= 1
      elif direction == "right":
          if self.player_position[0] < len(self.map[0]) - 1:
              self.player_position[0] += 1
      else:
          print("Invald move")
          return False
      self.current_room = self.map[self.player_position[1]][self.player_position[0]]
      return True

  def play(self):
      while True:
           print("Enter your move (up/down/left/right) or exit to quit")
           move = input()
           if move == "exist":
                break
           if self.move(move):
               print("You entered the next room!")
               print(self.current_room)
               if self.current_room == "exit":
                   print("You win!")
                   break
     

       