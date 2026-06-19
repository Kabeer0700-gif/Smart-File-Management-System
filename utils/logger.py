from datetime import datetime

class Logger:
    def __init__(self):
        self.log_file = "app.log"

    def log(self,level,message):
        try: 
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
        except PermissionError:

            print(
                "Logger Error: "
                "Permission denied."
            )

        except OSError as e:

            print(
                f"Logger Error: {e}"
            )

        except Exception as e:

            print(
                f"Unexpected Logger Error: {e}"
            )

logger = Logger()
    