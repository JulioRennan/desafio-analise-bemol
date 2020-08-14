#  Analise Bemol

## Descrição
  Foi fornecido uma planilha xlsx, com dados **fictícios**  com a seguinte estrutura:
  
### Folha 1
num_compra|	usuario|	nome	|dados|	Filial	|data_compra|	valor_compra	|Imposto	|Informado sobre importo?
------------|-------|-------|------|--------|-----------|---------------|---------|------------------------|
24937847	|295|	Daniel	|12	|Loja Armando Mendes|	2019-01-06 11:53:01	|R$129,12|	R$2,60	|Sim
23600787	|295	|Daniel	|12|	Loja Manoa	|2019-06-01 17:27:11	|R$95,96|	R$1,94	|Sim
23802765	|331|	Alex|	12	|Loja Manoa|	2019-06-11 20:10:43|	R$586,20|	R$11,82	|Sim


### Folha 2

Loja|	data_compra|	inicio	|termino	|Loja_nome	|codloja	|produto	|EAN|	quantidade	|valor_total|	Imposto|
----|------------|----------|----------|----------|---------|---------|---|-------------|------------|---------|
430	|2019-07-05 |10:30:41	|2019-07-05	|2019-07-20	|Mercadinho Daskina|	4,96186E+13	|Açaí 1L|	3,29849E+12|1|	R$ 9,23	|R$ 1,58|
430 |	2019-07-07|13:50:44	2019-07-05	|2019-07-20|	Mercadinho Daskina|4,96186E+13	|Açaí| 1L Zero|7,8949E+12|1|	R$ 5,59|	R$ 0,96|

  
  E a partir dessa informações deveria ser feito um código capaz de capturar pelo menos os seguintes dados:
1. **Questão**
    1. Melhor vendedor por unidade
    1. Venda por vendedor
    
1. **Questão**
    1. Produto mais vendido
    
  
