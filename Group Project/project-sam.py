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
    stored in the variable "stdlibs".
    Parameters:
        No parameters.
    Returns:
        No returns.
    Assumptions:
        A variable named "stdlibs" is created to store all the
        external package names in StdLib, later used with function calls to 
        get_stdlib_packages()
    """
    import platform

    stdlibs = sorted(list(get_stdlib_packages()))  # get sorted StdLib list
    os_name = platform.platform()                  # get OS name
    py_ver = platform.python_version()             # get Python version

    print("Python {py_ver} on {os_name}".format(py_ver=py_ver, os_name=os_name))
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
        stdlibs.discard(None)           # remove None from the last step
        stdlibs.discard("this")         # remove "this"
        stdlibs.discard("antigravity")  # remove "antigravity"

        return stdlibs


def task2():
    """
    The function calls a function named "get_real" and uses its result
    (a set of importable package names) to print the information
    (OS and Python version) about the packages which cannot be used
    on the execution platform. At the end, all the importable external
    package names in "stdlibs" from task 1 are stored in a
    variable named "importable_stdlibs".
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

    
    stdlibs  = get_stdlib_packages()                              # all external StdLib package names                   # all importable StdLib package names in stdlibs
    importable_stdlibs = set(get_real(stdlibs))  # importable packages from stdlibs
    # subtract importable modules and get a set of unimportable modules
    unimportable_stdlibs = stdlibs.difference(importable_stdlibs)
    os_name = platform.platform()                # get OS name
    py_ver = platform.python_version()           # get Python version

    print("These StdLib packages on Python-{py_ver}/{os_name} are not importable:".format(py_ver=py_ver, os_name=os_name))
    print(", ".join(sorted(list(unimportable_stdlibs))))
    print("\n")
    

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
        Task 1 and task 2 run without errors and exceptions. Variables
        "stdlibs" and "importable_stdlibs" are created to store all the package
        names of external modules and all the package names of importable external
        modules.
    """


    stdlibs  = get_stdlib_packages()                                           # all importable StdLib package names in stdlibs
    importable_stdlibs = set(get_real(stdlibs))

    # initialize a dictionary to store dependency information
    # key: package name, value: number of its dependent modules, initialized with 0
    stdlibs_dependency = dict.fromkeys(importable_stdlibs, 0)

    # get dependency information of each importable external module
    for importable_stdlib in importable_stdlibs:
        dependent_stdlib = module_dependency(importable_stdlibs, importable_stdlib)
        stdlibs_dependency[importable_stdlib] = len(dependent_stdlib)

    # print most dependent package names and the number of their dependent modules
    print("The following StdLib packages are most dependent:")
    most_dependent_modules(stdlibs_dependency, n=5, descending=True)  # top "n" modules sorted in descending order
    # print total number of core packages and core package examples
    core_stdlibs = sorted(list(core_modules(stdlibs_dependency)))   # sort core modules by names
    print("The {} core packages are:".format(len(core_stdlibs)))
    print(", ".join(core_stdlibs[:5]) + " ... " + ", ".join(core_stdlibs[-5:]))
    print("")



def module_dependency(module_names, name):
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
            The input variables "module_names" and "name" are valid package names derived
                from task 1 and task 2.
        """
        import importlib


        mod = importlib.import_module(name)
        resource = set(vars(mod).keys())                # get resources of the module "name"
        dependent_mods = resource & module_names        # get dependent package names among "importable_stdlibs"
        dependent_mods.discard(name)                    # exclude duplicates (e.g. a function with the same name)
        dependent_mods = list(dependent_mods)

        return dependent_mods



def most_dependent_modules(stdlibs_dependency, n=5, descending=True):
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
        sorted_stdlibs = sorted(stdlibs_dependency.items(), key=lambda item: item[1], reverse=descending)
        for i in range(n):
            print("{}: {}".format(sorted_stdlibs[i][0], sorted_stdlibs[i][1]))


