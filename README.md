# Speaker diarization with AssemblyAI-STT-3.7

Companion code for the AssemblyAI blog post
[What is speaker diarization and how does it work?](https://www.assemblyai.com/blog/what-is-speaker-diarization-and-how-does-it-work).

`diarize_file.py` transcribes a recorded file with `speech_models=["assemblyai-stt-3-7"]`
and `speaker_labels=True`, then prints each utterance with its speaker label.

## Run it

Requires Python 3.9+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ASSEMBLYAI_API_KEY=your_api_key_here
python diarize_file.py https://assembly.ai/wildfires.mp3 --min-speakers 2 --max-speakers 4
```

## Speaker-count options

- `--speakers N` sets `speakers_expected`. Use it only when you know the exact count.
- `--min-speakers` / `--max-speakers` set `speaker_options.min_speakers_expected` and
  `max_speakers_expected`. Both are hard boundaries: extra voices beyond the max are
  merged into existing labels, so leave a little headroom.

## Live audio

For streaming diarization with `assemblyai-stt-3-7-realtime`, see
[streaming-speaker-diarization-assemblyai](https://github.com/kelsey-aai/streaming-speaker-diarization-assemblyai).

## Pricing

AssemblyAI-STT-3.7 is $0.21/hr. Speaker diarization is a $0.02/hr add-on on pre-recorded audio.
See [pricing](https://www.assemblyai.com/pricing).
