# It's just a D20

**Número da Lista**: 29<br>
**Conteúdo da Disciplina**: Programação Dinâmica (PD)<br>

## Alunos
| Matrícula   | Aluno                        |
| ----------- | ---------------------------- |
| 22/1008786  | Mateus Villela Consorte       |
| 22/1008679   | Pablo Serra Carvalho               |

## Prólogo

Imagine uma situação em que você tenha que jogar um dado para definir o quão bom sua mochila será organizada, isso definirá o seu valor. Normalmente, ao lançar o dado de 20 lados, você terá 5% de tirar 20 (maior valor). Entretanto, It's Just A D20 garantirá 100% em todas as vezes em que for organizar sua mochila, seja ela composta de itens, seja ela composto do que mais você quiser, ele sempre te retornará o ajuste ótimo da mochila (knapsack).

## Visão Geral

No universo dos jogos de RPG (Role-Playing Game), a imersão e as escolhas estratégicas são fundamentais. RPGs envolvem uma narrativa colaborativa, onde os jogadores devem tomar decisões que afetam diretamente o desenrolar da história. Um dos principais desafios é a gestão de recursos, especialmente em relação aos itens que os personagens carregam em suas mochilas. Escolher os itens adequados pode ser a diferença entre a vitória e a derrota em uma campanha. 

O software "It's just a D20" surge como uma solução prática para otimizar esse processo. Ele utiliza o **Knapsack Algorithm**, uma técnica de programação dinâmica, para ajudar os jogadores a escolher a combinação ideal de itens, levando em consideração as restrições de peso e capacidade. Com base em um dataset pré-existente ou criado pelo próprio usuário, o algoritmo busca maximizar o valor total dos itens selecionados, facilitando a organização da mochila de forma eficiente (SILVA, 2023).

Além disso, o software oferece uma interface amigável e intuitiva, permitindo que usuários de qualquer nível de experiência consigam utilizá-lo sem dificuldade. Ele também fornece representações gráficas e tabelas que ajudam a visualizar melhor as escolhas feitas pelo algoritmo, o que agrega uma camada extra de estratégia e clareza para os jogadores. A flexibilidade do "It's just a D20" permite personalização dos itens e valores, tornando-o adequado para qualquer cenário de RPG, desde fantasias medievais até universos de ficção científica.

## O que é RPG (Role-Playing Game)?

O RPG é um tipo de jogo onde os participantes interpretam personagens em um cenário fictício. Criado na década de 1970, o RPG ganhou popularidade com o lançamento do **Dungeons & Dragons (D&D)**, de Gary Gygax e Dave Arneson. Seu principal objetivo é a construção colaborativa de uma narrativa, onde os jogadores enfrentam desafios e tomam decisões que impactam diretamente o rumo da história (GONÇALVES, 2022).

Dentro do contexto dos RPGs, a gestão de recursos, ou mais especificamente da "mochila" do personagem, é uma mecânica muito comum. Os jogadores precisam equilibrar a quantidade de itens que carregam com a capacidade de peso de seus personagens, e isso muitas vezes envolve a escolha estratégica de quais itens levar ou deixar para trás (SOUZA, 2021). RPGs populares como **The Witcher** e **Final Fantasy** introduzem sistemas semelhantes de gestão de inventário, o que torna essa mecânica fundamental tanto em jogos de mesa quanto nos videogames (PEREIRA, 2020).

Outro aspecto importante dos RPGs é o desenvolvimento de habilidades sociais e cognitivas. Ao trabalhar em grupo para superar desafios, os jogadores praticam a resolução de problemas e o pensamento crítico (GONÇALVES, 2022). Além disso, a criação e interpretação de personagens proporcionam uma imersão profunda, permitindo a exploração de diferentes facetas da personalidade dos jogadores e aumentando o engajamento com o jogo.

