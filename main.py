import pygame
import sys
from random import randint

BLACK = (0,0,0)
WHITE = (255, 255, 255)
LOTNISKOWIEC = (169, 169, 169)
KRAZOWNIK = (100, 100, 100)
PODWODNA = (50, 50, 50)
BLUE = (0, 0, 255)
BLOCKS_HEIGHT = 6
BLOCKS_WIDTH = 6
B_SIZE_W = 100
B_SIZE_H = 100
SCREEN_WIDTH = BLOCKS_WIDTH*B_SIZE_W
SCREEN_HEIGHT = BLOCKS_HEIGHT*B_SIZE_H+80
ILOSC_LOTNISKOWCOW = 2
ILOSC_KRAZOWNIKOW = 3
ILOSC_PODWODNYCH = 4
ILOSC_TRAFIEN_P = ILOSC_PODWODNYCH+ILOSC_LOTNISKOWCOW*3+ILOSC_KRAZOWNIKOW*2
ILOSC_RUCHOW=25
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

def randLotniskowiec(boardComp):
    #Losowanie lotniskowcow
    for i in range(ILOSC_LOTNISKOWCOW):
        direction = randint(1, 4)
        #1-północ
        #2-południe
        #3-zachód
        #4-wschód


        if direction == 1:
            start_y=randint(-5,-2)
            start_x=randint(0,5)
            start_y=start_y*-1
            middle_y=start_y-1
            end_y=start_y-2

            while boardComp[start_y][start_x] == 1 or boardComp[middle_y][start_x] == 1 or boardComp[end_y][start_x] == 1:
                start_y=randint(-5,-2)
                start_x=randint(0,5)
                start_y=start_y*-1
                middle_y=start_y-1
                end_y=start_y-2
            boardComp[start_y][start_x]=1
            boardComp[middle_y][start_x]=1
            boardComp[end_y][start_x]=1
        
        if direction == 2:
            start_y=randint(0,3)
            start_x=randint(0,5)
            middle_y=start_y+1
            end_y=start_y+2

            while boardComp[start_y][start_x] == 1 or boardComp[middle_y][start_x] == 1 or boardComp[end_y][start_x] == 1:
                start_y=randint(0,3)
                start_x=randint(0,5)
                middle_y=start_y+1
                end_y=start_y+2
            boardComp[start_y][start_x]=1
            boardComp[middle_y][start_x]=1
            boardComp[end_y][start_x]=1

        if direction == 3:
            start_x=randint(-5,-2)
            start_y=randint(0,5)
            start_x=start_x*-1
            middle_x=start_x-1
            end_x=start_x-2

            while boardComp[start_y][start_x] == 1 or boardComp[start_y][middle_x] == 1 or boardComp[start_y][end_x] == 1:
                start_x=randint(-5,-2)
                start_y=randint(0,5)
                start_x=start_y*-1
                middle_x=start_x-1
                end_x=start_x-2
            boardComp[start_y][start_x]=1
            boardComp[start_y][middle_x]=1
            boardComp[start_y][end_x]=1
        
        if direction == 4:
            start_x=randint(0,3)
            start_y=randint(0,5)
            middle_x=start_x+1
            end_x=start_x+2

            while boardComp[start_y][start_x] == 1 or boardComp[start_y][middle_x] == 1 or boardComp[start_y][end_x] == 1:
                start_x=randint(0,3)
                start_y=randint(0,5)
                middle_x=start_x+1
                end_x=start_x+2
            boardComp[start_y][start_x]=1
            boardComp[start_y][middle_x]=1
            boardComp[start_y][end_x]=1
            
def randKrazownik(boardComp):
    #Losowanie krazownikow
    for i in range(ILOSC_KRAZOWNIKOW):
        direction = randint(1, 4)
        #1-północ
        #2-południe
        #3-zachód
        #4-wschód


        if direction == 1:
            start_y=randint(-5,-2)
            start_x=randint(0,5)
            start_y=start_y*-1
            end_y=start_y-1

            while boardComp[start_y][start_x] == 1 or boardComp[end_y][start_x] == 1 or boardComp[start_y][start_x] == 2 or boardComp[end_y][start_x] == 2:
                start_y=randint(-5,-2)
                start_x=randint(0,5)
                start_y=start_y*-1
                end_y=start_y-1
            boardComp[start_y][start_x]=2
            boardComp[end_y][start_x]=2

        if direction == 2:
            start_y=randint(0,3)
            start_x=randint(0,5)
            end_y=start_y+1

            while boardComp[start_y][start_x] == 1 or boardComp[end_y][start_x] == 1 or boardComp[start_y][start_x] == 2 or boardComp[end_y][start_x] == 2:
                start_y=randint(0,3)
                start_x=randint(0,5)
                end_y=start_y+1
            boardComp[start_y][start_x]=2
            boardComp[end_y][start_x]=2
        
        if direction == 3:
            start_y=randint(0,5)
            start_x=randint(-5, -2)
            start_x=start_x*-1
            end_x=start_x-1

            while boardComp[start_y][start_x] == 1 or boardComp[start_y][end_x] == 1 or boardComp[start_y][start_x] == 2 or boardComp[start_y][end_x] == 2:
                start_y=randint(0,5)
                start_x=randint(-5, -2)
                start_x=start_x*-1
                end_x=start_x-1
            boardComp[start_y][start_x]=2
            boardComp[start_y][end_x]=2

        if direction == 4:
            start_y=randint(0,5)
            start_x=randint(0,3)
            end_x=start_x+1

            while boardComp[start_y][start_x] == 1 or boardComp[start_y][end_x] == 1 or boardComp[start_y][start_x] == 2 or boardComp[start_y][end_x] == 2:
                start_y=randint(0,5)
                start_x=randint(0,3)
                end_x=start_x+1
            boardComp[start_y][start_x]=2
            boardComp[start_y][end_x]=2

