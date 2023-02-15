# Class_notes_BME547
I will use this repos to take down notes while learning and practice the skill I learned meanwhile.

## Lec Jan 18__Intro to git  

* Mac change prompt main 

* git commit -m “purpose”

* Commit steps:
    1. nano file
    1. git status
    1. git add file
    1. git status 
    1. git commit -m “purpose”

* Open .

* Two space at the end to start a new line

* ls -a

* git log --oneline

* To cover the content on github, follow the steps below:
    1. git add .
    1. git commit -m""
    1. git pull
    1. git push
  

* Use different signs to start different samples: *,-,+ and with "\t"

* git commit [forget to have purpose, type "I" to switch to insert mode, then "esc" to ":", type "wq" to quit] [refer to "escaping VIM editor when git commit"
* markdown formatting "# Title", "## Subtitle"
* compare versions of commits:
    1. git log --oneline
    2. git diff xxx..xxx       [deleted contents shown in red, added changes shown in green?]
    3. use arrows to display and "esc" to quit

*  git diff, git diff xxx..xxx, git diff --staged

* Can also made changes directly on github, remember to change commit description

* rm -rf file
* rm file
* command+T [new window to continue]

### branch

* git branch  
* git branch test_info  [create new branch]
* git checkout test_info [change branch]
* Use "git add" to single file and use "git commit" to multiple files [sometime fixing same problem]
* Recommend merging branches on github [to test and get permission]
    - git push --set-upstream..
    - on github, choose "pull requests", choose branches and then merge


## Lec Jan 20__Intro to Python
* Function:
    - take input
    - do the work
    - return the output
* use "Tab" to automatically fill the filename

* 
    + print("The answer is {}".format(x)) [give variable]
    + print("The HDL result of {} is connected {}".format(HDL_value, HDL_analy))
    + print("The HDL result of {:.1f} is connected {}".format(HDL_value, HDL_analy)) [display a single decimal place]
    + round(weight,1) [give rounded number with specified number of decimals] 
  
  
* functions can have multiple returns with different types of variables [only Python can do that, no need to specify whether Boolean or Integer]
[image01]
[image02]
[image03]

* input("prompt") [get input from keyboard][this will give a string][need to transfer to integer--int()]
[image04]

* To keep updated, when doing projects, always remeber to checkout to main branch and then git pull

* in-function variables are local so same name of variables can be used in different functions

* "if, elif, else" in Python
[image05]
* "while" in Python
[image06]

* seperate the function name and variable name

## Lec Jan 25__Modules and Virtual Environments
* import files:
    1. import file [give access to all functions included]
    filename.function name
    1. import ...[filename] as ..[shortcut]
    1. from filename import function_name [import single function]
    when use the function, just use its name
    [image08]

* special variable with two "_" in front and back of it
 eg: format(__name__)
 
 with main module -- gives the main
 with other module -- gives the actual name
 [image07] 

* comment sign "#"   

* if __name__ == "__main__":   [!!]   [use this to later input anything, always shows at the bottom of the file]

* __pycache__ file
* touch .gitignore [!!] [usually do add this file in your repository][ignore everthing from there, include filename here]
* .gitignore always include:
    - `__pycache__`  
    - .ipynb_checkpoints
	- myvenv [not add virtual env to your repository]

* Create virtual env:
    0. create a new branch to setup venv
    1. python -m venv myvenv [on Mac][create virtual environment]
    2. source virtual_env_name/bin/activate [activate the env]
    1. nano requirements.txt [to capture a file with packages I need]
        - usually include:
            - jupyter
            - pytest [this two are for automatic testing]
            - pytest-pycodestyle
    1. touch .gitignore
    2. pip install -r requirements.txt
    3. pip list [show what package you download]
    3. git add .gitignore
       git add requirements.txt
    3. git commit
    3. git push branch
    3. deactivate

* pip install package_name [easy way but not recommended]

* install package:[!!]

  1. nano requirements.txt [to capture a file with packages I need]
  2. pip install -r requirements.txt
  3. pip list [show what package you download]

* Jupyter notebook:
    1. "shift+enter" [run jupyter notebook]
    1. "ctrl+enter"  [run but don‘t create new line]
    1. cell-> cell type -> markdown
    1. "ctrl+C" to exit

* sometime we don‘t push branches, we just commit them and leave them, then swith to main branch

* virtual env does nothing to git, they are seperate

* Markdown format  
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet  
    **text** bold  
    *emphasized text*  
    $\LaTeX$   
    $y = x^2$  
    a single back-tick(\`)  [give punctuation]  
    _if_  italic text

* %whos 【to inspect the types of all active variables】

* Python functions:
    - type() [see the type]
    [image09]
    - 
    [image10]
    - tuples and arrays
        + the first index of a list (or tuple or any array) is 0 in Python; MATLAB starts indexing at 1
        + access items of a tuple using []; MATLAB uses (). 
        + In Python, () is used to call functions and methods.

* commont terms:
    parenthese [  ()  ]

* nest tuples within tuples... and can mix datatypes
    [image11]
    - tuples are immutable

* lists
    - Lists are mutable. 
    - tuples are created and printed using parentheses 
    (example: my_tuple = (1, 2, 3));
    - lists are created and printed using square brackets (example: my_list = [1, 2, 3]). 
    - both use [ ] to access the contents
    - list functions:  
        + .append(), .pop(), .count(), .reverse() and .sort()
        + lists are mutable
        [image12]
    - List Comprehensions:
        - Python uses lists instead of loops:
             ```
             [x**2 for x in (1, 2, 3)]  # Output: [1, 4, 9]
             ```
        + x*2
        + x**2  [x^2]

* `for` loops
    - Python can directly iterate on the content of a tuple,   
    - unlike MATLAB, which likes to iterate on a specified range of numbers
    [image13]
    - conditionals in a list comprehension
    image[image15]
    - two different ways for iterating lists
        - iterating one list
    ```
    for i, patient in enumerate(db)
    print("Patient {} is in room {}".format(patient[0], room_numbers[i]))

    ```
        
    - iterating both lists

    ```
    for patient, rn in zip(db, room_numbers)
    print("Patient {} is in room {}".format(patient[0], rn))
    ```
    db, room_numbers should be in same size

* `enumerate()`  
    - carry along a numerical index that corresponds to which iteration you are on in the loop
    - first number is index, second one is the element
    [image14]


# Lec Jan 27__Merge conflicts, Modulartiy and Tags

* reasons to write modular codes:
    + organization(readibilty)
    + testing
    + reusability

* tags:        [start from that point]
    + git tag -a tag_name -m" "        [usually gives after the **merge pull** action] [usually tag on main branch][push tags and push branches are seperate processes]
    + git tag -a tag_name commit_id -m" "
    + git checkout v1.0
    + git tag                       [list all your tags]
    + git show v1.0
    + git push origin v1.0
    + git push --tags

# Lec Feb 1__Lists and loops

* `is` and `==`
```
if found_patient is False:
```
here we only use `is` when there is a __boolean variable__

* mutable varibles (like lists, dictionary and classes) __can be changed without `return`__ in a function, it doesn't work well with imutable variables (like strings, numbers)

* do add a `return` at the end of the function, it is visible for you showing the end of function, you can just use `return` sentence


# Lec Feb 3__Unit testing

* pytest convention
    - file name for testing: `test_+file_name` [always name like this thus pytest will automatically run the file with this name]
    - function name for testing: `test+function_name`

* 3As for testing:
    - Arrange   [~ data for testing]
    - Act       [call function]
    - Assert    [~ to check if the function is correct]
        ```
        assert a boolean/condition sentence 
        ```
        [continue ruuning if True, throw error if False, thus pytest will use the error to know the function fails]
        eg: assert answer == "Normal"
    eg: 
    ```
    def test_HDL_analysis():
    from blood_calculator import HDL_analysis
    # Arrange
    HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal" 
    ```

* `pytest` or `pytest -v`[give more details of testing]
   pytest + filename  [only run specific file]

* function decorator: [gives addtional function alias]
import module_name  
@module_name.mark.parametrize()
```
import pytest 

@pytest.mark.parametrize("HDL_input, expected",
[
(65, "Normal"),
(40, "Borderline Low"),
(20, "Low")
])
def test_HDL_analysis(expected, HDL_input):
    from blood_calculator import HDL_analysis
    # Arrange
    # HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected 
```

* unit testing:
    - we don't need to test every input, we just test every branch
    - if two test funtinos have the same name, the test will only output the last one
    - always write unit test before writing the function itself
    - write test and function itself on the same branch

* pytest -v --pycodestyle
    - PEP8 convention


# Lec Feb 8__Unit testing
* test: True, False, border
eg: if assert age >=18, test(15, 18, 20)

* test
```
import math
def area_of_ellipse(x: list):
    data = x.split(",")
    if len(data) = 1:
        area = math.pi * data[0]**2
    elif len(data) = 2:
        area = math.pi * data[0] * data[1]
    elif len(data) = 4:
        a = (data[2] - data[0]) / 2
        b = (data[3] - data[1]) / 2
        area = math.pi * a * b
    else:
        area = None
    return area
```

test:
[
([1.5], area)
([1.5, 2.5], area)
([1, 10, 20, 30], area)
([1, 2, 3], None)
([], None)
]

* plural [复数, eg: apples]

* robust test example:

          
        def parse_weight_input(weight_input):
            if weight_input == "":
                return None
            if weight_input.find(" ") < 0:
                return None
            weight, units = weight_input.split(' ')
            weight = float(weight)
            units = units.lower()
            if units[-1] == "s":
                units = units[0:-1]
            if units in ["lb", "pound"]:
                weight_kg = convert_lb_to_kg(weight)
            elif units == "kg":
                weight_kg = weight
            else:
                return None
            weight_kg = round(weight_kg)
            return weight_kg
    
    - weight_input.find(" "):
        - return -1 if there is no string 
        - return the location if find the string

    - units = lbs
        - units[-1] = s
        - units[0:-1] = lb

* when testing a function that will call another function, test the two different functions seperately

* pytest.approx(0.3, abs=0.1)
[0.3 +- 0.1]
[ Decimals are stored in binary, doesn't exactly equal to 0.3 ]
[ abs changes the absolute error]
eg:
import pytest
def test_add():
    from add import add
    answer = add(0.1, 0.2)
    assert answer == pytest.approx(0.3)

* always __create the .github folder when start__ a new repository, but __after create venv__

# Lec Feb 10__Dictionaries and Classes
* <= 29.9 and <30 [for the first case, 29.95 can not be captured, so be specific about the decimal comparison]

* dictionary: 
    - more readable and understandable to use key rather than index
    - as the dictionary gets larger, the search time won't increase [just give result based on the key][no meaning to iterate a larger number of patients, just search]

* use None instead of making error
    - use None:
    ```
    patient = db.get(mrn_to_find)
    if patient is None:
            return False
    return patient
    ```
    - will get error
    ```
    patient = db[mrn_to_find]
    for patient in db:
        if patient["MRN"] == mrn_to _find:
            return patient
    return False
    ```

    * `db.values()`  
    ``` 
    for key in db:
        print("MRN: {}, Full Name: {}, Age: {}".format(db[key][patient]["MRN"],
                                                       get_full_name(patient),
                                                       db[key][patient]["Age"]))
    ```
    [return error since patient are keys]

    ```
    for patient in db.values():
        print("MRN: {}, Full Name: {}, Age: {}".format(patient["MRN"],
                                                       get_full_name(patient),
                                                       patient["Age"]))
    ```
    [patient now is dictionary]

