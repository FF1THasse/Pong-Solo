import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 200
PADDLE_HEIGHT = 30
BALL_RADIUS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))

newbie = False
facile = False
moyen = False
difficile = False
hardcore = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

# Création de la fenêtre
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Solo")

myfont = pygame.font.SysFont('monospace', 50)

print("init")
screen.fill(BLACK)
title = myfont.render("Pong mais la version solo", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("Choisis ton mode de jeu", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("A - Newbie", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("Z - Facile", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("E - Moyen", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("R - Difficile", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("T - Hardcore", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()
pygame.time.delay(1000)
screen.fill(BLACK)
title = myfont.render("Alors ?", False, GREEN)
screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
pygame.display.update()

pygame.event.clear()
#Si un des 5 boutons est cliqué, la valeur renvoyant au mode de jeu correspondant est vraie
print("select level")
levelset = False
while levelset == False :
  event = pygame.event.wait()

  if event.type == pygame.KEYDOWN:
    print("key pressed")
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      speed = 4
      levelset = True
    elif keys[pygame.K_z]:
      speed = 5
      levelset = True
    elif keys[pygame.K_e]:
      speed = 7
      levelset = True
    elif keys[pygame.K_r]:
      speed = 9
      levelset = True
    elif keys[pygame.K_t]:
      speed = 11.2
      levelset = True
    else:
      speed = 4
      levelset = True

if levelset :
  screen.fill(BLACK)
  title = myfont.render("3 !", False, GREEN)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(1000)
  screen.fill(BLACK)
  title = myfont.render("2 !", False, GREEN)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(1000)
  screen.fill(BLACK)
  title = myfont.render("1 !", False, GREEN)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(1000)
  screen.fill(BLACK)
  title = myfont.render("GO !!!", False, GREEN)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(1000)

  clock = pygame.time.Clock()

  # Position initiale de la raquette
  paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
  paddle_y = HEIGHT - PADDLE_HEIGHT - 10

  # Position initiale de la balle
  ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
  ball_y = HEIGHT // 2
  ball_dx = random.choice([-(speed), (speed)])
  ball_dy = speed

  # Score
  score = 0




  # Boucle principale du jeu
  running = True
  while running:
      win.fill(BLACK)
      # Gestion des événements
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      # Mouvement de la raquette
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT] and paddle_x > 10:
          paddle_x -= 10
      if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH -10:
          paddle_x += 10



      # Rebond de la balle sur les bords
      if ball_x <= BALL_RADIUS or ball_x >= WIDTH - BALL_RADIUS:
          ball_dx = -ball_dx
      if ball_y <= BALL_RADIUS:
          ball_dy = -ball_dy

      # Rebond de la balle sur la raquette
      if ball_y >= paddle_y - BALL_RADIUS and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
          ball_dy = -ball_dy
          score += 1

      # Si la balle touche le bas (le joueur a perdu)
      if ball_y >= HEIGHT - BALL_RADIUS:
        title = myfont.render("Tu as perdu !", False, GREEN)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill(BLACK)
        title = myfont.render("Ton score :"+ str(score), False, GREEN)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() * 2))
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill(BLACK)
        pygame.quit()

      # Mouvement de la balle
      ball_x += ball_dx
      ball_y += ball_dy

      # Dessin de la raquette
      pygame.draw.rect(win, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

      # Dessin de la balle
      pygame.draw.circle(win, WHITE, (ball_x, ball_y), BALL_RADIUS)

      # Affichage du score
      font = pygame.font.SysFont(None, 36)
      text = font.render("Score: " + str(score), True, WHITE)
      win.blit(text, (10, 10))

      pygame.display.update()
      clock.tick(60)

      #if keys[pygame.K_ESCAPE]:
          #pygame.quit()
else:
  print("no level set")

pygame.quit()