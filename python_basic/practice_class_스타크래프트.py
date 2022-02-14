from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("<지상 유닛 이동>\n{0} : {1} 방향으로 이동합니다. [속도 : {2}]\n".format(self.name, location, self.speed))

    def damaged(self, damage):
        self.hp -= damage
        if self.hp <=0:
            print("{0} : {1} 데미지를 입었습니다. 파괴되었습니다.".format(self.name, damage))
        else: 
            print("{0} : {1} 데미지를 입었습니다. [현재 체력 {2}]".format(self.name, damage, self.hp))
# tank1.clocking = True #외부에서 멤버 변수를 추가할 수 있다. 다만 탱크 1에만 적용됨.

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #상속 
        self.damage = damage
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 2, 5)
    
    def stimpack(self):
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족합니다. 스팀팩을 사용할 수 없습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False #현재 시즈모드인지 여부

    def set_seize_mode(self):
        if Tank.seize_developed == False :
            return
        
        #현재 시즈모드가 아니라면 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드라면 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


#공중 일반 유닛
class FlyableUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]\n".format(name,location,self.flying_speed))
 
#공중 공격 유닛
class AttackFlyableUnit(AttackUnit, FlyableUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyableUnit.__init__(self,flying_speed)
    def move(self, location):
        print("<공중 유닛 이동>")
        self.fly(self.name, location)

class Wraith(AttackFlyableUnit):
    clocking_developed = False #클로킹 개발여부

    def __init__(self):
        AttackFlyableUnit.__init__(self,"레이스", 80, 20, 5)
        self.clocking_mode = False

    def set_clocking_mode(self):
        if Wraith.clocking_developed == False :
            return
        
        #현재 클라킹 상태가 아니라면
        if self.clocking_mode == False:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocking_mode = True
        else :
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocking_mode = False

#super().__init__() -> 가장 먼저 받은 부모 클래스만 상속시킴.

def game_start():
    print("3\n2\n1\n게임을 시작합니다.")
def game_over():
    print("player : gg")
    print("[player]님이 게임에서 퇴장하셨습니다.")

#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리
attack_units = [m1,m2,m3,t1,t2,w1]

#전군 이동
for unit in attack_units :
    unit.move("11시")

#탱크 시즈모드 개발 / 레이스 클로킹 개발
Tank.seize_developed = True #모든 탱크 업그레이드
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")
Wraith.clocking_developed = True #모든 레이스 업그레이드
print("[알림] 레이스 클로킹 모드 개발이 완료되었습니다.")

#공격 모드 변환
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.set_clocking_mode()

#전군 공격
for unit in attack_units:
    unit.attack("11시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,51))

#게임 종료
game_over()