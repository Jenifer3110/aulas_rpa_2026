import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("execucao_bot.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def processar_arquivo(caminho: str):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                logging.info("Linha lida: %s", linha)

    except FileNotFoundError:
        logging.error("Arquivo não encontrado: %s", caminho)

    finally:
        logging.info("Término da tentativa de processamento.")


if __name__ == "__main__":
    processar_arquivo("AULA04/transacoes.csv")