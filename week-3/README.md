# 🏆 Review a PR & Ignore unwanted files
In the last week's (week-12) exercise we pushed changes from local repository to GitHub. The local repository was name `master` and so was the remote GitHub repository. The `master` branch is your main branch, hence when collaborating on a project with multiple people or experimenting with a new code, you don't want to muddle the main branch. As such this week we will learn how to use user branches for experimenting and then pushing changes to master using `Pull Request` when ready. 

We will look at how a PR is reviewed and the changes are merged. In addition we will also take a look at how to ignore files that are temporary in nature.

# ✅ Prerequisites
I assume you have completed tasks from week-2

# 🤸 Let's get started
- Open your https://github.com profile
- Go to the profile icon and select "Your repositories"
- Select the repository you would like to work on
- Select Settings for repo
- Select Collaborators from the panel
- Add people
- They would have received the invitation 
- Open a command prompt or terminal window on your machine 
- Go to the `tools` folder
- You can open `vscode` from the current directory using the command below. The "." here represents the current directory you are in, while ".." represents the parent directory

    ```
    code .
    ```
- Create a user branch from master. The user branch is created from the local master branch. As such before we create the user branch we need to make sure that the local master branch is upto date. We do this by executing the following command.
    ```
    git pull origin master
    ```
    ```
    From https://github.com/wayoutisin/student
    * branch            master     -> FETCH_HEAD
    Already up to date.
    ```
- We can see that our local master branch has all the changes from GitHub.
- Next we create a user branch from our local master branch
    ```
    git checkout -b wayoutisin/modulus
    ```
- On the prompt you will see the message as 
    ```
    Switched to a new branch 'wayoutisin/modulus
    ```
- Create a file `modulus.py` under the `week-2` folder and add a simple function to compute the remainder in a division operation
    ```
    def mod(x, y):
    return x%y

    if __name__ == "__main__":
        x = 1
        y = 2
        print(f"{x} % {y} = {mod(x, y)}")
    ```
-  You can execute the file by starting a Terminal from inside vscode and executing the following command. Please ensure that path to modulus.py is correct.
    ```
    python week-2/modulus.py
    ```
- A successful execution would show the following results
    ```
    1 % 2 = 1
    ```
- So far our code is in our user branch. We need to commit this change in the user branch before pushing it to GitHub

    ```
    git add .
    git commit -m "Adding modulus function"
    ```
- You can switch to your master branch at this stage and check for yourself that the changes you committed to the user branch are not present in your local master branch.
    ```
    git switch master

    # Switch back to the user branch
    git switch wayoutisin
    ```

- Finally we push our committed code from the local git repository user branch to GitHub using the following command
    ```
    git push origin head
    ```
- This will create a new branch `wayoutisin/modulus` in GitHub. This is important because your changes are now available for someone to review before it can be merged to master. However we still need to perform a few steps before the code can be merged to master
- The change would appear on GitHub as below
    <img src="../img/userbranch.png">
- Click "Compare & pull request" to create a PR. A PR (pull request) is a way to push a change from your local branch to GitHub maain (master) branch
    <img src="../img/pullrequest.png">
- As you can see the code is being moved from the user branch `wayoutisin\modulus` to `master`. We have documented our PR with comments for ease of understanding. Ideally we would also assign reviewers to this PR, who would then review and approve the PR request, however that is an exercise for you to accomplish by next week 😄
- Once the reviewers have approved the PR request, we can merge the pull request using the "Merge pull request" option
    <img src="../img/mergepr.png">

- Finally after merging our changes to the main (master) branch in GitHu, we should refresh our local master branch using the command 
    ``` 
    git pull origin master
    ```
-  Why do we need to review the PR? Well when working in a large team with multiple developers we would like to have a process to ensure only quality code gets into the main branch (master). One way to ensure that is PR.
-  What do you with the user branch? You can drop 🗑️ the user branch both locally or on GitHub once you have merged your changes to main (master). Also remember when your PR is active you can make multiple changes to your local branch and push it to master. They will all be collected under the active PR you have in GitHub till it is merged to main (master) or closed.

    ```
    git branch -d wayoutisin/modulus
    ```
# 🤔 Exercise
Here are 2 exercise for you for the week 
- Add a few members to your GitHub repository and assign the PR to them for review before merging to main (master)
- Create one program each of the next 6 days. Choose a name for each file and stor it a separate `{name}.py` file in the week-2 folder. Use the workflow learnt here to push your code to GitHub from local machine. 