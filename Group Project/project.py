"""
Template for the COMP1730/6730 project assignment, S2 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators:
u7015074, Tanya Babbar
u7309356, Sam Eckton
u7351505, Yifan Luo
"""


def task1():
    import platform

    def get_stdlib_packages():
        import sys, isort

        major, minor = sys.version_info.major, sys.version_info.minor  # get Python version major.minor
        assert major == 3, "Python3 is used in this project."

        if 5 <= minor <= 9:
            stdlibs = set(eval("isort.stdlibs.py3" + str(minor) + ".stdlib"))
        elif minor >= 10:
            stdlibs = set(sys.stdlib_module_names)
        else:
            raise Exception("Python3.5+ is used in this project.")

        stdlibs = set(map(lambda stdlib: None if stdlib[0] == '_' else stdlib, stdlibs))
        stdlibs.discard(None)
        stdlibs.discard("this")
        stdlibs.discard("antigravity")

        return stdlibs

    stdlibs = sorted(list(get_stdlib_packages()))
    os_name = platform.platform()
    py_ver = platform.python_version()
    print("Python {py_ver} on {os_name}".format(py_ver=py_ver, os_name=os_name))
    print("StdLib contains {} external modules and packages:".format(len(stdlibs)))
    print(stdlibs[:5] + stdlibs[-5:])


def analyse_stdlib():
    task1()
    pass


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Yifan Luo'
    ID   = 'u7351505'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP6730.2022.S2')
    analyse_stdlib()
