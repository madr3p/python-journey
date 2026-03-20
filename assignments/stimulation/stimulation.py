import random, sys, time, pygame
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4

# Colors (Pastel Theme)
WHITE        = (255, 255, 255)
BLACK        = (0, 0, 0)
BRIGHTRED    = (255, 183, 197)
RED          = (255, 153, 170)
BRIGHTGREEN  = (186, 255, 201)
GREEN        = (150, 230, 180)
BRIGHTBLUE   = (186, 225, 255)
BLUE         = (150, 200, 240)
BRIGHTYELLOW = (255, 255, 186)
YELLOW       = (240, 240, 150)

bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    global BEEP1, BEEP2, BEEP3, BEEP4, BG_IMAGE

    pygame.init()
    pygame.mixer.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simon Game')

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
        BEEP1 = pygame.mixer.Sound('beep1.ogg')
        BEEP2 = pygame.mixer.Sound('beep2.ogg')
        BEEP3 = pygame.mixer.Sound('beep3.ogg')
        BEEP4 = pygame.mixer.Sound('beep4.ogg')
    except:
        BEEP1 = BEEP2 = BEEP3 = BEEP4 = DummySound()

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
    pygame.time.wait(3000)

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
            rect = getRectFromColor(hoverButton)
            DISPLAYSURF.blit(glowSurf, rect.topleft)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

        if not waitingForInput:
            pygame.display.update()
            pygame.time.wait(800)

            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))

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

def getRectFromColor(color):
    if color == YELLOW: return YELLOWRECT
    if color == BLUE: return BLUERECT
    if color == RED: return REDRECT
    if color == GREEN: return GREENRECT

def flashButtonAnimation(color):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rect = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rect = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rect = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rect = GREENRECT

    sound.play()

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE), pygame.SRCALPHA)
    r, g, b = flashColor

    for alpha in range(0, 255, 40):
        DISPLAYSURF.blit(origSurf, (0, 0))
        flashSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(flashSurf, rect.topleft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    for alpha in range(255, 0, -40):
        DISPLAYSURF.blit(origSurf, (0, 0))
        flashSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(flashSurf, rect.topleft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)

    text1 = BASICFONT.render("1", True, BLACK)
    text2 = BASICFONT.render("2", True, BLACK)
    text3 = BASICFONT.render("3", True, BLACK)
    text4 = BASICFONT.render("4", True, BLACK)

    DISPLAYSURF.blit(text1, text1.get_rect(center=YELLOWRECT.center))
    DISPLAYSURF.blit(text2, text2.get_rect(center=BLUERECT.center))
    DISPLAYSURF.blit(text3, text3.get_rect(center=REDRECT.center))
    DISPLAYSURF.blit(text4, text4.get_rect(center=GREENRECT.center))

def gameOverAnimation():
    for i in range(3):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(150)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(150)

def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint((x, y)): return YELLOW
    if BLUERECT.collidepoint((x, y)): return BLUE
    if REDRECT.collidepoint((x, y)): return RED
    if GREENRECT.collidepoint((x, y)): return GREEN
    return None

if __name__ == '__main__':
    main()
