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
    
    
    lines_dic = {}
    class_dic = {}
    non_python = []
    null_classes = []
    null_lines   = []
    stdlibs = set(get_stdlib_packages())
    importable_stdlibs = set(get_real(stdlibs))
    for stdlib in importable_stdlibs:
        if explore_package(stdlib) == None:
            non_python += [stdlib]
        else:
            (lines_count, class_count) = explore_package(stdlib)
            
         
            if class_count == 0 and lines_count == 0: 
                null_classes += [stdlib]
                null_lines   += [stdlib]
            
            
            elif class_count == 0:
                null_classes += [stdlib]
                lines_dic[stdlib] = lines_count
            
            
            else:
                lines_dic[stdlib] = lines_count
                class_dic[stdlib] = class_count
        
    
    lines_dic = [x[0] for x in sorted(lines_dic.items(), key = lambda kv : kv[1], reverse = True)]
    class_dic = [x[0] for x in sorted(class_dic.items(), key = lambda kv : kv[1], reverse = True)]
    
    #print(len(null_classes))
    #print((null_lines))
    
    #class_dic = [x[0] for x in class_dic]
    #lines_dic = [x[0] for x in lines_dic]
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
    mod = importlib.import_module(a_package)    
    lineslen = 0
    class_count = 0
    
    
    try:
        path = mod.__path__
        py_files = glob.glob(path[0] + "/**/*.py", recursive = True)
        
        if len(py_files) == 0:
            return None
        
        for file in set(py_files):
            data = open(file,"r", encoding="utf8")
            #print('here1')
            #print(file)
            
            
            
            data_test = [line for line in data]
            #print('here2')
            data.seek(0)
            #print('here3')
            lineslen += len(data.readlines())
            
            
            doc_string = False
               
                
            for line in data_test:  
                line = line.strip()
                                        
                if line[:3] == '"""' or line[-3:] == '"""':                            
                    if not doc_string:
                        doc_string = True
                    else:
                        doc_string = False
                
                words = line.split()
                    # print(words)
                if len(words) > 0 and words[0] == 'class' and not doc_string:
                    class_count += 1


            data.close()
            
            
        return (lineslen,class_count)
    
    
    
    except: 
        #print("arrived here") #to check if the code is correctly identify a single python file
        try: 
            file = mod.__file__
        
            if file[-3:] == '.py':
                data = open(file,"r", encoding="utf8")
                data_test = [line for line in data]
                data.seek(0)
                
                
                
                lineslen =  len(data.readlines())
                #class_count = len(data_test)
                
                # #print(len(data_test))
                
                # class_count = 0
                doc_string = False
               
                
                for line in data_test:  
                    line = line.strip()
                                        
                    if line[:3] == '"""' or line[-3:] == '"""':                            
                        if not doc_string:
                            doc_string = True
                        else:
                            doc_string = False
                
                    words = line.split()
                    # print(words)
                    if len(words) > 0 and words[0] == 'class' and not doc_string:
                         #print(line)
                         class_count += 1
                    
                
                
                data.close()
        
    
                return (lineslen,class_count)
            
            else:
                return None
   
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
    
    stdlibs = set(get_stdlib_packages())
    importable_stdlibs = set(get_real(stdlibs))
    
    cycles = find_cycles(importable_stdlibs)
    count = 0
    print("The StdLib packages form a cycle of dependency:")
    for cycle in cycles:
            count += 1
            print("{}: ".format(count) + "-> ".join(cycle))
    
    
    
    
