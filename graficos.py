import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from controller import ControllerVededor
class Graficos:
    def __init__(self):
        self.controller = ControllerVededor()
        self.loja = self.controller.loja
        self.vendedores = self.controller.vendedores

    def showGraficoLojas(self):
        x = []
        y = []
        for loja_name in self.loja:
            x.append(loja_name)
            y.append(self.loja[loja_name]['total'])
        plt.bar(x,y,color=['#FF4500','#FF8C00','#FFFF00'])
        plt.ylabel('Valor Arrecado')
        plt.title('Valor Arrecado x Unidade Bemol')
        plt.show()
    def showGraficoMelhorVendedor(self,loja):
        melhor_vendedor = self.loja[loja]['melhor_vendedor']
        self.showVendasPorVendedor(melhor_vendedor)


    def dataFormata(self,data):
        data = data.split("T")[0]
        data = data.split('-')
        data = data[2]+'/'+data[1]+"/"+data[0][2:4]
        return data
    def showVendasPorVendedor(self,vendedorId):

        manoa = {'x':[],'y':[],'cor':'#000080','loja':'Manoa'}
        cachoerinha = {'x': [], 'y': [],'cor':'#FF0000','loja':'Cachoerinha'}
        armando = {'x': [], 'y': [],'cor':'#FFFF00','loja':'Armando Mendes'}
        lojas_pontos = [manoa,cachoerinha,armando]
        vendedor = self.vendedores[vendedorId]
        x = []
        y = []
        data = []
        loja = []
        for venda in vendedor['infoVenda']:
            data.append(venda['data_compra'])
            loja.append(venda['filial'].replace("Loja ",''))
            y.append(venda['valor_compra'])
        data = sorted(data)
        for i in range(len(data)):
            x.append(self.dataFormata(data[i]))
        fig = plt.figure(1)

        plt.grid(axis='y')
        plt.plot(x,y,color='#565656',linewidth=0.5)
        for i in range(len(loja)):
            if('Manoa' in loja[i]):
                manoa['x'].append(x[i])
                manoa['y'].append(y[i])
            elif('Cachoerinha' in loja[i]):
                cachoerinha['x'].append(x[i])
                cachoerinha['y'].append(y[i])
            elif('Armando Mendes' in loja[i]):
                armando['x'].append(x[i])
                armando['y'].append(y[i])

        for i in lojas_pontos:
            if i['x']!=[]:
                plt.scatter(i['x'],i['y'],color=i['cor'],label=i['loja'],linewidths=0.8)


        for i in range(len(x)):
            plt.text(x[i],y[i],format(y[i],'.2f')+"\n\n", horizontalalignment='center',   verticalalignment='center',fontsize=8)
        plt.ylabel('Valor da Venda (R$)')
        plt.title('Vendas de '+vendedor['nome'])
        plt.xticks(rotation=90)
        plt.ylim(bottom = 0)
        plt.autoscale()
        plt.legend()
        plt.tight_layout()
        fig.savefig('samplefigure',bbox_inches='tight')
        plt.show()



g = Graficos()
g.showGraficoMelhorVendedor('Loja Armando Mendes')
