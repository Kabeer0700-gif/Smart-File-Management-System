import csv


class ReportGenerator:

    def generate_txt_report(self,files,statistics):

        with open(
            "report.txt",
            "w",
            encoding="utf-8"
        ) as report:

            report.write(
                "SMART FILE MANAGEMENT REPORT\n"
            )

            report.write(
                "=" * 50 + "\n\n"
            )

            report.write(
                f"Total Files: "
                f"{statistics['total_files']}\n"
            )

            report.write(
                f"Total Size: "
                f"{statistics['total_size']}\n\n"
            )

            for file in files:

                report.write(
                    f"Name: {file.name}\n"
                )

                report.write(
                    f"Extension: "
                    f"{file.extension}\n"
                )

                report.write(
                    f"Size: "
                    f"{file.size}\n"
                )

                report.write(
                    f"Path: "
                    f"{file.path}\n\n"
                )

        print(
            "TXT Report Generated"
        )