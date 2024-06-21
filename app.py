import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)

class CalculaGanador:
    def __init__(self):
        self.CANDIDATO = None
        self.ESVALIDO = None

    # Tecnica de parametrizacion: se añade un parametro nombre_archivo para poder leer cualquier archivo (hace el codigo más flexible)
    # Tecnica de Renombre: se renombra la funcion leer_datos a cargar_datos_de_csv que explica mejor lo que hace el metodo
    def cargar_datos_de_csv(self, nombre_archivo = '0204.csv'):  
        data = []
        try:
            with open(nombre_archivo, 'r') as csvfile:
                # Parsear encabezado
                encabezado = csvfile.readline().strip().split(',')
                self.parse_encabezado(encabezado)  # Tecnica de Extraccion de metodo 
                # Leer filas
                datareader = csv.reader(csvfile)
                for fila in datareader:
                    data.append(fila)

        except FileNotFoundError:
            print(f"No se encontro el archivo {nombre_archivo}")
        except ValueError as ve:
            print(f"No se encontro la columna {ve}")

        return data

    def calcularganador(self, data):
        votosxcandidato = {}

        VALIDO = '1' # Tecnica de introducir variable descripitiva
        CONTEO_VOTOS = 0 # Tecnica de introducir variable descripitiva

        for fila in data:
            if not fila[self.CANDIDATO] in votosxcandidato:
                votosxcandidato[fila[self.CANDIDATO]] = 0

            if fila[self.ESVALIDO] == VALIDO:
                votosxcandidato[fila[self.CANDIDATO]] += 1
                CONTEO_VOTOS += 1

        # Tecnica de renombre: se renombra la variable ordenado a resultados_ordenados en base al value
        resultados_ordenados = sorted(votosxcandidato, key=votosxcandidato.get, reverse=True)

        # Tecnica de extraccion de metodo: se extrae el metodo imprimir_resultados
        self.imprimir_resultados(votosxcandidato)

        # Tecnica de sustituir de codigo reduntante: se elimino el for innecesario

        # Tecnica de extraccion de metodo: se extrae el metodo definir_resultado
        return self.definir_resultado(resultados_ordenados,CONTEO_VOTOS, votosxcandidato[resultados_ordenados[0]])

    def parse_encabezado(self, encabezado):
        # Tecnica de introducir variable descripitiva
        self.CANDIDATO = encabezado.index('candidato')
        self.ESVALIDO = encabezado.index('esvalido')
        if self.CANDIDATO == -1 or self.ESVALIDO == -1:
            raise ValueError("Candidato o Esvalido en el archivo CSV ")

    def definir_resultado(self, resultados_ordenado, CONTEO_VOTOS, votos_ganador):
        if votos_ganador > CONTEO_VOTOS / 2:
            return [resultados_ordenado[0]]        
        return [resultados_ordenado[0], resultados_ordenado[1]]

    def imprimir_resultados(self, votosxcandidato):
        for candidato in votosxcandidato:
            print(f"Candidato {candidato} tiene {votosxcandidato[candidato]} votos")

c = CalculaGanador()
print("Resultados :", c.calcularganador(c.cargar_datos_de_csv()))

print()
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print("Resultados :",c.calcularganador(datatest))
