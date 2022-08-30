
## Exercise 1(a) from Lab 3: a version of print_grades that uses only
## simple tests (no boolean combinations) and if-else statements.

def print_grade_v1(mark):
    '''Print the grade corresponding to the given mark.
    Assumption: mark is between 0 and 100. (The function will
    work for other values, but there is no check that the mark
    is sensible.)'''
    if mark >= 80:
        print("High Distinction")
    else:
        if mark >= 70:
            print("Distinction")
        else:
            if mark >= 60:
                print("Credit")
            else:
                if mark >= 50:
                    print("Pass")
                else:
                    print("Fail")


## Here is a different way to do the same thing: Can you work out why
## this prints only one line, but would print more than one if we put
## the prints directly into the if statements?

def get_grade(mark):
    if mark >= 80:
        return "High Distinction"
    if mark >= 70:
        return "Distinction"
    if mark >= 60:
        return "Credit"
    if mark >= 50:
        return "Pass"
    return "Fail"

def print_grade_v2(mark):
    print(get_grade(mark))


## Exercise 1(b): a version of print_grades that uses if-elif-else.

def print_grade_v3(mark):
    '''Print the grade corresponding to the given mark.
    Assumption: mark is between 0 and 100. (The function will
    work for other values, but there is no check that the mark
    is sensible.)'''
    if mark >= 80:
        print("High Distinction")
    elif mark >= 70:
        print("Distinction")
    elif mark >= 60:
        print("Credit")
    elif mark >= 50:
        print("Pass")
    else:
        print("Fail")
