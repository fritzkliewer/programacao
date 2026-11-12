#include <stdio.h>
#include <string.h>
#include <locale.h>
int main(){
    setlocale(LC_ALL, ".UTF8");
    printf("\nutilizando range():\n");
    for (int x = 0; x <= 7; x++)
        printf("Estamos na iteração %d\n", x);    
    printf("\nPercorrendo uma lista:\n");
    char *colecao[3] = {"oi", "5", "último da lista"};
    for (int x = 0; x < 3; x++)
        printf("%s\n",colecao[x]);
    const char *s = "fritzkliewer";
    printf("\nPercorrendo a string %s\n", s);
    for (int x = 0; x < strlen(s); x++)
        printf("%c\n", s[x]);
}