import random

def guess_number(value, number_to_guess=None):
    if value == number_to_guess:
        return "恭喜你！你猜对了！"
    elif value < number_to_guess:
        return "太小了！再试一次。"
    else:
        return "太大了！再试一次。"

def main():
    print("欢迎来到猜数字游戏！")
    print("我已经选择了一个1到100之间的数字。你能猜到它是什么吗？")
    number_to_guess = random.randint(1, 100)
    print(f"作弊器，答案是：{number_to_guess}")
    while True:
        try:
            user_input = int(input("请输入你的猜测："))
            if 1 <= user_input <= 100:
                result = guess_number(user_input, number_to_guess)
                print(result)
                if result == "恭喜你！你猜对了！":
                    break
            else:
                print("请输入一个在1到100之间的数字。")
        except ValueError:
            print("无效输入，请输入一个数字。")

main()