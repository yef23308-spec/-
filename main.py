import random


def check_guess(secret_number, guess):
    if guess < secret_number:
        return "low"
    if guess > secret_number:
        return "high"
    return "correct"


def run_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的数字。")

    while True:
        user_input = input("请输入你的猜测：")

        if not user_input.isdigit():
            print("请输入数字。")
            continue

        guess = int(user_input)
        attempts += 1
        result = check_guess(secret_number, guess)

        if result == "low":
            print("太小了。")
        elif result == "high":
            print("太大了。")
        else:
            print(f"恭喜你，猜对了！你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    run_game()
