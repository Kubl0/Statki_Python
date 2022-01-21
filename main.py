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
SCREEN_WIDTH = BLOCKS_WIDTH*B_SIZE_W*2+20
SCREEN_HEIGHT = BLOCKS_HEIGHT*B_SIZE_H+80
ILOSC_LOTNISKOWCOW = 2
ILOSC_KRAZOWNIKOW = 2
ILOSC_PODWODNYCH = 3
ILOSC_TRAFIEN_P = ILOSC_PODWODNYCH+ILOSC_LOTNISKOWCOW*3+ILOSC_KRAZOWNIKOW*2
ILOSC_RUCHOW=20
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

    if x<0 or x>5 or y<0 or y>5:
        wart="                 PUDŁO!                    "
    elif x>=0 and x <=5 and y>=0 and y<=5:
        if board[y][x]==1 or board[y][x]==2 or board[y][x]==3:
            wart="               TRAFIENIE!             "
            board[y][x]="t"
        elif board[y][x]=="t":
            wart="JUZ TU STRZELALES!  "
        elif board[y][x]=="p":
            wart="JUZ TU STRZELALES!  "
        elif board[y][x]==0:
            wart="                 PUDŁO!                    "
            board[y][x]="p"
    text=font.render(wart, True, (255,255,255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300,660)
    screen.blit(text, textRect)


def strzelanieComp(board, screen):
    font=pygame.font.Font('freesansbold.ttf', 25)
    x=randint(0,5)
    y=randint(0,5)

    if board[y][x]==5 or board[y][x]==6 or board[y][x]==7:
        wart="               TRAFIENIE!             "
        board[y][x]="t"
    elif board[y][x]=="t":
            wart="JUZ TU STRZELALES!  "
    elif board[y][x]=="y":
            wart="JUZ TU STRZELALES!  "
    elif board[y][x]==0:
        wart="                 PUDŁO!                    "
        board[y][x]="y"

    text=font.render(wart, True, (255,255,255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (900,660)
    screen.blit(text, textRect)



def color(content):
    if content == 5:
        color = LOTNISKOWIEC
    if content == 6:
        color = KRAZOWNIK
    if content == 7:
        color = PODWODNA
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
    if content == "y":
        color = YELLOW
    return color

def drawText(screen, boardComp, ilosc_strzalow, boardPlayer, ilosc_strzalow_comp):
    ilosc_trafien=0
    for x in boardComp:
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
    ilosc_trafien_comp=0
    for x in boardPlayer:
        for n in x: 
            if n=="t":
                ilosc_trafien_comp=ilosc_trafien_comp+1
    wart="Ilość trafien Comp: "+str(ilosc_trafien_comp)
    wart2="Ilość strzałów Comp: "+str(ilosc_strzalow_comp)
    font=pygame.font.Font('freesansbold.ttf', 25)
    text=font.render(wart, True, (255,255,255), (0, 0, 0))
    text2=font.render(wart2, True, (255,255,255), (0, 0, 0))
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = (1080, 625)
    text2Rect.center = (760, 625)
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)

def trafienia(board):
    trafienia=0
    for x in board:
        for n in x:
            if n=="t":
                trafienia=trafienia+1
    return trafienia

def selectLotniskowiec(boardPlayer):
    
        pos = pygame.mouse.get_pos()
        
        x=pos[0]//B_SIZE_W-6
        y=pos[1]//B_SIZE_H
        
        direction=str(input("Podaj kierunek łodzi: 1-północ, 2-południe, 3-zachód, 4-wschód >> "))

        if direction == "1":
            if x>=0 and x<=5 and y>=2 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y-1][x]!=5 and boardPlayer[y-2][x]!=5:
                    boardPlayer[y][x]=5
                    boardPlayer[y-1][x]=5
                    boardPlayer[y-2][x]=5
                else:
                    print("Złe pole")
            else:
                    print("Złe pole")
        if direction == "2":
            if x>=0 and x<=5 and y>=0 and y<=3:
                if boardPlayer[y][x]!=5 and boardPlayer[y+1][x]!=5 and boardPlayer[y+2][x]!=5:
                    boardPlayer[y][x]=5
                    boardPlayer[y+1][x]=5
                    boardPlayer[y+2][x]=5
                else:
                    print("Złe pole")
            else:
                print("Złe pole")
        if direction == "3":
            if x>=3 and x<=5 and y>=0 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y][x-1]!=5 and boardPlayer[y][x-2]!=5:
                    boardPlayer[y][x]=5
                    boardPlayer[y][x-1]=5
                    boardPlayer[y][x-2]=5
                else:
                    print("Złe pole")
            else:
                print("Złe pole")
        if direction == "4":
            if x>=0 and x<=3 and y>=0 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y][x+1]!=5 and boardPlayer[y][x+2]!=5:
                    boardPlayer[y][x]=5
                    boardPlayer[y][x+1]=5
                    boardPlayer[y][x+2]=5
                else:
                    print("Złe pole")
            else:
                print("Złe pole")



