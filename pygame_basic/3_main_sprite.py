import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game Jay")

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

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창 닫기 버튼 누를 때 실행됨
            running = False #게임이 진행중이 아님

    screen.blit(background, (0,0)) #배경 그리기 -> 좌표는 왼쪽 상단 기준.

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기 -> 좌표는 왼쪽 상단 기준.

    pygame.display.update() #게임 화면 계속 업데이트하면서 다시 그려줘야 함

pygame.quit()