import secrets
from os import system
import pyperclip
import re
system("del dist\\* /F /Q")
filename = "setup.py"
# Öffne die setup.py Datei und lies ihren Inhalt
with open(filename, "r") as file:
	setup_content = file.read()

# Finde die aktuelle Version
version_pattern = r"version\s*=\s*'(\d+\.\d+)'"
match = re.search(version_pattern, setup_content)

if match:
	current_version = match.group(1)
	major, minor = current_version.split(".")
	new_version = f"{major}.{int(minor) + 1}"

	# Ersetze die alte Version mit der neuen Version
	new_content = re.sub(version_pattern, f"version='{new_version}'", setup_content)

	# Schreibe den neuen Inhalt zurück in die Datei
	with open(filename, "w") as file:
		file.write(new_content)

	print(f"Neue Version: {new_version}")
else:
	print("Konnte keine Version in der setup.py finden.")
	exit()



system("python setup.py sdist bdist_wheel")

print("Drücke Strg + V und danach Enter")
pyperclip.copy(secrets.apikey)
system("twine upload dist/*")
