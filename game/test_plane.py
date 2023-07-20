import pygame as pg

pg.init()

print()
fps = int(input("Enter 45, 60 or 75 fps.Default value is 60 fps : "))

# Create a display window
window_size = (900, 800)
screen = pg.display.set_mode(window_size)

# Load image with transparency and convert_alpha()
plane_with_alpha = pg.image.load("user_plane_images/base_plane.png").convert_alpha()

clock = pg.time.Clock()
x = 100
y = 100

plane_speed = {
    45: 4.5,
    60: 3.5,
    75: 2.5,
}

speed = plane_speed.get(fps, 3)

# Main loop
running = True
while running:
    clock.tick(int(fps))

    print(f"now running on {fps}fps ----- moving with {speed} pixels per iteration")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    screen.fill((255, 255, 255))

    if pg.key.get_pressed()[pg.K_a]:
        x -= speed

    if pg.key.get_pressed()[pg.K_d]:
        x += speed

    if pg.key.get_pressed()[pg.K_w]:
        y -= speed

    if pg.key.get_pressed()[pg.K_s]:
        y += speed

    screen.blit(plane_with_alpha, (x, y))

    pg.display.flip()

pg.quit()