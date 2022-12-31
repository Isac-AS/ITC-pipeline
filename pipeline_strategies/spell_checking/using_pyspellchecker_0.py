from pipeline_strategies.strategy import Strategy
from spellchecker import SpellChecker

class UsingPySpellChecker(Strategy):
    
    @classmethod
    def execute(cls, text: str) -> str:
        """
        Implementation of the spell checking part of the pipeline using the
        pyspellchecker library.

        :param text: Text to perform the spell checking on
        :type text: str
        :return: Spell checked text
        :rtype: str
        """
        spanish_spell_checker = SpellChecker(language="es")
        spell_checked_text = " ".join([spanish_spell_checker.correction(token) for token in text.split()])
        return spell_checked_text
