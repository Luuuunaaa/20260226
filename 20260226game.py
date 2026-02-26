import random

print("🎮 歡迎來到猜數字小遊戲！")
answer = random.randint(1, 10)

# 讓玩家輸入數字
guess = input("請猜一個 1 到 10 之間的數字：")
guess = int(guess)

# 判斷輸贏
if guess == answer:
    print("✨ 太神啦！你猜對了！")
else:
    print(f"💀 猜錯囉，答案是 {answer}。下次再來！")

    