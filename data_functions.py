
#funkcja wykonuje zapis do pliku: wynik punktowy , poziom gry , czas trwania gry
def input(score, time, level):
	file = open('data.txt','a')
	file.write('  '+str(score)+'   		    	  '+str(level)+' 		    	   '+str(time)+'\n')
	file.close()
	return


#funkcja wykonuje odczyt z pliku danych i zwraca zmienną w której te dane są zapisane
def output():
	file = open('data.txt','r')
	text='Punkty 		  Poziom        Czas\n'
	x = file.readlines()
	for i in range(len(x),0,-1):
		text=text+x[i-1]+'\n'
	return text



'''# importing the required modules  
import pygame               # importing the pygame module  
from pygame.locals import * # importing everything from the pygame.locals module  
import random      
import time
import Bird_Class
import Button_Class 
import Ptera_Class
import data_functions
        # importing the random module  



# using the init() function to initialize the pygame window  

  
  

def main(freq,level):
     
    pygame.init()
    # creating an object of the Clock() class of the pygame.time module  
    game_clock = pygame.time.Clock()  
      
    # defining the fps for the game  
    game_fps = 60  
  
    # defining the width and height of the game screen
    global display_screen  
    global SCREEN_WIDTH 
    global SCREEN_HEIGHT
    global birdGroup
    global pteraGroup
    global bird,screen,startButton
    SCREEN_HEIGHT = 720 
    SCREEN_WIDTH = 600     
    global timer
    global check
    # using the set_mode() function of the pygame.display module to set the size of the screen  
    display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
      
    # setting the title of the application using the set_caption() function  
    pygame.display.set_caption('Flappy Bird nad Pteras - ArseniiBrazhnyk')  
      
    # defining the font style  
    fontStyle = pygame.font.SysFont('arial black', 55)  
      
    # defining the font color  
    black = (0, 0, 0) 
       
    # declaring and initializing the game variables  
    baseScroll = 0  
    scrollSpeed = 4  
    birdFlying = False   
    gameOver = False  
    #pipeGap = 150  
    pteraFrequency = freq # milliseconds  
    lastPtera = pygame.time.get_ticks() - pteraFrequency  
    playerScore = 0  
    passPtera = False  
    check = True  
    # loading images  
    background = pygame.image.load('images/background.png')  
    base = pygame.image.load('images/base.png')  
    button = pygame.image.load('images/restart.png')
    button_menu = pygame.image.load('images/menu.png')   
   
    # creating a class of the pygame's Sprite() class to display the bird  
    restartButton = Button_Class.Button(175, 350, button,display_screen)
    menuButton = Button_Class.Button(325,350,button_menu,display_screen)
 

    


    


        # creating the objects of the Group() class of the pygame.sprite module  
    birdGroup = pygame.sprite.Group()  
    pteraGroup = pygame.sprite.Group()  
          
        # creating an object of the FlappyBird() class with  
    bird = Bird_Class.FlappyBird(50, int(SCREEN_HEIGHT / 2))  
          
        # using the add() function to add the object of the FlappyBird() class to the group  
    birdGroup.add(bird)  
          
        # creating the restart button instance  

        # declaring a variable and initializing its value with True  
    game_run = True  
    timer = time.time()
        # using the while loop  
    while game_run: 
         
        game_clock.tick(game_fps)
            # setting the fps of the game  
        #game_clock.tick(game_fps)  
          
            # drawing the background  
        display_screen.blit(background, (0, 0))  
          
            # drawing the bird  
        birdGroup.draw(display_screen)  
          
            # calling the update() function  
        birdGroup.update(birdFlying,gameOver)  
          
            # drawing the pipes  
        pteraGroup.draw(display_screen)  
          
            # drawing the base  
        display_screen.blit(base, (baseScroll, 576))  
          
            # checking the score  
        if len(pteraGroup) > 0:  
                # checking if the bird is over the pipe and passed the left side of it but not the right size  
            if birdGroup.sprites()[0].rect.left > pteraGroup.sprites()[0].rect.left \
                and birdGroup.sprites()[0].rect.left < pteraGroup.sprites()[0].rect.right \
                    and passPtera == False:
                  
                        # setting the boolean value to true  
                        passPtera = True  
                  
        if passPtera == True:  
            try: 
                if birdGroup.sprites()[0].rect.left > pteraGroup.sprites()[0].rect.right:
                    # incrementing the score by 1
                    playerScore += 1
                    passPtera=False   
                    # setting the boolean value back to false 
            except IndexError  :
                playerScore+=1
                playerScore=resetGame()
            #except TypeError:
            #    playerScore+=1
            #    playerScore=resetGame()

                
          
            # calling the drawText() function to display the calculated score on the screen  
        drawText(str(playerScore), fontStyle, black, int(SCREEN_WIDTH / 2), 15)  
          
            # looking for collision  
        if pygame.sprite.groupcollide(birdGroup, pteraGroup, False, False) or bird.rect.top < 0:  
            gameOver = True  
          
            # checking if bird has hit the ground  
        if bird.rect.bottom >= 576:  
            gameOver = True  
            birdFlying = False  
            #sprawdzamy czy ptaszek udzerzył się w górną część ekranu    
        if bird.rect.top <= 0:  
            gameOver = True  
            birdFlying = False     





          
            # checking if the game is not over  
        if gameOver == False and birdFlying == True:  
            
                # generating new pipes  
            timeNow = pygame.time.get_ticks() 
            if timeNow - lastPtera > pteraFrequency:  
                ptera_x = random.randint(650,700)
                ptera_y = random.randint(40, 500)  
        
                ptera = Ptera_Class.Ptera(ptera_x, ptera_y,10)

                pteraGroup.add(ptera)  
                
                lastPtera = timeNow  
            
                # scrolling the base  
            baseScroll -= scrollSpeed  
            if abs(baseScroll) > 70:  
                baseScroll = 0  
                      
                # calling the update() function  
            pteraGroup.update()  
          
            # checking if the game over and reset  
        if gameOver == True:
            
            if check == True:
                print(time.time()-timer)
                timer=time.time()-timer
                data_functions.input(playerScore, round(timer,2),level)
                data_functions.output()
                check = False
            if restartButton.draw() == True:  
                gameOver = False  
                playerScore = resetGame()
                timer, check = resetVariables()

            if menuButton.draw() == True:
                break  
          
            # using the for loop to iterate through the events of the game  
        for event in pygame.event.get():  
                # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
                
            if event.type == QUIT:  
                game_run = False

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                birdFlying = False
                
                

            if event.type == KEYDOWN and event.key == K_SPACE and birdFlying == False:
                quit()
                # setting the variable value to True if the event's type is equivalent to pygame's MOUSEBUTTONDOWN constant, the bird is not flying and game is not over  
            if event.type == MOUSEBUTTONDOWN and birdFlying == False and gameOver == False:  
                birdFlying = True  
          
            # using the update() function of the pygame.display module to update the events of the game  
        pygame.display.update()  
          
        # using the quit() function to quit the game  

    return 0





def drawText(text, fontStyle, textColor, x_coordinate, y_coordinate): 
    # using the render() function to render the text as image  
    image = fontStyle.render(text, True, textColor)  
  
    # using the blit() function to display the image on the screen  
    display_screen.blit(image, (x_coordinate, y_coordinate))  
  
# defining a function to reset the game  
def resetGame():  
    # calling the empty() function to remove all the sprites  
    pteraGroup.empty()
    birdGroup = pygame.sprite.Group()  

    # describing the coordinates for the rectangle placement  
    bird.rect.x = 50  
    bird.rect.y = int(SCREEN_HEIGHT / 2)  
    # setting the player score to 0  
    playerScore = 0
    # returning the score  
    return playerScore

def resetVariables():
    return time.time(), True

# if __name__=='__main__':
# # start programu
#     main()
# pygame.quit()  


'''