# incomplete still testing find_acycle
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
    cycles = []             # initiate the list of dependencies 

    for stdlib in importable_stdlibs:
        std_cycles = []
        mod = importlib.import_module(stdlib)
        resource = set(vars(mod).keys())                  # get resources of the module "name"
        dependent_mods = resource & importable_stdlibs    # get dependent package names among "importable_stdlibs"
        dependent_mods.discard(stdlib)                    # exclude duplicates (e.g. a function with the same name)
        dependent_mods = list(dependent_mods)
        
        for elem in dependent_mods:             # recursive for every dependecy of the stdlib
            current_cycles = []                 # initiate the list of cycles fo the stdlib
            current_cycle = [stdlib, elem]      # Add the current elem - dependency of stdlib and stdlib to the current cycle
            # call the recursive function
            current_cycles = recursive_help(importable_stdlibs, stdlib, elem, 
                                        current_cycle, current_cycles)
            # add the current cycles to the stdlibs cycles
            std_cycles += current_cycles
        
        
        # add the stdlib cycles to the list of overall cycles
        cycles += std_cycles

    return cycles


# recurisve helper function to check for all possible cycles
def recursive_help(importable_stdlibs, stdlib, elem, 
                   current_cycle, current_cycles):
    """
    
    recursive function called by find_cycles to find all cyclical depdencies 
    for a given stdlib by calling itself and itterating over the dependicies 
    of the current stdlib 'elem' which is a sub dependency of the stdlib

    Parameters
    ----------
    importable_stdlibs : list
        A list of all importable_stdlibs.
    stdlib : package
        the stdlib package whos cycles are being inspected.
    elem : package
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
    
    mod = importlib.import_module(elem)
    resource = set(vars(mod).keys())                  # get resources of the module "name"
    dependent_mods = resource & importable_stdlibs    # get dependent package names among "importable_stdlibs"
    dependent_mods.discard(elem)                      # exclude duplicates (e.g. a function with the same name)
    dependent_mods = list(dependent_mods)
    
    # to stop recursion depth errors
    if len(current_cycle) > 20:
        return;
    
    # itterate over every dependent module for the current stdlib - elem
    for obj in dependent_mods:
        if obj == stdlib:
            # if the depedent module is the stdlib we are searching for cycles of then add this 
            # cycle to the list of all current cycles for the stdlib
            current_cycles += [current_cycle + [obj]]

        else:
            # if the dependent module is not the stdlib we are searching for cycle of
            # continue recursive calls to check if a subdependecy is the stdlib we are searching for
            if current_cycle.count(obj) == 0:       #check if obj is already in the current cycle
                recursive_help(importable_stdlibs, stdlib, obj, 
                               current_cycle + [obj], current_cycles)
            
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
    

# used for testing 
# def get_dep_mods(stdlib):
#     import importlib
#     stdlibs = set(get_stdlib_packages())
#     importable_stdlibs = set(get_real(stdlibs))
    
#     mod = importlib.import_module(stdlib)
#     resource = set(vars(mod).keys())                  # get resources of the module "name"
#     dependent_mods = resource & importable_stdlibs    # get dependent package names among "importable_stdlibs"
#     dependent_mods.discard(stdlib)                    # exclude duplicates (e.g. a function with the same name)
#     dependent_mods = list(dependent_mods)
    
#     return dependent_mods
    



# used to check there are no repeated cycles in our output for task5()
# doesnt really work and isnt actually needed i dont think as all cycles are 
# cylical and therefore cannot be the same



# def check_cycles(cycles_to_be_ordered):
#     import copy
#     cycles = copy.deepcopy(cycles_to_be_ordered)
#     for cycle in cycles:
#          cycle.sort()

#     for cycle in cycles:
#         count = 0
#         for i in range (len(cycles)): 
#             if cycles[i] == cycle and count > 0:
#                 cycles_to_be_ordered.remove[i]
#             elif cycles[i] == cycle:
#                 count += 1

#     return cycles_to_be_ordered
    
    
    
    
    
    
def analyse_stdlib():
    task1()
    task2()
    task3()
    task4()
    task5()


# The section below will be executed when you run this file.
# Use it to run tests of your analysis function on the data
# files provided.

if __name__ == '__main__':
    NAME = 'Sam Eckton'
    ID   = 'u7309356'
    print(f'My name is {NAME}, my id is {ID}, and these are my findings for Project COMP1730.2022.S2')
    analyse_stdlib()