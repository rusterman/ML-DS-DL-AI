# ✅ Math & ML & DS & DL & AI

---

## 📦 Setup and Requirements

### Step 1: Install Python

If Python is not already installed, follow these simple instructions:

- **macOS**:

Install via [Homebrew](https://brew.sh/):

```bash
brew install python
```

- **Windows**:

Download and install Python from [python.org](https://www.python.org/downloads/windows/). Ensure "Add Python to PATH" is checked during installation.

- **Ubuntu/Linux**:

Open Terminal and run:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/rusterman/ML-DS-DL-AI.git
cd ML-DS-DL-AI
```

### Step 3: Create and Activate Virtual Environment

Create a virtual environment to avoid dependency conflicts:

- **macOS/Ubuntu:**

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies

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