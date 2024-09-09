from django import forms

class KnapsackForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV", required=True)
    capacidade = forms.IntegerField(label="Capacidade da mochila", required=True)
    nome_coluna = forms.CharField(label="Coluna para os nomes dos itens", required=True)
    peso_coluna = forms.CharField(label="Coluna para o peso dos itens", required=True)
    valor_coluna = forms.CharField(label="Coluna para o valor dos itens", required=True)
    item_nomes = forms.CharField(label="Nomes dos itens (separados por vírgula)", required=True)
