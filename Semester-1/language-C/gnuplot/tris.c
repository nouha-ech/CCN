#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// TRI À BULLES 
void triBulles(int *tab, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (tab[j] > tab[j + 1]) {
                int temp = tab[j];
                tab[j] = tab[j + 1];
                tab[j + 1] = temp;
            }
        }
    }
}

//  TRI PAR INSERTION
void triInsertion(int *tab, int n) {
    for (int i = 1; i < n; i++) {
        int cle = tab[i];
        int j = i - 1;
        while (j >= 0 && tab[j] > cle) {
            tab[j + 1] = tab[j];
            j--;
        }
        tab[j + 1] = cle;
    }
}

//  TRI PAR SÉLECTION
void triSelection(int *tab, int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (tab[j] < tab[min_idx]) {
                min_idx = j;
            }
        }
        int temp = tab[min_idx];
        tab[min_idx] = tab[i];
        tab[i] = temp;
    }
}

//  TRI RAPIDE (QUICK SORT) 
int partition(int *tab, int bas, int haut) {
    int pivot = tab[haut];
    int i = bas - 1;
    
    for (int j = bas; j < haut; j++) {
        if (tab[j] < pivot) {
            i++;
            int temp = tab[i];
            tab[i] = tab[j];
            tab[j] = temp;
        }
    }
    int temp = tab[i + 1];
    tab[i + 1] = tab[haut];
    tab[haut] = temp;
    return i + 1;
}

void triRapideRecursif(int *tab, int bas, int haut) {
    if (bas < haut) {
        int pi = partition(tab, bas, haut);
        triRapideRecursif(tab, bas, pi - 1);
        triRapideRecursif(tab, pi + 1, haut);
    }
}

void triRapide(int *tab, int n) {
    triRapideRecursif(tab, 0, n - 1);
}

