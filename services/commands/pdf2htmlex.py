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
    PDF2HTML_BINARY = "/usr/local/bin/pdf2htmlEX"

    def execute(self, *args):
        output = subprocess.run([self.PDF2HTML_BINARY, args[0]], capture_output=True)
        pprint(output.stderr.decode('utf-8'))
