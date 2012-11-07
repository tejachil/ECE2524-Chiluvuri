# Nayana Teja Chiluvuri Homework 5 (Makefile)

CC			= g++
CFLAGS		= -Wall -g -o
OUTPUT		= exprtest
GENFILES	= *tab* *hh scanner.cpp exprtest

all: exprtest

exprtest: driver.cpp driver.hpp expression.hpp exprtest.cpp parser.ypp scanner.hpp scanner.ll
	bison parser.ypp
	flex -t scanner.ll > scanner.cpp
	${CC} ${CFLAGS} ${OUTPUT} exprtest.cpp driver.cpp parser.tab.cpp scanner.cpp

clean:
	rm ${GENFILES}
