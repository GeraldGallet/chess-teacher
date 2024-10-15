import pygame
from config import cell_width, cell_height, special_line_weight, select_color, potential_target_color

class Cell:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.piece = None
    self.is_potential_target = False
    self.is_selected = False


  def is_empty(self):
    return self.piece == None
  
  def draw(self, screen):
    color = "white" if (self.x + self.y) % 2 == 0 else "black"
    margin = 0

    if self.is_selected:
      pygame.draw.rect(screen, select_color, (self.x * cell_width, self.y * cell_height, cell_width, cell_height))
      margin += special_line_weight
    elif self.is_potential_target:
      pygame.draw.rect(screen, potential_target_color, (self.x * cell_width, self.y * cell_height, cell_width, cell_height))
      margin += special_line_weight

    pygame.draw.rect(screen, color, (self.x * cell_width + margin, self.y * cell_height + margin , cell_width - margin * 2, cell_height - margin * 2))
    
    if (self.piece):
        self.piece.draw(screen, self)

  def set_as_potential_target(self):
    self.is_potential_target = True
  
  def unset_as_potential_target(self):
    self.is_potential_target = False
  
  def select(self):
    self.is_selected = True
  
  def unselect(self):
    self.is_selected = False
