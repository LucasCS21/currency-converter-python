import os
import requests


# ==============================
# Configuração da API
# ==============================

API_KEY = os.getenv("API_KEY")

BASE_URL = (
    f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"
)


# ==============================
# Função para buscar as taxas
# ==============================

def buscar_taxas(moeda_origem):
    """
    Consulta a API de câmbio e retorna
    as taxas disponíveis para a moeda de origem.
    """

    url = BASE_URL + moeda_origem.upper()

    try:
        resposta = requests.get(url, timeout=10)

        # Verifica se houve erro HTTP
        resposta.raise_for_status()

        dados = resposta.json()

        # Verifica se a API retornou sucesso
        if dados.get("result") != "success":
            print("\nErro retornado pela API.")
            return None

        return dados["conversion_rates"]

    except requests.exceptions.Timeout:
        print("\nTempo de resposta da API excedido.")
        return None

    except requests.exceptions.ConnectionError:
        print("\nErro de conexão com a internet.")
        return None

    except requests.exceptions.HTTPError:
        print("\nErro HTTP ao acessar a API.")
        return None

    except KeyError:
        print("\nFormato inesperado de resposta da API.")
        return None


# ==============================
# Função de conversão
# ==============================

def converter(valor, origem, destino):
    """
    Realiza o cálculo da conversão.
    """

    taxas = buscar_taxas(origem)

    if taxas is None:
        return

    destino = destino.upper()

    if destino not in taxas:
        print("\nMoeda de destino não encontrada.")
        return

    taxa = taxas[destino]

    resultado = valor * taxa

    print("\n==============================")
    print("Resultado da conversão")
    print("==============================")
    print(
        f"{valor:.2f} {origem.upper()} = "
        f"{resultado:.2f} {destino}"
    )


# ==============================
# Função principal
# ==============================

def main():

    print("==============================")
    print("      Conversor de Moedas")
    print("==============================")


    # Verifica se a chave existe
    if not API_KEY:
        print(
            "\nERRO: API_KEY não encontrada."
            "\nConfigure a variável de ambiente antes de executar."
        )
        return


    try:

        valor = float(
            input("\nDigite o valor: ")
        )

        origem = input(
            "Digite a moeda de origem (ex: USD): "
        )

        destino = input(
            "Digite a moeda de destino (ex: BRL): "
        )


        if valor <= 0:
            print("\nO valor deve ser maior que zero.")
            return


        converter(
            valor,
            origem,
            destino
        )


    except ValueError:
        print("\nDigite um número válido.")



# ==============================
# Ponto de entrada do programa
# ==============================

if __name__ == "__main__":
    main()
