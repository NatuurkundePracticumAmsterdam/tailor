uisrcdir=src/tailor/resources
uidir=src/tailor

uifiles = ui_tailor.py ui_data_sheet.py ui_create_plot_dialog.py ui_csv_format_dialog.py ui_plot_tab.py ui_data_source_dialog.py ui_rename_dialog.py ui_preview_dialog.py ui_multiplot_tab.py

.PHONY: help
help:
	@echo "Run:"
	@echo "make ui     -- translate the UI files to Python files."
	@echo "make build  -- build an installer package."

.PHONY: ui
ui: $(addprefix $(uidir)/,$(uifiles))

$(uidir)/ui_%.py: $(uisrcdir)/%.ui
	pyside6-uic $< -o $@

.PHONY: build
build:
	python -m pip install briefcase==0.3.17
	briefcase create
	python pruner.py
	briefcase build
	briefcase package