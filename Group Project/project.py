"""
Template for the COMP1730/6730 project assignment, S2 2022.
The assignment specification is available on the course web
site, at https://cs.anu.edu.au/courses/comp1730/assessment/project/

Collaborators:
u7015074, Tanya Babbar
u7309356, Sam Eckton
u7351505, Yifan Luo
"""
import os
import sys
from importlib.metadata import requires


def task1():
    """
    The function calls a function named "get_stdlib_packages" and uses its
    results (a set of package names in StdLib) to print the Python version,
    the OS name, and the first five and the last five package names. At the
    end, all the external package names except "this" and "antigravity" are
    stored in the variable "stdlibs".

    Parameters:
        No parameters.

    Returns:
        No returns.

    Assumptions:
        The function assumes the program is running on Python3.5+.
    """
    import platform

    stdlibs = sorted(list(get_stdlib_packages()))  # get a sorted list of external StdLib
    os_name = platform.platform()  # get the OS name
    py_ver = platform.python_version()  # get the Python version

    print("\nPython {py_ver} on {os_name}".format(py_ver=py_ver, os_name=os_name))
    print("StdLib contains {} external modules and packages:".format(len(stdlibs)))
    print(", ".join(stdlibs[:5]) + " ... " + ", ".join(stdlibs[-5:]))
    print("\n")


def get_stdlib_packages():
    """
    The function returns a set containing external StdLib package names
    (without two packages "this" and "antigravity") according to different
    Python versions.

    Parameters:
        No parameters.

    Returns:
        stdlibs (set): A set of external StdLib except "this" and "antigravity"

    Assumptions:
        The function assumes the program is running on Python3.5+.
    """
    import sys
    import isort

    # get the Python version major.minor, e.g. 3.8 (major = 3, minor = 8)
    major, minor = sys.version_info.major, sys.version_info.minor

    # check if the requirement of Python version is met
    assert major == 3, "Python3 is used in this project."
    assert minor >= 5, "Python3.5+ is used in this project."

    # get StdLib for each Python version
    if 5 <= minor <= 9:
        stdlibs = set(eval("isort.stdlibs.py3" + str(minor) + ".stdlib"))
    elif minor >= 10:
        stdlibs = set(sys.stdlib_module_names)

    # remove internal packages and substitute them with None
    stdlibs = set(map(lambda stdlib: None if stdlib[0] == '_' else stdlib, stdlibs))
    stdlibs.discard(None)  # remove None from the last step
    stdlibs.discard("this")  # remove "this"
    stdlibs.discard("antigravity")  # remove "antigravity"

    return stdlibs



def task2():
    """
    The function calls a function named "get_real" and uses its result
    (a set of importable package names) to print the information
    (OS and Python version) about the packages which cannot be used
    on the execution platform. At the end, all the importable external
    package names in the variable "stdlibs" provided by get_stdlib_packages() 
    are stored in a variable named "importable_stdlibs".

    Parameters:
        No parameters.

    Returns:
        No returns.

    Assumptions:
        Task 1 runs without errors and exceptions. The set of stdlibs returned by
        get_stdlib_packages() is correct and a the variable returned by get_real(stdlibs)
        contains all importable package names.
    """
    import platform

    stdlibs = get_stdlib_packages()  # all external StdLib package names from task 1
    importable_stdlibs = get_real(stdlibs)  # all importable package names from stdlibs
    unimportable_stdlibs = stdlibs.difference(importable_stdlibs)  # all non-importable package names from stdlibs
    os_name = platform.platform()  # get OS name
    py_ver = platform.python_version()  # get Python version

    print(
        "These StdLib packages on Python-{py_ver}/{os_name} are not importable:".format(py_ver=py_ver, os_name=os_name))
    print(", ".join(sorted(list(unimportable_stdlibs))))
    print("\n")


def get_real(package_names):
    """
        The function iterates through a sequence of package names, and
        determine which ones are importable. The returned list is a new
        object containing importable package names.

        Parameters:
            package_names (set): A set of StdLib package names from task 1

        Returns:
             importable_package_names (set): A set containing all the importable
                package names from the input package_names.

        Assumptions:
            This function assumes pack_names is a set of sorted external StdLib
                package names (exclude "this and "antigravity"") from task 1
        """

    import importlib

    assert hasattr(package_names, '__iter__'), "The input package_names must be iterable."

    importable_package_names = []
    for package_name in package_names:
        try:
            importlib.import_module(package_name)  # import the module from the package name
            importable_package_names.append(package_name)
            # keep the module "importlib", and delete others from the program namespace
            if package_name != "importlib":
                del package_name
        except:
            # if any error happens during importing the module, skip this module
            continue
    importable_package_names = set(importable_package_names)

    return set(importable_package_names)