def core_modules(stdlibs_dependency):
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
        Assumes that functions 1 and 2 run as intended returning values for sets stdlibs
        and importable_stdlibs to be used in this task. Assumes that any pakcages
        without any lines of python code are not python packages. 
     """
    
    
    lines_dic = {}              # initiate the dictionary for each stdlib and the number of lines of code
    class_dic = {}              # initiate the dictionary for each stdlib and the number of class instances
    non_python = []             # initiate the list of non python code modules
    null_classes = []           # initate the list of modules with no class instances
    stdlibs = set(get_stdlib_packages())            # find the set of all stdlibs 
    importable_stdlibs = set(get_real(stdlibs))     # find the set of all importable stdlibs using stdlibs
    for stdlib in importable_stdlibs:               # test each importable stdlib
        if explore_package(stdlib) == None:         # if the helper function try cases have failed, this is a non python code module
            non_python += [stdlib]             
        else:
            (lines_count, class_count) = explore_package(stdlib)    # assignt the tuple returned from the hlper function to lines and class counters
            
                        
            if class_count == 0:                                    # check if the module had no class instances
                null_classes += [stdlib]                            # add the module to the null_classes list
                lines_dic[stdlib] = lines_count                     # add the module to the dictionary with its associated number of lines
            
            
            else:
                lines_dic[stdlib] = lines_count                     # add the module to the dictionary with its number of lines
                class_dic[stdlib] = class_count                     # add the module to the dictionary with its number of class instances
        
    
    # sort the lines and class dictionaries from highest to lowest and remove the keys:
    lines_dic = [x[0] for x in sorted(lines_dic.items(), key = lambda kv : kv[1], reverse = True)]
    class_dic = [x[0] for x in sorted(class_dic.items(), key = lambda kv : kv[1], reverse = True)]
    null_classes.sort()    

    print("The following StdLib packages are the largest in terms of lines of code:")
    print(", ".join(lines_dic[:5]))
    print("\n")
    print("The following StdLib packages are the smallest in terms of lines of code:")
    print(", ".join(lines_dic[-5:]))
    print("\n")
    print("The following StdLib packages are the largest in terms of the number of classes defined:")
    print(", ".join(class_dic[:5]))
    print("\n")
    print("The following StdLib packages define no custom classes:")
    print(", ".join(null_classes))
    print("\n")

    
        
        
      
def explore_package(a_package):
    """
    Helper function for task 4, explores the individual code associated with each 
    module from the importable_stdlibs set. The function test to see if the module 
    is a folder of an indiviudal python file, otherwise returns values of 0. If 
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
        the computers files using its own __path__ method. Assumes that lines of code 
        includes both docstrings and comments.
    """
    
    import importlib
    import glob
    mod = importlib.import_module(a_package)            # import the current stdlib
    lineslen = 0                                        # initalise the lines count to 0
    class_count = 0                                     # initialise the class count to 0

    import asynchat
        
    try:                                                # try case to test for python code module (folder case)
        path = mod.__path__                             # use __path__ module to check for the location of the python folder for the module
        py_files = glob.glob(path[0] + "/**/*.py", recursive = True)    # return the list of all python files within the modules folder
        
        if len(py_files) == 0:                          # if there are no python files, the module is not python coded
            return None
        
        for file in set(py_files):                      # open each python file in the modules folder
            data = open(file,"r", encoding='ISO-8859-1')

            data_test = [line for line in data]         # create a list for each line in the file
            data.seek(0)                                # return to the start of the file
            lineslen += len(data.readlines())           # count the number of lines in the file
                    
            
            doc_string = False                          # initialise the docString tester to false
               
            for line in data_test:                      # test for each line in data_test
                line = line.strip()
                                        
                # if the line starts or ends with a doctring symbol, assign the tester to true or false depending on what it currently is
                if line[:3] == '"""' and line[-3:] == '"""':
                    doc_string=False
                else:        
                    # if the line starts or ends with a docstring symbol, assign the tester to true or false depending on what it currently is
                    if line[:3] == '"""' or line[-3:] == '"""' or line [:4] == 'r"""':                            
                        if not doc_string:
                            doc_string = True
                        else:
                            doc_string = False
                
                words = line.split()            # split each line into a list of words/elements

                # test if the element is class instances using several conditon testers
                if len(words) > 0 and words[0] == 'class' and not doc_string:
                    class_count += 1
                    
            data.close()                     
            
        return (lineslen,class_count)
    
    
    
    except:                                     # if the current module is not a python folder try the file case:
        
        
        try:
            #print('here')                                    # try statement to check if the current module is python coded (single file case)
            file = mod.__file__                 # use the __file__ method to check for the location of the python file
        
                         # check the file is python coded
            data = open(file,"r", encoding='ISO-8859-1')      # open the current file
            data_test = [line for line in data]         # create the data_test as a list of each line
            data.seek(0)                                # return to the start of the file
                
                
                
            lineslen =  len(data.readlines())           # count the number of lines in the python file

            doc_string = False                          # assign the docString tester to flase
               
            for line in data_test:                      # test for each line in data_test
                line = line.strip()    
                
                # if line[:3] == '"""' and line[-3:] == '"""': 
                #     continue
                          
                if line[:3] == '"""' and line[-3:] == '"""':
                    doc_string=False
                else:        
                    # if the line starts or ends with a docstring symbol, assign the tester to true or false depending on what it currently is
                    if line[:3] == '"""' or line[-3:] == '"""' or line [:4] == 'r"""':                            
                        if not doc_string:
                            doc_string = True
                        else:
                            doc_string = False
                        
                
                
                words = line.split()        # split each line into a list of each word/element 

                    # check if the element is a class instances base on several conditions
                if len(words) > 0 and words[0] == 'class' and not doc_string:
                         #print(line)
                    class_count += 1
                    
            data.close()
        
    
            return (lineslen,class_count)
            
        # excpetions if the code fails, i.e. the modul/file is not python coded - return None
           
   
        except: 
            return None
    
    
    
    



