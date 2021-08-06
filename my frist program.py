def conversor(tipo_moneda, valor_dolar):
    tipo_moneda = input ('cuantos ' + tipo_moneda +' quieres cambiar:')
    tipo_moneda = float (tipo_moneda)
    dolares = tipo_moneda / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares +  'dolares'

menu = """
Welcome to dollar converter 
1 - Soles
2 - Pesos Argentinos 
3 - Pesos Colombianos

Choose an option :  """

option = input(menu)

if option == '1':
    conversor('soles', 3.96)
elif option == '2':
    conversor('Pesos Argentinos', 63.00)
elif option == '3':
    conversor('Pesos Colombianos', 3895)
    


