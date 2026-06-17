class StatisticsManager:

    def total_files(
        self,
        files
    ):

        return len(files)

    def total_storage(
        self,
        files
    ):

        return sum(
            file.size
            for file in files
        )

    def category_statistics(
        self,
        files
    ):

        categories = {}

        for file in files:

            categories[
                file.extension
            ] = (
                categories.get(
                    file.extension,
                    0
                ) + 1
            )

        return categories

    def largest_file(
        self,
        files
    ):

        return max(
            files,
            key=lambda file:
            file.size
        )

    def smallest_file(
        self,
        files
    ):

        return min(
            files,
            key=lambda file:
            file.size
        )

    def format_size(
        self,
        size
    ):

        if size < 1024:
            return f"{size} B"

        elif size < 1024**2:
            return (
                f"{size/1024:.2f} KB"
            )

        elif size < 1024**3:
            return (
                f"{size/(1024**2):.2f} MB"
            )

        else:
            return (
                f"{size/(1024**3):.2f} GB"
            )