# ✅ Math & ML & DS & DL & AI

---

## 📦 Setup and Requirements

### 🛠️ What is Git?

Git is a version control system that tracks changes in your code over time.
Think of it like a “save game” system for your project, where you can:

* **Commit** your progress.
* **Revert** to an earlier version if something breaks.
* Work on different features simultaneously using **branches**.

### 🌐 What is GitHub?

GitHub is a cloud platform for hosting Git repositories. It lets you:

* Store and back up code remotely.
* Share projects publicly or privately.
* Collaborate with others through pull requests and code reviews.
* Showcase your work as an online portfolio.

## 🚀 Installation Steps

### Step 0: Install Git

If Git is not installed, follow these instructions:

* **macOS (Homebrew):**

  
bash
  brew install git

* **Windows:**

  1. Download Git for Windows: [https://git-scm.com/download/win](https://git-scm.com/download/win)
  2. Run the installer and accept the defaults.
  3. Verify installation:

     
powershell
     git --version

* **Ubuntu/Linux:**

  
bash
  sudo apt update
  sudo apt install git

* **Optional:** Configure your Git identity:

  
bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"


* **Optional:** You can check what you’ve set:
  
bash
    git config user.name
    git config user.email


### Step 1: Install Python

If Python is not installed, follow these instructions:

* **macOS (Homebrew):**

  
bash
  brew install python

* **Windows:**

  1. Download Python: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
  2. Ensure **Add Python to PATH** is checked during installation.
* **Ubuntu/Linux:**

  
bash
  sudo apt update
  sudo apt install python3 python3-pip python3-venv


### Step 2: Clone the Repository

bash
git clone https://github.com/virgin-code/ML-DS-DL-AI.git
cd ML-DS-DL-AI


### Step 3: Create and Activate a Virtual Environment

Use venv to isolate project dependencies:

* **macOS / Ubuntu:**

  
bash
  python3 -m venv venv
  source venv/bin/activate

* **Windows:**

  
powershell
  python -m venv venv
  .\venv\Scripts\activate


### Step 4: Install Dependencies

bash
pip install -r requirements.txt


## 💻 Workflow for Students

Follow this Git workflow to submit your solutions:

| Actor   | Step                               | Git Commands                                                 |
| ------- | ---------------------------------- | ------------------------------------------------------------ |
| Student | Create a personal solution branch  | git checkout -b solutions/<username>                       |
| Student | Work locally and commit frequently | git add .<br>git commit -m "solve: exercise description" |
| Student | Pull latest changes                | git pull origin <branch>                                   |
| Student | Push your solutions                | git push -u origin solutions/<username>                    |

> Replace <username> with your GitHub username and <branch> with your base branch (e.g., main).

## 🛠️ Useful Git Commands

* **Check configured Git user**

  * git config user.name — shows your Git user name.
  * git config user.email — shows your Git user email.

* **See current branch**

  * git branch — lists all branches; the current branch is highlighted.

* **List remote repositories**

  * git remote -v — shows fetch/push URLs for each remote.

* **Fetch updates from remote**

  * git fetch — downloads commits and branches without merging.

* **Pull latest changes (merge)**

  * git pull origin <branch> — fetches and merges a remote branch.

* **Pull with rebase**

  * git pull --rebase origin <branch> — fetches and rebases your commits on top of the remote branch, keeping history linear.

* **Switch to another branch**

  * git checkout <branch> — changes your working branch.

* **Push your branch**

  * git push origin <branch> — uploads your local branch to the remote.

## ℹ️ Difference Between System Python and venv

* **System Python**

  * Installed globally.
  * Requires admin privileges (sudo) for global pip installs.
  * Can lead to version conflicts between projects.

* **Virtual Environment (venv)**

  * Creates an isolated environment per project.
  * Dependencies live in the venv directory.
  * Avoids conflicts and allows different projects to use different package versions.
  * Enhances reproducibility and clean dependency management.

Happy coding! 🚀
