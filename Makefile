PAPER = main
TEX = $(wildcard *.tex changes/*.tex)
BIB = references.bib
FIGS = $(wildcard fig/*.pdf fig/*.png fig/*.eps)

$(PAPER).pdf: $(TEX) $(BIB) $(FIGS)
	echo $(FIGS)
	pdflatex -shell-escape $(PAPER)
	bibtex $(PAPER)
	pdflatex -shell-escape $(PAPER)
	pdflatex -shell-escape $(PAPER)
	@/bin/echo ""
	@/bin/echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	@/bin/echo "               ++++ ANY UNDEFINED REFERENCES ++++"
	-@grep -i undef $(PAPER).log || echo "No undefined references."
	@/bin/echo "                 ++++ ANY EMPTY REFERENCES ++++"
	-@egrep -i -n -e 'cite{ *}' -e 'ref{ *}' $(TEX) $(FIGS) || echo "No empty references."
	@/bin/echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	@/bin/echo ""

all: $(PAPER).pdf

clean:
	rm -f *.aux *.bbl *.blg *.log *.out $(PAPER).pdf
