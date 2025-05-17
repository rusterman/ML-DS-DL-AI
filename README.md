# ✅ Math & ML & DS & DL & AI

## 📦 Setup and Requirements

### 🛠️ What is Git?

Git is a **version‑control system** — a time machine for your code.  It lets you:

* **Commit** snapshots of your work.
* **Revert** to any earlier state.
* Experiment safely on **branches**.

### 🌐 What is GitHub?

GitHub hosts Git repositories in the cloud and adds collaboration tools:

* Private/public storage for your code.
* Pull‑requests and code review.
* Issue tracking, CI workflows, and an online portfolio.

---

## 🚀 Getting Started

> **If you have *read‑only* access:** first **fork** the repository to your GitHub account, then clone **your fork**.
> **If you have write access:** you can clone the instructor’s repo directly and skip the fork step.

### 0️⃣ Install Git

#### macOS

```bash
brew install git
```

#### Windows

1. Download **Git for Windows**: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer and accept the defaults.
3. Verify installation:

   ```powershell
   git --version
   ```

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

Configure your identity (one‑time):

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

---

### 1️⃣ Install Python (≥ 3.9)

#### macOS

```bash
brew install python
```

#### Windows

1. Download from [https://python.org/downloads/windows/](https://python.org/downloads/windows/)
2. **Check “Add Python to PATH”** during installation.

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

---

### 2️⃣ Clone the repository

```bash
# Clone your fork (recommended for students)
git clone https://github.com/<your-username>/ML-DS-DL-AI.git

# — or, if you have direct write access —
# git clone https://github.com/virgin-code/ML-DS-DL-AI.git

cd ML-DS-DL-AI
```

Add the instructor’s repo as **upstream** (one‑time):

```bash
git remote add upstream https://github.com/virgin-code/ML-DS-DL-AI.git
git remote -v   # origin = your fork, upstream = instructor
```

---

### 3️⃣ Create and activate a virtual environment

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

### 4️⃣ Install project dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Student Workflow

1. **Sync your fork with upstream**

   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main      # or: git rebase upstream/main
   git push origin main
   ```

2. **Create your homework branch**

   ```bash
   git checkout -b solutions/<github-username>/<assignment>
   ```

3. **Work & commit frequently**

   ```bash
   git add <files>
   git commit -m "feat: solve HW-1"
   ```

4. **Push your branch**

   ```bash
   git push -u origin solutions/<github-username>/<assignment>
   ```

5. **Open a Pull Request** (GitHub UI) — instructor will review and give feedback.

6. **Update your homework branch after instructor changes**

   ```bash
   git fetch upstream
   git rebase upstream/main     # or: git merge upstream/main
   # Resolve any conflicts…
   git push --force-with-lease
   ```

   > **Tip:** Use `rebase` for a clean history; if you do, remember to push with `--force-with-lease`.

---

## 🛠️ Handy Git Commands

* `git status` — show changed files and current branch.
* `git log --oneline --graph --all` — compact commit graph.
* `git branch -a` — list local **and** remote branches.
* `git remote -v` — show remotes and their URLs.
* `git fetch <remote>` — download commits without merging.
* `git pull [--rebase] <remote> <branch>` — fetch *and* integrate.
* `git checkout <branch>` — switch branches.
* `git push <remote> <branch>` — upload your branch.

---

## ℹ️ System Python vs `venv`

|                      | **System Python**               | **Virtual Environment (`venv`)** |
| -------------------- | ------------------------------- | -------------------------------- |
| Scope                | Global (shared by all projects) | Isolated per project             |
| Admin rights needed? | Often yes (`sudo`)              | No                               |
| Dependency clashes   | Likely                          | Impossible between projects      |
| Reproducibility      | Hard                            | Easy (pin versions)              |

> Always create a fresh `venv` for every new project to keep dependencies tidy. 🎉

---

Happy coding & learning! 🚀
