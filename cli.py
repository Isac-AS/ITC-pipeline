from pipeline.tools.file_checker import FileChecker
from pipeline.tools.record_audio import record_sample
from pipeline.pipeline import Pipeline
import logging

from pipeline.tools.strategy_navigator import StrategyNavigator

def record_audio():
    duration = input("Numero de segundos: ")
    print("Grabando audio...")
    return record_sample(int(duration), current_output_dir)
    
if __name__ == "__main__":
    current_output_dir = FileChecker.check_files()

    if current_output_dir is None:
        logging.error("Exiting program due to file checking error.")
        exit(1)

    if input("¿Realizar grabación? (y/n): ") == "y":
        if not record_audio():
            exit(1)
    
        if input("¿Pipeline de 3 pasos? (y/n): ") == "y":
            pipeline_type = True
        else : pipeline_type = False

        show_pipeline_outputs = False
        if input("¿Mostrar resultados por consola? (y/n): ") == "y":
            show_pipeline_outputs = True
        pipeline = Pipeline()
        if pipeline_type:
            pipeline.run_3_step_pipeline(output_path=current_output_dir, verbose=show_pipeline_outputs)
        else: 
            write_pipeline_outputs = False
            if input("¿Guardar resultados? (y/n): ") == "y":
                write_pipeline_outputs = True
            pipeline.run_5_step_pipeline(output_path=current_output_dir, verbose=show_pipeline_outputs, write_all_steps=write_pipeline_outputs)
    