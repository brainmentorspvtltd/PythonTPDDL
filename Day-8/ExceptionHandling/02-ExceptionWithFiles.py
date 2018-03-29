import csv
def main():
    try:
        file = open('users.csv')
        reader = csv.reader(file)

    except FileNotFoundError:
        print("File not found...")

    except ValueError:
        print("Some error")

    else:
        # print(data)
        for data in reader:
            print(data)

    finally:
        print("I will always execute...")
        file.close()


if __name__ == '__main__':
    main()


# print("This is some text")