import numpy as np

class VectorIndex:
    def __init__(self):
        self.vectors = None
        self.texts = []
        self.dimension = None

    def add(self, vectors, texts):
        vectors = np.array(vectors, dtype=float)
        texts = list(texts)

        if vectors.ndim != 2:
            raise ValueError("Vectors must be 2D array.")
        if vectors.shape[0] != len(texts):
            raise ValueError("Number of vectors and number of texts must be equal.")

        dimension = vectors.shape[1]

        if self.dimension is not None and self.dimension != dimension:
            raise ValueError("Vector dimensions must match.")

        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        if np.any(norms == 0):
            raise ValueError("Zero vectors cannot be normalized.")

        vectors = vectors / norms
        
        if self.dimension is None:
                    self.dimension = dimension
            
        if self.vectors is None:
            self.vectors = vectors
        else:
            self.vectors = np.vstack((self.vectors, vectors))

        self.texts.extend(texts)

        
        