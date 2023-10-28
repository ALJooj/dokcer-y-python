from sys import argv 
import argparse
import matplotlib.pyplot as plt
import json


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', required=True, nargs='+', type=int)
    parser.add_argument('-y', required=True, nargs='+', type=int)

    return parser

def createPlot(x, y):
    plt.plot(x, y)

    # Добавляем подписи осей и заголовок
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')

    plt.savefig('output.png')
    


if __name__ == '__main__':
    parser = createParser()
    namespaces = parser.parse_args(argv[1:])
    print(namespaces.x, namespaces.y)