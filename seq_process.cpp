/*
 *
 * this program use for sequences modify 
 *
 *
 */

#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>

#define MAXREADSIZE 1024

using namespace std;

int main(int argc, char* args[]) {
		ifstream map_f(args[1], ios::in);
		ifstream seq_f(args[2], ios::out);
		int num_threads = int(args[3]);
		
		if(!map_f) {
				cout << "can't open the map file\n";
				exit(1)
		}

		if(!seq_f) {
				cout << "can't open the sequences file\n";
				exit(1)
		}

		char buffer[MAXREADSIZE];
		char temp[MAXREADSIZE];
		map_f.getline(temp, MAXREADSIZE);

		while(!map_f.eof()) {
				map_f.getline(buffer, MAXREADSIZE)
		}	
		
}
