"""
Template for the COMP1730/6730 project assignment, S2 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators:
u7015074, Tanya Babbar
u7309356, Sam Eckton
u7351505, Yifan Luo
"""
import platform


def task1():
    """
    The function calls the function get_stdlib_packages and uses its
    results (a set of StdLib package names) to print the Python version,
    the OS name, and the first five and the last five StdLib package names.

    Parameters:
        No parameters.

    Returns:
        No returns.

    Assumptions:
        No assumptions.
    """
    import platform

    def get_stdlib_packages():
        """
        The function returns a set containing external StdLib package names
        (without two packages "this" and "antigravity") according to different
        Python versions.

        Parameters:
            No parameters.

        Returns:
            stdlibs (set): A set containing StdLib, without internal packages
                and two external packages "this" and "antigravity".

        Assumptions:
            The function assume the program is working on Python3.5+.
        """
        import sys
        import isort

        # get the Python version major.minor, e.g. 3.8 (major = 3, minor = 8)
        major, minor = sys.version_info.major, sys.version_info.minor

        # check if the requirement of Python version is met
        assert major == 3, "Python3 is used in this project."
        assert minor >= 5, "Python3.5+ is used in this project."

        # get StdLib for each Python version
        global stdlibs
        if 5 <= minor <= 9:
            stdlibs = set(eval("isort.stdlibs.py3" + str(minor) + ".stdlib"))
        elif minor >= 10:
            stdlibs = set(sys.stdlib_module_names)

        # remove internal packages, and substitute them with None
        stdlibs = set(map(lambda stdlib: None if stdlib[0] == '_' else stdlib, stdlibs))
        stdlibs.discard(None)  # remove None from the last step
        stdlibs.discard("this")  # remove "this"
        stdlibs.discard("antigravity")  # remove "antigravity"

        return stdlibs

    stdlibs = sorted(list(get_stdlib_packages()))  # get sorted StdLib list
    os_name = platform.platform()  # get OS name
    py_ver = platform.python_version()  # get Python version

    print("Python {py_ver} on {os_name}".format(py_ver=py_ver, os_name=os_name))
    print("StdLib contains {} external modules and packages:".format(len(stdlibs)))
    print(", ".join(stdlibs[:5]) + " ... " + ", ".join(stdlibs[-5:]))
    print("\n")

def task2():
    """
    The function calls the function get_real() and uses its result
    (a set of importable package names) to print the information
    (OS and Python version) about the packages which cannot be used
    on the execution platform.

    Parameters:
        No parameters.

    Returns:
        No returns.

    Assumptions:
        No assumptions.
    """
    import platform

    def get_real(package_names):
        """
        The function iterates through a sequence of package names, and
        determine which ones are importable. The returned list is a new
        object containing importable package names.

        Parameters:
            package_names (set): A set of StdLib package names to be tested.

        Returns:
             importable_package_names (list): A list containing all the importable
                package names from the input package_names.

        Assumptions:
            No assumptions.
        """
        import importlib

        assert hasattr(package_names, '__iter__'), "The input package_names must be iterable."

        importable_package_names = []
        for package_name in package_names:
            try:
                importlib.import_module(package_name)  # import modules from strings
                importable_package_names.append(package_name)
                # keep the module importlib, and delete others from the program namespace
                if package_name != "importlib":
                    exec("del package_name")
            except:
                # if any error happens during importing the module
                # skip this unimportable module
                continue

        return importable_package_names

    global stdlibs                          # all external StdLib package names
    importable_stdlibs = get_real(1)  # importable packages from stdlibs
    # subtract importable modules and get a set of unimportable modules
    unimportable_stdlibs = stdlibs.difference(importable_stdlibs)
    os_name = platform.platform()       # get OS name
    py_ver = platform.python_version()  # get Python version

    print("These StdLib packages on Python-{py_ver}/{os_name} are not importable:".format(py_ver=py_ver, os_name=os_name))
    print(", ".join(sorted(list(unimportable_stdlibs))))
    print("\n")


def analyse_stdlib():
    task1()
    task2()


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Yifan Luo'
    ID = 'u7351505'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP6730.2022.S2')
    stdlibs = set()  # a global variable containing external package names
    analyse_stdlib()
