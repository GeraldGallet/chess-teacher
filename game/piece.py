import pygame
from config import cell_width, cell_height, select_color, potential_target_color

class PotentialMove:
  def __init__(self, x, y, needs_target):
    self.x = x
    self.y = y
    self.needs_target = needs_target

class Piece:
  def __init__(self, color):
    self.color = color

class Pawn(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "Pawn"
    self.potential_moves = [
      PotentialMove(0, 1, False),
      PotentialMove(0, 2, False),
      PotentialMove(1, 1, True),
      PotentialMove(-1, 1, True)
    ]

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"
  
  def draw(self, screen, cell):
    pygame.draw.rect(screen, "red", (cell.x * cell_width + 10, cell.y * cell_height + 10, cell_width - 20, cell_height - 20))

class King(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "King"

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"
  
class Queen(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "Queen"

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"
  
class Bishop(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "Bishop"

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"
  
class Tower(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "Tower"

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"
  
class Knight(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.name = "Pawn"

  def __str__(self):
    return f"{self.color} {self.name} at {self.posX}, {self.posY}"