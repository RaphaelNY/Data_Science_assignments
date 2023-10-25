import time

# 非刷新文本进度条
def static_progress_bar():
    print("-----执行开始-----")
    for i in range(101):
        c = i
        a = i // 2
        b = 50 - a

        if i % 10 == 0:
            print(" {:3}%[{}{}]\n".format(c, "*" * a, "." * b), end="")

        time.sleep(0.1)
    print("\n-----执行结束-----")

# 单行动态刷新文本进度条
def dynamic_progress_bar():
    print("-----执行开始-----")
    for i in range(101):
        c = i
        a = i // 2
        b = 50 - a

        print("\r {:3}%[{}{}]".format(c, "*" * a, "." * b), end="")
        time.sleep(0.1)
    print("\n-----执行结束-----")

print("非刷新文本进度条：")
static_progress_bar()
print("\n")

# 单行动态刷新文本进度条
print("单行动态刷新文本进度条：")
dynamic_progress_bar()
print("\n")
