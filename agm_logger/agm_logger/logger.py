import datetime
import os

import logging


class Logger:

    def __init__(self, filename):
        self.filename = filename

        # Create log file
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w"):
            pass

        # Set up logger
        logging.basicConfig(
            filename=filename,
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(name)s %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def log(self, log_type, log_data: str):
        """
        Print the log at the output and write it to the log file
        """

        if type(log_type) is not str:
            raise TypeError(f"Argument 'log_type' has wrong type: '{type(log_type)}'. Type must be 'str'.")
        if type(log_data) is not str:
            raise TypeError(f"Argument 'log_data' has wrong type: '{type(log_type)}'. Type must be 'str'.")

        # Print log to the output
        print(datetime.datetime.now(), log_data)

        # Add log to the log file
        if log_type == 'info':
            self.logger.info(log_data)
        elif log_type == 'warn':
            self.logger.warning(log_data)
        elif log_type == 'err':
            self.logger.error(log_data)
        else:
            raise ValueError(
                f"Argument 'log_type' has wrong value: '{log_type}'. Value must be: 'info', 'warn' or 'err'.")
