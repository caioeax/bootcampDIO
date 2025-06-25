sorteio = {1, 23}

sorteio # {1,23}
sorteio.clear()
sorteio # {}​

sorteio.add(25) # {1, 23, 25}​
sorteio.add(42) # {1, 23, 25, 42}​
sorteio.add(25) # {1, 23, 25, 42}​

sorteio # {1, 23}​
sorteio.copy()
sorteio # {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}
 
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 0
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}

