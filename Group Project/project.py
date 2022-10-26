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
    """
    The function calls a function named "get_stdlib_packages" and uses its
    results (a set of package names in StdLib) to print the Python version,
    the OS name, and the first five and the last five package names. At the
    end, all the external package names except "this" and "antigravity" are
    stored in the global variable "stdlibs".
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        A global variable named "stdlibs" is created to store all the
        external package names in StdLib.
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
    The function calls a function named "get_real" and uses its result
    (a set of importable package names) to print the information
    (OS and Python version) about the packages which cannot be used
    on the execution platform. At the end, all the importable external
    package names in the global variable "stdlibs" are stored in a
    global variable named "importable_stdlibs".
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        Task 1 runs without errors and exceptions. A global variable named
        "importable_stdlibs" is created to store all the importable external
        package names in the global variable "stdlibs".
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
                    del package_name
            except:
                # if any error happens during importing the module
                # skip this unimportable module
                continue

        return importable_package_names

    global stdlibs  # all external StdLib package names
    global importable_stdlibs  # all importable StdLib package names in stdlibs
    importable_stdlibs = set(get_real(stdlibs))  # importable packages from stdlibs
    # subtract importable modules and get a set of unimportable modules
    unimportable_stdlibs = stdlibs.difference(importable_stdlibs)
    os_name = platform.platform()  # get OS name
    py_ver = platform.python_version()  # get Python version

    print(
        "These StdLib packages on Python-{py_ver}/{os_name} are not importable:".format(py_ver=py_ver, os_name=os_name))
    print(", ".join(sorted(list(unimportable_stdlibs))))
    print("\n")


def task3():
    """
    The function calls a function named "module_dependency" to decide the
    dependency of each module and store its dependent modules in the global
    variable "importable_stdlibs". Then, a function named "core_modules"
    stores all the package names which are independent with others in
    "importable_stdlibs". Besides, a functions named "most_dependent_modules"
    is used to find the most dependent modules according to the results from
    "module_dependency". Finally, task 3 shows information about the most
    dependent modules and the number of core modules based on the functions
    above.
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        Task 1 and task 2 run without errors and exceptions. Global variables
        "stdlibs" and "importable_stdlibs" are created to store all the package
        names of external modules and all the package names of importable external
        modules.
    """

    def module_dependency(module_name, name):
        """
        The function takes a module denoted as "name", and returns names of its
        dependent modules among a set of module names denoted as "module_name".

        Parameters:
            module_name (set): A set of module names.
            name (str): A module name.

        Returns:
            dependent_mods (list): A list of dependent module names of "name" among
                "module_name".

        Assumptions:
            The input variables "module_name" and "name" are valid package names derived
                from task 1 and task 2.
        """
        import importlib
        global importable_stdlibs

        mod = importlib.import_module(name)
        resource = set(vars(mod).keys())  # get resources of the module "name"
        dependent_mods = resource & importable_stdlibs  # get dependent package names among "importable_stdlibs"
        dependent_mods.discard(name)  # exclude duplicates (e.g. a function with the same name)
        dependent_mods = list(dependent_mods)

        return dependent_mods

    def most_dependent_modules(n=5, descending=True):
        """
        The function sorts module names by the number of dependent modules of
        each module. Then, print names of the most dependent modules and the
        number of its dependent modules.

        Parameters:
            n (int): The number of package names.
            descending (bool): Sort package names in descending order or not.

        Returns:
            No returns.

        Assumptions:
            The main function calls "module_dependency" and the dependency information
            of each module is stored in "stdlibs_dependency", a dictionary containing
            each package name and its dependent package names from "importable_stdlibs".
        """
        nonlocal stdlibs_dependency
        sorted_stdlibs = sorted(stdlibs_dependency.items(), key=lambda item: item[1], reverse=descending)
        for i in range(n):
            print("{}: {}".format(sorted_stdlibs[i][0], sorted_stdlibs[i][1]))

    def core_modules():
        """
        The function uses results from "module_dependency" and returns a set of core
        package names, which are independent modules among "importable_stdlibs".

        Parameters:
            No parameters.

        Returns:
            core_stdlibs (set): A set of core package names among "importable_stdlibs".

        Assumptions:
            The main function calls "module_dependency" and stores dependency
            information in "stdlibs_dependency", a dictionary containing each package
            name and its dependent package names from "importable_stdlibs".
        """
        nonlocal stdlibs_dependency

        core_stdlibs = set([k for k, v in stdlibs_dependency.items() if v == 0])
        return core_stdlibs

    global importable_stdlibs

    # initialize a dictionary to store dependency information
    # key: package name, value: number of its dependent modules, initialized with 0
    stdlibs_dependency = dict.fromkeys(importable_stdlibs, 0)

    # get dependency information of each importable external module
    for importable_stdlib in importable_stdlibs:
        dependent_stdlib = module_dependency(importable_stdlibs, importable_stdlib)
        stdlibs_dependency[importable_stdlib] = len(dependent_stdlib)

    # print most dependent package names and the number of their dependent modules
    print("The following StdLib packages are most dependent:")
    most_dependent_modules(n=5, descending=True)  # top "n" modules sorted in descending order
    # print total number of core packages and core package examples
    core_stdlibs = sorted(list(core_modules()))  # sort core modules by names
    print("The {} core packages are:".format(len(core_stdlibs)))
    print(", ".join(core_stdlibs[:5]) + " ... " + ", ".join(core_stdlibs[-5:]))


def analyse_stdlib():
    task1()
    task2()
    task3()


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Yifan Luo'
    ID = 'u7351505'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP6730.2022.S2')
    stdlibs = set()  # a global variable containing external package names
    importable_stdlibs = set()  # a global variable containing importable package names in stdlibs
    analyse_stdlib()