// TRI FUSION (MERGE SORT)
void fusionner(int *tab, int gauche, int milieu, int droite) {
    int n1 = milieu - gauche + 1;
    int n2 = droite - milieu;
    
    int *G = (int *)malloc(n1 * sizeof(int));
    int *D = (int *)malloc(n2 * sizeof(int));
    
    for (int i = 0; i < n1; i++)
        G[i] = tab[gauche + i];
    for (int j = 0; j < n2; j++)
        D[j] = tab[milieu + 1 + j];
    
    int i = 0, j = 0, k = gauche;
    while (i < n1 && j < n2) {
        if (G[i] <= D[j]) {
            tab[k] = G[i];
            i++;
        } else {
            tab[k] = D[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        tab[k] = G[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        tab[k] = D[j];
        j++;
        k++;
    }
    
    free(G);
    free(D);
}

void triFusionRecursif(int *tab, int gauche, int droite) {
    if (gauche < droite) {
        int milieu = gauche + (droite - gauche) / 2;
        triFusionRecursif(tab, gauche, milieu);
        triFusionRecursif(tab, milieu + 1, droite);
        fusionner(tab, gauche, milieu, droite);
    }
}

void triFusion(int *tab, int n) {
    triFusionRecursif(tab, 0, n - 1);
}

//  TRI SHELL
void triShell(int *tab, int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = tab[i];
            int j;
            for (j = i; j >= gap && tab[j - gap] > temp; j -= gap) {
                tab[j] = tab[j - gap];
            }
            tab[j] = temp;
        }
    }
}

//  TIMSORT
#define RUN 32

void triInsertionTimSort(int *tab, int gauche, int droite) {
    for (int i = gauche + 1; i <= droite; i++) {
        int temp = tab[i];
        int j = i - 1;
        while (j >= gauche && tab[j] > temp) {
            tab[j + 1] = tab[j];
            j--;
        }
        tab[j + 1] = temp;
    }
}

void fusionnerTimSort(int *tab, int g, int m, int d) {
    int len1 = m - g + 1, len2 = d - m;
    int *gauche = (int *)malloc(len1 * sizeof(int));
    int *droite = (int *)malloc(len2 * sizeof(int));
    
    for (int i = 0; i < len1; i++)
        gauche[i] = tab[g + i];
    for (int i = 0; i < len2; i++)
        droite[i] = tab[m + 1 + i];
    
    int i = 0, j = 0, k = g;
    while (i < len1 && j < len2) {
        if (gauche[i] <= droite[j]) {
            tab[k] = gauche[i];
            i++;
        } else {
            tab[k] = droite[j];
            j++;
        }
        k++;
    }
    
    while (i < len1) {
        tab[k] = gauche[i];
        k++;
        i++;
    }
    
    while (j < len2) {
        tab[k] = droite[j];
        k++;
        j++;
    }
    
    free(gauche);
    free(droite);
}

void timSort(int *tab, int n) {
    for (int i = 0; i < n; i += RUN)
        triInsertionTimSort(tab, i, (i + RUN - 1) < (n - 1) ? (i + RUN - 1) : (n - 1));
    
    for (int size = RUN; size < n; size = 2 * size) {
        for (int start = 0; start < n; start += 2 * size) {
            int milieu = start + size - 1;
            int fin = (start + 2 * size - 1) < (n - 1) ? (start + 2 * size - 1) : (n - 1);
            
            if (milieu < fin)
                fusionnerTimSort(tab, start, milieu, fin);
        }
    }
}


void remplirTableauAleatoire(int *tab, int n) {
    for (int i = 0; i < n; i++) {
        tab[i] = rand() % 1000000;
    }
}

double mesurer_temps(void (*fonction_tri)(int*, int), int *tab, int n) {
    int *copie = (int *)malloc(n * sizeof(int));
    memcpy(copie, tab, n * sizeof(int));
    clock_t debut = clock();
    fonction_tri(copie, n);
    clock_t fin = clock();
    free(copie);
    return ((double)(fin - debut)) / CLOCKS_PER_SEC;
}

int main() {
    FILE *fp = fopen("resultats_tri.dat", "w");
    if (fp == NULL) {
        printf("Erreur: Impossible de créer le fichier de résultats!\n");
        return 1;
    }
    
    // En-tête du fichier de données
    fprintf(fp, "# Taille Bulles Insertion Selection Rapide Fusion Shell TimSort\n");
    
    srand(time(NULL));
    
    
    // Tailles à tester
    int tailles[] = {1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1000000};
    int nb_tailles = sizeof(tailles) / sizeof(tailles[0]);
    
    for (int t = 0; t < nb_tailles; t++) {
        int n = tailles[t];
        printf("► Test avec taille = %d éléments...\n", n);
        
        int *tableau = (int *)malloc(n * sizeof(int));
        remplirTableauAleatoire(tableau, n);
        
        fprintf(fp, "%d ", n);
        
        // Tri à Bulles (limité à 64000 pour éviter les temps trop longs)
        if (n <= 64000) {
            double temps = mesurer_temps(triBulles, tableau, n);
            fprintf(fp, "%.6f ", temps);
            printf("  • Tri à Bulles     : %.6f s\n", temps);
        } else {
            fprintf(fp, "NaN ");
            printf("  • Tri à Bulles     : [Trop lent - ignoré]\n");
        }
        
        // Tri par Insertion (limité à 64000)
        if (n <= 64000) {
            double temps = mesurer_temps(triInsertion, tableau, n);
            fprintf(fp, "%.6f ", temps);
            printf("  • Tri par Insertion: %.6f s\n", temps);
        } else {
            fprintf(fp, "NaN ");
            printf("  • Tri par Insertion: [Trop lent - ignoré]\n");
        }
        
        // Tri par Sélection (limité à 64000)
        if (n <= 64000) {
            double temps = mesurer_temps(triSelection, tableau, n);
            fprintf(fp, "%.6f ", temps);
            printf("  • Tri par Sélection: %.6f s\n", temps);
        } else {
            fprintf(fp, "NaN ");
            printf("  • Tri par Sélection: [Trop lent - ignoré]\n");
        }
        
        // Tri Rapide
        double temps_rapide = mesurer_temps(triRapide, tableau, n);
        fprintf(fp, "%.6f ", temps_rapide);
        printf("  • Tri Rapide       : %.6f s\n", temps_rapide);
        
        // Tri Fusion
        double temps_fusion = mesurer_temps(triFusion, tableau, n);
        fprintf(fp, "%.6f ", temps_fusion);
        printf("  • Tri Fusion       : %.6f s\n", temps_fusion);
        
        // Tri Shell
        double temps_shell = mesurer_temps(triShell, tableau, n);
        fprintf(fp, "%.6f ", temps_shell);
        printf("  • Tri Shell        : %.6f s\n", temps_shell);
        
        // TimSort
        double temps_timsort = mesurer_temps(timSort, tableau, n);
        fprintf(fp, "%.6f", temps_timsort);
        printf("  • TimSort          : %.6f s\n", temps_timsort);
        
        fprintf(fp, "\n");
        printf("\n");
        
        free(tableau);
    }
    
    fclose(fp);
    
    return 0;
}