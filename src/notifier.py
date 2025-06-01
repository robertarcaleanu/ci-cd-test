import logging


class Notifier:
    def __init__(self, process_name: str):
        self.process = process_name

    def send_email_notification(self):
        # LOGIC TO SEND EMAIL NOTIFICATION
        pass

    def send_slack_notification(self):
        # LOGIC TO SEND SLACK NOTIFICATION
        pass

    def send_custom_notification(self):
        # LOGIC TO SEND CUSTOM NOTIFICATION 
        pass

    def print_console_message(self):
        logging.error(f"{self.process} process failed!")