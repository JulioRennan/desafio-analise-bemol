import matplotlib.pyplot
import matplotlib.pyplot as plt
from unidecode import unidecode
from matplotlib.pyplot import figure
from controller_produto import ControllerProduto
from controller_venda import ControllerVededor
class Graficos:
    def __init__(self):
        self.controller = ControllerVededor()
        self.controller_produto = ControllerProduto()
        self.loja = self.controller.loja
        self.vendedores = self.controller.vendedores

    def showGraficoLojas(self):
        x = []
        y = []
        for loja_name in self.loja:
            x.append(loja_name)
            y.append(self.loja[loja_name]['total'])
        for i in range(len(x)):
            plt.text(x[i], y[i], "R$ " +format(y[i], '.2f') + "\n", horizontalalignment='center', verticalalignment='center',
                     fontsize=10)
        plt.bar(x,y,color=['#FF4500','#FF8C00','#FFFF00'],width=0.5)
        plt.ylabel('Valor Arrecado')
        plt.xlabel('\nUnidade Bemol')
        plt.tight_layout()
        plt.legend()
        plt.autoscale()
        plt.title('Valor Arrecado x Unidade Bemol')
        plt.show()

    def showGraficoMelhorVendedor(self,loja):
        cor = {
            'Loja Manoa':'#000080',
            'Loja Armando Mendes':'#FFFF00',
            'Loja Cachoerinha':'#FF0000',
        }

        melhor_vendedor = self.loja[loja]['melhor_vendedor']
        infoVendas = self.vendedores[melhor_vendedor]['infoVenda']

        x = []
        y = []
        data = []

        for venda in infoVendas:

            if(venda['filial']==loja):
                data.append(venda['data_compra'])
                y.append(venda['valor_compra'])
        data = sorted(data)
        for i in data:
            x.append(self.dataFormata(i))
        for i in range(len(x)):
            plt.text(x[i], y[i], format(y[i], '.2f') + "\n\n", horizontalalignment='center', verticalalignment='center',
                     fontsize=8)
        plt.plot(x, y, color='#565656', linewidth=0.5)
        plt.scatter(x,y,color=cor[loja],label=loja)
        plt.title("Melhor Vendedor:  " + self.vendedores[melhor_vendedor]['nome']+'\nUnidade: ' + loja, horizontalalignment="center")
        plt.grid(axis='y')
        plt.ylabel('Valor da Venda (R$)')
        plt.xticks(rotation=90)
        plt.ylim(bottom=0)
        plt.autoscale()
        plt.legend()
        plt.tight_layout()
        plt.show()
        self.showVendasPorVendedor(melhor_vendedor)


    def dataFormata(self,data):
        data = data.split("T")[0]
        data = data.split('-')
        data = data[2]+'/'+data[1]+"/"+data[0][2:4]
        return data

    def showVendasPorVendedor(self,vendedorId,show = False):
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
        arq_nome = vendedorId+'#'+unidecode(vendedor['nome'])
        fig.savefig("imagens/Questao 1/grafico venda por vendedor/"+arq_nome+".png",bbox_inches='tight')
        if show:
            plt.show()
            input('digite qualquer tecla para fechar')
        plt.close()
    #ESSE METODO IRA TENTAR SALVAR TODOS OS 2166 FUNCIONARIOS
    def salvarGraficoVendaPorVendedor(self):
        graficosNaoSalvos = []
        for vendedorId in self.vendedores:
            try:
                self.showVendasPorVendedor(vendedorId)
                print(vendedorId,'salvo')
            except:
                graficosNaoSalvos.append(vendedorId)
        if graficosNaoSalvos:
            print('Alguns Graficos nao puderam ser salvos, verificar arquivo na pasta "logs"')
            open('logs/Graficos nao salvos.txt','w').write("\n".join(graficosNaoSalvos))
            return graficosNaoSalvos
        print('todos os graficoos foram salvos com sucesso')
        return True





g = Graficos()


#Questao 1

#g.salvarGraficoVendaPorVendedor()
#g.showGraficoMelhorVendedor('Loja Manoa')
#g.showGraficoMelhorVendedor('Loja Armando Mendes')
#g.showGraficoMelhorVendedor('Loja Cachoerinha')
g.showGraficoLojas()

#Questao 2
#g.controller_produto.produtoMaisVendido('Mercadinho Daskina#430')


