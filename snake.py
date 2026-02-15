import pygame
import time
import random

def hungry_snake():
    pygame.init()
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Hungry Snake!")
    pygame.event.pump()
    clock=pygame.time.Clock()
    

    score=0
    snake_size=20
    color=(random.randint(0,240),random.randint(0,240),random.randint(0,240))
    target_pos=(random.randint(50,550),random.randint(50,450))
    target_size=20
    direction="RIGHT"
    start_time=time.time()
    snake=[pygame.Rect(300, 300, snake_size, snake_size),pygame.Rect(280, 300, snake_size, snake_size),pygame.Rect(260, 300, snake_size, snake_size),pygame.Rect(240, 300,  snake_size, snake_size)]
    head = snake[0]
    window_width=600
    window_height=600
    
    font=pygame.font.Font(None,30)
    start=font.render("Press any button to start the game.",True,(255,255,255))
    instruction=font.render("Instruction:Use the arrow keys to guide the snake ",True,(255,255,255))
    instruction2=font.render("and eat away your worries!",True,(255,255,255))
    instruction3=font.render("!!Stay within the screen, and don't bump into yourself!!",True,(255,255,255))
    waiting=True
    while waiting:
        screen.fill((0,0,0))
        screen.blit(start,(100,200))
        screen.blit(instruction,(40,300))
        screen.blit(instruction2,(170,325))
        screen.blit(instruction3,(40,400))
        pygame.display.flip()
         
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                return
            
            if event.type == pygame.KEYDOWN:
                waiting = False
        
    
    running=True
    
    while running:
        
        screen.fill((0,0,0))
        prev_positions = [seg.copy() for seg in snake]
        
        for s in snake:
            pygame.draw.rect(screen,color,s)
        target = pygame.Rect(target_pos[0], target_pos[1], target_size, target_size)
        pygame.draw.rect(screen,(255,255,255),target)
        
        font=pygame.font.Font(None,36)
        elapsed = int(time.time() - start_time)
        score_text=font.render(f"Score:{score}|Time:{elapsed}",True,(255,255,255))
        screen.blit(score_text,(20,20))
          
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_DOWN and direction!="up":
                    direction="DOWN"
                
                elif event.key== pygame.K_UP and direction!="DOWN":
                    direction="UP"
                
                elif event.key== pygame.K_LEFT and direction!="RIGHT":
                    direction="LEFT"
            
                elif event.key== pygame.K_RIGHT and direction!="LEFT":
                    direction="RIGHT"
                    
        
        if direction=="DOWN":
            snake[0].move_ip(0,20)
        
        if direction=="UP":
            snake[0].move_ip(0,-20)
        
        if direction=="LEFT":
            snake[0].move_ip(-20,0)
        
        if direction=="RIGHT":
            snake[0].move_ip(20,0)
                
        for i in range(1,len(snake)):
            snake[i].topleft = prev_positions[i-1].topleft
            
           
        if head.collidelist(snake[1:]) != -1: 
            running=False
        
        elif head.left<0 or head.right>window_width or head.top<0 or head.bottom>window_height:
            running=False
        
        
        if snake[0].colliderect(target):
            score+=1
            tail = snake[-1]
            snake.append(pygame.Rect(tail.topleft[0], tail.topleft[1], 10,10))
            color=(random.randint(0,240),random.randint(0,240),random.randint(0,240))
            target_pos=(random.randint(50,550),random.randint(50,450))
            
         
    
        pygame.display.flip()
        clock.tick(10)
    
        
            
    screen.fill((0,0,0))
    font=pygame.font.Font(None,50)
    text=font.render(f"Well done!Final Score:{score}",True,(255,255,255))
    screen.blit(text,(80,300))
    pygame.display.flip()
    pygame.time.wait(3000)
    
    pygame.quit()

if __name__ == "__main__":    
    hungry_snake()
            
            