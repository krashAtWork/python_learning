#include <stdio.h>
#include <stdlib.h>


void main(){
    
/*
 * This stores the total number of books in each shelf.
 */
int* total_number_of_books;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int** total_number_of_pages;

int n = 5;
total_number_of_books = (int*) calloc(n, sizeof(int));
for(int i = 0 ; i< 5 ; i++){
    printf("%d  value at the pointer \n", total_number_of_books[i]);
    printf("%p  hexadecimal address \n", total_number_of_books + i );
   // total_number_of_books[i] = 12 +i;
   // printf("%d  new value at pointer \n \n", total_number_of_books[i]);

}
 
// total_number_of_pages = &total_number_of_books;
total_number_of_pages = (int**) calloc(n, sizeof(int*));



for(int i = 0 ; i< n ;  i++){
    printf("%p value is an address \n", total_number_of_pages[i]);
    total_number_of_pages[i] = (int*) calloc(n , sizeof(int));
    // printf("%d value  of the value  is the value stored  \n", *total_number_of_pages[i]);
    // printf("%p \n", total_number_of_books + i );
    // total_number_of_books[i] = 12;
    // printf("%d \n", total_number_of_books[i]);

}

for(int i = 0 ; i <n ; i++){
    // first find the number of books in each shelf
    int count = total_number_of_books[i];
    if(count == 0){
        //increase the number of books by 1
        total_number_of_books[i]++ ;
        total_number_of_pages[i] = (int*) malloc(1 * sizeof(int));
        *(total_number_of_pages[i]) = 17;
        printf("%d \n",  *(*(total_number_of_pages +  i) + 0));
    }else{
        //increase the number of books by 1
        // total_number_of_books[i]++ ;
        //   total_number_of_pages[i] = (int*) realloc(1 * sizeof(int));
        // *(total_number_of_pages[i]) = 17;
    }
}

// for(int i = 0; i < n ; i++){
//     for(int j = 0 ; j< n; j++){
//         printf("%d ",*(*(total_number_of_pages + i) + j));
//     }
//     printf("\n");
// }



// for(int i = 0 ; i< 5 ; i++){
//     calloc(*total_number_of_pages, 1);
// }

}