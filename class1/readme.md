# Notes for class 1 of python network automation class
## Homework
### Git
1. Create a GitHub account (it's free for public repositories).

2. Create a new repository in GitHub for this class. Add a README file and a Python .gitignore file.

3. Clone the repository that you just created on GitHub into your home directory in the lab environment.

4. Configure your name and email address on the lab server:
```
$ git config --global user.name "John Doe"
$ git config --global user.email jdoe@domain.com
```

5. Add and commit three files into your repository in the lab environment. Use 'git status' to verify that all your changes have been committed and that you are working on the 'main' branch. Push these changes up to GitHub.

6. Create a 'test' branch in your repository.
a. Ensure that you are working on the 'test' branch.
b. Add two directories to the 'test' branch. Each directory should contain at least one file. These files should be committed into the 'test' branch.
c. Use 'git log' to look at your history of commits.
d. Modify one of your previously committed files. Use 'git diff' to look at the pending changes in this file. Add and commit these changes.

7. Push the 'test' branch up to GitHub.

8. Create a Pull Request inside of GitHub (pull request that would merge the 'test' branch into the 'main' branch). Look at the 'files changed' in the pull request. Merge the pull request.

9. Back on your AWS server
a. Switch back to the 'main' branch.
b. Use a 'git pull' to retrieve all of the updates from GitHub on the main branch.
c. Verify your 'main' branch now has all of the changes that you had previously made in the 'test' branch.

10. In the 'main' branch use 'git rm' to remove some file from the branch. Commit this change.

11. Edit one of your files. Once again use 'git diff' to look at the change pending in that file. Use 'git checkout -- <file>' to discard that pending change. Verify your 'git status' is now clean.

12. In GitHub, edit the README.md file and commit a change to the 'main' branch in GitHub. On the lab server also edit the README.md file and commit the change into the lab server. Use 'git pull' to pull the 'main' branch from GitHub into the lab server. At this point you should have a merge conflict. It should look something like this:
```
$ git pull origin main
From https://github.com/ktbyers/pyneta
 * branch            main     -> FETCH_HEAD
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.​


Edit the README.md file to correct the merge conflict. The README.md file should have something like the following inside of it:
```

```
​$ cat README.md
# pyneta
Test PyNet Repository

Some additional information on this repository.

<<<<<<< HEAD
Create a merge conflict.
=======
More changes to readme.
>>>>>>> 1690ce5a6ddb640198ccf3bca26f32a65d772b92


The ​'<<<<<', '=====', '>>>>>' indicate where the inconsistencies on the file are. Git is basically stating I have this first line(s) from one change and this second line(s) from another change and I don't know which one you want to keep. Which line do you want to keep (could be one of the lines, both of the lines, none of the lines).

Here is how I fixed the merge conflict in the above file:

$ cat README.md
-----------------
# pyneta
Test PyNet Repository

Some additional information on this repository.

Create a merge conflict.

More changes to readme.​
-----------------
# Then I need to add and commit the file
$ git add README.md 
$ git commit -m "Fixing merge conflict"
[main e87901a] Fixing merge conflict
```

### Netmiko
1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file. Simply print the router prompt back from this device to verify you are connecting to the device properly.

2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the Netmiko connection creation. Once again print the prompt back from the devices that you connected to.

3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.

