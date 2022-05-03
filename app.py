def completar(a):
    mes=a[0].split(" ")[0]
    year=a[0].split(" ")[2]
    minimo_dia=int(a[0].split(" ")[1].split(',')[0])
    maximo_dia=int(a[-1].split(" ")[1].split(',')[0])
    salida=[]
    for i in range(minimo_dia,maximo_dia+1):
         salida.append(mes+" "+str(i)+", "+year)
    print (salida)

completar(['Oct 2, 1969', 'Oct 5, 1969', 'Oct 7, 1969', 'Oct 9, 1969'])


# se realizo ejercicio que completa fechas para un mismo mes de un determinado año