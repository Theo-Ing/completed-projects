def bells(n):
    if n == 0:
        return [[]]
    else:
        array = bells(n-1)
        updatedArray = []
        for i in range(0, len(array)):
            if i%2:
                for j in range(0, len(array[i]) + 1):
                    updatedArray.append(array[i][:j] + [n] + array[i][j:])
            else:
                for j in range(0, len(array[i]) + 1):
                    updatedArray.append(array[i][:(len(array[i]) - j)] + [n] + array[i][(len(array[i]) - j):])
        return updatedArray

def print_table(array):
    for i in array:
        for j in i:
            print(j, end=' ')
        print()

def main():
    print_table(bells(int(input("How many bells are there? "))))

if __name__ == '__main__':
    main()