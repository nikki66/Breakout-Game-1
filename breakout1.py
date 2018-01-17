from SimpleGraphics import *
from time import sleep
from random import randint, random

setAutoUpdate(False)



def main():
        resize(600,600)
        background("black")

        #paddle
        x = getWidth()/2
        y = 11*getHeight()/12
        dx = 0
        dy = 0
        size1 = 100
        size2 = 30
        helpsize = size1*2
        halfsize=int(((size1)/2)*2)


        #bouncing ball
        ball_x, ball_y = randint(50, getWidth()-50), 2*getHeight()/5
        ball_size = 15             
        ball_c = 'yellow'          
        ball_dx = random()*5-2.5   
        ball_dy = random()*5-2.5
        colors = ['yellow']

        # some messages for the game
        score = 0
        left = 3
        setColor('white')

        

        while not closed():
                clear()
                
                setColor(ball_c)
                ellipse(ball_x, ball_y, ball_size, ball_size)
                
                setColor('white')
                rect(x-size1/2,y,size1,size2)
                text(75,20, "Number of balls left: " + str(left))
                text(75,40, "Score: " + str(score))

                #keys
                
                keys = getHeldKeys()
                step = 0.03

                if "Left" in keys:
                        dx = dx - step
                elif "Right" in keys:
                        dx = dx + step
               

                x = x+dx
                y = y+dy

                #help function
                if "h" in keys:
                        size1 = helpsize
                if 'h'not in keys:
                        
                        size1 =halfsize

                #paddle movement
                
                if x > getWidth()- size1/2:
                        x = getWidth()-size1/2
                elif x < size1/2:
                        x = size1/2

                #ball bouncing movement
                
                ball_y = ball_y + ball_dy
                ball_x = ball_x + ball_dx
                

                if ball_y < ball_size/2:
                        ball_dy = -ball_dy
                        ball_y = ball_y + ball_dy
                        ball_x = ball_x + ball_dx
                if ball_x > getWidth() - ball_size/2:
                        ball_dx = -ball_dx
                        ball_y = ball_y + ball_dy
                        ball_x = ball_x + ball_dx
                if ball_x < ball_size/2:
                        ball_dx = -ball_dx
                        ball_y = ball_y + ball_dy
                        ball_x = ball_x + ball_dx
                                   
                        
                #Collusion
                if ball_x > x and ball_x < x + size1 or ball_x + ball_size/2 > x and ball_x + ball_size/2 < x + size1:
                    if ball_y > y and ball_y < y + size2 or ball_y + ball_size/2 > y and ball_y + ball_size/2 < y + size2:
                        ball_dy = -ball_dy
                        
                #goes out
                def results(left,score):
                        while left > 1 :
                                score = score
                                left = left - 1
                                return(left,score)
                        else:
                                return(-1,score)                    
        
                
                if ball_y > getHeight()- ball_size/2:
                        ball_x, ball_y = randint(50, getWidth()-50), 2*getHeight()/5
                        left=results(left,score)[0]
                if left==-1:
                        break
                        
        
                                  
       















if __name__ == "__main__":
	main()
	
