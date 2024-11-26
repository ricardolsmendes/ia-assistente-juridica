import json
import os
import sys
import time

import deepgram
import dotenv
import httpx


def transcrever(nome_arquivo_audio: str) -> str:
    # PASSO 1: Cria um cliente Deepgram usando a chave da API disponível nas variáveis
    # de ambiente.
    dg_client = deepgram.DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

    # PASSO 2: Chama o transcribe_file para a audiência pré-gravada.
    with open(nome_arquivo_audio, "rb") as arquivo_audio:
        dados_buffer = arquivo_audio.read()

    payload: deepgram.FileSource = {
        "buffer": dados_buffer,
    }

    opcoes = deepgram.PrerecordedOptions(
        diarize=True, language="pt", model="whisper", smart_format=True, utterances=True
    )

    resposta = dg_client.listen.prerecorded.v("1").transcribe_file(
        payload, opcoes, timeout=httpx.Timeout(300.0, connect=10.0)
    )

    nome_arquivo_resultados = f"{nome_arquivo_audio[:-4]}-whisper.json"
    with open(nome_arquivo_resultados, "w", encoding="utf-8") as arquivo_resultados:
        arquivo_resultados.write(resposta.to_json(ensure_ascii=False, indent=4))

    return nome_arquivo_resultados


def formatar_marcacao_tempo(segundos: float):
    return time.strftime("%H:%M:%S", time.gmtime(segundos))


if __name__ == "__main__":
    dotenv.load_dotenv()

    nome_arquivo_transcricao = transcrever(sys.argv[1])
    with open(nome_arquivo_transcricao, "rb") as arquivo_transcricao:
        transcricao = json.loads(arquivo_transcricao.read())

    speaker_atual = None
    inicio_transcricao_atual = None
    transcricao_atual = ""
    nome_arquivo_texto = f"{nome_arquivo_transcricao[:-5]}-fmt.txt"
    with open(nome_arquivo_texto, "w") as arquivo_texto:
        for fala in transcricao["results"]["utterances"]:
            speaker_itr = fala["speaker"]

            if speaker_atual is not None and speaker_itr != speaker_atual:
                arquivo_texto.write(
                    f"\n\n"
                    f"[falante {speaker_atual},"
                    f" {formatar_marcacao_tempo(inicio_transcricao_atual)}]:"
                    f"\n"
                )
                arquivo_texto.write(transcricao_atual)

                inicio_transcricao_atual = None
                transcricao_atual = ""

            if not inicio_transcricao_atual:
                speaker_atual = speaker_itr
                inicio_transcricao_atual = fala["start"]

            transcricao_atual = f"{transcricao_atual} {fala['transcript']}"

        arquivo_texto.write(
            f"\n\n"
            f"[speaker {speaker_atual},"
            f" {formatar_marcacao_tempo(inicio_transcricao_atual)}]:"
            f"\n"
        )
        arquivo_texto.write(transcricao_atual)
