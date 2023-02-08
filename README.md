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
* import file [give access to all functions included]
  filename.function name
* import ...[filename] as ..[shortcut]
* from filename import function_name [import single function]
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
    - __pycache__
    - .ipynb_checkpoints
	- myvenv [not add virtual env to your repository]

* Create virtual env:
    1. python -m venv myvenv [on Mac][create virtual environment]
    2. source virtual_env_name/bin/activate [activate the env]
    1. nano requirements.txt [to capture a file with packages I need]
    1. touch .gitignore
    2. pip install -r requirements.txt
    3. pip list [show what package you download]
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
