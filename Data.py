# Classe Data

class Data(object):
    # Método construtor
    def __init__(self, dia, mes, ano):
        if self.dataValida(dia, mes, ano):
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:
            self.dia = 'Verifique se o dia está correto!'
            self.mes = 'Verifique se o mês está correto!'
            self.ano = 'Verifique se o ano está neste milênio!'

    # Encapsulamento
    def setDia(self, dia):
        if self.dataValida(dia, self.getMes(), self.getAno()):
            self.dia = dia
        else:
            self.dia = 'Dia inválido!'
    def getDia(self):
        return self.dia

    def setMes(self, mes):
        if self.dataValida(self.getDia(), mes, self.getAno()):
            self.mes = mes
        else:
            self.mes = 'Mês inválido!'
    def getMes(self):
        return self.mes

    def setAno(self, ano):
        if self.dataValida(self.getDia(), self.getMes(), ano):
            self.ano = ano
        else:
            self.ano = 'Ano fora do milênio!'
    def getAno(self):
        return self.ano

    # Retorno de dados da classe
    # Método String:
    # Transforma os dados da classe em uma cadeia de string
    def __str__(self):
        return (
            '\n Dia: ' + str(self.getDia()) +
            '\n Mes: ' + str(self.getMes()) +
            '\n Ano: ' + str(self.getAno())
        )

    def dataValida(self, dia, mes, ano):

        # Verificação do dia em um range
        if ano < 1 or ano > 3000:
            return False

        # Verificar se mês está no range correto
        if mes < 1 or mes > 12:
            return False

        # Verificação do ano bisexto
        anoBisexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

        diasNosMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if anoBisexto and mes == 2:
            diasNosMeses[2] = 29

        # Retornar o dia dentro de um intervalo válido
        return 1 <= dia <= diasNosMeses[mes]