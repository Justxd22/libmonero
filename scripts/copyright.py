import os

path = "../src"

ignore = []

# To update the header, only change the variable below

header = """/*
 * This file is part of OpenMonero's Go library monero.go
 *
 * Copyright (c) 2023 OpenMonero
 * All Rights Reserved.
 * The code is distributed under MIT license, see LICENSE file for details.
 * Generated by OpenMonero on 03-07-2023.
 *
 */
"""

def add_text_to_files(folder_path, text, ignored_extensions=[]):
    should_ignore = False
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            should_ignore = False
            for ignored_extension in ignored_extensions:
                if file_path.endswith(ignored_extension):
                    should_ignore = True
                    break
            if not should_ignore:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if len(lines) >= 4:
                        second_line = lines[0]
                        third_line = lines[1]
                        fourth_line = lines[2]
                        if second_line.startswith("/*") and third_line.startswith(" *") and fourth_line.startswith(" *"):
                            with open(file_path, 'w') as file:
                                file.seek(0, 0)
                                file.write(text + ''.join(lines[9:]))
                        else:
                            with open(file_path, 'w') as file:
                                file.seek(0, 0)
                                file.write(text + '\n' + ''.join(lines))
                    else:
                        with open(file_path, 'w') as file:
                            file.seek(0, 0)  # Move the file cursor to the start
                            file.write(text + '\n' + ''.join(lines))

add_text_to_files(path, header, ignore)