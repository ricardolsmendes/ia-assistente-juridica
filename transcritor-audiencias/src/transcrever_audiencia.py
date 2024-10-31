import json
import os
import sys
import time

import deepgram
import dotenv
import httpx

dotenv.load_dotenv()


def transcribe(audio_file_name: str) -> str:
    # STEP 1 Create a Deepgram client using the API key in the environment variables
    dg_client = deepgram.DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

    # STEP 2 Call the transcribe_file method on the prerecorded class
    with open(audio_file_name, "rb") as audio_file:
        buffer_data = audio_file.read()

    payload: deepgram.FileSource = {
        "buffer": buffer_data,
    }

    options = deepgram.PrerecordedOptions(
        diarize=True, language="pt", model="whisper", smart_format=True, utterances=True
    )

    response = dg_client.listen.prerecorded.v("1").transcribe_file(
        payload, options, timeout=httpx.Timeout(300.0, connect=10.0)
    )

    results_file_name = f"{audio_file_name[:-4]}-whisper.json"
    with open(results_file_name, "w", encoding="utf-8") as results_file:
        results_file.write(response.to_json(ensure_ascii=False, indent=4))

    return results_file_name


def convert_time(seconds: float):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


if __name__ == "__main__":
    transcript_file_name = transcribe(sys.argv[1])
    with open(transcript_file_name, "rb") as transcript_file:
        transcript = json.loads(transcript_file.read())

    current_speaker = None
    current_transcript_start = None
    current_transcript = ""
    text_file_name = f"{transcript_file_name[:-5]}-fmt.txt"
    with open(text_file_name, "w") as text_file:
        for utterance in transcript["results"]["utterances"]:
            itr_speaker = utterance["speaker"]

            if current_speaker is not None and itr_speaker != current_speaker:
                text_file.write(
                    f"\n\n"
                    f"[speaker {current_speaker},"
                    f" {convert_time(current_transcript_start)}]:"
                    f"\n"
                )
                text_file.write(current_transcript)

                current_transcript_start = None
                current_transcript = ""

            if not current_transcript_start:
                current_speaker = itr_speaker
                current_transcript_start = utterance["start"]

            current_transcript = f"{current_transcript} {utterance['transcript']}"

        text_file.write(
            f"\n\n"
            f"[speaker {current_speaker},"
            f" {convert_time(current_transcript_start)}]:"
            f"\n"
        )
        text_file.write(current_transcript)
