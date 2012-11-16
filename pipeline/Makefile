# Nayana Teja Chiluvuri pipeline (Makefile)

CC			= g++
CFLAGS		= -Wall -g -o

all: consumer generator

consumer: consumer.cpp
	${CC} ${CFLAGS} consumer consumer.cpp

generator: generator.cpp
	${CC} ${CFLAGS} generator generator.cpp

dispatcher: dispatcher.cpp
	${CC} ${CFLAGS} dispatcher dispatcher.cpp
	
clean:
	rm consumer generator
