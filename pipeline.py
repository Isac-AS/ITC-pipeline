from file_checker import check_files
from record_audio import record_sample
from speech_to_text import transcribe
import logging

def record_audio():
    duration = input("Numero de segundos: ")
    return record_sample(int(duration), current_output_dir)

if __name__ == "__main__":
    current_output_dir = check_files()

    if current_output_dir is None:
        logging.error("Exiting program due to file checking error.")
        exit(1)

    if input("¿Realizar grabación? (y/n): ") == "y":
        if not record_audio():
            exit(1)
    
        transcription = transcribe(current_output_dir)
        print(f"\nTranscription:\n{transcription}")

    