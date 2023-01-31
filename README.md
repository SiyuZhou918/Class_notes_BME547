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

* print("The answer is {}".format(x)) [give variable]
  print("The HDL result of {} is connected {]".format(HDL_value, HDL_analy))
  
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