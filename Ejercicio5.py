def anio_bisiesto():
  anio: int = int(input("Introduce un año "))

  if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
      print(f"El año {anio} es bisiesto")
  else:
      print(f"Lo sentimos. El año {anio} NO es bisiesto")

anio_bisiesto()