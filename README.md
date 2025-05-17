# ✅ Math & ML & DS & DL & AI

---

## 📦 Setup and Requirements

### Step 0: Install Git

If Git is not already installed, follow these instructions:

* **macOS (via Homebrew)**:

  ```bash
  brew install git
  ```
* **Windows**:

  1. Download Git for Windows from [https://git-scm.com/download/win](https://git-scm.com/download/win).
  2. Run the installer and accept the default options.

  ```powershell
  # After installation, verify:
  git --version
  ```
* **Ubuntu/Linux**:

  ```bash
  sudo apt update
  sudo apt install git
  ```
* **Optional**: Configure your Git user name and email:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

### Step 1: Install Python

If Python is not already installed, follow these instructions:

* **macOS (via Homebrew)**:

  ```bash
  brew install python
  ```
* **Windows**:

  1. Download Python from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).
  2. Run the installer and ensure **Add Python to PATH** is checked.
* **Ubuntu/Linux**:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip python3-venv
  ```

### Step 2: Clone the Repository

```bash
Git clone and navigate into the project directory:

    git clone https://github.com/virgin-code/ML-DS-DL-AI.git
    cd ML-DS-DL-AI
```

### Step 3: Create and Activate a Virtual Environment

It's recommended to use `venv` to isolate project dependencies:

* **macOS / Ubuntu**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows**:

  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Workflow for Students

Follow this simple Git workflow to submit and manage your solutions:

| Actor   | Step                              | Git Commands                                                 |
| ------- | --------------------------------- | ------------------------------------------------------------ |
| Student | Create a personal solution branch | `git checkout -b solutions/<username>`                       |
| Student | Work locally, commit often        | `git add .`<br>`git commit -m "solve: exercise description"` |
| Student | Pull latest changes before push   | `git pull origin <branch>`                                   |
| Student | Push solutions                    | `git push -u origin solutions/<username>`                    |

> Replace `<username>` with your GitHub username and `<branch>` with your current base branch (e.g., `main`).

## 🛠️ Useful Git Commands

* **Check configured Git user**

  * `git config user.name`: displays the name set for your commits.
  * `git config user.email`: displays the email set for your commits.

* **See current branch**

  * `git branch`: lists all local branches, with the current branch highlighted.

* **List remote repositories**

  * `git remote -v`: shows the URLs of the remote repositories (for fetch and push).

* **Fetch updates from remote**

  * `git fetch`: downloads new commits and branches from the remote without merging them into your working branch.

* **Pull latest changes (merge)**

  * `git pull origin <branch>`: fetches updates from the specified remote branch and merges them into your current branch.

* **Pull with rebase**

  * `git pull --rebase origin <branch>`: fetches updates and rebases your local commits on top of the fetched branch, keeping a linear history.

* **Switch to another branch**

  * `git checkout <branch>`: switches your working directory to the specified branch.

* **Push your branch**

  * `git push origin <branch>`: uploads your local commits from the specified branch to the remote repository.## ℹ️ Difference Between `venv` and System Python

* **System Python**:

  * Installed globally on your machine.
  * Packages installed with `pip` may require `sudo` or admin privileges.
  * Global installations can lead to version conflicts between projects.

* **Virtual Environment (`venv`)**:

  * Creates an isolated Python environment per project.
  * Dependencies are contained within the `venv` folder.
  * Avoids package conflicts and allows multiple projects to use different versions of the same library.
  * Recommended for project reproducibility and cleaner dependency management.

Happy coding! 🚀
