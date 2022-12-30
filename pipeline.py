from context import Context
from tools.text_file_handler import TextFileHandler

class Pipeline:

    context = None

    def __init__(self):
        self.context = Context()
    
    def run_pipeline(self, output_path: str, verbose: bool, write_all_steps: bool):
        transcription: str = self.context.execute_speech_to_text_strategy(output_path)
        spell_checked_transcription: str = self.context.execute_spell_check_strategy(transcription)
        dependency_parsing = self.context.execute_dependency_parsing_strategy(spell_checked_transcription)
        named_entity_recognition = self.context.execute_named_entity_recognition_strategy(spell_checked_transcription)
        ehr_output = self.context.execute_electronic_health_record_builder_strategy(dependency_parsing, named_entity_recognition)

        if verbose:
            print(f"\nTranscription:\n{transcription}")
            print(f"\nSpell_checked_transcription:\n{spell_checked_transcription}")
            print(f"\nDependency parsing:\n{[(t.text, t.dep_, t.head.text) for t in dependency_parsing]}\n")
            print(f"\nNamed-entity recognition:\n{named_entity_recognition['str']}")
            print(f"\nElectronic Health Record:\n{ehr_output}")
        
        if write_all_steps:
            dp_output = f"\nDependency parsing:\n{[(t.text, t.dep_, t.head.text) for t in dependency_parsing]}\n"
            TextFileHandler.write_to_text_file(output_path, "dependency_parsing", dp_output)
            TextFileHandler.write_to_text_file(output_path, "named_entity_recognition", named_entity_recognition["str"])

        TextFileHandler.write_to_text_file(output_path, "transcription", spell_checked_transcription)
        TextFileHandler.write_to_text_file(output_path, "spell_checked_transcription", spell_checked_transcription)
        TextFileHandler.write_to_text_file(output_path, "electronic_health_record", ehr_output)
        