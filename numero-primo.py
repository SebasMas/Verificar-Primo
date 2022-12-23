def es_primo(numero):
  if numero<2:
    return False
  for i in range(2, numero):
     if  (numero % i)== 0:
        return False
  # Hemos agotado el bucle sin encontrar divisores
  return True
  
n = int(input("Introduzca un número entero: "))
print(es_primo(n))