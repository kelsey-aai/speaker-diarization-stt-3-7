"""Speaker diarization on a recorded file with AssemblyAI-STT-3.7.

Usage:
    export ASSEMBLYAI_API_KEY=your_api_key_here
    python diarize_file.py https://assembly.ai/wildfires.mp3 --min-speakers 2 --max-speakers 4
"""
import argparse
import os
import sys

from assemblyai import SpeakerOptions
from assemblyai.prerecorded.v2 import Transcriber, TranscriptionConfig


def build_config(min_speakers=None, max_speakers=None, exact=None):
    if exact is not None:
        # Only when you know the exact count. It is a hard boundary, not a hint.
        return TranscriptionConfig(
            speech_models=["assemblyai-stt-3-7"],
            speaker_labels=True,
            speakers_expected=exact,
        )
    options = None
    if min_speakers is not None or max_speakers is not None:
        options = SpeakerOptions(
            min_speakers_expected=min_speakers,
            max_speakers_expected=max_speakers,
        )
    return TranscriptionConfig(
        speech_models=["assemblyai-stt-3-7"],
        speaker_labels=True,
        speaker_options=options,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", help="Local path or public URL")
    parser.add_argument("--min-speakers", type=int)
    parser.add_argument("--max-speakers", type=int)
    parser.add_argument("--speakers", type=int, help="Exact speaker count, if known")
    args = parser.parse_args()

    api_key = os.environ.get("ASSEMBLYAI_API_KEY")
    if not api_key:
        sys.exit("Set ASSEMBLYAI_API_KEY first.")

    config = build_config(args.min_speakers, args.max_speakers, args.speakers)
    transcript = Transcriber(api_key=api_key, config=config).transcribe(args.audio)

    if transcript.status == "error":
        sys.exit(f"Transcription failed: {transcript.error}")

    print(f"Model used: {transcript.speech_model_used}")
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")


if __name__ == "__main__":
    main()
