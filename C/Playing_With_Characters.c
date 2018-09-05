/*
Task

You have to print the character ch in the first line. Then print s in next line. In the last line print the sentence,sen .

*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char ch, s[20], sen[20];
    scanf("%c", &ch);
    scanf("\n");
    scanf("%[^\n]%*c", &s);

    scanf("%[^\n]%*c", &sen);
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s", sen);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}
