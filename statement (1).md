# VIT Bhopal 1st Semester CGPA Predictor Tool

**Course:** Python Programming (Course Project)
**Author:** Naitik Mishra
**University:** VIT Bhopal, 1st Semester
**Language:** Python 3 (no external libraries)
**File:** `python bigneer.py`

---

## 1. Problem Statement

At VIT, grades are given on a **relative grading** basis. A student's grade depends on how their marks compare with the rest of the class, not on fixed cut-off marks. Because the university does not publish the full class data, students cannot know their exact grade or GPA before the results are released.

This project builds a **command-line tool** that lets a first-semester student **predict** their semester GPA using only three numbers per subject, which are usually easy to find out:

1. The student's own marks
2. The class highest marks
3. The class average marks

---

## 2. Objectives

- Predict the grade (S, A, B, C, D, E, F) for each subject.
- Convert each grade into VIT grade points.
- Calculate the **credit-weighted semester GPA**. For a 1st-semester student, this is also the CGPA.
- Show a clear final report card on the screen.

---

## 3. Input

For each of the four subjects, the user enters:

| Input | Type | Description |
|---|---|---|
| Your Marks | float | Marks obtained by the student |
| Class Highest Marks | float | Highest marks in the class |
| Class Average Marks | float | Average marks of the class |

### Subjects and Credits

| Subject | Credits |
|---|---|
| Math | 4 |
| Python | 4 |
| EVS | 2 |
| English | 2 |
| **Total** | **12** |

---

## 4. Output

- The grade for every subject
- The predicted semester GPA, rounded to 2 decimal places

---

## 5. Method / Logic

### 5.1 Estimating the Standard Deviation (SD)

The real SD of the class is not available because we do not have every student's marks. So the program **estimates** it from the highest and average marks:

```
estimated_SD = (Highest − Average) / 2
```

If `estimated_SD ≤ 0`, it is set to `1.0`. This avoids problems when the highest and average are equal or wrongly entered.

### 5.2 Grade Boundaries

The boundaries are set around the class average:

| Limit | Formula |
|---|---|
| S limit | Average + 1.5 × SD |
| A limit | Average + 1.0 × SD |
| B limit | Average + 0.5 × SD |
| C limit | Average |
| D limit | Average − 0.5 × SD |
| E limit | Average − 1.0 × SD |

### 5.3 Grade and Grade Points

| Grade | Condition | Grade Points |
|---|---|---|
| S | Marks ≥ S limit | 10 |
| A | Marks ≥ A limit | 9 |
| B | Marks ≥ B limit | 8 |
| C | Marks ≥ C limit | 7 |
| D | Marks ≥ D limit | 6 |
| E | Marks ≥ E limit (and ≥ 40) | 5 |
| F | Marks < 40 **or** Marks < E limit | 0 |

### 5.4 GPA Formula

```
GPA = Σ (Grade Points × Credits) / Σ Credits
```

Here, total credits = 12.

---

## 6. Program Structure

| Function | Purpose |
|---|---|
| `get_grade_and_points(my_marks, highest_marks, avg_marks)` | Estimates the SD, finds the grade boundaries and returns the grade and grade points |
| `main()` | Takes input for all subjects, calls the function above, calculates the GPA and prints the report card |

**Data structures used:** dictionary (subjects with credits, predicted grades), variables and loops.

---

## 7. Sample Run

**Input**

| Subject | Your Marks | Highest | Average |
|---|---|---|---|
| Math | 82 | 95 | 65 |
| Python | 92 | 98 | 70 |
| EVS | 70 | 90 | 68 |
| English | 75 | 88 | 70 |

**Calculation**

| Subject | Estimated SD | Grade | Points | Credits | Points × Credits |
|---|---|---|---|---|---|
| Math | 15 | A | 9 | 4 | 36 |
| Python | 14 | S | 10 | 4 | 40 |
| EVS | 11 | C | 7 | 2 | 14 |
| English | 9 | B | 8 | 2 | 16 |
| **Total** | | | | **12** | **106** |

**Output**

```
=============================================
              FINAL REPORT CARD
=============================================
Math       | Grade: A
Python     | Grade: S
EVS        | Grade: C
English    | Grade: B
---------------------------------------------
Your Predicted Semester GPA is: 8.83
=============================================
```

GPA = 106 / 12 = **8.83**

---

## 8. Limitations

- The SD is only an **estimate**, so the predicted grade may differ from the real grade given by the university.
- The subjects and credits are fixed for the 1st semester and are written inside the code.
- Marks above 100 only show a warning, and the program continues with the same values.
- There is no check for non-numeric or negative input. Entering text will stop the program with an error.

---

## 9. Future Scope

- Take subjects and credits from the user, so other semesters can be used.
- Add full input validation, such as asking again on wrong input.
- Calculate the overall CGPA across several semesters.
- Build a GUI or a web version.

---

## 10. Setup and Run Instructions

These steps assume you know nothing about the project. Follow them in order. The whole setup takes about 5 minutes.

