# 🧮 Calculadora Científica Python

Calculadora científica web com backend Python/Flask e frontend HTML/CSS/JavaScript. Processa todas as operações matemáticas no servidor Python.

## 📋 Características

### Operações Básicas
- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 📊 Porcentagem (ex: 10% de 298 = 29.8)

### Funções Científicas
- √ Raiz quadrada
- 📐 Seno (em graus)
- 📐 Cosseno (em graus)
- 📐 Tangente (em graus)

### Recursos
- ✅ Backend Python/Flask para processamento dos cálculos
- ✅ Interface responsiva e moderna
- ✅ Suporte a teclado
- ✅ Tema claro/escuro automático
- ✅ Validação de erros (divisão por zero, raiz negativa, etc.)
- ✅ Indicador de carregamento durante cálculos
- ✅ Tratamento de erros de conexão

## 🛠️ Tecnologias

- **Backend**: Python 3.13 + Flask 3.1.2
- **Frontend**: HTML5 + CSS3 + JavaScript (ES6+)
- **Arquitetura**: Cliente-servidor com API REST

## 📁 Estrutura do Projeto

```
Calculadora Python/
├── app.py              # Backend Flask (servidor Python)
├── requirements.txt    # Dependências Python
├── README.md          # Este arquivo
└── templates/
    └── index.html     # Frontend (interface)
```

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.13+ instalado
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone ou baixe o projeto**
   ```bash
   cd "C:\Users\José\Downloads\Calculadora Python"
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
   
   Ou instale manualmente:
   ```bash
   pip install flask
   ```

5. **Execute o servidor**
   ```bash
   py app.py
   ```
   
   Ou:
   ```bash
   python app.py
   ```

6. **Acesse no navegador**
   ```
   http://localhost:5000
   ```
   
   Ou:
   ```
   http://127.0.0.1:5000
   ```

## 🎮 Como Usar

### Operações Básicas
1. Digite o primeiro número
2. Pressione um operador (+, −, ×, /)
3. Digite o segundo número
4. Pressione **=** para ver o resultado

### Porcentagem
1. Digite o valor base (ex: 298)
2. Pressione qualquer operador
3. Digite a porcentagem (ex: 10)
4. Pressione **%**
5. Resultado: 29.8 (10% de 298)

### Funções Científicas
1. Digite um número
2. Pressione **√**, **sin**, **cos** ou **tan**
3. O resultado aparece imediatamente

### Atalhos de Teclado
- **0-9**: Números
- **.**: Ponto decimal
- **+, -, *, /**: Operadores
- **Enter** ou **=**: Calcular
- **Backspace**: Apagar último caractere
- **Escape** ou **C**: Limpar tudo

## 📡 API Endpoints

### `GET /`
Retorna a interface HTML da calculadora.

### `POST /calculate`
Processa operações matemáticas.

**Corpo da requisição (JSON):**
```json
{
  "operation": "add|subtract|multiply|divide|percentage|sqrt|sin|cos|tan",
  "value1": 10,
  "value2": 5
}
```

**Resposta de sucesso:**
```json
{
  "result": 15
}
```

**Resposta de erro:**
```json
{
  "error": "Divisão por zero"
}
```

## 🔧 Solução de Problemas

### "ModuleNotFoundError: No module named 'flask'"
**Solução:** Instale o Flask:
```bash
pip install flask
```

### Comando `python` não funciona
**Solução:** Use `py` ao invés de `python`:
```bash
py app.py
```

### Servidor não inicia
**Solução:** Verifique se a porta 5000 está disponível:
```bash
netstat -ano | findstr :5000
```

### Erro de conexão no frontend
**Solução:** 
1. Verifique se o servidor está rodando
2. Confirme que está acessando `http://localhost:5000`
3. Verifique o console do navegador (F12) para erros

## 📝 Notas Técnicas

### Cálculo de Porcentagem
A operação `percentage` calcula: `(value1 × value2) / 100`

Exemplo: 
- Input: value1=298, value2=10
- Cálculo: (298 × 10) / 100
- Output: 29.8

### Funções Trigonométricas
- Todas as funções trigonométricas usam **graus**, não radianos
- Conversão interna: `math.radians(valor)` antes do cálculo

### Precisão
- Resultados são arredondados para 10 casas decimais
- Evita erros de ponto flutuante do tipo `0.30000000000000004`

## 🐛 Validações Implementadas

- ✅ Divisão por zero (operações `/` e `%`)
- ✅ Raiz quadrada de número negativo
- ✅ Valores inválidos (não numéricos)
- ✅ Operações inválidas
- ✅ Erros de conexão com o servidor

## 🎨 Personalização

### Alterar Porta do Servidor
Edite `app.py`, linha final:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Mude 5000 para 8080
```

### Alterar Cores
Edite as variáveis CSS em `templates/index.html`:
```css
:root {
    --color-primary: #21808d;  /* Cor primária */
    --color-background: #fcfcf9;  /* Cor de fundo */
    /* ... */
}
```

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

## 👨‍💻 Autor

Desenvolvido como projeto de calculadora científica com arquitetura cliente-servidor.

## 🆘 Suporte

Em caso de problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que o Python 3.13+ está instalado
3. Certifique-se de que a pasta `templates/` existe com `index.html` dentro
4. Use `py app.py` ao invés de `python app.py` no Windows

---

**Versão**: 1.0  
**Data**: Outubro 2025  
**Python**: 3.13+  
**Flask**: 3.1.2
