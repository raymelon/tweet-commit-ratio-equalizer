import os
import subprocess

# Define the repository directory and the filename
repo_dir = '.'  # Update this to your actual repository path
filename = 'blank_file.txt'

# Change directory to the repository
os.chdir(repo_dir)
print(os.getcwd())

# Create 12,494 commits
for i in range(12494):
    # Create or overwrite the blank file
    with open(filename, 'a') as file:
        file.write(f'Commit number {i + 1}\n')

    # Add the file to the Git staging area
    subprocess.run(['git', 'add', filename])

    # Commit the file
    commit_message = f'Commit number {i + 1}'
    subprocess.run(['git', 'commit', '-m', commit_message])

print('Completed 12,494 commits.')