### 10.1 What You Need

| Requirement | Details |
|---|---|
| Operating system | Windows 10/11, macOS or Linux |
| Python | Version **3.6 or higher** (3.8+ recommended) |
| Extra libraries | **None.** The project uses only Python's built-in features |
| Internet | Only needed once, to download Python (if not installed) |
| Tools | A terminal (Command Prompt / PowerShell on Windows, Terminal on macOS/Linux) |

### 10.2 Get the Project Files

The whole project is one file: `python bigneer.py`. Put it in a folder you can find easily, for example `cgpa_predictor`.

- **From a zip or submission folder:** extract it and note the folder path.
- **From GitHub (if hosted there):**
  ```bash
  git clone <repository-url>
  cd <repository-folder>
  ```

### 10.3 Environment Setup

**Step 1: Check whether Python is installed.** Open a terminal and run:

```bash
python --version
```

On macOS/Linux, if this gives an error, try:

```bash
python3 --version
```

You should see something like `Python 3.11.4`. If the version is 3.6 or higher, go to Step 3.

**Step 2: Install Python (only if Step 1 failed).**

- **Windows:** Download the installer from <https://www.python.org/downloads/>. Run it and **tick "Add Python to PATH"** on the first screen, then click *Install Now*.
- **macOS:** Download the installer from <https://www.python.org/downloads/> or run `brew install python`.
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install python3`

Close the terminal, open a new one and repeat Step 1 to confirm.

**Step 3 (optional): Create a virtual environment.** This keeps the project separate from other Python projects. Inside the project folder run:

```bash
python -m venv venv
```

Activate it:

- Windows (Command Prompt): `venv\Scripts\activate`
- Windows (PowerShell): `venv\Scripts\Activate.ps1`
- macOS/Linux: `source venv/bin/activate`

You will see `(venv)` at the start of the terminal line. To leave it later, type `deactivate`. This step can be skipped, because the project has no dependencies.

### 10.4 Dependency Installation

**No installation is needed.** The code does not import any module, and there is no `requirements.txt`. It uses only built-in Python features (`input`, `print`, `float`, `dict`, `round`). You do **not** need to run `pip install`.

### 10.5 Configuration

There are no configuration files, environment variables, API keys or command-line arguments.

The only setting is the subject list with credits, stored in the `subjects` dictionary inside `main()`:

```python
subjects = {
    "Math": 4,
    "Python": 4,
    "EVS": 2,
    "English": 2
}
```

To use different subjects, edit the names and credit values in this dictionary and save the file. The total credits and the GPA formula update automatically. **For the standard 1st-semester run, change nothing.**

### 10.6 Run the Program

1. Open a terminal and go to the project folder:
   ```bash
   cd path/to/cgpa_predictor
   ```
2. Run the program. The file name has a **space**, so it must be in quotes:
   ```bash
   python "python bigneer.py"
   ```
   On macOS/Linux, use `python3` if `python` does not work:
   ```bash
   python3 "python bigneer.py"
   ```
3. The program asks three questions for each subject: your marks, the class highest marks and the class average marks. Type a number and press **Enter** after each one.
4. After the last subject, the final report card and the predicted GPA are shown.

**Tip:** To avoid quotes, rename the file to `cgpa_predictor.py` and run `python cgpa_predictor.py`.

### 10.7 Try It with the Sample Data

To check that everything works, enter these 12 values in this order (Math, then Python, then EVS, then English):

```
82  95  65
92  98  70
70  90  68
75  88  70
```

Each row is Your Marks, Class Highest and Class Average, entered one value per line. Example of the first subject:

```
--- Enter details for Math (4 Credits) ---
Your Marks: 82
Class Highest Marks: 95
Class Average Marks: 65
```

If the setup is correct, the last line of the output will be:

```
Your Predicted Semester GPA is: 8.83
```

### 10.8 Troubleshooting

| Problem | Cause | Solution |
|---|---|---|
| `'python' is not recognized` (Windows) | Python is not installed or not in PATH | Reinstall Python and tick "Add Python to PATH", or try `py "python bigneer.py"` |
| `command not found: python` (macOS/Linux) | The command is named `python3` | Use `python3 "python bigneer.py"` |
| `can't open file ... No such file or directory` | You are in the wrong folder, or the quotes are missing | Use `cd` to go to the folder with the file, and put the file name in quotes |
| `ValueError: could not convert string to float` | You typed text or left the input empty | Run again and enter numbers only (decimals like `72.5` are allowed) |
| `Warning: Marks cannot be greater than 100` | A value above 100 was entered | This is only a warning, but check your input |
| `SyntaxError` on an f-string line | Python version is older than 3.6 | Install Python 3.6 or higher |

---

## 11. Conclusion

This tool helps a student estimate their semester GPA before results using simple statistics and the VIT relative grading idea. It also practises the core Python concepts learned in the course: functions, dictionaries, loops, user input, conditions and formatted output.
