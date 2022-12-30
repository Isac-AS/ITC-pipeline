from tools.file_checker import check_files
from tools.record_audio import record_sample
from pipeline import Pipeline
import logging

from tools.strategy_navigator import StrategyNavigator

def record_audio():
    duration = input("Numero de segundos: ")
    return record_sample(int(duration), current_output_dir)

def temp_decision_tree():
    if input("¿Realizar grabación? (y/n): ") == "y":
        if not record_audio():
            exit(1)
    
if __name__ == "__main__":
    current_output_dir = check_files()

    if current_output_dir is None:
        logging.error("Exiting program due to file checking error.")
        exit(1)

    if input("¿Realizar grabación? (y/n): ") == "y":
        if not record_audio():
            exit(1)
    
    show_pipeline_outputs = False
    write_pipeline_outputs = False
    if input("¿Mostrar resultados? (y/n): ") == "y":
        show_pipeline_outputs = True
    if input("¿Guardar resultados? (y/n): ") == "y":
        write_pipeline_outputs = True
    pipeline = Pipeline()
    pipeline.run_pipeline(output_path=current_output_dir,verbose=show_pipeline_outputs, write_all_steps=write_pipeline_outputs)
    