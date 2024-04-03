#!/usr/bin/env python3

import os
import subprocess

command = "if [ ! -d 'build' ]; then mkdir build; fi && cd build/ && cmake .. && cmake --build . --target example && cd .."

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)

if not os.path.exists("output"):
     os.makedirs("output", exist_ok=True)

subprocess.run(
    [
        "cppcheck",
        "--enable=all",
        "--inline-suppr",
        "--output-file=output/cppcheck_report.log",
        "--project=build/compile_commands.json",
    ]
)

with open("output/cppcheck_report.log", "r") as f:
    content = f.read()

# Remove non-printable characters
content_clean = "".join(
    ch for ch in content if ch.isprintable() or ch == "\t" or ch == "\n"
)

# Remove the [number] patterns
for number in range(101):
    content_clean = content_clean.replace(f"[{number}m", "")

# Split on the sequence ' ^' and join with newlines
sentences = content_clean.split(" ^")
content_clean = "\n".join(sentences)

# Write back the cleaned content
with open("output/cppcheck_report.log", "w") as f:
    f.write(content_clean)
