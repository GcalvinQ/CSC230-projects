/*
Programmer: Kadeem Jonas
Date: November 19, 2018
File Name: Volleyball Program
Purpose:
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <windows.h>
#include "Player.h"
#include "GameStats.h"
#include <time.h>

#define SIZE 25

#define RED 12
#define GREEN 10
#define YELLOW 14
#define BLUE 9
#define WHITE 15
#define CYAN 3
#define GRAY 7

void Authenticate(int *);
void GetPassword(char []);
void updateLogin();
char menu();
void welcome();
void addPlayerStat(Player );
void addGameStat (Game );
int search2(Player [], int);
void writePlayer(Player );
int playerCount();
char optionB();
void display(Player [], int);
int search (Player [], int);
void searchDisplay (Player [], int);
void gameDisplay (Game );
void readGameStat(Game );
void addPlayer();

int main()
{
    char choice, option;
    int loggedIn, players, searchResult, var;
    Game gm;
    Player plr[SIZE];

    Authenticate(&loggedIn);

    if(loggedIn == 1)
    {
        //welcome();
        readGameStat(gm);
        choice = menu();

        while(choice != 'G' && choice != 'g')
        {
            players = playerCount();
            switch (choice)
            {
            case 'A':
            case 'a':
                addPlayer();
                break;

            case 'B':
            case 'b':
                option = optionB();
                while(option != 'D' && option != 'd')
                {
                    switch (option)
                    {
                    case 'A':
                    case 'a':
                        var = search2(plr, players);
                        addPlayerStat(plr[var]);
                        break;

                    case 'B':
                    case 'b':
                        addGameStat(gm);
                        break;

                    default:
                        printf("\nPLEASE SELECT A VALID OPTION:");
                            break;
                    }
                        option = menu();
                }

                break;

            case 'C':
            case 'c':
                display(plr, players);
                break;

            case 'D':
            case 'd':
                searchResult = search(plr, players);
                searchDisplay(plr, searchResult);
                break;

            case 'E':
            case 'e':
                gameDisplay(gm);
                break;

            case 'F':
            case 'f':
                updateLogin();
                break;

            default:
                printf("\nINVALID OPTION\n");
                printf("press any key to continue");
                getch();
                break;
            }
            choice = menu();
        }
    }
    else
    {
        printf("\nCANNOT AUTHENTICATE USER");
        getch();
    }

    return 0;
}

char menu()
{
    system("cls");

    printf("\t\t __________________________________ \n");
    printf("\t\t||         CHOOSE AN OPTION       ||\n");
    printf("\t\t||================================||\n");
    printf("\t\t|| [A] Add a Player               ||\n");
    printf("\t\t|| [B] Add a Statistic            ||\n");
    printf("\t\t|| [C] View All Player Stats      ||\n");
    printf("\t\t|| [D] Search for a player        ||\n");
    printf("\t\t|| [E] Display Current Game Info  ||\n");
    printf("\t\t|| [F] Update your Login Info     ||\n");
    printf("\t\t|| [G] Exit the program           ||\n");
    printf("\t\t||________________________________||\n");
    printf("\t\t   Option: \n\n");

    return getch();
    system("cls");
}


void addPlayer()
{
    Player plr;

    system("cls");
    fflush(stdin);

    printf("\nPlayer Name: ");
    gets(plr.name);
    strupr(plr.name); //fix whatever is here
    fflush(stdin);
    printf("\nPlayer Position: ");
    scanf ("%c", plr.position);
    printf("\nPlayer Jersey Number: ");
    scanf ("%d", &plr.jerseyNum);
    fflush(stdin);

    plr.serves = 0;
    plr.blocks = 0;
    plr.attacks = 0;
    plr.serveMis = 0;
    plr.passMis = 0;

    plr.setMis = 0;
    plr.attackMis = 0;
    plr.blockMis = 0;
    plr.sets = 0;
    plr.passes = 0;

    writePlayer(plr);

    getch();
}

void writePlayer(Player plr)
{
    FILE *fp;
    if((fp = fopen("playerdata.dat", "ab"))==NULL) //open the file for writing to binary file
    {
        fprintf(stderr, "File could not be opened to store customer to File\n");
    }
    else
    {
        fwrite(&plr, sizeof(Player),1,fp);
        fclose(fp);
    }
}

void readPlayer(Player plr[])
{
    FILE *fp;
    int i=0;
    if((fp = fopen("playerdata.dat", "rb"))==NULL) //open the file for reading from binary file
    {
        fprintf(stderr, "File could not be opened\n");
    }
    else
    {
        while(!feof(fp))
        {
            fread(&plr[i], sizeof(Player),1,fp);
            i++;
        }
        fclose(fp);

    }
}

void displayStats (Player plr)
{

    printf("\nPlayer Serves: %i", plr.serves);
    printf("\nPlayer Passes: %i", plr.passes);
    printf("\nPlayer Blocks: %i", plr.blocks);
    printf("\nPlayer Sets: %i", plr.sets);
    printf("\nPlayer Attacks: %i", plr.attacks);
    printf("\nPlayer Serve Mistakes: %i", plr.serveMis);
    printf("\nPlayer Pass Mistakes: %i", plr.passMis);
    printf("\nPlayer Block Mistakes: %i", plr.blockMis);
    printf("\nPlayer Set Mistakes: %i", plr.setMis);
    printf("\nPlayer Attack Mistakes: %i", plr.attackMis);
}
/*
void welcome()
{
    printf("\t\t\t ________________________________________________\n");
    printf("\t\t\t|\t                                     \t|\n");
    printf("\t\t\t|\t  ===================================\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t||   WELCOME TO THE CAMPION COLLEGE  ||\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t||       VOLLEYBALL MANAGEMENT       ||\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t||             PROGRAM               ||\t|\n");
    printf("\t\t\t|\t||                                   ||\t|\n");
    printf("\t\t\t|\t  ===================================\t|\n");
    printf("\t\t\t|\t                                     \t|\n");
    printf("\t\t\t ------------------------------------------------\n\n\n\n");

    Sleep(3000);
    system("cls");
}
*/

