import pandas as pd

if __name__ == '__main__':

    series_objeto = pd.Series([1, 7, 9, 13, 17, 99])
    print(series_objeto)

    series_objeto2 = pd.Series([4, 7, 8, -2], index=['alfa', 'beta', 'teta', 'gama'])
    print(series_objeto2)

    lista_cursos = ['Estatística', 'Geometria', 'Cálculo', 'Economia']
    lista_creditos = [90, 60, 90, 40]
    lista_requisitos = [True, False, True, False]

    disciplinas = {'cursos': lista_cursos,
                   'créditos': lista_creditos,
                   'requisito' : lista_requisitos}

    dados = pd.DataFrame(disciplinas)
    print(dados)
    print(dados.info())

    dicioNotas = dict(zip(lista_cursos, lista_creditos))
    print('A nota de estatítica é: ' + str(dicioNotas['Estatística']))
    print('Geometria está na lista? ' + str('Geometria' in dicioNotas))
    print('Geografia está na lista? ' + str('Geografia' in dicioNotas))