def task3():
    """
    This function calls a helper function named "module_dependency" to decide the
    dependency of each module and store its dependent modules in the
    variable "dependent_stdlibs". Then, a function named "core_modules"
    stores all the package names which are independent of others in
    "importable_stdlibs". Additionally a functions named "most_dependent_modules"
    is used to find the most dependent modules according to the results from
    "module_dependency". Finally, task 3 prints information about the most
    dependent modules and the number of core modules based on the functions
    mentioned above.
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        Task 1 and task 2 run without errors and exceptions. stdlibs and importable_stdlibs
        returned by get_stdlib_packages() and get_real(stdlibs) are correct and provide
        a list of all importable external packages
    """

    stdlibs = get_stdlib_packages()
    importable_stdlibs = get_real(stdlibs)

    # initialize a dictionary to store dependency information
    # key: package name, value: number of its dependent modules, initialized with 0
    stdlibs_dependency = dict.fromkeys(importable_stdlibs, 0)

    # get dependency information of each importable external module
    for importable_stdlib in importable_stdlibs:
        dependent_stdlibs = module_dependency(importable_stdlibs, importable_stdlib)
        stdlibs_dependency[importable_stdlib] = len(dependent_stdlibs)

    # print most dependent package names and the number of their dependent modules
    print("The following StdLib packages are most dependent:")
    most_dependent_modules(stdlibs_dependency, n=5, descending=True)  # top "n" modules sorted in descending order
    # print total number of core packages and core package examples
    core_stdlibs = sorted(list(core_modules(stdlibs_dependency)))  # sort core modules by names
    print("The {} core packages are:".format(len(core_stdlibs)))
    print(", ".join(core_stdlibs[:5]) + " ... " + ", ".join(core_stdlibs[-5:]))
    print('\n')

def module_dependency(module_names, name):
    """
    The function takes a module denoted as "name", and returns names of its
    dependent modules among a set of module names denoted as "module_name".

    Parameters:
        module_names (set): A set of module names.
        name (str): A module name.

    Returns:
        dependent_mods (list): A list of dependent module names of the input module

    Assumptions:
        The input variables "module_name" and "name" are valid package names derived
            from task 1 and task 2.
    """
    import importlib

    mod = importlib.import_module(name)
    mod_resources = set(vars(mod).keys())  # get resources of the module "name"
    dependent_mods = mod_resources & module_names  # get dependent package names among "importable_stdlibs"
    dependent_mods.discard(name)  # exclude duplicates (e.g. a function with the same name)
    dependent_mods = list(dependent_mods)

    return dependent_mods


def most_dependent_modules(stdlibs_dependency, n=5, descending=True):
    """
    The function sorts module names by the number of dependent modules of
    each module. Then, print names of the most dependent modules and the
    number of its dependent modules.

    Parameters:
        stdlibs_dependency (dict): A dictionary that stores dependency information
        n (int): The number of package names.
        descending (bool): Sort package names in descending order or not.

    Returns:
        No returns.

    Assumptions:
        The main function calls "module_dependency" and the dependency information
        of each module is stored in "stdlibs_dependency", a dictionary containing
        each package name and its dependent package names from "importable_stdlibs".
    """

    sorted_stdlibs = sorted(stdlibs_dependency.items(), key=lambda item: item[1], reverse=descending)
    for i in range(n):
        print("{}: {}".format(sorted_stdlibs[i][0], sorted_stdlibs[i][1]))


def core_modules(stdlibs_dependency):
    """
    The function uses results from "module_dependency" and returns a set of core
    package names, which are independent modules among "importable_stdlibs".

    Parameters:
        stdlibs_dependency (dict): A dictionary that stores the dependency information
            of StdLib from task 2

    Returns:
        core_stdlibs (set): A set of core package names from "importable_stdlibs"

    Assumptions:
        The main function calls "module_dependency" and stores dependency
        information in "stdlibs_dependency", a dictionary containing each package
        name and its dependent package names from "importable_stdlibs".
    """

    core_stdlibs = set([k for k, v in stdlibs_dependency.items() if v == 0])
    return core_stdlibs


