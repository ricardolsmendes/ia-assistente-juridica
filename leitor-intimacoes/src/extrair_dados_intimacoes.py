import json
import sys

import dotenv

import leitor_intimacoes


if __name__ == "__main__":
    arquivo_intimacoes = sys.argv[1]
    familia_llm = sys.argv[2]

    with open(arquivo_intimacoes, "r") as f:
        intimacoes = json.load(f)

    dotenv.load_dotenv()

    leitor = leitor_intimacoes.LeitorIntimacoes(familia_llm)

    for indice_intimacao in [0, 2, 4, 8, 14]:
        intimacao = intimacoes.get("intimacoes")[indice_intimacao]

        intimacao_estruturada = {}
        intimacao_estruturada.update(leitor.extrair_data_disponibilizacao(intimacao))
        intimacao_estruturada.update(leitor.extrair_tribunal(intimacao))
        intimacao_estruturada.update(leitor.extrair_orgao(intimacao))
        intimacao_estruturada.update(leitor.extrair_vara(intimacao))
        intimacao_estruturada.update(leitor.extrair_determinacao_juiz(intimacao))
        intimacao_estruturada.update(leitor.extrair_prazo_inicial(intimacao))
        intimacao_estruturada.update(leitor.extrair_prazo_fatal(intimacao))

        print(
            json.dumps(
                intimacao_estruturada,
                indent=4,
                ensure_ascii=False,
            )
        )
