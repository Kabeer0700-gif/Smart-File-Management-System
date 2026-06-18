from datetime import datetime

class Logger:
    def __init__(self):
        self.log_file = "app.log"

    def log(self,level,message):
        timestamp = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"[{timestamp}] "
                f"[{level}] "
                f"{message}\n"
            )


logger = Logger()
    