////////////////////////////////////////////////////////
// ECE 2524, process-object, Nayana Teja Chiluvuri
//
// File name: Process.cpp
// Description: implementation of the Process object
// Date: 12/5/2012
//

#include "Process.h"

/* Initialize the process, create input/output pipes */
Process::Process(const std::vector<std::string> &args){
	m_name = args[0];
	
	//Convert vector from std::string to const char*
	std::vector<const char *> cargs;
	std::transform(args.begin(), args.end(), std::back_inserter(cargs), []( const std::string s) { return s.c_str(); } );
	cargs.push_back(NULL); // exec expects a NULL terminated array

	//Open the write and read pipes and validate that the are succesfully created
	if(pipe(writepipe)){
		std::cerr << "Error: Unable to create the write pipe.\n";
	}
	if(pipe(readpipe)){
		std::cerr << "Error: Unable to create the read pipe.\n";
	}

	//Create the child process
	m_pid = fork();
	if(m_pid == -1)	std::cerr << "Error: Child process not created.";

	//Child Process
	else if(m_pid == 0){
		//Duplicate the child write to parent read and close
		dup2(readpipe[1],STDOUT_FILENO);
		close(readpipe[1]);
		
		//Duplicate the parent write to child read and close
		dup2(writepipe[0],STDIN_FILENO);
		close(writepipe[1]);		

		close(readpipe[0]); //Close the parent read the child write
		close(writepipe[0]); //Close the parent write to the child read

		//Execute the process
		execve(m_name.c_str(), const_cast<char**>(&cargs[0]), NULL);
	}
	
	//Parent Process
	else{
		std::cout << "Parent[" << getpid() << "] Process-object constructor\n";
		close(readpipe[1]);
		close(writepipe[0]);
		m_pread = fdopen(readpipe[0], "r");
	}
}

/* Close any open file streams or file descriptors,
	insure that the child has terminated */
Process::~Process(){
    close(writepipe[1]);
	close(readpipe[0]);
	kill(m_pid, SIGTERM);
	waitpid(m_pid, NULL, 0);
}

/* write a string to the child process */
void Process::write(const std::string& str){
	::write(writepipe[1], str.c_str(), strlen(str.c_str()));
}

/* read a full line from child process, 
	if no line is available, block until one becomes available */
std::string Process::readline(){
	char* input;
	size_t length;
	getline(&input, &length, m_pread);
	return std::string(input);
}
