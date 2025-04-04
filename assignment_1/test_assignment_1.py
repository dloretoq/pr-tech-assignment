import pytest

from assignment_1 import (
    ConfusionMatrix,
    select_max_recall_matrix,
    analyze_threshold_data,
)


def test_confusion_matrix_recall():
    matrix = ConfusionMatrix(0.5, 20, 20, 5, 5)

    assert matrix.recall() == pytest.approx(matrix.tp / (matrix.tp + matrix.fn))


def test_confusion_matrix_recall_zero_denominator():
    matrix_zero_denominator = ConfusionMatrix(0.5, 0, 20, 5, 0)

    assert matrix_zero_denominator.recall() == 0.0


def test_select_max_recall_matrix():
    matrices = [
        ConfusionMatrix(0.1, 20, 10, 10, 10),  # recall = 0.66
        ConfusionMatrix(0.5, 25, 10, 10, 5),  # recall = 0.83
        ConfusionMatrix(0.8, 27, 10, 10, 3)  # max recall = 0.9
    ]

    max_recall_matrix = select_max_recall_matrix(matrices)

    assert max_recall_matrix.recall() == pytest.approx(0.9)
    assert max_recall_matrix.threshold == 0.8


def test_select_max_recall_first_matrix():
    matrices = [
        ConfusionMatrix(0.1, 20, 10, 10, 10),  # recall = 0.66
        ConfusionMatrix(0.5, 25, 10, 10, 5),  # recall = 0.83
        ConfusionMatrix(0.7, 27, 10, 10, 3),  # max recall = 0.9
        ConfusionMatrix(0.8, 27, 10, 10, 3)  # max recall = 0.9
    ]

    max_recall_matrix = select_max_recall_matrix(matrices)

    assert max_recall_matrix.recall() == pytest.approx(0.9)
    assert max_recall_matrix.threshold == 0.7


def test_analyze_threshold_data_valid():
    matrices = [
        ConfusionMatrix(0.1, 20, 10, 10, 10),  # recall = 0.66
        ConfusionMatrix(0.5, 25, 10, 10, 5),  # recall = 0.83
        ConfusionMatrix(0.8, 27, 10, 10, 3)  # recall = 0.9
    ]
    best_matrix = analyze_threshold_data(matrices, 0.9)

    assert best_matrix.recall() == pytest.approx(0.9)
    assert best_matrix.threshold == 0.8


def test_analyze_threshold_data_invalid():
    matrices = [
        ConfusionMatrix(0.1, 20, 10, 10, 10),  # recall = 0.66
        ConfusionMatrix(0.5, 25, 10, 10, 5),  # recall = 0.83
    ]

    best_matrix = analyze_threshold_data(matrices, 0.9)

    assert best_matrix is None
