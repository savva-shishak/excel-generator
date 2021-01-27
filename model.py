from enum import Enum

class HorizontalAlignEnum(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3

class VerticalAlignEnum(Enum):
    TOP = 1
    CENTER = 2
    BOTTOM = 3

class MCell:
    value = None # str/number/date 
    background = None #str
    color = None # int (index)
    italic = None # bool

    border_top = None # bool
    border_left = None # bool
    border_bottom = None # bool
    border_right = None # bool

    horizontal_align = None # HorizontalAlignEnum 

    vertical_align = None # VerticalAlignEnum

    font_size = None # int
    font_famile = None # str
    font_bold = None # bool
    font_underline = None # str/None

    def __init__(self, cell=None):
        if cell is not None:
            self.value = cell.value

            self.color = cell.font.color.index

            self.italic = cell.font.italic

            self.font_size = cell.font.size
            self.font_bold = cell.font.bold
            self.font_underline = cell.font.underline
            # self.font_famile = ... Разобраться
            
            self.horizontal_align = cell.font.underline
            self.vertical_align = cell.font.vertAlign





class MMergeredCell:
    parentCol = None # int
    parentRow = None # int
