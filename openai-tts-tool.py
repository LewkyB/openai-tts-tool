import sys
import os
from pydub import AudioSegment
from openai import OpenAI

def read_in_chunks(file_path, chunk_size=4096):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

def main(file_path, output_directory):
    # Check if the text file exists and is readable
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist or is not readable.")
        sys.exit(1)

    # Check if the output directory exists
    if not os.path.isdir(output_directory):
        print(f"Error: The output directory '{output_directory}' does not exist.")
        sys.exit(1)

    client = OpenAI(api_key="api-key-here")
    temp_output_filenames = []

    for i, chunk in enumerate(read_in_chunks(file_path), start=1):
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=chunk
        )

        temp_output_filename = os.path.join(output_directory, f"output{i}.mp3")
        response.stream_to_file(temp_output_filename)
        print(f"Chunk {i} processed and saved as {temp_output_filename}")

        temp_output_filenames.append(temp_output_filename)

    # Combine all the individual audio files after processing all chunks
    combined_audio = AudioSegment.empty()
    output_file = os.path.join(output_directory, 'combined_output.mp3')
    for filename in temp_output_filenames:
        sound = AudioSegment.from_mp3(filename)
        combined_audio += sound

    # Export the combined audio to a new MP3 file
    combined_audio.export(output_file, format="mp3")
    print(f"Combined audio file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <path_to_text_file> <output_directory>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
