.PHONY: all install clean
.SILENT: clean

all:
	$(MAKE) -C java2python/lang
	python setup.py build

install: all
	python setup.py install

clean:
	$(MAKE) -C java2python/lang clean
	rm -f *.pyo
	rm -f *.pyc
	rm -f *Parser.py
	rm -f *Lexer.py
	rm -f *.tokens
