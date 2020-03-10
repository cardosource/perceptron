#-*- encoding:utf-8 -*-



class Perceptron:
    global aprendizado
    w = [0, 0, 0]
    x = 0
    t = [1, 1, -1]
    y = 0
    max_int = 1000
    taxa_aprendizado =  0.036011493591690376

    def transferencia(self, y_in):
        if y_in >= 0:
            y = 1
            return y
        else:
            y = -1
            return y

    def iniciando(self):
        while self.max_int > 0:
            ok = 0
            for i in range(0, len(self.x)):

                calc = 0
                # para calcular a saida do adaline, cada entrada de x eh multiplicada
                # pelo seu peso w correspondente
                for j in range(0, len(self.x[i])):
                    calc = calc + self.x[i][j] * self.w[j]
                    print("Saida do adaline ",calc)
                # a saida eh igual a soma anterior
                # funcao TRANSFERENCIA
                self.y = Perceptron().transferencia(y_in=calc)
                # atualiza os pesos
                for j in range(0, len(self.w)):
                    # regra delta
                    apresenta = self.w[j] = self.w[j] + self.taxa_aprendizado * (self.t[i] - calc) * self.x[i][j]
                    print("peso atualizado ",apresenta, " ",self.x[i])
                if self.y == 1:
                    print("sinal fechado")
                elif self.y == -1:
                    print("sinal aberto")
                if self.y == self.t[i]:
                    ok += 1
                    rep = "Correto = %i" % self.y
                    #      print(self.x[i])
                    print("%s" % rep)
                else:
                    rep = "Erro %i" % self.y
                    print(rep)
            if ok == len(self.x):
                self.aprendizado = ok - 1
                break
            print("")
            self.max_int += 1


entrada \
    = [
    [1, 1, 1],
    [1, -1, 1],
    [-1, 1, 1]
]

if __name__ == '__main__':
    apt = Perceptron()
    apt.t = [1, 1, -1]
    apt.x = [
        [1, 1, 1],
        [1, -1, 1],
        [-1, 1, 1]
    ]
    apt.iniciando()
    print("""   
[ RNA ] - Rede Neural Perceptron obteve aprendizado na {}  Interacao

Inativo =1
Prossiga = -1
              Inativo           andar
+----------+-------------+--------------+
|vermelho__|_____1_______|______________|
|amarelo___|_____1_______|______________|
|verde     |             |      -1      |
+----------+-------------+--------------+    
.""".format(apt.aprendizado))



