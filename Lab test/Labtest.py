def start_cleaning(Area):
    vaccum_cleaner_pos = 0
    last_cleaned_pos = 0
    if sum(Area) == 0:
        print("Area is already clean")
    while (sum(Area) > 0):
        if Area[vaccum_cleaner_pos] == 1:
            if vaccum_cleaner_pos == 0:
                last_cleaned_pos = 0
                print("Cleaned left side")
            else:
                last_cleaned_pos = 1
                print("Cleaned right side")

            if vaccum_cleaner_pos == 1:
                if last_cleaned_pos == 0:
                    print("The area is clean")
                    break
                else:
                    vaccum_cleaner_pos = 0
            if vaccum_cleaner_pos == 0:
                if last_cleaned_pos == 1:
                    print("The area is clean")
                    break
                else:
                    vaccum_cleaner_pos = 1
        else:
            if vaccum_cleaner_pos == 0:
                print("Left side is clean")
                if last_cleaned_pos == 1:
                    print("Area is clean")
                    break
                else:
                    vaccum_cleaner_pos = 1
                    continue
            if vaccum_cleaner_pos == 1:
                print("Right side is clean")
                if last_cleaned_pos == 0:
                    print("Area is clean")
                    break
                else:
                    vaccum_cleaner_pos = 0


def start():
    Area = list(map(int,
                    input("Enter the status of left and right side of the area\n 1 for dirty and 0 for clean : ").split(
                        " ")))
    start_cleaning(Area)


start()