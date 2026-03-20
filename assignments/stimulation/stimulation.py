import random, sys, time, pygame
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BUTTONSIZE = 120
BUTTONGAPSIZE = 20
TIMEOUT = 4

# Colors (Pastel Theme)
WHITE        = (255, 255, 255)
BLACK        = (0, 0, 0)
YELLOW       = (240, 240, 150)
BRIGHTYELLOW = (255, 255, 186)
BLUE         = (150, 200, 240)
BRIGHTBLUE   = (186, 225, 255)
RED          = (255, 153, 170)
BRIGHTRED    = (255, 183, 197)
GREEN        = (150, 230, 180)
BRIGHTGREEN  = (186, 255, 201)
ORANGE       = (255, 200, 150)
PURPLE       = (200, 150, 255)
PINK         = (255, 180, 220)
CYAN         = (150, 255, 255)
WRONG        = (255, 50, 50)

bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (3 * BUTTONSIZE) - 2 * BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (3 * BUTTONSIZE) - 2 * BUTTONGAPSIZE) / 2)

# Define buttons in a 3x3 grid
BUTTON_COLORS = [YELLOW, BLUE, RED,
                 GREEN, ORANGE, PURPLE,
                 PINK, CYAN, BRIGHTYELLOW]

BRIGHT_COLORS = [BRIGHTYELLOW, BRIGHTBLUE, BRIGHTRED,
                 BRIGHTGREEN, ORANGE, PURPLE,
                 PINK, CYAN, WHITE]

BUTTONS = [
    {"color": BUTTON_COLORS[row*3 + col], 
     "bright": BRIGHT_COLORS[row*3 + col],
     "rect": pygame.Rect(XMARGIN + (BUTTONSIZE + BUTTONGAPSIZE) * col,
                         YMARGIN + (BUTTONSIZE + BUTTONGAPSIZE) * row,
                         BUTTONSIZE, BUTTONSIZE)}
    for row in range(3) for col in range(3)
]

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    global BEEP, BG_IMAGE

    pygame.init()
    pygame.mixer.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simon 3x3 Game')

    BASICFONT = pygame.font.SysFont(None, 30)

    # Background image
    try:
        BG_IMAGE = pygame.image.load('background.jpg')
        BG_IMAGE = pygame.transform.scale(BG_IMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    except:
        BG_IMAGE = None

    class DummySound:
        def play(self): pass

    try:
        BEEP = pygame.mixer.Sound('beep.ogg')
    except:
        BEEP = DummySound()

    pattern = []
    currentStep = 0
    lastClickTime = 0
    score = 0
    streak = 0
    waitingForInput = False
    showNice = False
    niceTimer = 0

    # Loading screen
    if BG_IMAGE:
        DISPLAYSURF.blit(BG_IMAGE, (0, 0))
    else:
        DISPLAYSURF.fill(bgColor)

    loadingText = BASICFONT.render("Please wait for the game to load.", True, BLACK)
    loadingRect = loadingText.get_rect(center=(WINDOWWIDTH//2, WINDOWHEIGHT//2))
    DISPLAYSURF.blit(loadingText, loadingRect)
    pygame.display.update()
    pygame.time.wait(2000)

    while True:
        clickedButton = None

        # Background
        if BG_IMAGE:
            DISPLAYSURF.blit(BG_IMAGE, (0, 0))
        else:
            DISPLAYSURF.fill(bgColor)

        drawButtons()

        # Score
        scoreSurf = BASICFONT.render('Score: ' + str(score), True, BLACK)
        DISPLAYSURF.blit(scoreSurf, (500, 10))

        # Nice text
        if showNice:
            if pygame.time.get_ticks() - niceTimer < 800:
                niceText = BASICFONT.render("Nice!", True, (0, 150, 0))
                niceRect = niceText.get_rect(center=(WINDOWWIDTH//2, 15))
                DISPLAYSURF.blit(niceText, niceRect)
            else:
                showNice = False

        checkForQuit()

        mousex, mousey = pygame.mouse.get_pos()
        hoverButton = getButtonClicked(mousex, mousey)

        # Hover glow
        if hoverButton:
            glowSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE), pygame.SRCALPHA)
            glowSurf.fill((255, 255, 255, 60))
            rect = hoverButton['rect']
            DISPLAYSURF.blit(glowSurf, rect.topleft)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

        if not waitingForInput:
            pygame.display.update()
            pygame.time.wait(500)

            pattern.append(random.choice(BUTTONS))

            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.delay(80)

            waitingForInput = True
            currentStep = 0
            lastClickTime = time.time()

        else:
            if clickedButton and clickedButton == pattern[currentStep]:
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    streak += 1
                    score += 1

                    if streak % 3 == 0:
                        score += 2
                        showNice = True
                        niceTimer = pygame.time.get_ticks()

                    waitingForInput = False
                    currentStep = 0

            elif (clickedButton and clickedButton != pattern[currentStep]) or \
                 (currentStep != 0 and time.time() - lastClickTime > TIMEOUT):

                # Wrong click feedback
                if clickedButton:
                    flashWrongButton(clickedButton)
                shakeScreen()
                gameOverAnimation()
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                streak = 0
                showNice = False
                pygame.time.wait(800)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()

def getButtonClicked(x, y):
    for button in BUTTONS:
        if button['rect'].collidepoint((x, y)):
            return button
    return None

def flashButtonAnimation(button):
    BEEP.play()
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE), pygame.SRCALPHA)
    r, g, b = button['bright']

    for alpha in range(0, 255, 40):
        DISPLAYSURF.blit(origSurf, (0, 0))
        flashSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(flashSurf, button['rect'].topleft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    for alpha in range(255, 0, -40):
        DISPLAYSURF.blit(origSurf, (0, 0))
        flashSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(flashSurf, button['rect'].topleft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def flashWrongButton(button):
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf.fill(WRONG)
    DISPLAYSURF.blit(flashSurf, button['rect'].topleft)
    pygame.display.update()
    pygame.time.wait(300)

def shakeScreen():
    origSurf = DISPLAYSURF.copy()
    for dx, dy in [(5,0), (-5,0), (5,0), (-5,0), (0,0)]:
        DISPLAYSURF.blit(origSurf, (dx, dy))
        pygame.display.update()
        pygame.time.wait(30)

def drawButtons():
    for idx, button in enumerate(BUTTONS):
        pygame.draw.rect(DISPLAYSURF, button['color'], button['rect'])
        text = BASICFONT.render(str(idx+1), True, BLACK)
        DISPLAYSURF.blit(text, text.get_rect(center=button['rect'].center))

def gameOverAnimation():
    for i in range(3):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(150)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(150)

if __name__ == '__main__':
    main()
