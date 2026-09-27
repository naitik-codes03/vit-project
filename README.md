# VIT Bhopal Semester GPA Predictor Tool

A simple Python console program that predicts a student's 1st semester GPA
at VIT Bhopal using the relative grading system followed by the university.

## Why I made this

VIT follows relative grading, so your grade doesn't just depend on your own
marks — it depends on the class highest and class average too. Most students
don't have an easy way to check "if I score X, what grade will I probably
get?" before the actual result comes out. This tool takes your marks, the
class highest, and the class average for each subject, and gives you an
estimated grade and GPA based on that.

## How it works

1. For every subject, you enter:
   - Your marks
   - The highest marks in the class
   - The average marks of the class
2. The program estimates the class standard deviation using the formula:
   `SD = (Highest - Average) / 2`
   (This is an approximation since we don't have the full marks list, just
   highest and average.)
3. Using this estimated SD, it calculates the grade cutoffs (S, A, B, C, D, E)
   relative to the class average, the same way VIT's relative grading works.
4. Your marks are compared against these cutoffs to decide your grade and
   grade point.
5. Once all subjects are entered, the program multiplies each subject's
   grade point by its credit, adds them all up, and divides by the total
   credits to give the final predicted GPA.

## Subjects covered (1st Semester)

| Subject  | Credits |
|----------|---------|
| Math     | 4       |
| Python   | 4       |
| EBS      | 2       |
| English  | 2       |

(Total: 12 credits — change the `subjects` dictionary in the code if your
credit structure is different.)

## How to run

```bash
python gpa_predictor.py
```

You'll be prompted to enter your marks, class highest, and class average
one subject at a time. At the end, it prints a report card with your
predicted grade in every subject and your overall predicted GPA.

## Sample output

```
--- Enter details for Math (4 Credits) ---
Your Marks: 85
Class Highest Marks: 95
Class Average Marks: 70

...

=============================================
              FINAL REPORT CARD              
=============================================
Math       | Grade: A
Python     | Grade: S
EBS        | Grade: B
English    | Grade: A
---------------------------------------------
Your Predicted Semester GPA is: 8.83
=============================================
```

## Limitations

- This is only a **prediction**, not the actual result. The real class SD
  could be different from the estimated one since we're only using highest
  and average as inputs.
- If marks, highest, or average are entered wrong (typos, values over 100),
  the program shows a warning but doesn't fully validate every case — this
  can be improved further.
- Built for 1st semester subjects specifically; the subjects/credits need
  to be edited manually for other semesters.

## Possible improvements

- Take the full class marks list instead of just highest/average, for a
  more accurate SD.
- Add input validation so it rejects negative marks or marks above 100
  instead of just printing a warning.
- Store past semester results to calculate CGPA, not just one semester's GPA.

## Author

1st Semester student, VIT Bhopal — made as a Python course project.
