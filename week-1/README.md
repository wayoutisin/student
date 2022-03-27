# 🏆 Local git repository to GitHub
This week's goal is to get familiar with using various tools to write code as well as manage your code locally with git and remotely with GitHub. 

# ✅ Prerequisites
I assume you have installed the required tools as specified in the [README.md](../README.md) file

# 🤸 Let's get started
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
- A successful execution would show the following results
    ```
    1 + 2 = 3
    1 - 2 = -1
    1 * 2 = 2
    1 / 2 = 0.5
    ```
- So far our code is in our local machine. This code is being version controlled using `git` as can be seen below using the command

    ```
    git status
    ```
    ```
    No commits yet

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
            week-1/

    nothing added to commit but untracked files present (use "git add" to track)
    ```

- We can see the folder that we just added, however git is not yet tracking the changes to this folder. So let's ask git to track the changes by using the command below.
  ```
  git add .
  ```
- This will track all files and folders under the current directory including `week-1` (you can check for yourself executing the `git status` command)
  ```
    On branch master

    No commits yet

    Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
            new file:   week-1/README.md
            new file:   week-1/math.py  
  ```
- As per the message above 👆, we still need to commit or finalize the changes. So far the changes are only being tracked. In order to commit we execute the following command 
    ```
    git commit -m "Initial Commit"
    ```
- Here is the output from the command above 👆
    ```
    [master (root-commit) 2dab44d] Initial Commit
    1 file changed, 23 insertions(+)
    create mode 100644 week-1/math.py
    ```
- Note above that we committed or finalized the changes to 1 file `math.py` with 23 lines of code. This is now committed to a local git repository. However we still need to push it to GitHub. Let's try that
- In order to push our code to GitHub we need to connect to our GitHub account. To do that we would use `GitHub cli` installed earlier. Login to GitHub using the following command 

    ```
    gh auth login
    ```
- This will show a series of inputs that you need to choose from as specified below
    ```
    ? What account do you want to log into?  [Use arrows to move, type to filter]
    > GitHub.com
    GitHub Enterprise Server

    # Choose GitHub.com

    ? What is your preferred protocol for Git operations?  [Use arrows to move, type to filter]
    > HTTPS
    SSH

    # Choose HTTPS

    ? Authenticate Git with your GitHub credentials? (Y/n)

    # Say Y

    How would you like to authenticate GitHub CLI?  [Use arrows to move, type to filter]
    > Login with a web browser
    Paste an authentication token

    # Choose Login with a web browser

    ! First copy your one-time code: XXXX-XXXX
    - Press Enter to open github.com in your browser... 

    # Press "Enter", will open a web browser and ask you to sign in to GitHub. Once singed in you would be asked to enter the code generated in your terminal (XXXX-XXXX). Enter the code to login

    ✓ Authentication complete. Press Enter to continue...

    - gh config set -h github.com git_protocol https
    ✓ Configured git protocol
    ✓ Logged in as <<yourgithubhandle>>
    ```
- Now that we have a connection with our github.com account, we can create a repository to hold our code. In the simplest form repository is a container to host your code and provide version control features
    ```
    gh repo create
    ```
-  The above command will again give you a series of options as shown below
    ```
    ? Repository name tools
    ? Repository description "Host all the example code samples for student mentoring"
    ? Visibility Public
    ? This will add an "origin" git remote to your local repository. Continue? Yes
    ✓ Created repository wayoutisin/student on GitHub
    ✓ Added remote https://github.com/wayoutisin/student.git`
    ```
-  This has now created a repository with the name `tools` under your GitHub.com account. You can verify using the link provided 👆
-  Finally we push our committed code from the local git repository from our machine to GitHub using the following command
    ```
    git push origin head
    ```
-  Why do we need to push our work to GitHub from our local machine? Well if you feel code on your machine can be safely managed forever ⌛ or you could collaborate with multiple other developers working on the same code on you local machine, you don't need GitHub 😄

# 🤔 Exercise
Here are 2 exercise for you for the week 
- The division code can lead to divide by zero error when the denominator is 0. E.g. 1/0 is infinite. How would you handle that in the code and then merge the changes all the way to GitHub.
- Create one program each of the next 6 days. Choose a name for each file and stor it a separate `{name}.py` file in the week-1 folder. Use the workflow learnt here to push your code to GitHub from local machine. 
