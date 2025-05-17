# ✅ Math & ML & DS & DL & AI

---

## 📦 Setup and Requirements

### 🛠️ What is Git?

Git is a **version‑control system** that records every change in your codebase. Think of it as a *save‑game* button:

* **Commit** your progress.
* **Revert** to any previous snapshot.
* Explore new ideas on **branches** without breaking the main line of development.

### 🌐 What is GitHub?

GitHub is a cloud platform that hosts Git repositories and adds collaboration tools:

* Store your code privately or publicly.
* Review changes through **pull requests**.
* Track issues, automate tests, and showcase your portfolio.

---

## 🚀 Getting Started

> **Students:** if you only have *read* permission on the upstream repo, start by **forking** it to your own account, then follow the steps below. If you have direct write access, you can clone the upstream repo directly and skip the *fork* step.

### 0️⃣ Install Git (if needed)

| OS                                      | Command / Steps                                                                                                                                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **macOS**                               | `brew install git`                                                                                                                                                                       |
| **Windows**                             | 1. Download **Git for Windows** [https://git-scm.com/download/win](https://git-scm.com/download/win)<br>2. Run the installer and accept the defaults.<br>3. Verify with `git --version`. |
| **Ubuntu / Debian**                     | \`\`\`bash                                                                                                                                                                               |
| sudo apt update && sudo apt install git |                                                                                                                                                                                          |

````|

Add your identity (once):

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
````

---

### 1️⃣ Install Python (≥ 3.9)

| OS                                                                   | Command / Steps                                                                                                                                           |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **macOS**                                                            | `brew install python`                                                                                                                                     |
| **Windows**                                                          | 1. Download from [https://python.org/downloads/windows/](https://python.org/downloads/windows/)<br>2. **Check “Add Python to PATH”** during installation. |
| **Ubuntu / Debian**                                                  | \`\`\`bash                                                                                                                                                |
| sudo apt update && sudo apt install python3 python3-pip python3-venv |                                                                                                                                                           |

````|

---

### 2️⃣ Clone **your fork** (or the upstream repo)

```bash
# If you forked:
 git clone https://github.com/<your‑username>/ML-DS-DL-AI.git

# If you have write access and did NOT fork:
# git clone https://github.com/virgin-code/ML-DS-DL-AI.git
cd ML-DS-DL-AI
````

Add the instructor’s repo as **upstream** so you can pull future updates:

```bash
git remote add upstream https://github.com/virgin-code/ML-DS-DL-AI.git
git remote -v          # origin = your fork, upstream = instructor
```

---

### 3️⃣ Create & activate a virtual environment (recommended)

| OS                       | Command    |
| ------------------------ | ---------- |
| **macOS / Linux**        | \`\`\`bash |
| python3 -m venv venv     |            |
| source venv/bin/activate |            |

````|
| **Windows (PowerShell)** | ```powershell
python -m venv venv
.\venv\Scripts\activate
``` |

---

### 4️⃣ Install project dependencies

```bash
pip install -r requirements.txt
````

---

## 💻 Student Workflow

| Step                                                     | Command    | Purpose |
| -------------------------------------------------------- | ---------- | ------- |
| **1. Sync your fork**                                    | \`\`\`bash |         |
| git fetch upstream                                       |            |         |
| git checkout main                                        |            |         |
| git merge upstream/main   # or: git rebase upstream/main |            |         |
| git push origin main                                     |            |         |

````| Bring instructor updates into your fork. |
| **2. Create your homework branch** | `git checkout -b solutions/<github‑username>/<assignment>` | Keep your work separate and organized. |
| **3. Work & commit frequently** | ```bash
git add <files>
git commit -m "feat: solve HW‑1"
``` | Save logical checkpoints. |
| **4. Push your branch** | `git push -u origin solutions/<username>/<assignment>` | Upload work to GitHub. |
| **5. Open a Pull Request** | (GitHub UI) | Submit for review & feedback. |
| **6. Update branch after instructor changes** | ```bash
git fetch upstream
git rebase upstream/main   # or merge
# Resolve conflicts if prompted
git push --force-with-lease
``` | Keep branch current and conflict‑free. |

> ⭐ **Tip:** Use `rebase` for a clean history, `merge` if you prefer the default behaviour. If you rebase, remember to force‑push with `--force-with-lease`.

---

## 🛠️ Handy Git Commands

| Purpose | Command |
|---------|---------|
| Show your Git identity | `git config user.name && git config user.email` |
| List branches (local) | `git branch` |
| List remotes | `git remote -v` |
| Fetch without merge | `git fetch [remote]` |
| Pull & merge | `git pull [remote] [branch]` |
| Pull & rebase | `git pull --rebase [remote] [branch]` |
| Switch branch | `git checkout <branch>` |
| Push branch | `git push [remote] <branch>` |

---

## ℹ️ System Python vs `venv`

| | **System Python** | **Virtual Environment (`venv`)** |
|---|---|---|
| Scope | Global, shared by all projects | Isolated per project |
| Admin rights needed? | Often yes (`sudo`) | No |
| Dependency clashes | Likely | Impossible across projects |
| Reproducibility | Harder | Easier (pin versions in `requirements.txt`) |

Use a fresh `venv` for every new project and enjoy conflict‑free development 🎉.

---

Happy coding! 🚀

````
