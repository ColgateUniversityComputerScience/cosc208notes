NOTEBOOKS = $(wildcard *.ipynb)

HTML = $(NOTEBOOKS:.ipynb=.html)
MARKDOWN = $(NOTEBOOKS:.ipynb=.md)

all: $(HTML) $(MARKDOWN)
	python3 index.py

.PRECIOUS: %.notes.md %.slides.html %.worksheet.md

%.html: %.slides.html;
%.md: %.notes.md %.worksheet.md ;

%.notes.md: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags  "worksheet-only" --TagRemovePreprocessor.remove_cell_tags  "colab-only" --TagRemovePreprocessor.remove_all_outputs_tags "notes-code-only" --to markdown --output='$@'

%.slides.html: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_all_outputs_tags "none" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --to slides --output='$*'

%.worksheet.md: %.ipynb
	jupyter nbconvert $< --TagRemovePreprocessor.remove_cell_tags "none" --TagRemovePreprocessor.remove_cell_tags "notes-only" --TagRemovePreprocessor.remove_cell_tags "colab-only" --TagRemovePreprocessor.remove_all_outputs_tags "worksheet-code-only" --to markdown --output='$@'

%.colab: %.ipynb
	jupyter nbconvert --to notebook $< --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags "notes-only" --output='$@'

clean:
	rm *.slides.html *.notes.md *.worksheet.md
