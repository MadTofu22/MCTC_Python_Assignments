def calculate_averages(grades):
    averages = []
    for obj in grades:
        count = 0
        sum = 0
        for itm in obj:
            sum += itm
            count += 1
        averages.append(sum/count)
    return averages

def main():
    calculate_average([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    print(averages)

main()
