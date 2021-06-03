from tkinter import *
def openWindow():
    new_window = Toplevel(screen)
    new_window.geometry("800x600")
    new_window.title("How to play")
    new_window.configure(background="orange")
    new_window.resizable(False, False)
    heading=Label(new_window,text="Instructions",font="Jokerman")
    lbl = Label(new_window, text="To move the Hanuman ji in the right direction press right arrow -> .",font="Times",bg="orange")
    lbl2 = Label(new_window, text="To move the Hanuman ji in the left direction press left arrow <- .",font="Times",bg="orange")
    lbl3=Label(new_window, text="Player should try to defend from the obstacles falling.",font="Times",bg="orange")
    lbl4 = Label(new_window, text="To shoot the obstacles press the space bar.", font="Times",bg="orange")
    lbl5 = Label(new_window, text="After shooting an obstacle your score will increase.", font="Times", bg="orange")
    lbl6 = Label(new_window, text="When obstacles touch Hanuman ji the game will over.", font="Times", bg="orange")
    lbl8 = Label(new_window,text="Player will be able to shoot only when the previous bullet will goes at zero coordinate.",font="Times", bg="orange")
    heading.pack()
    lbl.pack(side=TOP)
    lbl2.pack(side=TOP)
    lbl3.pack(side=TOP)
    lbl4.pack(side=TOP)
    lbl5.pack(side=TOP)
    lbl6.pack(side=TOP)
    lbl8.pack(side=TOP)
def new_win():
    import math
    import pygame
    import random
    from pygame import mixer

    # Intialize the pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((800, 600))
    # Background
    background = pygame.image.load('bg.png')
    # Sound
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Hanuman Game")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('hg.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('ufos1.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    # Bullet
    bulletImg = pygame.image.load('weapon.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    testY = 10

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False

    # Game Loop
    running = True
    while running:

        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # movement mechanism
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound("laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the hanumanji
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
screen = Tk()
#define image
bg=PhotoImage(file="last4.png")
#create a label
my_label=Label(screen,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
h=Label(screen, text="Hanuman Game",fg="red",font="Times 16 bold italic",bg="orange")
h.place(x=20,y=30)
btn2 = Button(screen, text="Start Game", fg="Blue", command = new_win)
btn2.place(x=730,y=250)
btn = Button(screen, text="Instruction", command=openWindow, fg="Red")
btn.place(x=730,y=275)
screen.resizable(False,False)
screen.geometry("800x600")
screen.title("Hanuman Game")
screen.mainloop()