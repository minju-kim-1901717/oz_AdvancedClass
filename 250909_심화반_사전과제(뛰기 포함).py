class Bird:
    def __init__(self, name, sound, fly, speed):
        self.name = name
        self.sound = sound   
        self.fly = fly
        self.speed = speed

    def make_sound(self):
        print(f"{self.name}(이)가 '{self.sound}' 울음소리를 냈습니다")

    def do_fly(self):
        print(f"{self.name}(이)가 {self.fly}")

    def run(self):
        weight = int(input("몸무게를 입력하세요: "))
        run = weight * self.speed
        print(f"{self.name}(이)가 {run} 속도로 뛰어갑니다")


# 데이터 : (짹, 날기, 속도)
bird_data = {
    "앵무새": ("앵무", "날고 있습니다", 3),
    "참새" : ("포로롱", "잠깐 날았습니다", 2),
    "비둘기": ("구구", "날 수 있을까요?", 4),
    "닭"   : ("꼬꼬", "나는게 쉽지 않아보입니다", 1),
    "러버덕": ("꽉", "날 수 없습니다", 0)
}

# Bird 객체 -> 딕셔너리 저장 
birds = {name: Bird(name, *data) for name, data in bird_data.items()}

bird, action = input("새와 행동을 입력하세요 : ").split(",")
bird = bird.strip()
action = action.strip()


if bird not in birds:
    print("등록되지 않은 새입니다")
else:
    actions = {
        "짹": birds[bird].make_sound,
        "날기": birds[bird].do_fly,
        "뛰기": birds[bird].run
    }
    func = actions.get(action)
    if func:
        func()
    else:
        print("잘못된 입력")
