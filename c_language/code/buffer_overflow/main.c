# include <stdio.h>
# include <string.h>

int main(int argc, char *argv[]){
    int value = 5;
    char buffer_one[8], buffer_two[8];

    strcpy(buffer_one, "one");
    strcpy(buffer_two, "one");
    
    printf("buffer_two ポインター : %p \n", buffer_two);
    printf("buffer_two 値 : %s \n", buffer_two);
    printf("buffer_one ポインター : %p \n", buffer_one);
    printf("buffer_one 値 : %s \n", buffer_one);
    printf("value ポインター : %p \n", value);
    printf("value 値 : %d \n", value);
    /*最初の引数をbuffer_twoにコピーする*/
    strcpy(buffer_two, argv[1]);
    
    printf("buffer_two ポインター : %p \n", buffer_two);
    printf("buffer_two 値 : %s \n", buffer_two);
    printf("buffer_one ポインター : %p \n", buffer_one);
    printf("buffer_one 値 : %s \n", buffer_one);
    printf("value ポインター : %p \n", value);
    printf("value 値 : %d \n", value);
}