import os
from typing import Tuple, List


class InputValidator:
    COLUMN_NAME_TO_INDEX = {
             'a': 0,
             'b': 1,
             'c': 2,
             'd': 3,
             'e': 4,
             'f': 5,
             'g': 6,
             'h': 7,
             'i': 8,
             'j': 9
    }
    def __init__(self) -> None:
        pass
    
    def validate_column(self, column: str):
        return column in self.COLUMN_NAME_TO_INDEX.keys()
    
    def validate_row(self, row: int):
        return row in range(0, 10)


class InputProccesor:
    
    def __init__(self) -> None:
        self.input_validator = InputValidator()

    def get_ship_cordinates_and_direction(self) -> Tuple[int, int, str]:
        column: str = self.input_column()
        row: int = self.input_row()
        orientation = self.get_choice_input(
            "Введите ориентацию (vertical / horizontal): ",
            (
              "v",
              "h",
              "vertical",
              "horizontal"
            )
        )
        return column, row, orientation
    
    def get_shoot_cordinates(self):
        column: str = self.input_column()
        row: int = self.input_row()
        return column, row

    def input_column(self) -> int:
        column: str = self.get_string_input_lower('Введите столбец(A-J): ')
        while not self.input_validator.validate_column(column):
            column: str = self.get_string_input_lower('Введите столбец(A-J): ')
        return self.convert_column_letter_to_index(column)

    def input_row(self) -> int:
        row: int = self.get_int_input('Введите строку(0-9): ')
        while not self.input_validator.validate_row(row):
            row: int = self.get_int_input('Введите строку(0-9): ')
        return row

    def get_string_input_lower(self, message: str):
        return input(message).lower()

    def get_int_input(self, message: str):
        user_input: str = input(message)
        if not user_input.isdigit():
            user_input = self.get_int_input(message)
        return int(user_input)

    def get_choice_input(self, message: str, choices: Tuple[str]):
        user_input: str = self.get_string_input_lower(message)
        if not user_input in choices:
            user_input = self.get_choice_input(message, choices)
        return user_input
    
    def convert_column_letter_to_index(self, column: str) -> int:
        return self.input_validator.COLUMN_NAME_TO_INDEX.get(column)





class Cell:
    
    def __init__(self, *, column_index: int, row_index: int) -> None:
        self.ship_placed: bool = False
        self.is_damaged: bool = False
        self.is_miss: bool = False
        self.column_index: int = column_index
        self.row_index: int = row_index

    def __repr__(self) -> str:
        return f"row: {self.row_index}, col: {self.column_index}"
    
    def shoot(self):
        if self.ship_placed:
            self.is_damaged = True
            return True
        if not self.ship_placed:
            self.is_miss = True
            return False


class OutputProccesor:
    
    def __init__(self, size) -> None:
        self.size = size

    def display_board(self, board, hide_ships = False):
        header = self.get_header()
        rows = [header]
        for index, row in enumerate(board.grid):
            rows.append(self.get_row_display(index, row, hide_ships))
        print("\n".join(rows))
        
        
    def get_row_display(self, index, row, hide_ships):
        cells = [str(index)]
        cells.extend([self.get_cell_display(cell, hide_ships) for cell in row])
        return " ".join(cells)
    
    def get_cell_display(self, cell: Cell, hide_ships):
        if cell.ship_placed and not cell.is_damaged and hide_ships:
            return "_|"
        if not cell.ship_placed and not cell.is_miss:
            return "_|"
        if cell.ship_placed and cell.is_damaged:
            return "X|"
        if cell.ship_placed and not cell.is_damaged:
            return "1|"
        return "0|"

    def get_header(self):
        return '  ' + '  '.join([chr(i + 65) for i in range(self.size)]) 

    def clear_screen(self):
        os.system("CLS") 

class Ship:
    
    def __init__(self, cells: List[Cell]) -> None:
        self.cells = cells

    def is_destroyed(self):
        return all([cell.is_damaged for cell in self.cells])

    def is_damaged(self):
        return any([cell.is_damaged for cell in self.cells])

    def get_size(self):
        return len(self.cells)


