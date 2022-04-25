import pygame as pg
import time
import sys
from pygame.locals import *

#variables

winner=None #stores the winner
draw=False #stores value to check for draw or win
turn="red" #stores whose turn it is
play_again=False #stores the condition if they want to play again
red=(255,0,0) #stores the red rgb code
blue=(0,0,255) #stores the blue rgb code
black=(0,0,0) #stores the black rgb code
white=(255,255,255) #stores the white rgb code
line=50
#the actual size of the board is only 10 rows and 10 columns but we are taking 4 extra rows and columns on each side to make checking for a win or draw easier
board=[[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,\
      [None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,\
      [None]*18,[None]*18,[None]*18,[None]*18]

#display window
pg.init()
fps=30
clock=pg.time.Clock()
screen=pg.display.set_mode((500,600))
pg.display.set_caption("CONNECT 4")
opening_img=pg.image.load('opening.jpg')
opening_img=pg.transform.scale(opening_img,(500,600))

#opening
def opening():
    screen.blit(opening_img,(0,0)) #loads the connect 4 image
    pg.display.update()
    time.sleep(1)
    screen.fill(white) #fills the scree with white

    #to draw row lines
    for x in range(1,11):
        pg.draw.line(screen,blue,(0,line*x),(500,line*x),3)

    #to draw column lines
    for x in range(1,10):
        pg.draw.line(screen,blue,(line*x,0),(line*x,500),3)

    pg.display.update()
    status() #call status to display only whose turn and not if it is a win or draw because game has just started

#displaying the message
def status():
    global draw,winner
    #message to be displayed
    if winner is None: #if there is no winner display whose turn
        message=turn + "'s turn"
    elif(winner is not None): #if there is a winner display the winner
        message=winner + " wins!"
    elif draw is True: #if game is a draw display it is a draw
        message="It's a draw"

    #displaying the message
    font=pg.font.Font(None,30)
    img=font.render(message,1,white)
    screen.fill((0,0,0),(0,500,600,100))
    img_rect=img.get_rect(center=(250,550))
    screen.blit(img,img_rect)
    pg.display.update()

#if game is a draw or someone wins
def reset():
    #initialize all variables to their original values
    global board,winner,draw,turn

    turn="red"
    winner=None
    draw=False
    board=[[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18,[None]*18]
    pg.display.update()
    time.sleep(2)
    opening() #call opening() to load the window and start the game


def game():

    global board,winner,draw,turn

    if event.type==MOUSEBUTTONDOWN:
        #getting mouse click coordinates
        x,y=pg.mouse.get_pos()

        #column corresponding to the click
        if(x<50):col=4
        elif(x<50*2):col=5
        elif(x<50*3):col=6
        elif(x<50*4):col=7
        elif(x<50*5):col=8
        elif(x<50*6):col=9
        elif(x<50*7):col=10
        elif(x<50*8):col=11
        elif(x<50*9):col=12
        else:col=13

        #getting the row which is empty in the corresponding column and drawing the player's coin
        for row in range(13,3,-1):
            #if the corresponding box is clear and game is not over by a draw or a win then do the corresponding actions
            if board[row][col] is None and winner is None and draw is False:

                #getting x coordinate for origin of circle
                if(col==4):center_x=25
                elif(col==5):center_x=75
                elif(col==6):center_x=125
                elif(col==7):center_x=175
                elif(col==8):center_x=225
                elif(col==9):center_x=275
                elif(col==10):center_x=325
                elif(col==11):center_x=375
                elif(col==12):center_x=425
                else:center_x=475

                #getting y coordinate for origin of circle
                if(row==4):center_y=25
                elif(row==5):center_y=75
                elif(row==6):center_y=125
                elif(row==7):center_y=175
                elif(row==8):center_y=225
                elif(row==9):center_y=275
                elif(row==10):center_y=325
                elif(row==11):center_y=375
                elif(row==12):center_y=425
                else:center_y=475

                #setting the corresponding box to the player's color
                board[row][col]=turn

                #if red's turn
                if(turn=="red"):
                    turn="black" #changes the turn
                    pg.draw.circle(screen,red,(center_x,center_y),15,0) #draws the corresponding player's coin
                    pg.display.update()
                    break
                #if black's turn
                elif(turn=="black"):
                    turn="red" #changes the turn
                    pg.draw.circle(screen,black,(center_x,center_y),15,0) #draws the corresponding player's coin
                    pg.display.update()
                    break
                #break statement in the if and elif block is used to break the for loop if the corresponding player's coin is drawn
                #if break is missed it'll continue to draw the coin alternating between red and black for the rest of the empty boxes in that column

        #checks for a win
        #winner=board[row][col] sets the winner according to the player's color in the corresponding box

        #checks columns
        if(board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]):#checks columns to the right
            winner=board[row][col]
        elif(board[row][col] == board[row][col-1] == board[row][col-2] == board[row][col-3]):#checks columns to the left
            winner=board[row][col]
        elif(board[row][col]==board[row][col-1]==board[row][col+1]==board[row][col+2]): #checks 1 column to the left and 2 columns to the right
            winner=board[row][col]
        elif(board[row][col]==board[row][col-1]==board[row][col+1]==board[row][col-2]): #checks 2 columns to the left and 1 column to the right
            winner=board[row][col]

        #checks row
        elif(board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]):#checks rows going down
            winner=board[row][col]

        #checks diagonals
        elif(board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]):#checks diagonal to the right and down
            winner=board[row][col]
        elif(board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]):#checks diagonal to the right and top
            winner=board[row][col]
        elif(board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]):#checks diagonal to the left and down
            winner=board[row][col]
        elif(board[row][col] == board[row-1][col-1] == board[row-2][col-2] == board[row-3][col-3]):#checks diagonal to the left and top
            winner=board[row][col]

        #checks diagonals when the coin is inserted in the 2nd or 3rd place
        elif(board[row][col]==board[row+1][col-1]==board[row-1][col+1]==board[row-2][col+2]): #checks diagonal when coin inserted in 2nd place
            winner=board[row][col]
        elif(board[row][col]==board[row-1][col+1]==board[row+1][col-1]==board[row+2][col-2]): #checks diagonal when coin inserted in 3nd place
            winner=board[row][col]
        elif(board[row][col]==board[row-1][col-1]==board[row+1][col+1]==board[row+2][col+2]): #checks diagonal when coin inserted in 2nd place
            winner=board[row][col]
        elif(board[row][col]==board[row-1][col-1]==board[row-2][col-2]==board[row+1][col+1]): #checks diagonal when coin inserted in 3nd place
            winner=board[row][col]

        #checks for a draw if there is no winner
        if winner is None:
            count=0 #variable to keep count of occupied boxes
            #2 for loops to go through each box
            for C in range(4,14):
                for R in range(4,14):
                    if(board[R][C] is not None):#if the box is occupied increase the count by 1
                        count+=1
            if(count==100):#since there are 100 boxes in total, if count=100 it means that all the boxes are occupied and there is no winner,so set draw=True
                draw=True

        status() #call status to display whose turn or if it is a win or draw

#call opening() to load the window and start the game
opening()


while(True):

    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            sys.exit()
        #to start the game call game()
        game()
        if(winner is not None or draw is True):
            reset()

    pg.display.update()
    clock.tick(fps)