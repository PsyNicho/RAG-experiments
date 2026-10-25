import numpy as np

class VectorIndex:
    def __init__(self):     #initialize
        self.vectors = None
        self.texts = []
        self.dimension = None

    #add method
    def add(self, vectors, texts):
        vectors = np.array(vectors, dtype=float)        #input to array/list
        texts = list(texts)

        if len(texts) == 0 and len(vectors) == 0:       #no operation
            return

        if vectors.ndim != 2:       
            raise ValueError("Vectors must be 2D array.")
        if vectors.shape[0] != len(texts):
            raise ValueError("Number of vectors and number of texts must be equal.")

        dimension = vectors.shape[1]    #numbers of column in array

        if self.dimension is not None and self.dimension != dimension:  
            raise ValueError("Vector dimensions must match.")

        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        if np.any(norms == 0):
            raise ValueError("Zero vectors cannot be normalized.")

        vectors = vectors / norms
        
        if self.dimension is None:              #set for 1st batch
                    self.dimension = dimension
            
        if self.vectors is None:                #check if its the first batch 
            self.vectors = vectors
        else:
            self.vectors = np.vstack((self.vectors, vectors))   #if its not add to current list of vectors

        self.texts.extend(texts)    #add new text to text list

    #search method
    def search(self, query_vector, k):
        if self.vectors is None:                        
            return []      
            
        if isinstance(k, bool) or not isinstance(k, int) or k <= 0:     #validate k
            raise ValueError("k must be a positive integer.")

        query_vector = np.array(query_vector, dtype=float)      #vector to array of floating point

        if query_vector.ndim != 1:
            raise ValueError("Query vector's dimension must be 1.")
            
        if query_vector.shape[0] != self.dimension:
            raise ValueError("Query vector dimension must match the index")


        Qnorm = np.linalg.norm(query_vector)
        if Qnorm == 0:
            raise ValueError("Zero vectors cannot be normalized.")

        query_vector = query_vector / Qnorm

        scores = self.vectors @ query_vector

        indices = np.argsort(-scores, kind="stable")[:k]    #preserves relative order

        results = []
        for i in indices:
            results.append((self.texts[i], float(scores[i])))
        return results