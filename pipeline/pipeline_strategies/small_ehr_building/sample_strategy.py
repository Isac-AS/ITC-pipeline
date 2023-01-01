from pipeline.pipeline_strategies.strategy import Strategy

class SampleEHRBuildStrategy(Strategy):

    @classmethod
    def execute(cls, dependency_parsing, ner):
        return "Placeholder"
