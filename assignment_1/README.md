# Assignment 1

This Python script determines the optimal threshold for binary classification based on recall. It handles confusion matrix data either by generating samples or reading from a CSV.

## Requirements

* Python 3.x
* Standard libraries: `random`, `sys`, `logging`, `csv`, `dataclasses`

## Usage

To run with a randomly generated dataset:

```bash
python assignment_1.py
```

To analyze thresholds from a CSV file:

```bash
python assignment_1.py <filename.csv>
```

The file must have the following columns:

```csv
threshold,tp,tn,fp,fn
0.1,481,47,422,50
0.2,390,104,409,97
0.3,343,151,362,144
```

Example:

```bash
python assignment_1.py data.csv
```

## Testing

Run unit tests with:

```bash
pytest test_assignment_1.py
```

## File Overview

* `assignment_1.py` - Main script for threshold analysis
* `test_assignment_1.py` - Unit tests using pytest

## Code Overview

* `ConfusionMatrix Class`: Data structure to represent the metrics of the confusion matrix: threshold, tp, tn, fp, fn. Includes the `recall()` function to compute recall.

* `generate_sample_data()` Function: Generate sample data for the specified thresholds.

* `read_data_csv()` Function: Read confusion matrix data from a CSV file.

* `parse_data()` Function: Convert data tuples into a list of ConfusionMatrix.

* `select_max_recall_matrix()`: Select the best threshold based on the recall. If multiple threshold are maximal, the function returns the first one encountered.

* `analyze_threshold_data()`: Analyzes the threshold data to find the best recall threshold over the specified minimum.

* `main()` Function: Accepts an optional CSV filename via command-line argument. If no file is provided generates random data. Outputs the best threshold and recall if condition met, otherwise logs a message indicating no threshold found.
