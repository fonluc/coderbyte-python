---

### **String Reduction**

Dada uma string composta pelas letras `a`, `b` e `c`, você pode realizar a seguinte operação:

- Escolher dois caracteres distintos adjacentes e substituí-los pelo terceiro caractere.

O objetivo é encontrar o comprimento da string mais curta que pode ser obtida aplicando essa operação repetidamente.

**Exemplo:**

- Dada a string `aba`, você pode reduzi-la a uma string de 1 caractere substituindo `ab` por `c` e `ca` por `b`:
    
    ```
    aba -> ca -> b                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ```
    

**Descrição da Função**

Complete a função `stringReduction` abaixo. Ela deve retornar um inteiro que representa o comprimento da string mais curta obtida.

**Parâmetros da Função:**

- `s`: uma string composta apenas pelas letras `a`, `b` e `c`.

**Formato de Entrada:**

- A primeira linha contém o número de casos de teste `t`.
- Cada uma das próximas `t` linhas contém uma string `s` a ser processada.

**Restrições:**

- **1 ≤ t ≤ 100**
- **1 < |s| ≤ 100**

**Formato de Saída:**

- Para cada caso de teste, imprima o comprimento da string resultante mínima em uma nova linha.

**Exemplo de Entrada:**

```
3
cab
bcab
ccccc
```

**Exemplo de Saída:**

```
2
1
5
```

**Explicação:**

- Para o primeiro caso, há duas soluções possíveis: `cab -> cc` ou `cab -> bb`.
- Para o segundo caso, uma solução ótima é: `bcab -> aab -> ac -> b`.
- Para o terceiro caso, nenhuma operação pode ser realizada, então o comprimento da string permanece 5.

---

### **Código da Solução**

Aqui está a implementação da função `stringReduction` sem comentários no código:

```python
def StringReduction(strParam):

  # code goes here
    def reduce(two_letters):
        if two_letters[0] == two_letters[1]:
            return two_letters
        elif two_letters in ('ab', 'ba'):
            return 'c'
        elif two_letters in ('ac', 'ca'):
            return 'b'
        else:
            return 'a'
    
    if len(strParam) < 2:
        return strParam

    i = 1
    reduced = reduce(strParam[0:2])
    ans = ''
    while i < len(strParam) - 1:
        if len(reduced) == 2:
            ans += reduced[0]
        i += 1
        reduced = reduce(reduced[-1] + str[i])
    if reduced:
        ans += reduced
    return len(ans)

def StringReduction(the_strParam):
    change =  False
    letters = set(['a', 'b', 'c'])
    duo = [the_strParam[0]]
    final = ''
    for s in the_strParam[1:]:
        duo.append(s)
        if duo[0] == duo[1]:
            final += duo[0]
            duo = [duo[1]]
        else:
            change = True
            reduced = list((letters - set(duo)))[0]
            duo = [reduced]
    final += ''.join(duo)
    if change:
        return StringReduction(final)
    return len(final)
# keep this function call here 
print(StringReduction(input()))
```

### **Explicação da Solução**

1. **Função `reduce`**:
    - Essa função é responsável por reduzir dois caracteres distintos adjacentes para um único caractere. Ela usa as seguintes substituições:
        - `ab` e `ba` são substituídos por `c`.
        - `ac` e `ca` são substituídos por `b`.
        - `bc` e `cb` são substituídos por `a`.
2. **Processo de Redução**:
    - A função começa reduzindo os primeiros dois caracteres da string.
    - Em seguida, itera sobre os caracteres restantes da string, aplicando a função de redução em pares de caracteres adjacentes.
    - A variável `reduced` mantém o estado da string reduzida após cada operação.
3. **Resultado Final**:
    - O comprimento da string reduzida final é retornado.

---

### Seating Students

Crie a função `SeatingStudents(arr)` que recebe um array de inteiros armazenados em `arr` no seguinte formato: `[K, r1, r2, r3, ...]`, onde `K` representa o número total de mesas em uma sala de aula, e os demais inteiros no array estarão em ordem crescente e representarão as mesas que já estão ocupadas. Todas as mesas estarão dispostas em 2 colunas, onde a mesa #1 está no canto superior esquerdo, a mesa #2 está no canto superior direito, a mesa #3 está abaixo da mesa #1, a mesa #4 está abaixo da mesa #2, e assim por diante.

Seu programa deve retornar o número de maneiras de 2 alunos poderem se sentar lado a lado. Isso significa que 1 aluno está à esquerda e 1 aluno está à direita, ou 1 aluno está diretamente acima ou abaixo do outro aluno.

**Exemplo:**

