from django import forms

class KnapsackForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV", required=False)
    capacidade = forms.IntegerField(label="Capacidade da mochila", required=False)
    nome_coluna = forms.CharField(label="Coluna para os nomes dos itens", required=False)
    peso_coluna = forms.CharField(label="Coluna para o peso dos itens", required=False)
    valor_coluna = forms.CharField(label="Coluna para o valor dos itens", required=False)
    item_nomes = forms.CharField(label="Nomes dos itens (separados por vírgula)", required=False)
