from git import Repo, Actor  # GitPython
import git.exc as GitExceptions  # GitPython
import os  # Python Core
import sys  # Python Core
import datetime  # Python Core


def commit(daysToGoBack):
    your_timestamp = (
        datetime.datetime.now().timestamp() * 1000 - daysToGoBack * 1000 * 60 * 60 * 24
    )
    print("Timestamp: " + str(your_timestamp))
    respository_directory = "."
    new_file_path = "definitely_new_file.txt"
    date = datetime.datetime.fromtimestamp(your_timestamp / 1e3)
    action_date = date.strftime("%Y-%m-%d %H:%M:%S")
    print("Creating commit with date" + action_date)
    action_date = str(action_date)
    message = "I am a commit log! See commit log run. Run! Commit log! Run!"
    actor = Actor("Maciej", "maciek2baba2@gmail.com")

    # Open repository
    try:
        repo = Repo(respository_directory)
    except GitExceptions.InvalidGitRepositoryError:
        print("Error: %s isn't a git repo" % respository_directory)
        sys.exit(5)

    # Set some environment variables, the repo.index commit function
    # pays attention to these.
    os.environ["GIT_AUTHOR_DATE"] = action_date
    os.environ["GIT_COMMITTER_DATE"] = action_date

    # Add your new file/s
    repo.index.add([new_file_path])

    # Do the commit thing.
    repo.index.commit(message, author=actor, committer=actor)


for dayNum in range(0, 10):
    commit(dayNum)
