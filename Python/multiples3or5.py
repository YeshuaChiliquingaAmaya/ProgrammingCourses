def solution(number):
    """
    Returns the sum of all multiples of 3 or 5 below the given number.
    If the number is negative, returns 0.
    
    Args:
        number: An integer
        
    Returns:
        The sum of all multiples of 3 or 5 below the number
    
    Example:
        >>> solution(10)
        23
    """
    # Tu código aquí

    number = int(number)
    # Verifica si el número es un entero
    if not isinstance(number, int):
        raise ValueError("El número debe ser un entero")
    
    # Verifica si el número es menor que 0
    if number < 0:
        return 0
    
    # Variable para llevar la suma
    total = 0
    
    # Iteración desde 1 hasta number - 1    
    for i in range(1, number):
        # Verifica si i es múltiplo de 3 o 5
        if i % 3 == 0 or i % 5 == 0:
            total += i
    
    # Iteración desde 1 hasta number - 1
    # Añade tu código aquí para verificar múltiplos de 3 o 5 y sumarlos
    
    return total

# Pruebas
print("Ejemplo con 20:", solution(10))  # Debería imprimir: Ejemplo con 10: 22