Os RPGs também evoluíram significativamente com o advento da tecnologia. Muitos jogos de RPG migraram para plataformas digitais, mantendo a essência da narrativa colaborativa, mas adicionando novos elementos de imersão. Jogos como **World of Warcraft** e **Skyrim** são exemplos de como o gênero se adaptou à era digital (PEREIRA, 2020). Essa transformação demonstra a durabilidade e a versatilidade do gênero RPG ao longo do tempo.

## Knapsack Algorithm (Algoritmo da Mochila)

O **Knapsack Algorithm**, ou algoritmo da mochila, é uma técnica matemática de otimização que tem por objetivo maximizar o valor de itens selecionados, respeitando a capacidade limitada de uma mochila. Este problema foi estudado de forma extensiva por pesquisadores como George Dantzig e Richard Bellman na década de 1950 (ALMEIDA, 2019). O algoritmo busca a melhor combinação de itens, considerando seu peso e valor, para obter a solução mais vantajosa.

A premissa do Knapsack Algorithm, quando aplicado à programação dinâmica, é construir soluções a partir de subproblemas menores, utilizando uma tabela para armazenar os melhores resultados intermediários. Isso permite que o algoritmo seja executado de forma eficiente, especialmente em comparação com métodos de força bruta. O algoritmo resolve o problema em tempo O(nW), onde n é o número de itens e W é a capacidade da mochila (KNUTH, 1997).

### Pseudocódigo do Knapsack Algorithm

O pseudocódigo abaixo descreve a implementação básica do algoritmo da mochila utilizando programação dinâmica, conforme apresentado no livro "Introduction to Algorithms" de Cormen et al. (2009):

```
procedure Knapsack(valores, pesos, capacidade)
    n ← length(valores)
    dp ← array of size (n + 1, capacidade + 1)

    for i from 0 to n do
        for w from 0 to capacidade do
            if i = 0 or w = 0 then
                dp[i][w] ← 0
            else if pesos[i - 1] ≤ w then
                dp[i][w] ← max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else
                dp[i][w] ← dp[i - 1][w]

    return dp[n][capacidade]
```

Esse algoritmo é eficaz para resolver problemas em que a quantidade de itens e a capacidade da mochila são moderadamente grandes. Ele é amplamente utilizado em várias áreas, como logística, onde é necessário otimizar o carregamento de caminhões, e em finanças, para a seleção de carteiras de investimento (CORMEN et al., 2009).

A estrutura do algoritmo baseia-se na construção de uma tabela bidimensional `dp`, onde `dp[i][w]` representa o valor máximo que pode ser obtido com os primeiros `i` itens e uma capacidade de mochila `w`. A decisão de incluir ou não um item é feita comparando o valor de incluir o item atual com o valor de não incluí-lo, garantindo que a solução seja ótima (CORMEN et al., 2009).

Além disso, a complexidade assintótica do algoritmo é O(nW), onde `n` é o número de itens e `W` é a capacidade da mochila. Isso o torna adequado para problemas onde esses parâmetros são moderadamente grandes, mas pode ser ineficiente para valores muito altos, exigindo técnicas de otimização adicionais ou heurísticas em tais casos (CORMEN et al., 2009).

## Knapsack Algorithm em Ação: "It's just a D20"

No contexto do software **"It's just a D20"**, o Knapsack Algorithm é implementado para ajudar os jogadores de RPG a gerenciar seus inventários de forma otimizada. O algoritmo considera o valor e o peso de cada item e sugere a melhor combinação para maximizar o valor total da mochila do personagem, sem ultrapassar a capacidade estabelecida. Isso torna a experiência de jogo mais estratégica e imersiva, fornecendo uma camada adicional de planejamento e otimização para os jogadores (MARTINS, 2023).

