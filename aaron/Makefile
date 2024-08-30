NOTEBOOKS = $(wildcard *.ipynb)

HTML = $(NOTEBOOKS:.ipynb=.html)

all: $(HTML)
	python3 index.py

.PRECIOUS: %.notes.html %.slides.html %.worksheet.html

%.html: %.slides.html %.notes.html %.worksheet.html ;

%.notes.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags  "worksheet-only" --TagRemovePreprocessor.remove_cell_tags  "colab-only" --TagRemovePreprocessor.remove_all_outputs_tags "notes-code-only" --HTMLExporter.exclude_input_prompt=True --to html --output='$@'

%.slides.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_all_outputs_tags "none" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --to slides --output='$*'

%.worksheet.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags "notes-only" --TagRemovePreprocessor.remove_cell_tags "colab-only" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --HTMLExporter.exclude_input_prompt=True --to html --output='$@'

%.colab: %.ipynb
	jupyter nbconvert --to notebook $< --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags "notes-only" --output='$@'

clean:
	rm *.slides.html *.notes.html *.worksheet.html
