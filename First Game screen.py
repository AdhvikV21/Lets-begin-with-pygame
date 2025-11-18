import pygame

WINDOW_SIZE = (500, 500)
WINDOW_CAPTION = 'My first game screen'
BACKGROUND_COLOR = (58, 58, 58) 
IMAGE_FILE = ('background.png') 
IMAGE_SIZE = (300, 300)

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)

image = pygame.image.load(IMAGE_FILE).convert_alpha()
image = pygame.transform.scale(image, IMAGE_SIZE)
image_rect = image.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
font = pygame.font.Font(None, 36)
caption_text = font.render(WINDOW_CAPTION, True, (255, 255, 255))
text_rect = caption_text.get_rect(center=(WINDOW_SIZE[0] // 2, 30))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BACKGROUND_COLOR)
    screen.blit(image, image_rect)
    screen.blit(caption_text, text_rect)
    pygame.display.flip()

pygame.quit()