def randPodwodne(boardComp):
    for i in range(ILOSC_PODWODNYCH):
        x=randint(0,5)
        y=randint(0,5)

        while boardComp[y][x]==1 or boardComp[y][x]==2 or boardComp[y][x]==3:
            x=randint(0,5)
            y=randint(0,5)
        boardComp[y][x]=3

def strzelanie(board, pos, screen):
    font=pygame.font.Font('freesansbold.ttf', 25)

    x=pos[0]//B_SIZE_W
    y=pos[1]//B_SIZE_H

    if board[y][x]==1 or board[y][x]==2 or board[y][x]==3:
        wart="               TRAFIENIE!!!           "
        board[y][x]="t"
    elif board[y][x]=="t":
        wart="JUZ TU STRZELALES!!!"
    elif board[y][x]=="p":
        wart="JUZ TU STRZELALES!!!"
    elif board[y][x]==0:
        wart="                 PUDŁO!!!                  "
        board[y][x]="p"
    text=font.render(wart, True, (255,255,255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300,660)
    screen.blit(text, textRect)
    time=10


def color(content):
    if content == 3:
        color = BLUE
    if content == 2:
        color = BLUE
    if content == 1:
        color = BLUE
    if content == 0:
        color = BLUE
    if content == "t":
        color = RED
    if content == "p":
        color = (169, 169, 169)
    return color

def drawText(screen, board, ilosc_strzalow):
    ilosc_trafien=0
    for x in board:
        for n in x: 
            if n=="t":
                ilosc_trafien=ilosc_trafien+1
    wart="Ilość trafien: "+str(ilosc_trafien)
    wart2="Ilość strzałów: "+str(ilosc_strzalow)
    font=pygame.font.Font('freesansbold.ttf', 25)
    text=font.render(wart, True, (255,255,255), (0, 0, 0))
    text2=font.render(wart2, True, (255,255,255), (0, 0, 0))
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = (480, 625)
    text2Rect.center = (120, 625)
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)

def checkForWin(board, screen):
    ilosc_trafien=0
    win=pygame.image.load("assets\win.png")
    for x in board:
        for n in x: 
            if n=="t":
                ilosc_trafien=ilosc_trafien+1
    if ilosc_trafien==ILOSC_TRAFIEN_P:
        screen.blit(win,(150, 150))

def drawBoard(board, screen):
    for j, tile in enumerate(board):
        for i, tile_content in enumerate(tile):
            rect=pygame.Rect(i*B_SIZE_W, j*B_SIZE_H, B_SIZE_W, B_SIZE_H)
            pygame.draw.rect(screen, color(tile_content), rect)
            pygame.draw.rect(screen, BLACK, rect, width=2)




def main():

    boardPlayer = [[0] * BLOCKS_WIDTH for i in range(BLOCKS_HEIGHT)]
    boardComp = [[0] * BLOCKS_WIDTH for i in range(BLOCKS_HEIGHT)]

    pygame.init()
    pygame.display.set_caption("Statki")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    screen.fill(BLACK)
    randLotniskowiec(boardComp)
    randKrazownik(boardComp)
    randPodwodne(boardComp)

    

    ilosc_strzalow=0
    ilosc_trafien=0

    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ilosc_strzalow<ILOSC_RUCHOW:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        x=pos[0]//B_SIZE_H
                        y=pos[1]//B_SIZE_W
                        ilosc_strzalow=ilosc_strzalow+1
                        strzelanie(boardComp, pos, screen)
 
                         
        drawBoard(boardComp, screen)
        drawText(screen, boardComp, ilosc_strzalow)   
        checkForWin(boardComp, screen)

        if ilosc_strzalow==ILOSC_RUCHOW:
            lose=pygame.image.load("assets\lose.jpg")
            screen.blit(lose,(150, 150))

        pygame.display.update()
        clock.tick(30)

        




if __name__=="__main__":
    main()