char optionB()
{
    system("cls");

    printf("\t\t __________________________________ \n");
    printf("\t\t||         CHOOSE AN OPTION       ||\n");
    printf("\t\t||================================||\n");
    printf("\t\t|| [A] Add Player Statistic       ||\n");
    printf("\t\t|| [B] Add Game Statistic         ||\n");
    printf("\t\t|| [C] Return to Main Menu        ||\n");
    printf("\t\t||________________________________||\n");
    printf("\t\t   Option: ");

    return getch();
    system("cls");
}

int playerCount()
{
    Player plr;
    FILE *fp;
    int i=0; //Counter for the Number of Players
    if((fp = fopen("playerdata.dat", "rb"))==NULL)
    {
        fprintf(stderr, "File could not be opened\n");
    }
    else
    {
        while(!feof(fp))
        {
            fread(&plr, sizeof(Player),1,fp);
            i++;
        }
        fclose(fp);
    }

    return i;
}

void addPlayerStat(Player plr)
{
    char choice;

    system("cls");

    printf("CHOOSE AN OPTION: ");
    printf("\n[A]   Add Successful Serve");
    printf("\n[B]   Add Successful Block");
    printf("\n[C]   Add Successful Attack");
    printf("\n[D]   Add Successful Set");
    printf("\n[E]   Add Successful Pass");
    printf("\n[F]   Add Serve Mistakes");
    printf("\n[G]   Add Block Mistakes");
    printf("\n[H]   Add Attack Mistakes");
    printf("\n[I]   Add Set Mistakes");
    printf("\n[J]   Add Pass Mistakes");
    printf("\n[K]   Return");
    printf("\n\n    Choice:");

    while(choice != 'K' && choice != 'k')
    {
        switch (choice)
        {
        case 'A':
        case 'a':
            plr.serves++;
            break;

        case 'B':
        case 'b':
            plr.blocks++;
            break;

        case 'C':
        case 'c':
            plr.attacks++;
            break;

        case 'D':
        case 'd':
            plr.sets++;
            break;

        case 'E':
        case 'e':
            plr.passes++;
            break;

        case 'F':
        case 'f':
            plr.serveMis++;
            break;

        case 'G':
        case 'g':
            plr.blockMis++;
            break;

        case 'H':
        case 'h':
            plr.attackMis++;
            break;

        case 'I':
        case 'i':
            plr.setMis++;
            break;

        case 'J':
        case 'j':
            plr.passMis++;
            break;

        default:

            printf("\nPLEASE SELECT A VALID OPTION:");
            break;
        }
        choice = menu();
    }
}

void addGameStat(Game gm)
{
    char choice;

    system("cls");

    printf("CHOOSE AN OPTION: ");
    printf("\n[A]   Add Set");
    printf("\n[B]   Add Point to Team 1");
    printf("\n[C]   Add Point to Team 2");
    printf("\n[D]   Timeout for Team 1");
    printf("\n[E]   Timeout for Team 2");
    printf("\n[F]   Substitution for Team 1");
    printf("\n[G]   Substitution for Team 2");
    printf("\n[H]   Return");
    printf("\n\n    Choice:");

    while(choice != 'H' && choice != 'h')
    {
        switch (choice)
        {
        case 'A':
        case 'a':
            gm.setNum++;
            break;

        case 'B':
        case 'b':
            gm.points1++;
            break;

        case 'C':
        case 'c':
            gm.points2++;
            break;

        case 'D':
        case 'd':
            gm.timeOut1++;
            if (gm.timeOut1 == 2)
            {
                printf("\nFINAL TIMEOUT FOR THIS SET");
            }
            break;

        case 'E':
        case 'e':
            gm.timeOut2++;
            if (gm.timeOut2 == 2)
            {
                printf("\nFINAL TIMEOUT FOR THIS SET");
            }
            break;

        case 'F':
        case 'f':
            gm.subs1++;
            break;

        case 'G':
        case 'g':
            gm.subs2++;
            break;

        default:

            printf("\nPLEASE SELECT A VALID OPTION:");
            break;
        }
        choice = menu();
    }
}


