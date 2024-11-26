import json
import sys

import dotenv

import leitor_intimacoes

if __name__ == "__main__":
    dotenv.load_dotenv()

    arquivo_intimacoes = sys.argv[1]
    familia_llm = sys.argv[2]

    with open(arquivo_intimacoes, "r") as f:
        intimacoes = json.load(f)

    leitor = leitor_intimacoes.LeitorIntimacoes(familia_llm)

    for indice_intimacao in [0, 2, 4, 8, 14]:
        dados = intimacoes.get("intimacoes")[indice_intimacao]

        dados_estruturados = {}
        dados_estruturados.update(leitor.extrair_data_disponibilizacao(dados))
        dados_estruturados.update(leitor.extrair_tribunal(dados))
        dados_estruturados.update(leitor.extrair_orgao(dados))
        dados_estruturados.update(leitor.extrair_vara(dados))
        dados_estruturados.update(leitor.extrair_determinacao_juiz(dados))
        dados_estruturados.update(leitor.extrair_prazo_inicial(dados))
        dados_estruturados.update(leitor.extrair_prazo_fatal(dados))

        print(
            json.dumps(
                dados_estruturados,
                indent=4,
                ensure_ascii=False,
            )
        )
