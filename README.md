# Cricket Team Performance Analysis Using Pandas & NumPy (Python)

## Project Description

The Cricket Team Performance Analysis project is a Python application that uses Pandas and NumPy to analyze cricket players' performance data. The program performs structured DataFrame operations to calculate team statistics, handle missing values, compute strike rates, and identify top-performing players.

This project demonstrates practical sports data analysis using Pandas and NumPy and is suitable for beginners learning group-based aggregation, data cleaning, and performance evaluation in Python.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store team and player performance data using a Pandas DataFrame
* Count unique teams
* Calculate number of players per team
* Compute total runs per team
* Perform multiple statistical aggregations (sum, mean, max, min)
* Detect and handle missing values
* Calculate team averages after cleaning data
* Compute strike rate for each player
* Identify player with highest strike rate

---

## Concepts Used

### Python Fundamentals

* Variables
* Dictionaries and lists
* Arithmetic operations
* Output formatting

### Pandas Concepts

* DataFrame creation
* Grouping using groupby()
* Aggregation using agg()
* Value counting using value_counts()
* Missing value detection using isnull()
* Filling missing data using fillna()
* Index-based row selection using idxmax()

### NumPy Concepts

* Handling missing values using np.nan
* Numerical calculations for performance metrics

### Programming Concepts

* Sports data analysis
* Group-based statistical computation
* Data cleaning and preprocessing
* Performance comparison using strike rate
* Team-wise evaluation

---

## Project Structure

```
cricket-team-performance-analysis/
│
├── team_analysis.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* Pandas library installed
* NumPy library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python team_analysis.py
```

---

## Operations Performed

```
1. Create team performance DataFrame
2. Count unique teams
3. Count players per team
4. Calculate total runs per team
5. Perform multiple aggregations (sum, mean, max, min)
6. Detect missing values
7. Fill missing runs with 0
8. Calculate team average after cleaning
9. Compute strike rate for each player
10. Identify player with highest strike rate
```

---

## Sample Output

```
Unique Teams: 2

Total Runs per Team:
Australia    210
India        240

Highest Strike Rate Player:
Player E
```

---

## Edge Cases Handled

* Missing run values handled using fillna()
* Accurate team-wise aggregation
* Safe strike rate calculation after cleaning data
* Correct identification of highest strike rate using idxmax()
* Reliable grouping without data duplication

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updated: 2026
