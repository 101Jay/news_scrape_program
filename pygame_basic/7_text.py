import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game Jay")

#fps 설정
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/jsKim/Desktop/PythonWorkspace/pygame_basic/background.png") #역슬래시 처리 유의

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\jsKim\\Desktop\\PythonWorkspace\\pygame_basic\\character.png")

#캐릭터 크기 설정
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) #위치는 도형의 왼쪽 상단 기준이라는 것 유의!
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

#캐릭터 이동 속도
character_speed = 1

#적 캐릭터
enemy = pygame.image.load("C:\\Users\\jsKim\\Desktop\\PythonWorkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #위치는 도형의 왼쪽 상단 기준이라는 것 유의!
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

#적 이동 속도
enemy_speed = 1

#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True
while running:
    dt = clock.tick(60) #원하는 프레임 수 입력
    # print(clock.get_fps())
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창 닫기 버튼 누를 때 실행됨
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: #눌렀다 떼면 다시 to_x / to_y 0으로 만들어줌
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt #프레임 별로 이동속도가 달라지지 않게 하기 위해 dt를 곱해줌
    character_y_pos += to_y * dt 

    #가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0 #좌측 화면 밖으로 나가지 않게 함
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width #우측 화면은 기준이 도형의 좌측 상단임을 유의
        
    #세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    #충돌 처리를 위한 rect 정보 업데이트 -> 지금까지는 화면에 그리기만 한거지, rect 정보 자체를 업데이트 해준 건 아니었음
    character_rect = character.get_rect()
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos 
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos 

    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False
    

    screen.blit(background, (0,0)) #배경 그리기 -> 좌표는 왼쪽 상단 기준.
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기 -> 좌표는 왼쪽 상단 기준.
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #단위가 ms이기 때문에 초단위로 바꿔주기위해 1000으로 나눠줌

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0,0,0))
    #출력할 글자 , True, 글자 색상

    screen.blit(timer, (10,10))

    game_over_text = game_font.render("Game Over", True, (0,0,0))

    if total_time - elapsed_time <= 0 :
        screen.blit(game_over_text, (220, 300))
        running = False

    pygame.display.update() #게임 화면 계속 업데이트하면서 다시 그려줘야 함

pygame.time.delay(2000) #ms 단위

pygame.quit()