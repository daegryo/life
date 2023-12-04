import pygame
import copy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, 'green',
                                     (self.left + (self.cell_size * j), self.top + (self.cell_size * i),
                                      self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, 'white',
                                     (self.left + (self.cell_size * j), self.top + (self.cell_size * i),
                                      self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                x1 = self.left + (self.cell_size * j)
                x2 = self.cell_size + x1
                y1 = self.top + (self.cell_size * i)
                y2 = self.cell_size + y1
                if x1 <= mouse_pos[0] <= x2 and y1 <= mouse_pos[1] <= y2:
                    return (i, j)

    def on_click(self, cell_coords):
        if self.board[cell_coords[0]][cell_coords[1]] == 0:
            self.board[cell_coords[0]][cell_coords[1]] = 1
        else:
            self.board[cell_coords[0]][cell_coords[1]] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def next_move(self):
        cop = copy.deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    count = 0
                    for l in range(i - 1, i + 2):
                        for k in range(j - 1, j + 2):
                            try:
                                if cop[l][k] == 1:
                                    count += 1
                            except IndexError:
                                pass
                    if count == 3:
                        cop[i][j] = 1
                else:
                    count = 0
                    for l in range(i - 1, i + 2):
                        for k in range(j - 1, j + 2):
                            if l == i and k == j:
                                continue
                            try:
                                if cop[l][k] == 1:
                                    count += 1
                            except IndexError:
                                pass
                    if count < 2 or count > 3:
                        cop[i][j] = 0
        self.board = copy.deepcopy(cop)


board = Board(20, 20)
running = True
size = 600, 600
screen = pygame.display.set_mode(size)
life_on = -1
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            life_on *= -1

    screen.fill((0, 0, 0))
    if life_on == 1:
        board.next_move()
    board.render(screen)
    clock.tick(fps)
    pygame.display.flip()
