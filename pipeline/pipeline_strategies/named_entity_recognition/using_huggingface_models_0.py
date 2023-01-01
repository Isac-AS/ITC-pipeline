from transformers import pipeline
from pipeline.pipeline_strategies.strategy import Strategy

class ClinicalAndGenericNER(Strategy):

    @classmethod
    def execute(cls, text: str) -> dict:
        """
        Concrete implementation of the named-entity recognition (NER) step in the pipeline. The 
        strategy here is to use some huggingface models.
        :param str text: The text to perform named-entity recognition on
        :return: The results of both the clinical and generic NER
        :rtype: dict
        """
        clinical_ner_result = cls.clinical_ner(text)
        generic_ner_result = cls.generic_ner(text)
        string_representation = cls.str_DISO(ner=clinical_ner_result, text=text) + cls.str_CHEM(ner=clinical_ner_result, text=text)
        return {"clinical": clinical_ner_result, "generic": generic_ner_result, "str": string_representation}

    @classmethod
    def clinical_ner(cls, text: str) -> list:
        """
        Clinical named-entity recognition model.
        Source: https://huggingface.co/lcampillos/roberta-es-clinical-trials-ner
        TAGS:
            ANAT: body parts and anatomy (e.g. garganta, 'throat')
            CHEM: chemical entities and pharmacological substances (e.g. aspirina,'aspirin')
            DISO: pathologic conditions (e.g. dolor, 'pain')
            PROC: diagnostic and therapeutic procedures, laboratory analyses and medical research activities (e.g. cirugía, 'surgery')
        :param str text: The text to perform named-entity recognition on
        :return: The result of the clinical named-entity recognition
        :rtype: list of dicts of the type: [{'entity': 'B-DISO', 'score': 0.998966, 'index': 8, 'word': 'Ġdolor', 'start': 40, 'end': 45}]
        """
        ner = pipeline(model = "lcampillos/roberta-es-clinical-trials-ner")
        return ner(text)
    
    @classmethod
    def generic_ner(cls, text: str) -> list:
        """
        Generic named-entity recognition model.
        Source: https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-ner
        :param str text: The text to perform named-entity recognition on
        :return: The result of the generic named-entity recognition
        :rtype: list of dicts such as [{'entity': 'B-PER', 'score': 0.9991167, 'index': 3, 'word': 'Juan', 'start': 13, 'end': 17}]
        """
        ner = pipeline(model = "mrm8488/bert-spanish-cased-finetuned-ner")
        return ner(text)

    def str_DISO(ner, text):
        pathologic_conditions = []
        for dictionary in ner:
            if dictionary["entity"] == "B-DISO":
                pathologic_conditions.append(text[dictionary["start"]:dictionary["end"]])
            if dictionary["entity"] == "I-DISO":
                pathologic_conditions[-1] += " " + (text[dictionary["start"]:dictionary["end"]])
        return f"\nPathologic conditions detected:\n{pathologic_conditions}"

    def str_CHEM(ner, text):
        chemical_entities = []
        for dictionary in ner:
            if dictionary["entity"] == "B-CHEM":
                chemical_entities.append(text[dictionary["start"]:dictionary["end"]])
            if dictionary["entity"] == "I-CHEM":
                chemical_entities[-1] += " " + (text[dictionary["start"]:dictionary["end"]])
        return f"\nChemical entities and pharmacological substances:\n{chemical_entities}"