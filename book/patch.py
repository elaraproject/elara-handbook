import re
import os
import sys

START_TEXT = """
Script usage:
	python path/to/patch.py [--preview]

Arguments:
	--preview: perform a dry run that only shows result after
	\t   patching without modifying any files, if
	\t   not specified it writes to the build TeX file

Running patch script...
Warning: Make sure you have the LaTeX source already built,
in a _build/ folder, otherwise the script won't be able to work!
"""

# LaTeX environments to patch
ENVIRONMENTS = ["align", "gather", "matrix", "aligned", "equation"]

# Newlines can be \n or \r or \r\n
# so we need to match all of them
# https://stackoverflow.com/questions/587345/regular-expression-matching-a-multiline-block-of-text
REGEX_NEWLINE = r"((?:\n.+)+)"
NEWLINE = "\n"

# Regexes to match each environment to patch
# for these I don't know why you need to do double backslash
# AS WELL AS raw strings, it is just profoundly strange

def begin_equation_regex(environment: str):
	if "equation" in environment:
		return r"\\begin{equation.?}.\\begin{split}"
	return r"\\begin{equation.?}.\\begin{split}.\\begin{" + environment + ".?}"

def end_equation_regex(environment: str):
	if "equation" in environment:
		return r"\\end{split}.\\end{equation.?}"
	return r"\\end{" + environment + r".?}.\\end{split}.\\end{equation.?}"

def patch_environment(source_text: str, environment_name: str):
	# first replace \begin{...}
	first_regex = begin_equation_regex(environment_name)
	# for reasons I don't understand you need to escape \begin
	# AND use raw strings
	first_replacement = NEWLINE + r"\\begin{" + environment_name + "}"
	first_matches = re.findall(first_regex, source_text, flags=re.DOTALL)
	print(f"Found {len(first_matches)} occurence(s) of {environment_name} environment")
	# early return if no matches found
	if len(first_matches) == 0:
		print("No need for replacements, continuing.\n")
		return source_text

	tex_source_firstpass = re.sub(first_regex,
								  first_replacement,
								  source_text,
								  flags=re.DOTALL)
	# then replace \end{...}
	second_regex = end_equation_regex(environment_name)
	# same deal with \end needing to be escaped with 
	# double backslash (not sure why)
	second_replacement = r"\\end{" + environment_name + "}" + NEWLINE
	# second_replacement = r"\\end{split}" + NEWLINES
	tex_source_secondpass = re.sub(second_regex,
								   second_replacement,
								   tex_source_firstpass,
								   flags=re.DOTALL)
	print(f"Replacements for {environment_name} environment complete.\n")
	return tex_source_secondpass

working_dir = os.path.dirname(os.path.abspath(__file__))
tex_source_path = os.path.join(working_dir, "_build/latex/elara-handbook.tex")
print(tex_source_path)
# tex_source_path = os.path.join(working_dir, "../debug/test-regex-replace.tex")

print(f"Found script directory {working_dir}")

if not os.path.exists(tex_source_path):
	print("The LaTeX source files weren't located - perhaps you haven't built them yet.")
	print("Please check and then run again.")
	exit()

print(f"Processing TeX source file {tex_source_path}\n")

# Read generated TeX file
with open(tex_source_path, "r") as f:
	tex_source = f.read()

# print(tex_source)

for env in ENVIRONMENTS:
    print(f"Patching `{env}` environments")
    tex_source = patch_environment(tex_source, env)

if len(sys.argv) > 1:
	if sys.argv[1] == "--preview":
		print("Output:\n", tex_source)
		exit()

# write to file if not preview mode
with open(tex_source_path, "w") as f:
	f.write(tex_source)

print(f"Replacements complete. Results written to {os.path.relpath(tex_source_path)}")
