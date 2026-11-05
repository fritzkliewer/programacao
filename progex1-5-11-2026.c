#include <stdio.h>
#include <math.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, ".UTF8");
    float dados[7] = {-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0}, p;
    bool y = true;
    int i;
    while (y == true)
    {
        printf("Opções:\n");
        printf("1)Função exponencial\n");
        printf("2)Função logarítmica\n");
        printf("3)Ambas as funções\n");
        printf("4)Sair\n");
        char opcao = getc(stdin);
        while (getchar() != '\n');
        if (opcao == '4')
            break;
        printf("---------------\n| %4s | %4s |\n---------------\n", "x", "f(x)");
        if (opcao == '1' || opcao == '3')
            for (i = 0; i < 7; i++)
                printf("%6.2f %6.3f\n", dados[i], pow(2, dados[i]));
        printf("%6s %6s\n", "x", "g(x)");
        if (opcao == '2' || opcao == '3')
            for (i = 0; i < 7; i++)
                printf("%6.3f %6.2f\n", pow(2, dados[i]), log(pow(2, dados[i])) / log(2));
    }
    return 0;
}
