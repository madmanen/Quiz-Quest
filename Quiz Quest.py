import pygame
pygame.init()

HEIGHT=800
WIDTH=800
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Quiz Quest')

END_WIDTH = 80
END_HEIGHT =80

PLAYER_WIDTH=40
PLAYER_HEIGHT=60
PLAYER_VEL=10
#player sprites
p_rw1=pygame.transform.scale(pygame.image.load('player_image (9).png'),(PLAYER_WIDTH,PLAYER_HEIGHT))
p_rw2=pygame.transform.scale(pygame.image.load('player_image (8).png'),(PLAYER_WIDTH,PLAYER_HEIGHT))
p_lw1=pygame.transform.scale(pygame.image.load('player_image.png'),(PLAYER_WIDTH,PLAYER_HEIGHT))
p_lw2=pygame.transform.scale(pygame.image.load('player_image.png(7).png'),(PLAYER_WIDTH,PLAYER_HEIGHT))
p_fw1=pygame.transform.scale(pygame.image.load('player_image (4).png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
p_fw2=pygame.transform.scale(pygame.image.load('player_image (6).png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
p_bw1=pygame.transform.scale(pygame.image.load('player_image (2).png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
p_bw2=pygame.transform.scale(pygame.image.load('player_image (1).png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
current_pi=p_fw1

#NPC sprites
q1_image=pygame.transform.scale(pygame.image.load('q1_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
q2_image=pygame.transform.scale(pygame.image.load('q2_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
q3_image=pygame.transform.scale(pygame.image.load('q3_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
q4_image=pygame.transform.scale(pygame.image.load('q4_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
q5_image=pygame.transform.scale(pygame.image.load('q5_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
tutorial_image=pygame.transform.scale(pygame.image.load('tutorial_image.png'),(PLAYER_WIDTH, PLAYER_HEIGHT))
end_image=pygame.transform.scale(pygame.image.load('end_image.png'),(END_WIDTH, END_HEIGHT))

#Defines font for game text
FONT=pygame.font.SysFont('comicsans', 30)

#Loads and scales background map images
bg1=pygame.transform.scale(pygame.image.load('pixil-frame-0.png'),(WIDTH,HEIGHT))
bg2=pygame.transform.scale(pygame.image.load('pixil-frame-01.png'),(WIDTH,HEIGHT))
bg3=pygame.transform.scale(pygame.image.load('pixil-frame-0(1).png'),(WIDTH,HEIGHT))
bg4=pygame.transform.scale(pygame.image.load('pixil-frame-0(2)1.png'),(WIDTH,HEIGHT))
bg5=pygame.transform.scale(pygame.image.load('pixil-frame-11.png'),(WIDTH,HEIGHT))
bg6=pygame.transform.scale(pygame.image.load('pixil-frame-0(1)1.png'),(WIDTH,HEIGHT))
current_bg=bg1

#Text parameters
text_color=(0,0,0)
font = pygame.font.Font(None, 30)
line_spacing=1


#Writes text with multiple lines
def write(text, x, y, font, color, line_spacing):
    lines = text.splitlines()  # Split text into lines
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + i * (font.get_height() + line_spacing)))

#Dialog
easter_egg='fire from heat'
credits_text='Max------Programmer\nMax------Game Tester\nMax------Digital artist\nMax------Project Lead'
tutorial_text='Welcome to Quiz Island\nUse the arrow keys to move around\nfind the questers and answer their questions.'
q1_text='What is 2*4?'
q2_text='Who is the president of the USA?'
q3_text='Who made this game?'
q4_text='Is this game cool?'
q5_text='Coffee or tea?'
answer= ""
win_text='Congratulations!!\nYou beat the game :3'

#text size
win_text_width, win_text_height = font.size(win_text)
tutorial_text_width, tutorial_text_height = font.size(tutorial_text)
q1_text_width, q1_text_height = font.size(q1_text)
q2_text_width, q2_text_height = font.size(q2_text)
q3_text_width, q3_text_height = font.size(q3_text)
q4_text_width, q4_text_height = font.size(q4_text)
q5_text_width, q5_text_height = font.size(q5_text)

#Draws everything in the game
def draw(player, current_bg, tutorial,point, q1, q2,q3,q4,q5, answer, end, current_pi):
    screen.blit(current_bg,(0,0))

    if current_bg == bg1:
        if point == 5:
            screen.blit(end_image,(end))
            if end.colliderect(player): #Checks when player touches end
                write(win_text, WIDTH-win_text_width, HEIGHT/2-win_text_height, font, (0, 255, 0), line_spacing)
                pygame.display.flip()
                pygame.time.delay(1000)
                screen.fill(0)
                write(win_text, WIDTH / 2,0, font, (0, 255, 0), line_spacing)
                write(credits_text, WIDTH / 2,HEIGHT/2, font, (255, 255, 255), line_spacing)
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.quit()
        screen.blit(tutorial_image,(tutorial))
        if tutorial.y+PLAYER_HEIGHT>=player.y and tutorial.colliderect(player):
            write(tutorial_text,tutorial.centerx-(tutorial_text_width-WIDTH),tutorial.top-(tutorial_text_height+line_spacing)*3, font, text_color, line_spacing)


    if current_bg == bg2:
        screen.blit(q2_image,(q2))
        if q2.y+PLAYER_HEIGHT>=player.y and q2.colliderect(player):
            write(q2_text,q2.centerx-q2_text_width,q2.top-q2_text_height,font, text_color, line_spacing)

    if current_bg == bg3:
        screen.blit(q1_image,(q1))
        if q1.y + PLAYER_HEIGHT >= player.y and q1.colliderect(player):
            write(q1_text,q1.centerx-q1_text_width,q1.top-q1_text_height, font, text_color, line_spacing)

    if current_bg == bg4:
        screen.blit(q3_image,(q3))
        if q3.y+PLAYER_HEIGHT>=player.y and q3.colliderect(player):
            write(q3_text,q3.centerx-q3_text_width,q3.top-q3_text_height, font, text_color, line_spacing)

    if current_bg == bg5:
        screen.blit(q4_image,(q4))
        if q4.y+PLAYER_HEIGHT>=player.y and q4.colliderect(player):
            write(q4_text,q4.centerx-q4_text_width,q4.top-q4_text_height, font, text_color, line_spacing)

    if current_bg == bg6:
        screen.blit(q5_image,(q5))
        if q5.y+PLAYER_HEIGHT>=player.y and q5.colliderect(player):
            write(q5_text,q5.centerx-q5_text_width,q5.top-q5_text_height, font, text_color, line_spacing)

    screen.blit(current_pi,(player))

    point_text=font.render(f'Your score is: {point}', True, text_color)
    screen.blit(point_text,(10,10))

    write(answer, player.centerx, player.top-20, font, text_color, line_spacing)
    if answer=='heat from fire':
        write(easter_egg,player.centerx, player.top-50, font, (0,50,255), line_spacing)

    pygame.display.update()


def main(current_bg, answer, current_pi):
    point = 0
    end=pygame.Rect(WIDTH/2, HEIGHT/2,END_WIDTH, END_HEIGHT )
    player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    tutorial=pygame.Rect(400, HEIGHT/2-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    q1=pygame.Rect(WIDTH/2, HEIGHT/2-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    q2=pygame.Rect(WIDTH-100, HEIGHT/1.5-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    q3=pygame.Rect(WIDTH/3, HEIGHT-PLAYER_HEIGHT*5, PLAYER_WIDTH, PLAYER_HEIGHT)
    q4=pygame.Rect(WIDTH/2.5, HEIGHT-PLAYER_HEIGHT**1.5, PLAYER_WIDTH, PLAYER_HEIGHT)
    q5=pygame.Rect(WIDTH/1.5, HEIGHT-PLAYER_HEIGHT*10, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock=pygame.time.Clock()

    have_answered_q1=False
    have_answered_q2=False
    have_answered_q3=False
    have_answered_q4=False
    have_answered_q5=False

    run=True
    while run:
        pygame.time.delay(80)

        # Checks for pressing the x at top of window, to end program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN:
                    if current_bg==bg3 and q1.colliderect(player) and have_answered_q1 == False and (answer == "8"):
                        point += 1
                        have_answered_q1 = True
                        answer = ""

                    elif current_bg==bg2 and q2.colliderect(player) and have_answered_q2 == False and (answer == "Trump" or answer == 'trump' or answer == 'donald trump' or answer == 'Donald trump' or answer == 'Donald Trump'):
                        point += 1
                        have_answered_q2 = True
                        answer = ""

                    elif current_bg==bg4 and q3.colliderect(player) and have_answered_q3 == False and (answer == "max" or answer == 'Max' or answer == 'snakequeen' or answer == 'SnakeQueen'):
                        point += 1
                        have_answered_q3 = True
                        answer = ""

                    elif current_bg==bg5 and q4.colliderect(player) and have_answered_q4 == False and (answer == "yes" or answer == 'Yes'):
                        point += 1
                        have_answered_q4 = True
                        answer = ""

                    elif current_bg==bg6 and q5.colliderect(player) and have_answered_q5 == False and (answer == "Coffee" or answer == 'coffee' or answer == 'Tea' or answer == 'tea'):
                        point += 1
                        have_answered_q5 = True
                        answer = ""
                    else:
                        answer = ''

                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]
                else:
                    answer += event.unicode

        # Checks for button inputs to move player
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x-=PLAYER_VEL
            if current_pi==p_lw1:
                current_pi=p_lw2
            else:
                current_pi=p_lw1
        if keys[pygame.K_RIGHT]:
            player.x+=PLAYER_VEL
            if current_pi==p_rw1:
                current_pi=p_rw2
            else:
                current_pi=p_rw1
        if keys[pygame.K_UP]:
            player.y-=PLAYER_VEL
            if current_pi==p_fw1:
                current_pi=p_fw2
            else:
                current_pi=p_fw1
        if keys[pygame.K_DOWN]:
            player.y+=PLAYER_VEL
            if current_pi==p_bw1:
                current_pi=p_bw2
            else:
                current_pi=p_bw1

        # Checks when player reaches top of the screen
        if player.y<=0:
            if current_bg==bg1:
                current_bg=bg2
                player.y = HEIGHT-1
            elif current_bg==bg3:
                current_bg=bg5
                player.y=HEIGHT-1
            elif current_bg==bg4:
                current_bg=bg6
                player.y=HEIGHT-1

            # Checks when player reaches top end
            elif current_bg==bg2:
                player.y=0
            elif current_bg==bg5:
                player.y=0
            elif current_bg==bg6:
                player.y=0

        # Checks when player reaches bottom of screen
        elif player.y>=HEIGHT:
            if current_bg==bg2:
                current_bg=bg1
                player.y=1
            elif current_bg==bg5:
                current_bg=bg3
                player.y=1
            elif current_bg==bg6:
                current_bg=bg4
                player.y=1

        # Checks when player reaches bottom end
        elif player.y>=HEIGHT-PLAYER_HEIGHT and current_bg==bg1:
            player.y=HEIGHT-PLAYER_HEIGHT
        elif player.y>=HEIGHT-PLAYER_HEIGHT and current_bg==bg3:
            player.y=HEIGHT-PLAYER_HEIGHT
        elif player.y>=HEIGHT-PLAYER_HEIGHT and current_bg==bg4:
            player.y=HEIGHT-PLAYER_HEIGHT

        # Checks when player reaches right side of screen
        elif player.x>=WIDTH:
            if current_bg==bg1:
                current_bg=bg4
                player.x=1
            elif current_bg==bg3:
                current_bg=bg1
                player.x=1
            elif current_bg==bg5:
                current_bg=bg2
                player.x=1
            elif current_bg==bg2:
                current_bg=bg6
                player.x=1

        # Checks when player reaches right end
        elif player.x>=WIDTH-PLAYER_WIDTH and current_bg==bg4:
            player.x=WIDTH-PLAYER_WIDTH
        elif player.x>=WIDTH-PLAYER_WIDTH and current_bg==bg6:
            player.x=WIDTH-PLAYER_WIDTH

        # Checks when player reaches left side of screen
        elif player.x<=0:
            if current_bg==bg1:
                current_bg=bg3
                player.x=WIDTH-1
            elif current_bg==bg4:
                current_bg=bg1
                player.x=WIDTH-1
            elif current_bg==bg6:
                current_bg=bg2
                player.x=WIDTH
            elif current_bg==bg2:
                current_bg=bg5
                player.x=WIDTH-1

            # Checks when player reaches left end
            elif current_bg==bg3:
                player.x=0
            elif current_bg==bg5:
                player.x=0

        draw(player, current_bg, tutorial,point, q1,q2,q3,q4,q5, answer, end, current_pi)

    pygame.quit()

if __name__ == '__main__':
    main(current_bg, answer, current_pi)