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

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창 닫기 버튼 누를 때 실행됨
            running = False #게임이 진행중이 아님

    screen.blit(background, (0,0)) #배경 그리기 -> 좌표는 왼쪽 상단 기준.
    #screen.fill((0,0,255)) #이렇게 rgb값으로 배경 채워 넣을 수도 있음.
    pygame.display.update() #게임 화면 계속 업데이트하면서 다시 그려줘야 함

pygame.quit()