import numpy as np
from vector_index import VectorIndex

def assert_raises_value_error(function):
    try:
        function()
    except ValueError:
        return
    raise AssertionError("Expected ValueError, but none was raised")


# Test 1: Ranking order
index = VectorIndex()

index.add(
    [[1, 0], [0, 1], [1, 1]],
    ["right", "up", "diagonal"]
)

results = index.search([1, 0], k=3)

assert [text for text, score in results] == [   #norms are 1, 0.7 and 0
    "right", "diagonal", "up"
]


# Test 2: Similarity scores
assert np.isclose(results[0][1], 1.0)                   
assert np.isclose(results[1][1], 0.7071 )
assert np.isclose(results[2][1], 0.0)


# Test 3: Vector length shouldn't matter
index_length = VectorIndex()

index_length.add(
    [[1, 0], [10, 0]],
    ["right", "long_right"]
)

results_length = index_length.search([1, 0], k=2)

assert np.isclose(results_length[0][1], results_length[1][1])
assert np.isclose(results_length[0][1], 1.0)


# Test 4: Query length should't matter
results_a = index.search([1, 0], k=3)
results_b = index.search([5, 0], k=3)

assert np.allclose(
    [score for text, score in results_a],
    [score for text, score in results_b]
)

assert [text for text, score in results_a] == [
    text for text, score in results_b
]


# Test 5: Two separate add() calls, Each returned text must belong to the vector that scored it
index = VectorIndex()

index.add(
    [[1, 0]],
    ["right_batch"]
)

index.add(
    [[0, 1]],
    ["up_batch"]
)

results_right = index.search([1, 0], k=2)
results_up = index.search([0, 1], k=2)

assert results_right[0][0] == "right_batch"
assert results_up[0][0] == "up_batch"


# Test 6: Size matching, no. of vectors = no. of texts
assert len(index.texts) == index.vectors.shape[0]


# Test 7: k larger than the index
index = VectorIndex()

index.add(
    [[1, 0], [0, 1], [1, 1]],
    ["right", "up", "diagonal"]
)

assert len(index.search([1, 0], 10)) == 3


# Test 8: k=1
assert len(index.search([1, 0], 1)) == 1


# Test 9: Invalid k
for invalid_k in [0, -1, 2.5, True]:
    assert_raises_value_error(lambda: index.search([1, 0], invalid_k))


# Test 10: Empty index
index = VectorIndex()
assert index.search([1, 0], 3) == []


# Test 11: Query with the wrong dimension
index = VectorIndex()

index.add(
    [[1, 0], [0, 1]],
    ["right", "up"]
)

assert_raises_value_error(lambda: index.search([1, 0, 1], k=1))


# Test 12: Zero vector as the query
assert_raises_value_error(lambda: index.search([0, 0], k=1))


# 13. Zero vector in add
index = VectorIndex()

assert_raises_value_error(lambda: index.add([[0, 0]], ["zero"]))


# Test 14: Number of vectors differs from number of texts
assert_raises_value_error(lambda: index.add([[1, 0], [0, 1]],["right"]))


# 15. 1D array passed to add
assert_raises_value_error(lambda: index.add([1, 0], ["right"]))


# 16. Mismatched dimensions
index.add(
    [[1, 0], [0, 1]],
    ["right", "up"]
)

assert_raises_value_error(lambda: index.add([[1, 0, 0]],["forward"]))
