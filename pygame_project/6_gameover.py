import os
import pygame
#####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ballon Game")

# FPS 설정
clock = pygame.time.Clock()
#####################################################################################

## 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트, 시간 등)
current_path = os.path.dirname(__file__) #현재 파일 위치 변환
image_path = os.path.join(current_path, "images")

# 배경화면 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))

stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0
# 캐릭터 속도
character_speed = 10

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능 -> 리스트 형태로 정의
weapons = []

# 무기 스피드
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 리스트로 따로 처리)
# 공 이미지 처리
ball_images = [
    pygame.image.load(os.path.join(image_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_path,"balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # 공이 바닥에 튕기고 하늘로 가야함으로 마이너스를 사용(y값이 감소해야함)

# 실제 공들
balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6, #처음에 살짝 위로 올라가는 모먼트를 만들어주기 위함
    "init_spd_y" : ball_speed_y[0]}) # y최초 속도

#사라질 공, 무기들 인덱스 변수
weapon_to_remove = -1
ball_to_remove = -1

# Font 정의
game_font = pygame.font.Font(None, 40)

# 시간 설정
total_time = 30
start_ticks = pygame.time.get_ticks()


# 게임 종료 메시지 / Time Out, Mission Complete, Game Over
game_result = "Game Over"

running = True
while running:
    dt = clock.tick(60) # 원하는 프레임 수 입력 # print(clock.get_fps())

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE : # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) #리스트 형태로 하나의 무기를 추가 해줌

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    # 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 발사
    
    # 벽에 닿으면 무기 삭제
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ]
    # 위와 같이 하면 0보다 작거나 같은 애들만 weapons에 남게됨!

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls) : # enumerate -> 리스트 인덱스, 값 형태로 뽑아줌
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 벽에 닿았을 때 공 가로 방향 이동 위치 변경 (튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else : # 그 외의 모든 경우에는 속도를 증가 -> 포물선을 그리며 올라갔다 내려오게 함
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
 
    # 4. 충돌 처리
    # 1) 캐릭터와 공의 충돌

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
   
    for ball_idx, ball_val in enumerate(balls) : # enumerate -> 리스트 인덱스, 값 형태로 뽑아줌
        ball_pos_x =ball_val["pos_x"]
        ball_pos_y =ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 2) 무기와 공의 충돌
        for weapon_idx, weapon_val in enumerate(weapons) :
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect() # weapon 이미지에서 rect 정보를 따옴
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            # 충돌 처리
            if weapon_rect.colliderect(ball_rect) :
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                # 가장 작은 크기의 공이 아니라면 다음 단계의 공 두개로 나눠주기
                if ball_img_idx < 3 :
                    # 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]


                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 기존 공의 가운데에서 새로운 공 생성
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" : -3,
                        "to_y" : -6, 
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})

                    # 오른쪽으로 튕겨나가는 작은 공 -> to_x 양수로 설정
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1,
                        "to_x" :  3,
                        "to_y" : -6, 
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})

                break
        else : 
            continue # for문과 함께 동작하여 안에 있는 for가 break를 통해 깨지면 자연스럽게 그 밑에 있는 break로 바깥 쪽 for문도 깸
        break

    # 충돌된 공, 무기 제거 
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    if not balls: # len으로 확인해도 됨
        game_result = "Mission Complete"
        running = False



    # 5. 화면에 그리기 
    screen.blit(background, (0,0)) # 먼저 그려지는 순서로 밑에 있는 레이어로 인식.

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        screen.blit(ball_images[val["img_idx"]], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255)) # 글자 쓰기
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update() # 게임 화면 계속 업데이트하면서 다시 그려줘야 함

msg = game_font.render(game_result, True, (255,255,0)) # yellow
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2))) # 이런 방식도 있군
screen.blit(msg, msg_rect)

pygame.display.update()

pygame.time.delay(1500) # 종료 전 대기

pygame.quit()


# image source
# <a href='https://www.freepik.com/vectors/vintage'>Vintage vector created by stockgiu - www.freepik.com</a>
# <a href='https://www.freepik.com/vectors/background'>Background vector created by brgfx - www.freepik.com</a>
# http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator