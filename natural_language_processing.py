import spacy
from ner_temp_module import drug_ner, generic_ner
from unidecode import unidecode


def print_DISO(ner, text):
    print("\nPathologic conditions detected:")
    pathologic_conditions = []
    for dictionary in ner:
        if dictionary["entity"] == "B-DISO":
            pathologic_conditions.append(text[dictionary["start"]:dictionary["end"]])
        if dictionary["entity"] == "I-DISO":
            pathologic_conditions[-1] += " " + (text[dictionary["start"]:dictionary["end"]])
    print(pathologic_conditions)
    return None

def print_CHEM(ner, text):
    print("\nChemical entities and pharmacological substances:\n")
    chemical_entities = []
    for dictionary in ner:
        if dictionary["entity"] == "B-CHEM":
            chemical_entities.append(text[dictionary["start"]:dictionary["end"]])
        if dictionary["entity"] == "I-CHEM":
            chemical_entities[-1] += " " + (text[dictionary["start"]:dictionary["end"]])
    print(chemical_entities)
    return None

if __name__ == "__main__":
    nlp = spacy.load("es_dep_news_trf")
    # Some transcription to work with as an example text
    path = "pipeline_output\\2022-12-13\\17-43-52\\transcription.txt"
    with open(path, encoding="utf-8") as f:
        text = f.read()
        print(f"Raw transcription:\n{text}")
        """text = unidecode(text)
        print(f"Processed transcription:\n{text}")"""
        doc = nlp(text)
        clinical_ner = drug_ner(text)
        general_ner = generic_ner(text)
        print(f"Clinical NER:\n{clinical_ner}\n")
        print_DISO(clinical_ner, text)
        print_CHEM(clinical_ner, text)
        print(f"\n\nGeneric NER:\n{general_ner}\n")
        print(f"Dependency parsing:\n{[(t.text, t.dep_, t.head.text) for t in doc]}\n")
