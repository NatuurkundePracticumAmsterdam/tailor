import textwrap
from importlib import resources
from pathlib import Path

import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

DELIMITER_CHOICES = {
    "detect": None,
    "comma": ",",
    "semicolon": ";",
    "tab": "\t",
    "space": " ",
}
NUM_FORMAT_CHOICES = {"1,000.0": (".", ","), "1.000,0": (",", ".")}


class CSVFormatDialog(QtWidgets.QDialog):
    def __init__(self, filename):
        """Create the CSV file format selection dialog."""
        super().__init__()

        self.filename = Path(filename).expanduser()

        uic.loadUi(
            pkg_resources.resource_stream("tailor.resources", "csv_format_dialog.ui"),
            self,
        )
        self.delimiter_box.addItems(DELIMITER_CHOICES.keys())
        self.num_format_box.addItems(NUM_FORMAT_CHOICES.keys())

        self.delimiter_box.currentIndexChanged.connect(self.show_preview)
        self.num_format_box.currentIndexChanged.connect(self.show_preview)
        self.use_header_box.stateChanged.connect(self.show_preview)
        self.header_row_box.valueChanged.connect(self.show_preview)
        self.preview_choice.buttonClicked.connect(self.show_preview)

        self.show_preview()

    def show_preview(self):
        """Show a preview of the CSV data."""
        if self.preview_choice.checkedButton() == self.preview_csv_button:
            (
                delimiter,
                decimal,
                thousands,
                header,
                skiprows,
            ) = self.get_format_parameters()
            try:
                df = pd.read_csv(
                    self.filename,
                    delimiter=delimiter,
                    decimal=decimal,
                    thousands=thousands,
                    header=header,
                    skiprows=skiprows,
                )
            except pd.errors.ParserError as exc:
                text = textwrap.dedent(
                    f"""\
                    An error occured while parsing the data file. Most probably
                    the format is different from what was expected. You can
                    change the options in this screen to fix this. If you switch
                    to a *Plain text* preview you will be able to inspect the
                    literal text of the data file. Please check the column
                    delimiter and numeric format. In the case of comments or
                    introductory text at the start of the file you can skip a
                    number of lines.

                    The exception was:

                    {exc!s}
                    """
                )
            else:
                text = df.to_string()
        else:
            try:
                with open(self.filename) as f:
                    text = "".join(f.readlines())
            except Exception as exc:
                text = textwrap.dedent(
                    f"""\
                    An error occured while showing the literal text of the data
                    file. This should not happen. Please file an issue at:

                    https://github.com/davidfokkema/tailor/issues

                    If possible, include the data file. The exception was:

                    {exc!s}
                    """
                )
        self.preview_box.setPlainText(text)

    def get_format_parameters(self):
        """Get CSV format parameters

        Returns:
            delimiter, decimal, thousands, header: a tuple of format options.
        """
        delimiter = DELIMITER_CHOICES[self.delimiter_box.currentText()]
        decimal, thousands = NUM_FORMAT_CHOICES[self.num_format_box.currentText()]
        if self.use_header_box.isChecked():
            header = self.header_row_box.value()
            skiprows = 0
        else:
            header = None
            skiprows = self.header_row_box.value()
        return delimiter, decimal, thousands, header, skiprows
