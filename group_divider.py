#!/usr/bin/python

import csv


def get_data(file_path):
    sites = []
    log_numbers = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            sites.append(row[1])
            log_numbers.append(row[2])
    sites = sites[1:]
    log_numbers = map(int, log_numbers[1:])
    return sites, log_numbers

def divider(log_numbers, group_number):
    avg_number = sum(log_numbers)/group_number
    print sum(log_numbers)
    aggregate_number = 0
    divide_index = []
    for i in range(len(log_numbers)):
        aggregate_number += log_numbers[len(log_numbers) - 1 - i]
        if aggregate_number >= avg_number:
            aggregate_number = 0
            divide_index.append(len(log_numbers) - 1 - i)
    return divide_index


def get_sites(sites, divide_index):
    groups = []
    group = []
    index = len(divide_index) - 1
    for i in range(len(sites)):
        if i == divide_index[index] or i == len(sites) - 1:
            if group == []:
                group.append(sites[i])
            index -= 1
            groups.append(group)
            group = []
        else:
            group.append(sites[i])
    return groups


def main():
    sites, log_numbers = get_data('/Users/yni/workspace/log1.csv')
    divide_index = divider(log_numbers, 5)
    groups = get_sites(sites, divide_index)
    for i in groups:
        print i


if __name__ == "__main__":
    main()
