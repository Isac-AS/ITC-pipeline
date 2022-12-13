import logging
import whisper

def transcribe(path):
    try:
        logging.info("Starting transcription...")
        model = whisper.load_model("medium")
        result = model.transcribe(f"{path}/recording.wav")
        logging.info("Finished transcribing.")

        with open(f"{path}/transcription.txt", "w", encoding="utf-8") as f:
            f.write(result["text"])
        logging.info("Finished writing transcription to file.")
        return result["text"]
        
    except Exception as e:
        logging.error("Error while attempting transcription.")
        logging.error(e)
        return "Error durante la transcripción."
