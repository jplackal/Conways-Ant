import pygame

pygame.init()

WIDTH = 1300
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conways Ant")
clock = pygame.time.Clock()
positions = [[0,1],[1,1],[0,0],[1,0]]
cam_x = 0
cam_y = 0
tile_size = 1
buffer = 50
min_tile_size = 500
view_x = 0
view_y = 0
view_tile_size = 0
catchup = 0.1
running = True
def view_check():
    if len(positions) != 0:
        global cam_x, cam_y, view_x, view_y, view_tile_size, tile_size, buffer, min_tile_size,catchup, HEIGHT
        bottom = positions[0][1]
        top = positions[0][1]
        right = positions[0][0]
        left = positions[0][0] 
        for x, y in positions:
            if y>top:
                top = y
            if y<bottom:
                bottom = y
            if x>right:
                right = x
            if x<left:
                left = x
        cam_x = (left+right)/-2
        cam_y = (bottom+top)/-2
        width_range = right - left + 1
        height_range = top - bottom + 1

        # Fit all tiles inside the screen
        tile_size = int(min(
            (WIDTH - 2 * buffer) / width_range,
            (HEIGHT - 2 * buffer) / height_range
        ))
        tile_size = max(1, tile_size)
        view_x += (cam_x-view_x)*catchup
        view_y += (cam_y-view_y)*catchup
        view_tile_size += (tile_size - view_tile_size)*catchup
def draw():
    global tile_size
    for x, y in positions:
        pygame.draw.circle(screen, (255, 255, 255),((x+view_x) * view_tile_size+WIDTH/2, (y+view_y)*view_tile_size+HEIGHT/2), int(view_tile_size/2))
    pygame.draw.circle(screen, (255, 255, 255),(WIDTH/2,HEIGHT/2),0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    view_check()
    draw()
    pygame.display.flip()
    clock.tick(60)
    print(view_x)

    print(view_y)

    print(view_tile_size)


pygame.quit()