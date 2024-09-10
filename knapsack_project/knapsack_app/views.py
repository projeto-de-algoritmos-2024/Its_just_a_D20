import pandas as pd
from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render
from .forms import KnapsackForm
import re
from django.shortcuts import redirect
# Função para extrair números de strings (como "135 (18d10+36)")
def extrair_numero(string):
    match = re.search(r'\d+', str(string))
    return int(match.group()) if match else 0

# Função para o algoritmo de Knapsack
def knapsack(capacidade, pesos, valores, n):
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    item_selecionado = [[[] for _ in range(capacidade + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        # Laço para percorrer todas as capacidades possíveis da mochila (0 até a capacidade máxima)
        for w in range(capacidade + 1):
            # Verifica se o peso do item atual (pesos[i-1]) é menor ou igual à capacidade atual (w)
            if pesos[i - 1] <= w:
                # Se incluir o item atual resulta em um valor maior do que não incluí-lo
                if valores[i - 1] + dp[i - 1][w - pesos[i - 1]] > dp[i - 1][w]:
                    dp[i][w] = valores[i - 1] + dp[i - 1][w - pesos[i - 1]]
                    item_selecionado[i][w] = item_selecionado[i - 1][w - pesos[i - 1]] + [i - 1]
                else:
                    # Caso contrário, mantém o valor máximo anterior sem incluir o item
                    dp[i][w] = dp[i - 1][w]
                    item_selecionado[i][w] = item_selecionado[i - 1][w]
            else:
                # Se o item atual não pode ser incluído (peso maior que a capacidade w),
                dp[i][w] = dp[i - 1][w]
                item_selecionado[i][w] = item_selecionado[i - 1][w]

    # Retorna o valor máximo possível que pode ser carregado na mochila (dp[n][capacidade])
    # e a lista de itens selecionados para alcançar esse valor (item_selecionado[n][capacidade])
    return dp[n][capacidade], item_selecionado[n][capacidade]

def processar_csv(file, nome_coluna, peso_coluna, valor_coluna):
    # Lê o arquivo CSV e carrega os dados em um DataFrame do pandas
    df = pd.read_csv(file)
    # Preenche os valores nulos da coluna de nomes com strings vazias ('')
    df[nome_coluna] = df[nome_coluna].fillna('')
    # Aplica a função 'extrair_numero' na coluna de peso para extrair apenas os números das strings
    df[peso_coluna] = df[peso_coluna].apply(extrair_numero)
    # Aplica a função 'extrair_numero' na coluna de valor para extrair apenas os números das strings
    df[valor_coluna] = df[valor_coluna].apply(extrair_numero)
    # Retorna o DataFrame processado
    return df

# Função para exibir o resultado final após a execução do algoritmo de Knapsack
def resultado_view(request):
    # Recupera o resultado do valor máximo da mochila armazenado na sessão
    resultado = request.session.get('resultado')
    
    # Recupera os itens selecionados também armazenados na sessão
    itens_selecionados = request.session.get('itens_selecionados')
    
    # Renderiza a página de resultados ('resultado.html') e passa o resultado e os itens selecionados como contexto
    return render(request, 'resultado.html', {
        'resultado': resultado,
        'itens_selecionados': itens_selecionados
    })



def knapsack_view(request):
    if request.method == 'POST':
        form = KnapsackForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('csv_file')  # Use get() para evitar KeyError

            if not csv_file:
                messages.error(request, 'Você deve enviar um arquivo CSV.')
                return render(request, 'mochila.html', {'form': form})
            csv_file = request.FILES['csv_file']
            capacidade = form.cleaned_data['capacidade']
            nome_coluna = form.cleaned_data['nome_coluna']
            peso_coluna = form.cleaned_data['peso_coluna']
            valor_coluna = form.cleaned_data['valor_coluna']
            item_nomes = form.cleaned_data.get('item_nomes', '').split(',')

            df = processar_csv(csv_file, nome_coluna, peso_coluna, valor_coluna)

            if item_nomes:
                df = df[df[nome_coluna].isin([nome.strip() for nome in item_nomes])]

            pesos = df[peso_coluna].tolist()
            valores = df[valor_coluna].tolist()
            nomes = df[nome_coluna].tolist()

            max_valor, itens_selecionados = knapsack(capacidade, pesos, valores, len(valores))
            itens_nomes = [nomes[i] for i in itens_selecionados]
            resultado = f'O valor máximo que pode ser carregado é: {max_valor}.'
            itens_selecionados = f'Itens selecionados: {", ".join(itens_nomes)}'

            # Salvar resultados na sessão
            request.session['resultado'] = resultado
            request.session['itens_selecionados'] = itens_selecionados

            return redirect('resultado')  # Redirecionar para a view de resultados
    else:
        form = KnapsackForm()

    return render(request, 'mochila.html', {'form': form})



def resultado_view(request):
    resultado = request.session.get('resultado')
    itens_selecionados = request.session.get('itens_selecionados')
    return render(request, 'resultado.html', {
        'resultado': resultado,
        'itens_selecionados': itens_selecionados
    })
from .forms import KnapsackForm

def seu_view(request):
    if request.method == 'POST':
        form = KnapsackForm(request.POST, request.FILES)
        if form.is_valid():
            # Processar os dados do formulário
            pass
        else:
            # Adicionar mensagem de erro
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
    else:
        form = KnapsackForm()

    return render(request, 'mochila.html', {'form': form})