import pygame
import random
pygame.init()
width = 500
hight = 600
first_time=1
window = pygame.display.set_mode((width,hight))
def start_data():
    global bird_img,back_img,x,y,game_over,clock,bird_down,count,rec_x,rec_lenght,score,bird_x
    bird_img = pygame.image.load("Nice.png")
    back_img = pygame.image.load(("the taxies.png"))
    pygame.display.set_caption("Flappy Bird")
    pygame.display.set_icon(bird_img)
    x=1350
    y=250
    game_over = False
    clock = pygame.time.Clock()
    bird_down = 2
    count = 0
    rec_x=500
    rec_lenght = random.randint(100,250)
    score = 0
    bird_x=100
start_data()
def handel_imgs(y):
    global x
    window.blit(back_img, (x-1350, -30))
    window.blit(back_img,(x,-30))
    if(x<=0):
        x=1350
    window.blit(bird_img, (bird_x, y))
def handel_key_events():
    global y
    global bird_down
    global count
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_down =2
                bird_down=-bird_down
                count = 0
def handel_rect():
    global rec_x
    global rec_lenght
    pygame.draw.rect(window,(140,255,100),[rec_x,0,30,rec_lenght])
    pygame.draw.rect(window,(140,255,100),[rec_x,210+rec_lenght,30,hight])
    if rec_x<=-50:
        rec_x=500
        rec_lenght=random.randint(50,350)
def handel_gameover():
    global game_over
    if(rec_x>=110 and rec_x<=100+140):
        if(rec_lenght-10>=y or 210+rec_lenght<=y+90): #90 is image height
            game_over =True
    if(y+95>=hight):
        game_over =True
def print_score():
    global score
    if(rec_x==100):
        score=score+100
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Score={score}", True, (0,23,0), (45,90,255))
    window.blit(text, (30,30))

def game():
    global y,clock,x,bird_down,count,rec_x,first_time
    while not game_over:
        handel_imgs(y)
        handel_key_events()
        handel_rect()
        print_score()
        handel_gameover()
        clock.tick(120)
        #for image
        if score>200:
            x-=1.25
        elif score>400:
            x-=1.5
        elif score>700:
            x-=6
        else:
            x -= 1
        #for bird
        
        y = y + bird_down
        if y<0:
            y=0
        if count>=40:
            bird_down =2
        count+=1
        #for rectangle
        if score>200:
            rec_x-=1.25
        elif score>400:
            rec_x-=1.5
        elif score>700:
            rec_x-=6
        else:
            rec_x-=1
        pygame.display.update()
        first_time=0
if first_time ==1:
    game()
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global end
            end=True
            game_over=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_data()    
                game()
                
    '''if bird_x>=50:
    bird_x-=0.25
    if y<=hight+100:
        y+=1
    window.blit(bird_img,(bird_x,y))'''
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Game over!! Score={score}", True, (0, 0, 0), (255, 255, 255))
    text2 = font.render(f"To Play again Press Enter", True, (0, 0, 0), (255, 255, 255))
    window.blit(text, (80, 300))
    window.blit(text2,(60,340))
    pygame.display.update()
    