def task4():
    """
    The function calls the function explore package() using the previously found 
    set of importabel_stdlibs and creates a dictionary, linking each module 
    with the numbers of lines of code it contains, and the number of class 
    instances. It then returns the five largest and smallest modules in terms 
    of lines of code and class instances.
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        Assumes that tasks 1 and 2 run as intended returning values for stdlibs
        and all importable_stdlibs to be used in this task. Assumes that any packages
        without any lines of python code are not python packages. Assumes that any 
        Python coded package will posses either the __path__ or __file__ attribute and 
        if the package is Non Python coded, explore_package() will return '-1,-1'. 
     """
    stdlibs = get_stdlib_packages()
    importable_stdlibs = get_real(stdlibs)

    loc_and_custom_types = {}

    for importable_stdlib in importable_stdlibs:
        loc, custom_types = explore_package(importable_stdlib)
        if loc == custom_types == -1:  # only count python code, other types return -1, -1
            continue
        loc_and_custom_types[importable_stdlib] = (loc, custom_types)

    loc_rank = sorted(list(loc_and_custom_types.items()), key=lambda x: x[1][0], reverse=True)
    classes_rank = sorted(list(loc_and_custom_types.items()), key=lambda x: x[1][1], reverse=True)

    print("The following StdLib packages are the largest in terms of LOC:")
    print(', '.join(map(lambda x: str(x[0]) + ': ' + str(x[1][0]), loc_rank[:5])))
    print("\nThe following StdLib packages are the smallest in terms of LOC:")
    print(', '.join(map(lambda x: str(x[0]) + ': ' + str(x[1][0]), loc_rank[-5:])))
    print("\nThe following StdLib packages are the largest in terms of the number of classes defined:")
    print(', '.join(map(lambda x: str(x[0]) + ': ' + str(x[1][1]), classes_rank[:5])))
    print("\nThe following StdLib packages define no custom classes:")
    print(', '.join(map(str, sorted([cr[0] for cr in classes_rank if cr[1][1] == 0]))))
    print('\n\n')



def explore_package(a_package):
    """
    Helper function for task 4, explores the individual code associated with each 
    module from the importable_stdlibs set. The function test to see if the module 
    is a folder of an indiviudal python file, otherwise returns values of '-1,-1'. If 
    it is a folder, for every python file within the folder (summation), the 
    lines of code and number of class instances are counted and returned as a tuple. 
    The same is returned for an individual python file. 
    
    Parameters:
        No parameters.
        
    Returns:
        A tuple value representing the total number of lines of code and the total
        class instances within the given python package
        
    Assumptions:
        Assumes all importable python files to be tested can be found within
        the computers files using its own __file__ attribute. Assumes that lines of code 
        includes both docstrings and comments.
    """
    import os
    import importlib
    import sys
    def count_lines_and_classes(pkg_path):
        loc, custom_types = 0, 0
        mod_name = pkg_path.split('\\')[-1].split('.py')[0]
        with open(pkg_path, 'r', encoding='ISO-8859-1') as f:
            loc = len(f.readlines())
            f.seek(0)  # reset to the beginning of the file
            # skip doc
            line_idx = 0
            content = f.readlines()
            is_doc_string = False
            for line in content:
                line = line.strip()
                # if the line starts and ends with docstring assign it to false
                if line[:3] == '"""' and line[-3:] == '"""':
                    is_doc_string = False
                else:
                    # if the line starts or ends with a docstring symbol, assign the tester to true or false depending on what it currently is
                    if line[:3] == '"""' or line[-3:] == '"""' or line[:4] == 'r"""':
                        if not is_doc_string:
                            is_doc_string = True
                        else:
                            is_doc_string = False
                words = line.split()  # split each line into a list of each word/element
                # check if the element is a class instances base on several conditions
                if len(words) > 0 and words[0] == 'class' and not is_doc_string:
                    custom_types += 1

        return loc, custom_types

    loc, custom_types = 0, 0
    pkg = importlib.import_module(a_package)

    if not hasattr(pkg, '__file__') and not hasattr(pkg, '__path__'):  # builtlin binary code
        return -1, -1
    if hasattr(pkg, '__file__'):
        pkg_path = os.path.abspath(pkg.__file__)
        if pkg_path.endswith('.py'):  # python code
            if pkg_path.endswith('__init__.py'):  # a directory
                for dir_path, dir_names, file_names in os.walk(os.path.dirname(pkg_path)):
                    for file_name in file_names:
                        if file_name.endswith('.py'):
                            file_loc, file_types = count_lines_and_classes(
                                dir_path + '\\' + file_name)  # TODO: different seperators for different OS?
                            loc += file_loc
                            custom_types += file_types
            elif pkg_path.endswith(a_package + '.py'):  # a single file
                loc, custom_types = count_lines_and_classes(pkg_path)
            else:  # shared library
                return -1, -1

    return loc, custom_types