int search(Player plr[], int players)
{
    char name[50];
    int i = 0;

    readPlayer(plr);

    system("cls");

    printf("\nENTER THE PLAYER NAME: ");
    fflush(stdin);
    gets(name);

    //make search case-insensitive
    while (strcmp (plr[i].name, strupr(name)) !=0)
    {
        if (i > players)
        {
            i = -1;
            return i;
        }
        i++;
    }

    return i;
}

int search2(Player plr[], int players)
{
    int i = 0, num;

    players = playerCount();

    readPlayer(plr);

    system("cls");

    printf("\nEnter the Player Jersey Number: ");
    scanf("%d", &num);

    while (num != plr[i].jerseyNum)
    {
        if (i > players)
        {
            i = -1;
            return i;
        }
        i++;
    }

    return i;
}

void GetPassword(char password[])
{
    char c;
    int i = 0;

    while((c = getch()) != '\r')//return or enter key
    {
        if(c == '\b')
        {
            password[i] = '0';
            i--;
            printf("\b \b");
        }else
        {
            password[i] = c;
            printf("*");
            i++;
        }
    }
    password[i] = '\0';
}

void Authenticate(int *loggedIn)
{
    char nameOnFile[25], passwordOnFile[25], uname[25], pwd[25];
    FILE *fpRead, *fpWrite;
    long size;

    if((fpRead = fopen("Login.dat", "a+")) != NULL)
    {
        fseek(fpRead, 0, SEEK_END);
        size = ftell(fpRead);
        //check if to sign up or login
        if(size != 0)// something is on file
        {
            fseek(fpRead, 0, SEEK_SET);
            fscanf(fpRead, "%s %s", nameOnFile, passwordOnFile);

            //login

            printf("\tLOGIN \n");
            printf("\n________________________\n");
            printf("ENTER YOUR USERNAME: ");
            scanf("%s", uname);
            printf("ENTER YOUR PASSWORD: ");
            GetPassword(pwd);
            printf("\n________________________\n");
            system("cls");

            while(strcmp(uname, nameOnFile) != 0 || strcmp(pwd, passwordOnFile) != 0)
            {
                printf("Incorrect Username or Password. Try Again");
                printf("\n________________________\n");
                printf("\tLOGIN \n");
                printf("\n________________________\n");
                printf("ENTER YOUR USERNAME: ");
                scanf("%s", uname);
                printf("ENTER YOUR PASSWORD: ");
                GetPassword(pwd);
                printf("\n________________________\n");
                system("cls");
            }
            while(strcmp(uname, nameOnFile) != 0 || strcmp(pwd, passwordOnFile) != 0);

            *loggedIn = 1;
        }
        else
        {
            //sign up
            do
            {
                printf("SIGN UP\n");

                printf("ENTER A USERNAME: \n");
                scanf("%s", uname);
                printf("ENTER A PASSWORD: \n");
                GetPassword(pwd);
                system("cls");
            }
            while(strcmp(uname, "") == 0 || strcmp(pwd, "") == 0);

            ///write the new user to file
            if((fpWrite = fopen("Login.dat", "w")) != NULL)
            {
                fprintf(fpWrite, "%s %s", uname, pwd);
                *loggedIn = 1;//user logged in
                fclose(fpWrite);
            }else
            {
                *loggedIn = 0;//user not logged in
            }
        }
        fclose(fpRead);
    }
    else
    {
        *loggedIn = 0;//user not logged in
    }
}

void updateLogin()
{
    char uname[25], pwd[25];
    FILE *fp;

    system("cls");

    if((fp = fopen("Login.dat", "w")) != NULL)
    {
        do
        {
            printf("CHANGE USERNAME AND PASSWORD\n");

            printf("ENTER NEW USERNAME: \n");
            scanf("%s", uname);
            printf("ENTER NEW PASSWORD: \n");
            GetPassword(pwd);
            system("cls");
        }
        while(strcmp(uname, "") == 0 || strcmp(pwd, "") == 0);

        fprintf(fp, "%s %s", uname, pwd);
        fclose(fp);
    }else
    {
        printf("\n CANNOT UPDATE AT THIS TIME...");
        getch();
    }
}

