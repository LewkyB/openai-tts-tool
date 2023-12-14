# OpenAI Text-to-Speech Conversion Tool

## Overview

Python script for converting text files to MP3 speech with OpenAI's TTS API. 

### Cost

  `tts-1-hd` - 11 requests (approx. 4096 chars each) cost $1.32.

  `tts-1` - 7 requests (approx. 4096 chars each) cost $0.52. 

So far it doesn't seem like `tts-1-hd` is worth the extra cost.

## Setup Instructions

### Installation

  1. `python -m venv openai-tts-tool`
  2. `source env_name/bin/activate` or `.\openai-tts-tool\Scripts\Activate.ps1`
  3. `pip install pydub openai`

### Usage

  `python src/text_to_speech.py <path_to_text_file> <output_directory>`

### Convert EPUB to TXT

`winget install pandoc`
`sudo apt install pandoc`
`brew install pandoc`

`pandoc book.epub -o book.txt`

## Documentation

https://platform.openai.com/docs/guides/text-to-speech
