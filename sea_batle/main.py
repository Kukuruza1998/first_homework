import os


class SeaBattle:
    def __init__(self, size):
        self.size = size
        self.grid = [['_|' for _ in range(size)] for _ in range(size)]
        self.ships = []
        
    def __str__(self):
        header = '  ' + ' '.join([str(i) for i in range(self.size)])
        rows = [f"{i} {''.join([str(cell) for cell in row])}" \
                for i, row in enumerate(self.grid)]
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
    
    def setup_board(self):
      ships_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
      clear_screen()
      for size in ships_sizes:
          while True:
              
              print(self)
              print(f"Корабль размером {size}")
              x = int(input('Введите строку: '))
              y = int(input('Введите столбец: '))
              orientation = input("Введите ориентацию (vertical / horizontal): ")
              if orientation == 'v':
                    if x + size > self.size:
                        clear_screen()
                        print("Корабль выходит за границы поля. Попробуйте еще раз.")
                        continue
                    for i in range(x, x+size):
                        if self.is_ship(i, y):
                            clear_screen()
                            print("Корабль пересекается с другим кораблем. Попробуйте еще раз.")
                            break
                    else:
                        for i in range(x, x+size):
                            clear_screen()
                            self.place_ship(i, y)
                        self.ships.append((x, y, size, orientation))
                        break
                
              elif orientation == 'h':
                    if y + size > self.size:
                        print("Корабль выходит за границы поля. Попробуйте еще раз.")
                        continue
                    for j in range(y, y+size):
                        if self.is_ship(x, j):
                            print("Корабль пересекается с другим кораблем. Попробуйте еще раз.")
                            break
                        elif self.is_ship(x+1, j) or \
                              self.is_ship(x+1, j+1) or \
                                self.is_ship(x+1, j-1) or \
                                  self.is_ship(x, j+1) or \
                                    self.is_ship(x-1, j) or \
                                      self.is_ship(x-1, j-1) or \
                                        self.is_ship(x-1, j+1) or \
                                          self.is_ship(x, j-1):
                            print("Корабль в пределах другого корабля. Попробуйте еще раз.")
                            break
                    else:
                        for j in range(y, y+size):
                            self.place_ship(x, j)
                        self.ships.append((x, y, size, orientation))
                        break

def clear_screen():
    return os.system('CLS')

game = SeaBattle(10)
game.setup_board()
print(game.is_hit(2, 3)) # проверяем на хит
print(game.is_miss(5, 5)) # на промах