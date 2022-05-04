from datetime import timedelta, date

def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

def meses(mes):
    if mes=='Jan':
        return 1
    elif mes=='Feb':
        return 2
    elif mes=='Mar':
        return 3
    elif mes=='Apr':
        return 4
    elif mes=='May':
        return 5
    elif mes=='Jun':
        return 6
    elif mes=='Jul':
        return 7
    elif mes=='Aug':
        return 8
    elif mes=='Sep':
        return 9
    elif mes=='Oct':
        return 10
    elif mes=='Nov':
        return 11
    elif mes=='Dec':
        return 12

def completar(a):
    mes_inicial=meses(a[0].split(" ")[0])
    mes_final=meses(a[-1].split(" ")[0])
    year_incial=int(a[0].split(" ")[2])
    year_final=int(a[-1].split(" ")[2])
    dia_inicial=int(a[0].split(" ")[1].split(',')[0])
    dia_final=int(a[-1].split(" ")[1].split(',')[0])
    start_date = date(year_incial, mes_inicial, dia_inicial)
    end_date = date(year_final, mes_final, dia_final+1)
    fechas=[]
    for single_date in daterange(start_date, end_date):
        fechas.append(single_date.strftime("%b %d, %Y"))

    print(fechas)

completar(['Oct 2, 1969', 'Oct 5, 1969', 'Oct 7, 1969', 'Oct 9, 1969'])