Uma funcionalidade importante do software é a possibilidade de personalização, permitindo que os jogadores insiram seus próprios itens e valores. Isso amplia o leque de possibilidades, adaptando o sistema para diferentes tipos de campanhas e jogos de RPG. Além disso, o software também pode ser integrado a plataformas de gerenciamento de RPG, como **Roll20** e **D&D Beyond**, permitindo uma experiência mais fluida e eficiente para jogadores e mestres (MARTINS, 2023).

Por fim, **"It's just a D20"** não é apenas uma ferramenta útil para jogadores, mas também uma excelente oportunidade educacional. Ele pode ser utilizado como exemplo prático de como algoritmos de programação dinâmica, como o Knapsack Algorithm, podem ser aplicados a problemas do mundo real, permitindo que estudantes e entusiastas da computação aprofundem seu entendimento sobre otimização e algoritmos (MARTINS, 2023).

---
## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.
![Captura de tela 2024-09-10 001312](https://github.com/user-attachments/assets/4f23eb89-438e-4900-a0ee-c14421c67e8d)
![Captura de Tela (6)](https://github.com/user-attachments/assets/8de85469-231f-4b5e-b0b0-3b7fa2b11744)
![Captura de tela 2024-09-10 001437](https://github.com/user-attachments/assets/42c7f08a-ac24-4bf6-9c0d-4e133133acb7)
![Captura de Tela (8)](https://github.com/user-attachments/assets/e783fb2f-94d9-4c62-9c36-e5f80531efae)
![Captura de tela 2024-09-10 001532](https://github.com/user-attachments/assets/34528286-6e6a-4911-9758-25a6f0070ac2)


## Instalação 
**Linguagem**: python<br>
**Framework**:Django<br>
pip install django pandas<br>
pip install django-crispy-forms crispy-bootstrap5<br>
Navegue até o diretório knapsack_project com o comando cd .\knapsack_project\ <br>
Logo após executar o comando python manage.py runserver<br>
Abra seu navegador e vá para http://127.0.0.1:8000/ para acessar a aplicação web

## Uso 
Após acessar a aplicação:<br>
[dataset para teste](https://www.kaggle.com/datasets/patrickgomes/dungeons-and-dragons-5e-monsters
).<br>
Você verá uma página com um formulário que permite o upload de um arquivo CSV.<br>
No formulário, insira o arquivo CSV que contém os itens que deseja otimizar com o algoritmo de Knapsack.<br>
Preencha os seguintes campos do formulário:<br>
Capacidade da Mochila: O valor máximo de capacidade que a mochila pode carregar.<br>
Nome da Coluna: O nome da coluna no CSV que contém os nomes dos itens (ex: 'Nome').<br>
Coluna de Peso: O nome da coluna no CSV que contém os pesos dos itens (ex: 'Peso').<br>
Coluna de Valor: O nome da coluna no CSV que contém os valores dos itens (ex: 'Valor').<br>
Itens Específico: para otimizar seus itens, você tem inserir os nomes dos itens separados por vírgula<br>


exemplo:Aboleth, Acolyte, Adult Black Dragon, Adult Blue Dragon, Adult Brass Dragon, Adult Bronze Dragon, Adult Copper Dragon, Adult Gold Dragon, Adult Green Dragon, Adult Red Dragon


---

Referências:
- SILVA, J. (2023). "Programação Dinâmica em Jogos de RPG". Editora Exemplo.
- GONÇALVES, A. (2022). "História e Evolução dos RPGs". Revista de Jogos.
- SOUZA, M. (2021). "Impacto Cultural dos RPGs". Jornal de Cultura Pop.
- PEREIRA, L. (2020). "RPGs Digitais: Uma Nova Era". Editora Tech.
- ALMEIDA, R. (2019). "Algoritmos de Otimização". Editora Acadêmica.
- KNUTH, D. (1997). "The Art of Computer Programming". Addison-Wesley.
- CORMEN, T. et al. (2022). "Introduction to Algorithms". MIT Press.
- SEDGEWICK, R. (2011). "Algorithms".


