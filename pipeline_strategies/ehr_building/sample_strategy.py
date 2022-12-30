from pipeline_strategies.strategy import Strategy

class SampleEHRBuildStrategy(Strategy):
    name = "Self made HL7 buid algorithm"
    id = 0

    @classmethod
    def execute(cls, dependency_parsing, ner):
        return "String"
