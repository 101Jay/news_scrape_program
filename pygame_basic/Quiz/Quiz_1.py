# 검 피하기 게임 

import pygame
import random
#####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("검 피하기 게임")

#fps 설정
clock = pygame.time.Clock()
#####################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트, 시간 등)

# 배경, 캐릭터, 적 이미지 로드
background = pygame.image.load("C:\\Users\\jsKim\\Desktop\\PythonWorkspace\\pygame_basic\\Quiz\\background.png")
character = pygame.image.load("C:\\Users\\jsKim\\Desktop\\PythonWorkspace\\pygame_basic\\Quiz\\character.png")
enemy = pygame.image.load("C:\\Users\\jsKim\\Desktop\\PythonWorkspace\\pygame_basic\\Quiz\\enemy.png")

#캐릭터 크기 설정
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) #위치는 도형의 왼쪽 상단 기준이라는 것 유의!
character_y_pos = screen_height - character_height

#캐릭터 좌우 이동 변수
to_x = 0 

#캐릭터 속도
character_speed = 1

#적 크기 설정
enemy_size = enemy.get_rect().size #이미지 크기 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos =  random.randint(0, (screen_width - enemy_width))
enemy_y_pos = 0

enemy_speed = 0.9

#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 5

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#시작 텍스트 
start_wait = 0
game_start_text = game_font.render("Game Start", True, (255,255,255))
start_text_size = game_start_text.get_rect().size #이미지 크기 구해옴
start_text_width = start_text_size[0]
start_text_height = start_text_size[1]
start_text_x_pos = (screen_width / 2) - (start_text_width / 2)
start_text_y_pos = (screen_height / 2) - (start_text_height / 2)

#종료 텍스트_win
game_over_text = game_font.render("You Win", True, (255,255,255))
text_size = game_over_text.get_rect().size #이미지 크기 구해옴
text_width = text_size[0]
text_height = text_size[1]
text_x_pos = (screen_width / 2) - (text_width / 2)
text_y_pos = (screen_height / 2) - (text_height / 2)

#종료 텍스트_lose
game_over_text_lose = game_font.render("You Lose", True, (255,255,255))
lose_text_size = game_over_text_lose.get_rect().size #이미지 크기 구해옴
lose_text_width = lose_text_size[0]
lose_text_height = lose_text_size[1]
lose_text_x_pos = (screen_width / 2) - (lose_text_width / 2)
lose_text_y_pos = (screen_height / 2) - (lose_text_height / 2)


#이벤트 루프
running = True
while running:
    dt = clock.tick(60) #원하는 프레임 수 입력 # print(clock.get_fps())
    screen.blit(background, (0,0))

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창 닫기 버튼
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP: #눌렀다 떼면 다시 to_x = 0으로 만들어줌
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 

    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt  #프레임 별로 이동속도가 달라지지 않게 하기 위해 dt를 곱해줌

    #검 재생성 처리
    if enemy_y_pos >= screen_height :
        enemy_x_pos =  random.randint(0, (screen_width - enemy_width))
        enemy_y_pos = 0

    #캐릭터 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0 #좌측 화면 밖으로 나가지 않게 함
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width #우측 화면은 기준이 도형의 좌측 상단임을 유의
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos 
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos 

    if character_rect.colliderect(enemy_rect):
        screen.blit(game_over_text_lose, (text_x_pos, text_y_pos)) #레이어가 백그라운드 보다 위로 올라와 있어야 표시가 됨.
        running = False

    #타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #단위가 ms이기 때문에 초단위로 바꿔주기위해 1000으로 나눠줌
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) #출력할 글자 , True, 글자 색상
    
    # 5. 화면에 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기 -> 좌표는 왼쪽 상단 기준.
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10,10))

    # 게임 오버 텍스트 그리기

    if total_time - elapsed_time <= 0 :
        screen.blit(game_over_text, (text_x_pos, text_y_pos))
        running = False

    if start_wait == 0 :
        #시작 대기
        screen.blit(game_start_text, (start_text_x_pos, start_text_y_pos))
        pygame.display.update()
        pygame.time.delay(1000) #ms 단위
        start_wait += 1

    enemy_y_pos += enemy_speed * dt

    pygame.display.update() #게임 화면 계속 업데이트하면서 다시 그려줘야 함

pygame.time.delay(2000) #ms 단위

pygame.quit()