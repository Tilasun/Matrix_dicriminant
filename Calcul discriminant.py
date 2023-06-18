import numpy as np

def discriminant_calculation(matrix):
    n = matrix.shape[0]  # Retrieves matrix size
    
    if n != matrix.shape[1]:
        raise ValueError("The matrix must be square")  # Check if the matrix is square
    
    if n == 1:
        return matrix[0, 0]  # Basic case for a 1x1 matrix
    
    discriminant = 0
    
    for i in range(n):
        submatrix = np.delete(matrice, 0, axis=0)   # Deletes the first row of the matrix
        submatrix = np.delete(submatrix, i, axis=1)  # Deletes column i from the submatrix
        
        coefficient = matrice[0, i]  # Gets the coefficient of the first row and column i
        
        discriminant += (-1) ** i * coefficient * discriminant_calculation(submatrix)  #Recursive call
        
    return discriminant


matrix = np.array([[a,b], [c,d]]) #This line can be modified to suit your needs
discriminant = discriminant_calculation(matrix)
print("The discriminant of the matrix is :", discriminant)