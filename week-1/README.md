# Goal
This week's goal is to get familiar with using various tools to write code as well as manage your code locally with git and remotely with GitHub. 

# Prerequisites
I assume you have installed the required tools as specified in the [README.md](../README.md) file

# Let's get started
- Open a command prompt or terminal window on your machine 
- Choose a folder where you would like to keep all your code for reference. Remember this folder as this is going to be the place where most of our code will reside as we work through week on week
- Create a folder called `tools`
  
    ```
    mkdir tools
    ```

- Change to the newly created directory

    ```
    cd tools
    ```

- Initialize this folder to be a git repository. You can learn more about git [here](https://git-scm.com/)

    ```
    git init
    ```

- Now that the git repository is initialized we can start writing code. For this we would need a code editor. Here comes `vscode`. You can open `vscode` from the current directory using the command below. The "." here represents the current directory you are in, while ".." represents the parent directory

    ```
    code .
    ```

-  This will open up vscode with a solution named "TOOLS". Create a folder "week-1" under it.

-  Create a file `math.py` under the `week-1` folder and add a function for addition, subtraction, multiplication and division using Python. Ideally you should be writing this part of the code yourself, however you can refer to the code below if you need any help
    ```
    # add two numbers
    def add(x, y):
        return x + y

    # subtract two numbers
    def sub(x, y):
        return x - y

    # multiply two numbers
    def mul(x, y):
        return x * y

    # divide two numbers
    def div(x, y):
        return x/y

    if __name__ == "__main__":
        x = 1
        y = 2
        print(f"{x} + {y} = {add(x, y)}")
        print(f"{x} - {y} = {sub(x, y)}")
        print(f"{x} * {y} = {mul(x, y)}")
        print(f"{x} / {y} = {div(x, y)}")
    ```
-  You can execute the file by starting a Terminal from inside vscode and executing the following command. Please ensure that path to math.py is correct.
    ```
    python week-1/math.py
    ```


# Exercise
Here are 2 exercise for you for the week 
- The division code can lead to divide by zero error when the denominator is 0. E.g. 1/0 is infinite. How would you handle that in the code and then merge the changes all the way to GitHub.
- Create one program each of the next 6 days. Choose a name for each file and stor it a separate `{name}.py` file in the week-1 folder. Use the workflow learnt here to push your code to GitHub from local machine. 
