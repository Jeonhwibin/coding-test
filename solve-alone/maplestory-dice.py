import random

# 스탯 종류 : STR, DEX, INT, LUK
# 각 스탯의 min = 4 , max = 13 , total = 25

def roll_dice():
    return random.randint(4, 13)

def generate_stats():
    while True:
        stats = {
            "STR": roll_dice(),
            "DEX": roll_dice(),
            "INT": roll_dice(),
            "LUK": roll_dice()
        }   
        if sum(stats.values()) <= 26:
            return stats
        
print("주사위를 굴립니다")


if __name__ == "__main__":
    stats = generate_stats()
    print(f"결과: {stats}")
