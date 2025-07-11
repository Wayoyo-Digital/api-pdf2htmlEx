import subprocess
from pprint import pprint
from .base import Command

"""
Command handler for converting PDF files to HTML using pdf2htmlEX.

This command wraps the pdf2htmlEX command line tool to convert PDF documents
to HTML format while preserving the original layout and formatting.

Example:
    bus = BusCommand.get_instance()
    bus.execute('pdf2htmlex', 'input.pdf')

Args:
    args[0]: Path to the input PDF file to convert

The command will execute pdf2htmlEX on the input file and capture the output.
"""

class Pdf2HtmlExCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        pprint(args)
        command = f"/usr/local/bin/pdf2htmlEX {args[0]}"
        output = subprocess.run(args=[command], shell=True, capture_output=True)
        pprint(output.stderr.decode('utf-8'))
