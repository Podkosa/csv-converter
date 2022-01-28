#Тестовое задание для КВАРТА ВК.

class ConverterCSV:
    def convert(self, file_path: str):
        """Converts .csv file into YAML or JSON, creates the converted file in the same directory. Format must be specified in the first row, last collumn.
        """
        with open(file_path) as file:
            first_line = file.readline().split(sep=',')
            format = first_line.pop().lower()
            if 'yaml' in format or 'yml' in format:
                self._to_yaml(file, first_line)
            elif 'json' in format:
                self._to_json(file, first_line)
            else:
                raise Exception ("YAML or JSON indication not found. Check if the last collumn in .csv file contains the format name.")
    def _to_yaml(self, file, first_line):
        name = file.name.strip('.csv')
        with open (f'{name}_converted.yml', 'w') as file_converted:
            file_converted.write(f'---\n{file.name}:')
            for line in file:
                line = line.strip().split(sep=',')
                for index, cell in enumerate(line):
                    if not index:
                        file_converted.write(f'\n  - {first_line[index]}: {cell}')
                    else:
                        file_converted.write(f'\n    {first_line[index]}: {cell}')
    def _to_json(self, file, first_line):
        name = file.name.strip('.csv')
        with open (f'{name}_converted.json', 'w') as file_converted:
            file_converted.write('{\n'f'  "{file.name}": [')
            for index_line, line in enumerate(file):
                line = line.strip().split(sep=',')
                if index_line != 0:
                    file_converted.write(',')
                file_converted.write('\n    {')
                for index_cell, cell in enumerate(line):
                    if not cell.isalnum():
                        cell = f'"{cell}"'
                    file_converted.write(f'\n      "{first_line[index_cell]}": {cell}')
                    if index_cell != len(line)-1:
                        file_converted.write(',')
                file_converted.write('\n    }')
            file_converted.write('\n  ]\n}')

# #Пример использования
# import os
# csv = ConverterCSV()
# file_path = os.path.join('example.csv')
# csv.convert(file_path)