void display(Player plr[], int players)
{
    int i;

    readPlayer(plr);

    system("cls");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), GREEN);//set text color

    printf(" ___________________________________________________________________\n");
    printf("|-------------------------------------------------------------------|\n");
    printf("|--                    -- PLAYER STATS --                         --|");

    for(i = 0; i < players; i++)
    {
        printf("\n|-----------------------------------------------------------------|");
        printf("\n| | NAME          | NUMBER|                                       |");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |%s             | %d                                            |",plr[i].name, plr[i].jerseyNum);
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |  SERVES   |  BLOCKS   |   ATTACKS   |   SETS   |   PASSES     |");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n|--                      -- SUCCESSFUL --                       --|");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |    %d     |    %d     |     %d      |    %d    |    %d        |",plr[i].serves, plr[i].blocks, plr[i].attacks, plr[i].sets, plr[i].passes);
        printf("\n| |-------------------------------------------------------------| |\n");
        printf("\n|--                     -- UNSUCCESSFUL --                      --|");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |    %d     |    %d     |     %d      |    %d    |    %d        |",plr[i].serveMis, plr[i].blockMis, plr[i].attackMis, plr[i].setMis, plr[i].passMis);
        printf("\n| |-------------------------------------------------------------| |\n");

            //change to gray for even numbered customers to clearly separate each player
            if(i%2 == 0)
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), GRAY);
            else
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), GREEN);
        }

    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), WHITE);

    printf("\n| |-------------------------------------------------------------| |\n");
    printf("| |-------------------------------------------------------------| |\n");
    printf("| | Total Players\t\t\t| %i\t\t\t| |\n", players);
    printf("|_|_____________________________________________________________|_|\n");

    printf("\n Press any key to Return to menu...");
    getch();
}

void searchDisplay(Player plr[], int i)
{

    readPlayer(plr);

    system("cls");

    if(i != -1)
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), GREEN);//set text color

        printf(" ___________________________________________________________________\n");
        printf("|-------------------------------------------------------------------|\n");
        printf("|--                     -- SEARCH RESULTS --                      --|");
        printf("\n| | NAME          | NUMBER|                                       |");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |%s             | %d                                            |",plr[i].name, plr[i].jerseyNum);
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |  SERVES   |  BLOCKS   |   ATTACKS   |   SETS   |   PASSES     |");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n|--                      -- SUCCESSFUL --                       --|");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |    %d     |    %d     |     %d      |    %d    |    %d        |",plr[i].serves, plr[i].blocks, plr[i].attacks, plr[i].sets, plr[i].passes);
        printf("\n| |-------------------------------------------------------------| |\n");
        printf("\n|--                     -- UNSUCCESSFUL --                      --|");
        printf("\n| |-------------------------------------------------------------| |");
        printf("\n| |    %d     |    %d     |     %d      |    %d    |    %d        |",plr[i].serveMis, plr[i].blockMis, plr[i].attackMis, plr[i].setMis, plr[i].passMis);
        printf("\n| |-------------------------------------------------------------| |\n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), WHITE);
    }
    else
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), RED);//RED FOR NOT FOUND
        printf("|-----------------------------------------------------------------|\n");
        printf("|---                 ---  SEARCH RESULTS  ---                  ---|\n");
        printf("|-----------------------------------------------------------------|\n");
        printf("|--                         NOT FOUND                           --|\n");
        printf("|_|_____________________________________________________________|_|\n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), WHITE);
    }

    printf("\n Press any key to Return to menu...");
    getch();
    system("cls");
}

void gameDisplay(Game gm)
{
    system("cls");

    printf(" _________________________________________________________________\n");
    printf("|-----------------------------------------------------------------|\n");
    printf("|--                     -- GAME STATS --                        --|\n");
    printf("|-----------------------------------------------------------------|\n");
    printf("|--               SET NUMBER     | %d                           --|\n",gm.setNum);
    printf("|-----------------------------------------------------------------|\n");
    printf("|--           CAMPION STATS   --   OPPONENT STAT                --|\n");
    printf("|-- POINTS            | %d | %d                                 --|\n",gm.points1, gm.points2);
    printf("|-- TIMEOUTS USED     | %d | %d                                 --|\n",gm.timeOut1, gm.timeOut2);
    printf("|-- SUBSTITUTIONS USED| %d | %d                                 --|\n",gm.subs1, gm.subs2);
    printf("|_|_____________________________________________________________|_|\n");

    system("pause");
    system("cls");

}

void readGameStat(Game gm)
{
    gm.setNum = 1;
    gm.points1 = 0;
    gm.points2 = 0;
    gm.timeOut1 = 0;
    gm.timeOut2 = 0;
    gm.subs1 = 0;
    gm.subs2 = 0;
}