def task5():
    """
    Prints all cyclical depndecies for packages in importable_stdlibs using 
    arros to show dependencies in a numbered output

    Returns
    -------
    None.

    """
    
    stdlibs = set(get_stdlib_packages())               #find the list of all stdlibs 
    importable_stdlibs = set(get_real(stdlibs))        #use stdlibs to find the set of importable stdlibs
    
    cycles = find_cycles(importable_stdlibs)           #call the helper function find_cycles on the set of importable stdlibs
    count = 0                                          #initiate the counter for outpur listing
    print("The StdLib packages form a cycle of dependency:")
    for cycle in cycles:
            count += 1
            print("{}: ".format(count) + "-> ".join(cycle))
    
    
    
    

def find_cycles(importable_stdlibs):
    """
    A function called by task 5 to find all cyclical depdencies for packages 
    in importable_stdlibs using recurive_help()

    Parameters
    ----------
    importable_stdlibs : list
        A list of all importable_stdlibs.

    Returns
    -------
    cycles : list of lists
        the list of all cyclical dependencies in importable_stdlibs.

    """
    import importlib
    cycles = []             # initiate the list of cycles to empty  

    for stdlib in importable_stdlibs:
        std_cycles = []                                 # initiate the list of current cycles for the stdlib
        mod = importlib.import_module(stdlib)           # import the stdlib
        resource = set(vars(mod).keys())                # get resources of the module "stdlib"
        dependent_mods = resource & importable_stdlibs  # get dependent package names among "importable_stdlibs"
        dependent_mods.discard(stdlib)                  # exclude duplicates (e.g. a function with the same name)
        dependent_mods = list(dependent_mods)
        
        for depend in dependent_mods:             # check every dependecy of the stdlib
            current_cycles = []                 # initiate the list of cycles for the stdlib and current dependency
            current_cycle = [stdlib, depend]      # Add the current depend - dependency of stdlib and stdlib to the current cycle
            # call the recursive function:
            current_cycles = recursive_help(importable_stdlibs, stdlib, depend, 
                                        current_cycle, current_cycles)
            # add the current cycles to the stdlibs cycles:
            std_cycles += current_cycles
        
        
        # add the stdlib cycles to the list of overall cycle:
        cycles += std_cycles

    return cycles



def recursive_help(importable_stdlibs, stdlib, depend, 
                   current_cycle, current_cycles):
    """
    
    recursive function called by find_cycles to find all cyclical depdencies 
    for a given stdlib by calling itself and itterating over the dependicies 
    of the current stdlib 'depend' which is a sub dependency of the stdlib

    Parameters
    ----------
    importable_stdlibs : list
        A list of all importable_stdlibs.
    stdlib : package
        the stdlib package whos cycles are being inspected.
    depend : package
        the current stdlib package being inspected..
    current_cycle : list
        The current cycle we are forming.
    current_cycles : list of lists
        the list of current cycles for the given stdlib.

    Returns
    -------
    current_cycles : list of lists
        the list of current cycles for the given stdlib..

    """
    import importlib
    
    mod = importlib.import_module(depend)               # import the current dependency "depend"
    resource = set(vars(mod).keys())                  # get resources of the module "name"
    dependent_mods = resource & importable_stdlibs    # get dependent package names among "importable_stdlibs"
    dependent_mods.discard(depend)                      # exclude duplicates (e.g. a function with the same name)
    dependent_mods = list(dependent_mods)
    
    # to stop recursion depth errors
    if len(current_cycle) > 100:
        return;
    
    # itterate over every dependent module for the current stdlib - depend
    for depend in dependent_mods:
        if depend == stdlib:
            # if the depedent module is the stdlib we are searching for cycles of then add this 
            # cycle to the list of all current cycles for the stdlib
            current_cycles += [current_cycle + [depend]]

        else:
            # if the dependent module is not the stdlib we are searching for cycle of
            # continue recursive calls to check if a subdependecy is the stdlib we are searching for
            if current_cycle.count(depend) == 0:       #check if depend is already in the current cycle
                recursive_help(importable_stdlibs, stdlib, depend, 
                               current_cycle + [depend], current_cycles)
            
    return current_cycles


# used for testing to find the cycles fro one stdlib
# def find_acycle(stdlib):
#     std_cycles = []
#     import importlib
#     stdlibs = set(get_stdlib_packages())
#     importable_stdlibs = set(get_real(stdlibs))
    
#     mod = importlib.import_module(stdlib)
#     resource = set(vars(mod).keys())                  # get resources of the module "name"
#     dependent_mods = resource & importable_stdlibs    # get dependent package names among "importable_stdlibs"
#     dependent_mods.discard(stdlib)                    # exclude duplicates (e.g. a function with the same name)
#     dependent_mods = list(dependent_mods)
        
#     for elem in dependent_mods:
#         current_cycles = []
#         current_cycle = [stdlib, elem]
#         current_cycles = recursive_help(importable_stdlibs, stdlib, elem, 
#                                         current_cycle, current_cycles)
#         std_cycles += current_cycles
            
#     return (std_cycles)
    


    
    
def analyse_stdlib():
    #task1()
    #task2()
    #task3()
    task4()
    #task5()


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Sam Eckton'
    ID   = 'u7309356'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP1730.2022.S2')
    analyse_stdlib()