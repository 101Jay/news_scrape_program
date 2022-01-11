## Python_with_nado
##### Lecture_from : [NadoCoding_Youtube](https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw/featured)

#### Frame Source
```python
import pygame

pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Jay")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

pygame.quit()
```

* Index
  * background
  * keyevent / weapon
  * ball_movement
  * collision
  * ball_devision
  * final_version
