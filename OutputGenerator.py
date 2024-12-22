class OutputGenerator:

    @staticmethod
    def _generate_data_output(processed_data):
        # Core logic for generating the formatted output
        output = ""
        for candidate in processed_data:
            output += f"Hello {candidate['name']},\n"
            for exp in candidate["experiences"]:
                if "Gap in CV" in exp.get("title", ""):
                    output += f"{exp['title']} for {exp['gap_days']} days\n"
                elif "No Experience Found" in exp.get("title", ""):
                    output += "Candidate Has No Experience\n"
                else:
                    output += (
                        f"Worked as: {exp['title']}, From {exp['from']} To {exp['to']} in {exp['location']}\n"
                    )
            output += "\n"
        return output

    @staticmethod
    def print_to_console(processed_data):
        output = OutputGenerator._generate_data_output(processed_data)
        print(output)

    @staticmethod
    def write_to_file(processed_data, filename="output.txt"):
        output = OutputGenerator._generate_data_output(processed_data)
        with open(filename, "w") as file:
            file.write(output)

    @staticmethod
    def return_as_string(processed_data):
        return OutputGenerator._generate_data_output(processed_data)
