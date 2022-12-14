from pipeline.pipeline_strategies.strategy import Strategy
from pipeline.tools.strategy_navigator import StrategyNavigator

class Context:
    """
    Defines the interface of interest to clients.
    Mantains references to the different Strategy objects for
    the different steps in the pipeline.
    """

    def __init__(self,
                speech_to_text_strategy = StrategyNavigator.get_concrete_strategy_class("speech_to_text", "using_whisper_0"),
                spell_check_strategy = StrategyNavigator.get_concrete_strategy_class("spell_checking", "using_pyspellchecker_0"),
                dependecy_parsing_strategy = StrategyNavigator.get_concrete_strategy_class("dependency_parsing", "using_spacy_0"),
                named_entity_recognition_strategy = StrategyNavigator.get_concrete_strategy_class("named_entity_recognition", "using_huggingface_models_0"),
                small_electronic_health_record_builder_strategy = StrategyNavigator.get_concrete_strategy_class("small_ehr_building", "sample_strategy"),
                large_electronic_health_record_builder_strategy = StrategyNavigator.get_concrete_strategy_class("large_ehr_building", "default_adt_a01")
                ):
        self.speech_to_text_strategy = speech_to_text_strategy
        self.spell_check_strategy = spell_check_strategy
        self.dependecy_parsing_strategy = dependecy_parsing_strategy
        self.named_entity_recognition_strategy = named_entity_recognition_strategy
        self.small_electronic_health_record_builder_strategy = small_electronic_health_record_builder_strategy
        self.large_electronic_health_record_builder_strategy = large_electronic_health_record_builder_strategy
    
    def set_speech_to_text_strategy(self,speech_to_text_strategy):
        self.speech_to_text_strategy = speech_to_text_strategy

    def set_spell_check_strategy(self, spell_check_strategy):
        self.spell_check_strategy = spell_check_strategy

    def set_dependency_parsing_strategy(self, dependecy_parsing_strategy):
        self.dependecy_parsing_strategy = dependecy_parsing_strategy

    def set_named_entity_recognition_strategy(self, named_entity_recognition_strategy):
        self.named_entity_recognition_strategy = named_entity_recognition_strategy

    def set_small_electronic_health_record_builder_strategy(self, small_electronic_health_record_builder_strategy):
        self.small_electronic_health_record_builder_strategy = small_electronic_health_record_builder_strategy

    def set_large_electronic_health_record_builder_strategy(self, large_electronic_health_record_builder_strategy):
        self.large_electronic_health_record_builder_strategy = large_electronic_health_record_builder_strategy

    def execute_speech_to_text_strategy(self, recording_path: str) -> str:
        return self.speech_to_text_strategy.execute(recording_path)

    def execute_spell_check_strategy(self, text: str) -> str:
        return self.spell_check_strategy.execute(text)

    def execute_dependency_parsing_strategy(self, text: str):
        return self.dependecy_parsing_strategy.execute(text)

    def execute_named_entity_recognition_strategy(self, text: str):
        return self.named_entity_recognition_strategy.execute(text)

    def execute_small_electronic_health_record_builder_strategy(self, dependency_parsing, ner):
        return self.small_electronic_health_record_builder_strategy.execute(dependency_parsing, ner)

    def execute_large_electronic_health_record_builder_strategy(self, text: str):
        return self.large_electronic_health_record_builder_strategy.execute(text)
        