Se `arr` for `[12, 2, 6, 7, 11]`, a disposição das mesas na sala de aula seria a seguinte:

!https://i.imgur.com/rvP5cjj.jpg

Com base na disposição acima das mesas ocupadas, há um total de 6 maneiras de acomodar 2 novos alunos lado a lado. As combinações são: [1, 3], [3, 4], [3, 5], [8, 10], [9, 10], [10, 12]. Portanto, para essa entrada, seu programa deve retornar `6`.

`K` variará de 2 a 24 e será sempre um número par. Após `K`, o número de mesas ocupadas no array pode variar de 0 a `K`.

**Casos de Teste**

- **Entrada:** `[6, 4]`
    
    **Saída:** `4`
    
- **Entrada:** `[8, 1, 8]`
    
    **Saída:** `6`
    

**Descrição da Função**

A função `SeatingStudents(arr)` deve ler o array de inteiros armazenados em `arr` e calcular o número de maneiras possíveis para 2 novos alunos se sentarem lado a lado, considerando a disposição das mesas em 2 colunas e as mesas já ocupadas.

---

### Solução:

```python
def SeatingStudents(arr):
    K = arr[0]
    occupied = set(arr[1:])
    rows = K // 2
    seating = 0

    for i in range(rows):
        if (2 * i + 1) not in occupied and (2 * i + 2) not in occupied:
            seating += 1

    for i in range(rows - 1):
        if (2 * i + 1) not in occupied and (2 * (i + 1) + 1) not in occupied:
            seating += 1
        if (2 * i + 2) not in occupied and (2 * (i + 1) + 2) not in occupied:
            seating += 1

    return seating

print(SeatingStudents(input()))
```

### **Explicação do Código**

1. **Inicialização e Preparação dos Dados:**
    
    ```python
    K = arr[0]
    occupied = set(arr[1:])
    ```
    
    - `K` é o número total de mesas.
    - `occupied` é um conjunto contendo as mesas já ocupadas, o que facilita a verificação rápida de ocupação.
2. **Determinação do Número de Linhas:**
    
    ```python
    rows = K // 2
    ```
    
    - Calcula o número de linhas na sala de aula, dado que há duas colunas de mesas.
3. **Verificação das Combinações Possíveis:**
    
    ```python
    for i in range(rows):
        # Verificar horizontal
        if (2 * i + 1) not in occupied and (2 * i + 2) not in occupied:
            seating += 1
        # Verificar vertical (se não for a última linha)
        if i < rows - 1:
            if (2 * i + 1) not in occupied and (2 * (i + 1) + 1) not in occupied:
                seating += 1
            if (2 * i + 2) not in occupied and (2 * (i + 1) + 2) not in occupied:
                seating += 1
    ```
    
    - **Verificação Horizontal:** Para cada linha, verifica se ambos os assentos na linha (esquerda e direita) estão livres. Se sim, incrementa o contador de combinações possíveis.
    - **Verificação Vertical:** Para cada linha (exceto a última), verifica se o assento diretamente acima e o assento diretamente abaixo estão livres. Se sim, incrementa o contador de combinações possíveis.
4. **Retorno do Resultado:**
    
    ```python
    return seating
    ```
    
    - Retorna o número total de maneiras possíveis para 2 alunos se sentarem lado a lado.

---

### **Python Age Counting**

O desafio "Python Age Counting" do Coderbyte pode ser resolvido usando ou não a biblioteca `pandas`. O objetivo é contar quantas pessoas têm 50 anos ou mais a partir dos dados fornecidos por uma API. O dado retornado pela API é uma string no formato `age=<valor>`, e você deve calcular quantas dessas idades são 50 ou mais.

---

### **Solução Sem Usar Pandas:**

```python
import requests

def age_counting():
    result = requests.get('<https://coderbyte.com/api/challenges/json/age-counting>')
    response = result.json()["data"].split(",")
    count = 0
    for res in response:
        data = res.split("=")
        if data[0].strip() == 'age' and int(data[1]) >= 50:
            count += 1
    return count
```

### Explicação da Solução Sem Usar Pandas:

1. **Requisição à API:**
    - A função faz uma requisição HTTP GET para a URL da API que fornece os dados.
2. **Extração e Processamento dos Dados:**
    - Os dados são extraídos da resposta JSON e separados em uma lista de strings com base na vírgula.
3. **Contagem das Idades:**
    - Um loop percorre cada string na lista, divide a string para obter a idade e verifica se ela é 50 ou mais. Se for, o contador `count` é incrementado.
4. **Retorno da Contagem:**
    - O contador `count`, que representa o número de idades que são 50 ou mais, é retornado.
