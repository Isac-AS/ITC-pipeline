# Clinical ner
# https://huggingface.co/lcampillos/roberta-es-clinical-trials-ner
"""
TAGS:
    ANAT: body parts and anatomy (e.g. garganta, 'throat')
    CHEM: chemical entities and pharmacological substances (e.g. aspirina,'aspirin')
    DISO: pathologic conditions (e.g. dolor, 'pain')
    PROC: diagnostic and therapeutic procedures, laboratory analyses and medical research activities (e.g. cirugía, 'surgery')
"""

#https://huggingface.co/mrm8488/bert-spanish-cased-finetuned-ner

from transformers import pipeline

def drug_ner(text):
    ner = pipeline(model = "lcampillos/roberta-es-clinical-trials-ner")
    return ner(text)

def generic_ner(text):
    ner = pipeline(model = "mrm8488/bert-spanish-cased-finetuned-ner")
    return ner(text)

