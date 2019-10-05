class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None
        self.__ant = None

    def getDado(self):
        return self.__dado

    def getProx(self):
        return self.__prox

    def getAnt(self):
        return self.__ant

    def setDado(self, dado):
        self.__dado = dado

    def setProx(self, prox):
        self.__prox = prox

    def setAnt(self, ant):
        self.__ant = ant


class Pilha:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

    def setInicio(self, inicio):
        self._inicio = inicio

    def setFim(self, fim):
        self._fim = fim

    def buscar(self, dado):
        i = self._inicio
        while i is not None:
            if i.getDado() == dado:
                return i
            i = i.getProx()
        return i 

    def isVazia(self):
        return self._inicio is None

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if self.isVazia():
            self._inicio = novono
            self._fim = self._inicio
        else:
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
            self._inicio = novono

    def removerDado(self, dado):
        noRemovido = self.buscar(dado) 
        if noRemovido is not None:
            prox = noRemovido.getProx()
            ant = noRemovido.getAnt()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            elif noRemovido is self._inicio:
                prox.setAnt(None)
                self._inicio = prox
            elif noRemovido is self._fim:
                ant.setProx(None)
                self._fim = ant
            else:
                ant.setProx(prox)
                prox.setAnt(ant)
        return noRemovido

    def removerDoInicio(self):
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._inicio.getProx().setAnt(None)
                self._inicio = self._inicio.getProx()
            else:
                self._inicio = self._fim = None




n = int(input())
for i in range(n):
    entrada = input()
    expressao = Pilha()
    key = 0
    for char in entrada:
        if char == '(' or char == '[' or char == '{':
            expressao.inserirNoInicio(char)
        else:
            if not expressao.isVazia() and char == ')':
                if expressao.getInicio().getDado() == '(':
                    expressao.removerDoInicio()
                else:
                    key = 1
                    break
            elif not expressao.isVazia() and char == ']':
                if expressao.getInicio().getDado() == '[':
                    expressao.removerDoInicio()
                else:
                    key = 1
                    break
            elif not expressao.isVazia() and char == '}':
                if expressao.getInicio().getDado() == '{':
                    expressao.removerDoInicio()
                else:
                    key = 1
                    break
            else:
                key = 1
                break
    if key != 0 or not expressao.isVazia():
        print("N")
    else:
        print("S")
