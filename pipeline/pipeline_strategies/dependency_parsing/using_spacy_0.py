from pipeline.pipeline_strategies.strategy import Strategy
import spacy

class SpacyDependencyParsing(Strategy):
    
    @classmethod
    def execute(cls, text: str):
        """
        Concrete implementation of the dependency parsing strategy. 
        In this case the approach is to use spacy's processing of a text, which 
        already performs a dependency parsing.

        :param text: The text to perform the dependency parsing on
        :type text: str
        :return: Spacy type doc as commented above
        :rtype: spacy doc
        """
        nlp = spacy.load("es_dep_news_trf")
        doc = nlp(text)
        return doc
        