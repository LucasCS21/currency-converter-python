# currency-converter-python

# 💱 Conversor de Moedas

Aplicação em Python que realiza conversão entre diferentes moedas utilizando uma API de câmbio em tempo real.

O objetivo deste projeto é praticar consumo de APIs REST, requisições HTTP, manipulação de dados JSON e boas práticas de desenvolvimento em Python.

---

## ✨ Funcionalidades

- Conversão entre diversas moedas.
- Taxas de câmbio atualizadas em tempo real.
- Entrada de valor, moeda de origem e moeda de destino.
- Tratamento de erros para requisições e entradas inválidas.

---

## 🛠️ Tecnologias

- Python 3
- Requests
- ExchangeRate-API

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/LucasCS21/currency-converter-python.git
cd currency-converter-python
```

Instale as dependências:

```bash
pip install requests
```

---

## 🔑 Configuração

Obtenha uma chave gratuita na ExchangeRate-API.

No PowerShell:

```powershell
$env:API_KEY="sua_chave_aqui"
```

---

## ▶️ Como executar

```bash
python main.py
```

Exemplo de uso:

```
Digite o valor: 100
Moeda de origem: USD
Moeda de destino: BRL

100.00 USD = 548.30 BRL
```

---

## 📚 Conceitos praticados

- Consumo de APIs REST
- Requisições HTTP
- Manipulação de JSON
- Variáveis de ambiente
- Tratamento de exceções
- Organização de código em Python
