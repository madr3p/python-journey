import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHDELAY = 200
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
DARKGRAY     = (100, 100, 100)

bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    global BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    pygame.mixer.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simon Game')

    BASICFONT = pygame.font.SysFont(None, 20)

    infoSurf = BASICFONT.render('Repeat pattern (Q,W,A,S or mouse)', True, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    # Dummy sound (if files missing)
    class DummySound:
        def play(self):
            pass

    try:
        BEEP1 = pygame.mixer.Sound('beep1.ogg')
        BEEP2 = pygame.mixer.Sound('beep2.ogg')
        BEEP3 = pygame.mixer.Sound('beep3.ogg')
        BEEP4 = pygame.mixer.Sound('beep4.ogg')
    except:
        BEEP1 = DummySound()
        BEEP2 = DummySound()
        BEEP3 = DummySound()
        BEEP4 = DummySound()

    pattern = []
    currentStep = 0
    lastClickTime = 0
    score = 0
    waitingForInput = False

    while True:
        clickedButton = None
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('Score: ' + str(score), True, WHITE)
        DISPLAYSURF.blit(scoreSurf, (520, 10))
        DISPLAYSURF.blit(infoSurf, infoRect)

        checkForQuit()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN

        if not waitingForInput:
            pygame.display.update()
            pygame.time.wait(1000)

            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))

            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)

            waitingForInput = True
            lastClickTime = time.time()

        else:
            if clickedButton and clickedButton == pattern[currentStep]:
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0

            elif (clickedButton and clickedButton != pattern[currentStep]) or \
                 (currentStep != 0 and time.time() - lastClickTime > TIMEOUT):

                gameOverAnimation()
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


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

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE)).convert_alpha()

    sound.play()

    r = flashColor[0]
    g = flashColor[1]
    b = flashColor[2]

    for alpha in range(0, 255, 50):
        DISPLAYSURF.blit(origSurf, (0, 0))
        flashSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(flashSurf, rect.topleft)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    DISPLAYSURF.blit(origSurf, (0, 0))


def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)

    # Draw numbers
    text1 = BASICFONT.render("1", True, BLACK)
    text2 = BASICFONT.render("2", True, BLACK)
    text3 = BASICFONT.render("3", True, BLACK)
    text4 = BASICFONT.render("4", True, BLACK)

    DISPLAYSURF.blit(text1, text1.get_rect(center=YELLOWRECT.center))
    DISPLAYSURF.blit(text2, text2.get_rect(center=BLUERECT.center))
    DISPLAYSURF.blit(text3, text3.get_rect(center=REDRECT.center))
    DISPLAYSURF.blit(text4, text4.get_rect(center=GREENRECT.center))


def changeBackgroundAnimation():
    global bgColor
    bgColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


def gameOverAnimation():
    for i in range(3):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(200)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(200)


def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint((x, y)):
        return YELLOW
    elif BLUERECT.collidepoint((x, y)):
        return BLUE
    elif REDRECT.collidepoint((x, y)):
        return RED
    elif GREENRECT.collidepoint((x, y)):
        return GREEN
    return None


if __name__ == '__main__':
    main()
