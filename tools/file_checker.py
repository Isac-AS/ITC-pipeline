import glob
import time
import logging
from os import mkdir

def check_for_log_dir_and_file():
    """
    Will check for the logs subdirectory.
    If it doesn't exist, it will be created along with the log file.
    :return: Success in the checking
    :rtype: bool
    """
    if glob.glob('logs'):
        logging.basicConfig(filename="./logs/logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.INFO)
        return True
    try:
        mkdir("./logs")
        logging.basicConfig(filename="./logs/logs.txt", filemode="a" , format='%(asctime)s - [%(levelname)s]: %(message)s', level=logging.INFO)
        logging.info("Log files created successfully.")
        return True
    except Exception as e:
        logging.error("Problem with log file creation.")
        logging.error(e)
        return False

def check_for_output_subdirectory():
    """
    Will check for the pipeline output subdirectory.
    Will create it if it does not exist.
    :return: Success in the checking
    :rtype: bool
    """
    if glob.glob("pipeline_output"):
        return True
    try:
        mkdir("./pipeline_output")
        logging.info("Output subdirectory created successfully.")
        return True
    except Exception as e:
        logging.error()
        logging.error(e)
        return False

def get_current_output_subdirectory():
    """
    Will create the subdirectory in which the output for the pipeline excecution will be saved.
    This directory will be named after the moment of execution within a folder with the current
    date.
    :return: Output directory
    :rtype: String
    """
    current_time = time.localtime()
    date_dir = time.strftime("%Y-%m-%d", current_time)
    time_dir = time.strftime("%H-%M-%S", current_time)
    if not glob.glob(f"./pipeline_output/{date_dir}"):
        try:
            mkdir(f"./pipeline_output/{date_dir}")
        except Exception as e:
            logging.error("Problem creating date directory.")
            return None
    try:
        mkdir(f"./pipeline_output/{date_dir}/{time_dir}")
        return f"./pipeline_output/{date_dir}/{time_dir}"
    except Exception as e:
        logging.error("Problem with output dir creation.")
        logging.error(e)
        return None

def check_files():
    """
    Will call all the defined functions
    """
    if not check_for_log_dir_and_file() and not check_for_output_subdirectory():
        logging.error("Problem with the file check! Cannot procede.")
        return None
    current_output_dir = get_current_output_subdirectory()
    if current_output_dir is None:
        logging.error("Could not create current output directory.")
        return None
    logging.info("Files checked successfully.")
    return current_output_dir