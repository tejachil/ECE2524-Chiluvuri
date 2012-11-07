all: exprtest

exprtest:
	bison parser.ypp
	flex -t scanner.ll > scanner.cpp
	g++ -Wall -g -o exprtest exprtest.cpp driver.cpp parser.tab.cpp scanner.cpp

clean:
	rm *hh *tab* scanner.cpp exprtest
