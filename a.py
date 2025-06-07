import random
import logging
from tkinter import N
import matplotlib.pyplot as plt

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,  # 设置日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）
        format='%(asctime)s,%(name)s|%(levelname)s|%(message)s',  # 日志格式
        filename='app.log',  # 输出到文件（不设置则输出到控制台）
        filemode='w'  # 文件模式（'w' 覆盖写入，'a' 追加写入）
    )

def generate_random_list():
    return [random.randint(0, 1) for _ in range(1000)]

def calculate_total_sum(lst):
    return sum(lst)

def update_counter(b, total_sum):
    b[total_sum] += 1

def plot_and_save(b, n):
    plt.bar(range(1001), b)
    plt.xlabel('sum')
    plt.ylabel('times')
    plt.savefig('a' + str(n) + '.png')
    plt.close()

setup_logging()
a = [0] * 1000
b = [0] * 1001
#max_iterations = 100  # 设置最大迭代次数
n = 0
while 1:
    n+=1
    a = generate_random_list()
    logging.debug(a)
    total_sum = calculate_total_sum(a)
    #print(total_sum)
    logging.info(total_sum)
    update_counter(b, total_sum)
    #print(b)
    if n % 1000 == 0:
        print(n)
        plot_and_save(b, n)

