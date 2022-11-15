import logging
import whisper

def transcribe(path):
    try:
        model = whisper.load_model("medium")
        result = model.transcribe(f"{path}/recording.wav")
        logging.info("Finished transcribing.")

        with open(f"{path}/transcription.txt", "w", encoding="utf-8") as f:
            f.write(result["text"])
        logging.info("Finished writing transcription to file.")
        
    except Exception as e:
        logging.error("Error while attempting transcription.")
        logging.error(e)
    return result["text"]
