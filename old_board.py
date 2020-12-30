class oldBoard:
    import numpy
    def __init__(self, row, column, board, value):
        """Initializes all fields"""
        self.row = row
        self.column = column
        self.board = board
        self.value = value

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_board(self):
        return self.board

    def get_value(self):
        return self.value

