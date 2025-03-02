
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Y-City Builder")

class Building:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(['residential', 'commercial', 'industrial'])
        self.level = 1

    def draw(self):
        if self.type == 'residential':
            color = GREEN
        elif self.type == 'commercial':
            color = BLUE
        else:
            color = GRAY
        
        rect = pygame.Rect(
            self.x * GRID_SIZE,
            self.y * GRID_SIZE,
            GRID_SIZE,
            GRID_SIZE
        )
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

class City:
    def __init__(self):
        self.buildings = []
        self.money = 10000
        self.population = 0
        
    def add_building(self, x, y):
        if self.money >= 1000:
            self.buildings.append(Building(x, y))
            self.money -= 1000
            self.population += 10

    def draw(self):
        for building in self.buildings:
            building.draw()

def draw_grid():
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_WIDTH, y))

def draw_ui(city):
    font = pygame.font.Font(None, 36)
    money_text = font.render(f"Money: ${city.money}", True, BLACK)
    population_text = font.render(f"Population: {city.population}", True, BLACK)
    screen.blit(money_text, (10, 10))
    screen.blit(population_text, (10, 50))

def main():
    city = City()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x = x // GRID_SIZE
                grid_y = y // GRID_SIZE
                city.add_building(grid_x, grid_y)

        # Draw
        screen.fill(WHITE)
        draw_grid()
        city.draw()
        draw_ui(city)
        pygame.display.flip()
        
        # Control game speed
        clock.tick(60)

if __name__ == "__main__":
    main()
