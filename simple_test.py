import pygame

print("1. Initializing Pygame...")
pygame.init()

print("2. Setting Display Mode...")
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Window")

print("3. Starting Loop...")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 0, 0)) # Red background
    pygame.display.flip()

pygame.quit()
print("4. Done.")