class Board:
    
    def __init__(self, size):
        self.size: int = size
        self.grid = []
        self.ships: List[Ship] = []
        for row_index in range(size):
            row = []
            for column_index in range(size):
                row.append(Cell(row_index=row_index, column_index=column_index))
            self.grid.append(row)

    def check_possibility_placing_ship(self, start_column, end_column, start_row, end_row) -> bool:
        if end_column >= self.size or end_row >= self.size:
            return False
        start_column = start_column - 1 if start_column > 0 else start_column
        start_row = start_row - 1 if start_row > 0 else start_row
        end_column = end_column + 1 if end_column <= 9 else end_column
        end_row = end_row + 1 if end_row <= 9 else end_row
        cells = self.get_cells(start_column, end_column, start_row, end_row)
        return all ([not cell.ship_placed for cell in cells])
        
    def get_ship_start_end_indexes(self, start_column, start_row, orientation, size):
        end_column = start_column
        end_row = start_row
        if orientation in ("v", "vertical"):
            end_row += size -1
        if orientation in ("h", "horizontal"):
            end_column += size -1
        return start_column, end_column, start_row, end_row

    def get_cells(self, start_column, end_column, start_row, end_row) -> List[Cell]:
        cells = []
        for row in self.grid[start_row:end_row + 1]:
            cells.extend(row[start_column:end_column +1])
        return cells

    def place_ship(self, start_column, end_column, start_row, end_row):
        cells = self.get_cells(start_column, end_column, start_row, end_row)
        self.ships.append(Ship(cells))
        for cell in cells:
            cell.ship_placed = True

    def shoot(self, column, row):
        cell = self.grid[row][column]
        return cell.shoot()


class Player:
    
    def __init__(self, board: Board) -> None:
        self.board = board

    def is_live(self) -> bool:
        return any ([not ship.is_destroyed() for ship in self.board.ships])


class Game:
    
    BOARD_SIZE = 10
    SHIP_SIZES = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)

    def __init__(self) -> None:
        self.players = [Player(board=Board(self.BOARD_SIZE)) for _ in range(2)]
        self.input_proccesor = InputProccesor()
        self.output_proccesor = OutputProccesor(self.BOARD_SIZE)

    def fill_board(self, player):
        for ship_size in self.SHIP_SIZES:
            print(f"Разместите корабль размером {ship_size}")
            column, row, orientation = self.input_proccesor.get_ship_cordinates_and_direction()
            start_column, end_column, start_row, end_row = player.board.get_ship_start_end_indexes(column, row, orientation, ship_size)
            while not player.board.check_possibility_placing_ship(start_column, end_column, start_row, end_row):
                column, row, orientation = self.input_proccesor.get_ship_cordinates_and_direction()
                start_column, end_column, start_row, end_row = player.board.get_ship_start_end_indexes(column, row, orientation, ship_size)
            player.board.place_ship(start_column, end_column, start_row, end_row)
            self.output_proccesor.display_board(player.board)

    def run(self):
        self.output_proccesor.clear_screen()
        for index, player in enumerate(self.players):
            print(f"Игрок {index+1} заполняет поле: ")
            self.output_proccesor.display_board(player.board)
            self.fill_board(player=player)
            self.output_proccesor.clear_screen()
        round_number = 1
        while all ([player.is_live() for player in self.players]):
            if round_number % 2 == 0:
                player_index = 1
                hitting = self.process_step(player_index)
                if hitting:
                    continue
                input("Нажмите Enter to continue")
            else:
                player_index = 0
                hitting = self.process_step(player_index)
                if hitting:
                    continue
                input("Нажмите Enter to continue")
            round_number += 1

    def process_step(self, player_index):
        self.output_proccesor.clear_screen()
        print(f"Игрок {player_index + 1} стреляет")
        self.output_proccesor.display_board(self.players[player_index].board, True)
        hitting = self.shoot(self.players[player_index])
        if hitting:
            self.output_proccesor.display_board(self.players[player_index].board, True)
        return hitting
            
    def shoot(self, player):
        column, row = self.input_proccesor.get_shoot_cordinates()
        return player.board.shoot(column, row)


if __name__ == "__main__":
    game = Game()
    game.run()
    print("TY for game")