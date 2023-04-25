import os


def clear_screen():
    return os.system('CLS')

def convert_letter_to_str(y):
    CONVERTER = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9
        }
    return CONVERTER[y]


class SeaBattle:
    def __init__(self, size):
        self.size = size
        self.grid = [['_|' for _ in range(size)] for _ in range(size)]
        self.ships = []
        
    def __str__(self):
        header = '  ' + ' '.join([chr(i + 65) for i in range(self.size)])
        rows = [
                f"{i} {''.join([str(cell) for cell in row])}" \
                for i, row in enumerate(self.grid)
                ]
        return header + '\n' + '\n'.join(rows)
        
    def place_ship(self, x, y):
        self.grid[x][y] = '1|'
        
    def is_ship(self, x, y):
        return self.grid[x][y] == '1|'
        
    def is_hit(self, x, y):
        return self.grid[x][y] == 'X|'
        
    def mark_hit(self, x, y):
        self.grid[x][y] = 'X|'
        
    def is_miss(self, x, y):
        return self.grid[x][y] == 'o|'
        
    def mark_miss(self, x, y):
        self.grid[x][y] = 'o|'

    def check_near_ship(self, x, j):
        if self.is_ship(x+1, j) or \
              self.is_ship(x+1, j+1) or \
              self.is_ship(x+1, j-1) or \
              self.is_ship(x, j+1) or \
              self.is_ship(x-1, j) or \
              self.is_ship(x-1, j-1) or \
              self.is_ship(x-1, j+1) or \
              self.is_ship(x, j-1):
            return True
            
    def validation_place_ship_vertical(self, ships_sizes, size, y, x):
        if x + size > self.size:
            clear_screen()
            print("Корабль выходит за границы поля. Попробуйте еще раз.")
        for i in range(x, x+size):
            if self.is_ship(i, y):
                clear_screen()
                print("Корабль пересекается с другим кораблем. Попробуйте еще раз.")
                break
            elif self.check_near_ship(x, y) == True:
                clear_screen()
                print("Корабль в пределах другого корабля. Попробуйте еще раз.")
                break
        else:
            return True

    def validation_place_ship_horizontal(self, ships_sizes, size, y, x):
        if y + size > self.size:
            clear_screen()
            print("Корабль выходит за границы поля. Попробуйте еще раз.")
        for j in range(y, y+size):
            if self.is_ship(x, j):
                clear_screen()
                print("Корабль пересекается с другим кораблем. Попробуйте еще раз.")
                break
            elif self.check_near_ship(x, j) == True:
                clear_screen()
                print("Корабль в пределах другого корабля. Попробуйте еще раз.")
                break
        else:
            return True

    def setup_board(self):
        ships_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        clear_screen()
        for size in ships_sizes:
            while True:
                print(self)
                print(f"Корабль размером {size}")
                y = convert_letter_to_str(
                      input('Введите столбец(A-J): ').upper()
                    )
                x = int(input('Введите строку(0-9): '))
                orientation = input("Введите ориентацию (vertical / horizontal): ")
                if orientation == 'v':
                    if self.validation_place_ship_vertical(self, size, y, x) == True:
                        for i in range(x, x+size):
                            clear_screen()
                            self.place_ship(i, y)
                            self.ships.append((x, y, size, orientation))
                        break
                elif orientation == 'h':
                    if self.validation_place_ship_horizontal(self, size, y, x) == True:
                        for j in range(y, y+size):
                            clear_screen()
                            self.place_ship(x, j)
                            self.ships.append((x, y, size, orientation))
                        break
                else:
                    clear_screen()
                    print("Выбрано неверное направление")
                  



game = SeaBattle(10)
game.setup_board()
game2 = SeaBattle(10)
game2.setup_board()
# print(game.is_hit(2, 3)) 
# print(game.is_miss(5, 5)) 

print(game)
print(game2)

#убираем корабли с поля, но знаем их данные. Делаем бесконечный цикл на то чтобы выводить поля 1 и 2 добавляя к ним импут
#если импут == корабль, то выводим хит, если нет то мисс. если хит==тру, то стреляем дальше. while true(пока кто-то не выбьет все корабли)