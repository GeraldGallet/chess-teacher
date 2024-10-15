from config import number_of_cells
from cell import Cell
from piece import Pawn

class Board:
  def __init__(self, screen):
    self.screen = screen
    self.selected_cell = None

    self.cells = []
    for i in range(number_of_cells):
        self.cells.append([])
        for j in range(number_of_cells):
            self.cells[i].append(Cell(i, j))
            self.cells[i][j].draw(screen)

    self.cells[0][0].piece = Pawn("White")
    self.current_selected_cell = None
    self.current_potential_targets = []

  def draw(self):
    for i in range(number_of_cells):
        for j in range(number_of_cells):
            self.cells[i][j].draw(self.screen)

  def move_piece(self, src_x, src_y, dest_x, dest_y):
      self.cells[dest_x][dest_y].piece = self.cells[src_x][src_y].piece
      self.cells[src_x][src_y].piece = None

  def reset_selection(self):
    self.current_selected_cell.unselect()
    for cell in self.current_selected_cell:
      cell.unset_as_potential_target()

  def select_piece(self, x, y):
    target_cell = self.cells[x][y]

    if target_cell.is_empty():
      if self.current_selected_cell != None:
        self.current_selected_cell.unselect()
        self.current_selected_cell = None
      return
    
    if self.selected_cell == None:      
      self.current_selected_cell = target_cell
      self.current_selected_cell.select()

    # is_target_empty = target_cell.is_empty()

    # if (target.is_empty()):
    #   self.reset_selection()
    #   return
    
    # is_target_potential_target = self.cells[x][y].is_potential_target

    # if self.cells[x][y].is_selected or (is_target_empty and not(is_target_potential_target)):
    #    self.reset_selection()
    #    return
    
    # if is_target_empty and is_target_potential_target:
    #    self.move_piece(self.selected_cell.x, self.selected_cell.y, x, y)
    #    self.reset_selection()
    #    return
    
    # for i in range(number_of_cells):
    #   for j in range(number_of_cells):
    #     if i == x and j == y and not(self.cells[i][j].is_empty()):
    #       self.cells[i][j].select()
    #       self.selected_cell = self.cells[i][j]
    #       moves = self.cells[i][j].piece.potential_moves

    #       for move in moves:
    #         if move.x + i < 0 or move.x + i >= number_of_cells or move.y + j < 0 or move.y + j >= number_of_cells:
    #             continue

    #         target_cell = self.cells[i + move.x][j + move.y]

    #         if move.needs_target and not(target_cell.is_empty()):
    #             target_cell.set_as_potential_target()

    #         if not(move.needs_target) and target_cell.is_empty():
    #             target_cell.set_as_potential_target()
    #     else:
    #       self.cells[i][j].unselect()
