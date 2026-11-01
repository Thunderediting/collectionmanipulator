# Student Data Organizer

A simple command-line Python program for managing student information during one run of the program.

## Requirements

- Python 3
- No third-party packages

## Run

From the project directory, run:

```bash
python collectionmanipulator.py
```

## Menu Options

1. **Add students**: Enter a student ID, name, age, grade, subjects, and date of birth.
2. **Display all students**: Intended to display student information.
3. **Update student information**: Find a student by ID and update their name, age, grade, subjects, or date of birth.
4. **Delete student**: Remove a student by ID.
5. **Display subjects offered**: List Maths, Science, English, and Computer Science.
6. **Exit**: Close the program.

## Data and Limitations

Student records are kept in memory, so they are lost when the program exits. The display option currently prints only a student's name and may fail if no student has been added yet; it does not display all saved records as its menu label suggests.
