def completar(a):
    b=[]
    for i in a:
        b.append(int((i.split(" ")[1].split(',')[0])))
    mes=a[0].split(" ")[0]
    year=a[0].split(" ")[2]
    print(mes)
    print(year)
    minimo=b[0]
    maximo=b[-1]
    salida=[]
    for i in range(minimo,maximo+1):
         salida.append(mes+" "+str(i)+", "+year)
    print (salida)

completar(['Oct 2, 1969', 'Oct 5, 1969', 'Oct 7, 1969', 'Oct 9, 1969'])


# se realizo ejercicio que completa fechas para un mismo mes de un determinado año