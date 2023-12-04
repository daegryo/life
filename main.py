import pygame


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
                    pygame.draw.rect(screen, 'white',
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


board = Board(5, 7)
running = True
size = 600, 600
screen = pygame.display.set_mode(size)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