counter = 0
def task5():
    ListOfStdLibs = []
    standard_lib_path = os.path.join(sys.prefix, "Lib")
    for file in os.listdir(standard_lib_path):
        ListOfStdLibs.append(file.split(".py")[0].strip().lower())

     # ListOfStdLibs = ["pandas" , "numpy" , "xlrd" , "datetime" , "scipy"]

        CyclicDependencies = []

    def find_cycles2(packageName):
            (find_cycles())  ##gets all the depenencies
            global counter
            counter += 1

            try:
                dep = find_cycles()[counter]  # getting the dependency

            except Exception as data:
                print(counter, packageName, end="")
                print(f"--> {data}", end="")
                print("\n")
                return

            if dep == None:
                pass
            else:
                x = len(dep)
                cycles = find_cycles()
                for i, cycle in enumerate(cycles):
                    print(str(i + 1) + '. ' + packageName + ' -> '.join(cycle))
            return

    for packageUnderScan in ListOfStdLibs:
            find_cycles2(packageUnderScan)


def find_cycles():
    """
    A function called by task 5 to find all cyclical depdencies for packages 
    in importable_stdlibs using recurive_helper().

    Parameters
    ----------

    Returns
    -------
    cycles : list of lists
        the list of all cyclical dependencies in importable_stdlibs.

    Assumptions:
        Assumes all importable python files to be tested can be found within
        the computers files using its own __file__ attribute. Assumes that lines of code 
        includes both docstrings and comments. Assumes that get_stdlib_packages() and 
        get_real() return the correct values, providing a set of all importable packages. 

    """
    stdlibs = get_stdlib_packages()
    importable_stdlibs = get_real(stdlibs)
    pkg_dependency = dict.fromkeys(importable_stdlibs, 0)
    # get dependency information of each importable external module
    for importable_stdlib in importable_stdlibs:
        dependent_stdlibs = module_dependency(importable_stdlibs, importable_stdlib)
        pkg_dependency[importable_stdlib] = dependent_stdlibs

    cycles = []
    max_len = len(pkg_dependency)

    def recursive_helper(pkg, cycle):
        """
        recursive function used to find all cyclical depdencies 
        for a given stdlib by calling itself and itterating over the dependicies 
        of the current stdlib.

        Parameters
        ----------
        pkg : package
            A depdent package of the current package being explored.
        cycle : list
            the current cycle of the package being explore and its current depdendency.

        Returns
        -------
        None.

        """
        nonlocal cycles, pkg_dependency, max_len
        if len(cycle) >= max_len:
            return
        if len(cycle) > 1 and cycle[0] == cycle[-1]:
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if len(cycle) > len(set(cycle)):
            return
        for pkg_depend in pkg_dependency[pkg]:
            recursive_helper(pkg_depend, cycle + [pkg_depend])

    for pkg in pkg_dependency.keys():
        recursive_helper(pkg, [])

    return cycles




def task6():
    import networkx as nx
    import matplotlib.pyplot as plt

    cycles = find_cycles()

    G = nx.Graph()
    G.add_nodes_from([cycle[0] for cycle in cycles])

    for cycle in cycles:
        G.add_edges_from([(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)])

    plt.figure()
    nx.draw(G, with_labels=True)
    plt.savefig("task6_path.png")
    plt.show()


def analyse_stdlib():
    task1()
    task2()
    task3()
    task4()
    task5()
    # task6()


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Yifan Luo'
    ID = 'u7351505'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP6730.2022.S2')
    analyse_stdlib()
