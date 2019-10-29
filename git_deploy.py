from git.repo.base import Repo


class GitWork:
    """Working with git"""

    def __init__(self, repo_url, repo_dir):
        self.repo_url = repo_url
        self.repo_dir = repo_dir


    def clone_repo(self):
        """Clone repository"""

        try:
            Repo.clone_from(self.repo_url, self.repo_dir)
            print("Repo created.")
        except Exception as e:
            print(str(e))


    def create_branch(self, branch_name):
        """Create branch"""

        try:
            my_repo = Repo(self.repo_dir)
            my_repo.create_head(branch_name)
            print("New branch", branch_name, " was created.")
        except Exception as e:
            print(str(e))


    def switch_branch(self, new_branch):
        """Switch branch"""

        try:
            my_repo = Repo(self.repo_dir)
            curr_branch = str(my_repo.active_branch)
            my_repo.git.checkout(new_branch)
            print("Switch branch from ", curr_branch, "to", new_branch)
        except Exception as e:
            print(str(e))


    def commit_and_push(self, commit_message):
        """Commit and push changes"""

        try:
            my_repo = Repo(self.repo_dir)
            my_repo.git.add('--all')
            my_repo.index.commit(commit_message)
            origin = my_repo.remote('origin')
            origin.push(str(my_repo.active_branch))
            my_repo.git.add(update=True)
            print("Push completed.")
        except Exception as e:
            print(str(e))