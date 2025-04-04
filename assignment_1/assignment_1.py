import random
import sys
import logging
import csv

from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)


@dataclass
class ConfusionMatrix:
    threshold: float
    tp: int
    tn: int
    fp: int
    fn: int

    def recall(self) -> float:
        """Calculate the recall"""
        demominator = self.tp + self.fn

        if demominator == 0:
            return 0.0

        return self.tp / (self.tp + self.fn)


def generate_sample_data(n_sample: int, thresholds: list) -> list:
    """Generate sample data for the specified thresholds."""

    logging.info(f'Generating sample data')

    data = []
    targets = [random.randint(0, 1) for _ in range(n_sample)]
    predict_proba = [random.random() for _ in range(n_sample)]

    for threshold in thresholds:
        predictions = [int(proba >= threshold) for proba in predict_proba]
        tp = tn = fp = fn = 0

        for target, prediction in zip(targets, predictions):
            if target == 1 and prediction == 1:
                tp += 1
            elif target == 0 and prediction == 0:
                tn += 1
            elif target == 0 and prediction == 1:
                fp += 1
            elif target == 1 and prediction == 0:
                fn += 1

        data.append((threshold, tp, tn, fp, fn))

    return data


def read_data_csv(filename) -> list:
    """Read confusion matrix data from a CSV file."""

    logging.info(f'Reading data from {filename}')

    data = []

    try:
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append((float(row['threshold']), int(row['tp']), int(
                    row['tn']), int(row['fp']), int(row['fn'])))
    except Exception:
        logging.exception(f"Error reading CSV file: {filename}")
        sys.exit(1)

    return data


def parse_data(data: list) -> list:
    """Convert data tuples into a list of ConfusionMatrix."""
    logging.info(f'Converting data into confusion matrices')

    return [ConfusionMatrix(threshold, tp, tn, fp, fn) for (threshold, tp, tn, fp, fn) in data]


def select_max_recall_matrix(confusion_matrices: list) -> ConfusionMatrix:
    """Select the best threshold based on the recall. If multiple threshold are maximal, the function returns the first one encountered."""
    return max(confusion_matrices, key=lambda x: x.recall())


def analyze_threshold_data(confusion_matrices: list, min_recall: float) -> ConfusionMatrix:
    """Analyzes the threshold data to find the best recall threshold over the specified minimum."""
    best_matrix = select_max_recall_matrix(confusion_matrices)

    if best_matrix.recall() < min_recall:
        return None

    return best_matrix


def main():
    min_recall = 0.9

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        data = read_data_csv(filename)
    else:
        thresholds = [round(0.1 * i, 1) for i in range(1, 10)]
        data = generate_sample_data(1000, thresholds)

    confusion_matrices = parse_data(data)
    best_matrix = analyze_threshold_data(confusion_matrices, min_recall)

    if best_matrix:
        logging.info(
            f'Best threshold: {best_matrix}, Recall: {best_matrix.recall()}')
    else:
        logging.info(
            f'No threshold found with recall greater than {min_recall}')


if __name__ == '__main__':
    main()
