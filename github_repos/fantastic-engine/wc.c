#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char** argv){
  int bytes = 0;
  int words = 0;
  int newLine = 0;
  char buffer[1];
  enum states { WHITESPACE, WORD };
  int state = WHITESPACE;
  if(argc != 2)printf( "Usage: %s <filename>", argv[0]);
  else{
    FILE *file = fopen( argv[1], "r");
    if(file == 0)printf("can not find :%s\n",argv[1]);
    else{
      char *thefile = argv[1];
      char last = ' ';
      while (read(fileno(file),buffer,1) ==1 ){
        bytes++;
        if ( buffer[0]== ' ' || buffer[0] == '\t') state = WHITESPACE;
        else if (buffer[0]=='\n'){
          newLine++;
          state = WHITESPACE;
        }
        else{
          if (state == WHITESPACE) words++;
          state = WORD;
        }
        last = buffer[0];
      }
      printf("New Lines: %d, words: %d, bytes: %d, fileName: %s\n",newLine,words,bytes,thefile);
   }
 }
 return 0;
}