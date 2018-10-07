import numpy
from collections import defaultdict
from tqdm import tqdm
import time


def show_progress():
    for i in tqdm(range(100)):
        time.sleep(0.05)


def get_first_five():
    dataset_filename = '/Users/lirui/Desktop/LearningDataMiningwithPythonSecondEdition_Code/Chapter01/affinity_dataset.txt'
    x = numpy.loadtxt(dataset_filename)
    print(x[:5])
    return x


def count_apple_buyer():
    num_apple_purchase = 0
    for sample in get_first_five():
        if sample[3] == 1:
            num_apple_purchase += 1
    print(f'{num_apple_purchase} person bought apple.')


if __name__ == '__main__':
    count_apple_buyer()
