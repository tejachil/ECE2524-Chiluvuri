// Nayana Teja Chiluvuri pipeline ECE2524

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
	int fdPipe[2];
	
	if(pipe(fdPipe))	return EXIT_FAILURE;
	int generatorPID, consumerPID;
	char** buff = {NULL};

	// Create first fork to execute the generator
	generatorPID = fork();
	if(!generatorPID){
		dup2(fdPipe[1], STDOUT_FILENO);
		close(fdPipe[0]);	// close the write end of the pipe
		execve("./generator", buff, NULL);
		exit(0);
	}
	
	sleep(1); // Wait for one second
	
	// Kill the generator process
	if(!kill(generatorPID, SIGTERM))
		waitpid(generatorPID, NULL, 0);
	
	// Create the second fork to execute the consumer
	consumerPID = fork();
	if(!consumerPID){
		dup2(fdPipe[0], STDIN_FILENO);
		close(fdPipe[1]);
		execve("./consumer", buff, NULL);
		exit(0);
	}
	
	
	return EXIT_SUCCESS;
}
