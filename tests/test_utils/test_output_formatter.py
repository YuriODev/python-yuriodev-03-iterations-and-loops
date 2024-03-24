class TestOutputFormatter:
    @staticmethod
    def get_failure_details_in_table(input_value: list, expected_output, actual_output) -> str:
        # Ensure the first line of input is considered in the table printing process
        input_value_str = '\n'.join(input_value)  # Convert list to string if needed

        # ANSI escape code for yellow
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"
        # Print the "Failed test:" message
        output = f"\n{yellow_start}Failed test:{yellow_end}\n"

        # Find the longest output list for proper table formatting
        max_lines = max(len(expected_output), len(actual_output))
        max_length = max([len(input_value_str)] + [len(line) for line in expected_output + actual_output])
        column_width = max(max_length, len("| Expected Output |"))

        # Preparing the table border based on the longest content
        table_width = 3 * column_width + 9  # including padding and separators
        divider = yellow_start + "+" + "-" * (table_width - 1) + "+" + yellow_end

        # Printing the table headers and top border
        output += divider + "\n"
        header = f"| {'Input'.ljust(column_width)} | {'Expected Output'.ljust(column_width)} | {'Actual Output'.ljust(column_width)} |"
        output += yellow_start + header + yellow_end + "\n"
        output += divider + "\n"

        # Printing rows
        max_lines = max(len(input_value), len(expected_output), len(actual_output))
        for i in range(max_lines):
            row = "|"
            # Input value column
            if i < len(input_value):
                row += f" {input_value[i].ljust(column_width)} |"
            else:
                row += " " * (column_width + 2) + "|"

            # Expected and Actual Output columns
            for output_list in [expected_output, actual_output]:
                if i < len(output_list):
                    row += f" {output_list[i].ljust(column_width )} |"
                else:
                    row += " " * (column_width + 1) + "|"
            output += yellow_start + row + yellow_end + "\n"

        # Adding the bottom divider
        output += divider + "\n"

        return output

    @staticmethod
    def generate_message(title: str, content: str) -> str:
        """
        Generates a custom message in a table format with the given title and content.
        """
        yellow_start = "\x1b[38;5;208m"
        yellow_end = "\x1b[0m"
        message_lines = [
            "\n",
            yellow_start + "Failed test:" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
            yellow_start + f"| {title.center(50)} |" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
            yellow_start + f"| {content.center(50)} |" + yellow_end,
            yellow_start + "+-------------------------------------------------------+" + yellow_end,
        ]
        return "\n".join(message_lines)

    @staticmethod
    def generate_loop_usage_message():
        """
        Generates a custom message in a table format about the misuse of loops.
        """
        title = "Loop Usage Error"
        content = "The solution must use a 'for' or 'while' loop."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_continue_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'continue' statement.
        """
        title = "Continue Usage Error"
        content = "The solution must use the 'continue' statement."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_if_usage_message():
        """
        Generates a custom message in a table format about the misuse of the 'if' statement.
        """
        title = "If Usage Error"
        content = "The solution must not use the 'if' statement."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_list_usage_message():
        """
        Generates a custom message in a table format about the misuse of lists.
        """
        title = "List Usage Error"
        content = "The solution must not use lists."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_string_slice_message():
        """
        Generates a custom message in a table format about the misuse of string slicing.
        """
        title = "String Slice Usage Error"
        content = "The solution must not use string slicing."
        return TestOutputFormatter.generate_message(title, content)

    @staticmethod
    def generate_division_by_zero_message():
        """
        Generates a custom message in a table format about division by zero.
        """
        title = "Division by Zero Error"
        content = "The solution must not divide by zero."
        return TestOutputFormatter.generate_message(title, content)
