from pipeline.granular_strategy_runner import GranularStrategyRunner
from pipeline.tools.text_file_handler import TextFileHandler

if __name__ == "__main__":

    strategy_types = {
        "s2t": "speech_to_text",
        "spell" : "spell_checking",
        "nlp" : "large_ehr_building"
    }

    recording_path = "pipeline_output\\2023-01-01\\16-34-44\\recording.wav"
    transcription = GranularStrategyRunner.runStrategy(strategy_types["s2t"], "using_whisper_0", recording_path)
    print(transcription)

    """transcription_path = "pipeline_output\\2023-01-01\\13-12-53\\transcription.txt"
    text = TextFileHandler.read_text_file(transcription_path)
    result = GranularStrategyRunner.runStrategy(strategy_types["spell"], "using_pyspellchecker_0", text)
    print(result)"""