def selectKrazownik(boardPlayer):
        pos = pygame.mouse.get_pos()
        
        x=pos[0]//B_SIZE_W-6
        y=pos[1]//B_SIZE_H
        
        direction=str(input("Podaj kierunek łodzi: 1-północ, 2-południe, 3-zachód, 4-wschód >> "))

        if direction == "1":
            if x>=0 and x<=5 and y>=1 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y-1][x]!=5 and boardPlayer[y][x]!=6 and boardPlayer[y-1][x]!=6:
                    boardPlayer[y][x]=6
                    boardPlayer[y-1][x]=6
                else:
                    print("Złe pole")
            else:
                    print("Złe pole")
        if direction == "2":
            if x>=0 and x<=5 and y>=0 and y<=4:
                if boardPlayer[y][x]!=5 and boardPlayer[y+1][x]!=5 and boardPlayer[y][x]!=6 and boardPlayer[y+1][x]!=6:
                    boardPlayer[y][x]=6
                    boardPlayer[y+1][x]=6
                else:
                    print("Złe pole")
            else:
                print("Złe pole")
        if direction == "3":
            if x>=1 and x<=5 and y>=0 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y][x-1]!=5 and boardPlayer[y][x]!=6 and boardPlayer[y][x-1]!=6:
                    boardPlayer[y][x]=6
                    boardPlayer[y][x-1]=6
                else:
                    print("Złe pole")
            else:
                print("Złe pole")
        if direction == "4":
            if x>=0 and x<=4 and y>=0 and y<=5:
                if boardPlayer[y][x]!=5 and boardPlayer[y][x+1]!=5 and boardPlayer[y][x]!=6 and boardPlayer[y][x+1]!=6:
                    boardPlayer[y][x]=6
                    boardPlayer[y][x+1]=6
                else:
                    print("Złe pole")
            else:
                print("Złe pole")

def selectPodwodne(boardPlayer):
        pos = pygame.mouse.get_pos()
        
        x=pos[0]//B_SIZE_W-6
        y=pos[1]//B_SIZE_H
        
        if boardPlayer[y][x]!=5 and boardPlayer[y][x]!=6 and boardPlayer[y][x]!=7:
            boardPlayer[y][x]=7
        else:
            print("Złe pole")


def wybor(boardPlayer):
    suma_l = 0
    for x in boardPlayer:
        for y in x:
            if y == 5:
                suma_l=suma_l+1
    suma_k = 0
    for x in boardPlayer:
        for y in x:
            if y == 6:
                suma_k=suma_k+1
    suma_p = 0
    for x in boardPlayer:
            for y in x:
                if y == 7:
                    suma_p=suma_p+1
               
    if suma_l<ILOSC_LOTNISKOWCOW*3:
        selectLotniskowiec(boardPlayer)
    else:
        if suma_k<ILOSC_KRAZOWNIKOW*2:
            selectKrazownik(boardPlayer)
        else:
            if suma_p<ILOSC_PODWODNYCH:
                selectPodwodne(boardPlayer)



def checkForWin(board, screen):
    wygrana=False
    ilosc_trafien=0
    win=pygame.image.load("assets\win.png")
    for x in board:
        for n in x: 
            if n=="t":
                ilosc_trafien=ilosc_trafien+1
    if ilosc_trafien==ILOSC_TRAFIEN_P:
        screen.blit(win,(150, 150))
        wygrana=True
    return wygrana
 

def drawBoard(board, screen):
    for j, tile in enumerate(board):
        for i, tile_content in enumerate(tile):
            rect=pygame.Rect(i*B_SIZE_W, j*B_SIZE_H, B_SIZE_W, B_SIZE_H)
            pygame.draw.rect(screen, color(tile_content), rect)
            pygame.draw.rect(screen, BLACK, rect, width=2)

def drawBoardPlayer(board, screen):
    for j, tile in enumerate(board):
        for i, tile_content in enumerate(tile):
            rect=pygame.Rect(i*B_SIZE_W+620, j*B_SIZE_H, B_SIZE_W, B_SIZE_H)
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

    
    ilosc_strzalow_comp=0
    ilosc_trafien_comp=0
    ilosc_strzalow=0
    ilosc_trafien=0
    il_l=0
    check=False
    
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ilosc_strzalow<ILOSC_RUCHOW and checkForWin(boardComp, screen)==False:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        x=pos[0]//B_SIZE_H
                        y=pos[1]//B_SIZE_W
                        

                        for x in boardComp:
                            for n in x: 
                                if n=="t" or n=="p":
                                    check+=1
                        
                        if check > 0:
                            ilosc_strzalow=ilosc_strzalow+1
                            strzelanieComp(boardPlayer, screen)
                            if ilosc_strzalow==1:
                                ilosc_strzalow=ilosc_strzalow+1
                            if ilosc_strzalow_comp==1:
                                ilosc_strzalow_comp=ilosc_strzalow_comp+1
                            ilosc_strzalow_comp=ilosc_strzalow_comp+1
                            
                        else:
                            wybor(boardPlayer)

                        strzelanie(boardComp, pos, screen)
                        
                        


                                            
            


                                
                            
                            



     
                                    


        drawBoard(boardComp, screen)
        drawBoardPlayer(boardPlayer, screen)
        drawText(screen, boardComp, ilosc_strzalow, boardPlayer, ilosc_strzalow_comp)   
        checkForWin(boardComp, screen)

        if ilosc_strzalow==ILOSC_RUCHOW:
            if trafienia(boardPlayer)>trafienia(boardComp):
                lose=pygame.image.load("assets\lose.jpg")
                screen.blit(lose,(460, 150))
            if  trafienia(boardPlayer)<trafienia(boardComp):
                win=pygame.image.load("assets\win.png")
                screen.blit(win, (460, 150))
            if trafienia(boardPlayer)==trafienia(boardComp):
                draw=pygame.image.load("assets\draw.jpg")
                screen.blit(draw, (460, 150))

        pygame.display.update()
        clock.tick(30)


if __name__=="__main__":
    main()


