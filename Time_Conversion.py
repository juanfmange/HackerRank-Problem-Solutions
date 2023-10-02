def convertir_a_formato_militar(hora_am_pm):
    # Divide la cadena en partes para extraer la hora, los minutos y los segundos.
    hora, minutos, segundos = hora_am_pm[:-2].split(':')
    am_pm = hora_am_pm[-2:].upper()
    
    # Si es PM y la hora no es 12, suma 12 para convertirla a formato militar.
    if am_pm == 'PM' and hora != '12':
        hora = str(int(hora) + 12)
    
    # Si es AM y la hora es 12, establece la hora a 00.
    if am_pm == 'AM' and hora == '12':
        hora = '00'
    
    # Formatea la hora en formato militar y devuelve el resultado.
    hora_militar = f"{hora}:{minutos}:{segundos}"
    return hora_militar

hora_am_pm = "07:05:45PM"
hora_militar = convertir_a_formato_militar(hora_am_pm)
print(hora_militar) 