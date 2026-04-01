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

### Step 2: Clone the Repository

**If you're a student**, you'll need to fork this repository to get read access and sync with updates:

1. **Fork the Repository**: Click the "Fork" button on the [main repository](https://github.com/rusterman/ML-DS-DL-AI) to create your own copy.

2. **Clone Your Fork**:
```bash
git clone https://github.com/virgin-code/ML-DS-DL-AI.git 
cd ML-DS-DL-AI
```

Replace `<your-username>` with your actual GitHub username.

**Setup Upstream Remote** (Important for syncing updates):

This allows you to fetch the latest changes from the original repository:

```bash
git remote add upstream https://github.com/virgin-code/ML-DS-DL-AI.git
git remote -v  # Verify both origin and upstream are listed
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

## 🚀 Workflow for Students

Follow this simple Git workflow:

| Actor   | Step                             | Git Commands                              |
|---------|----------------------------------|-------------------------------------------|
| Student | Create a personal solution branch| `git checkout -b solutions/<username>`    |
| Student | Work locally, commit often       | `git add .`<br>`git commit -m "solve: exercise description"` |
| Student | Push solutions                   | `git push -u origin solutions/<username>` |

Replace `<username>` with your actual GitHub username.

---