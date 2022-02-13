#include <stdio.h>
#include <stdlib.h>

/*
 * This stores the total number of books in each shelf.
 */
int* total_number_of_books;
// pointed to nothing

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);

        //allocation of memory as shelves
        total_number_of_books = (int*) malloc( sizeof(int)* total_number_of_shelves );
        //pointed to the base of a chunk of memory of size - int * number of shelves
        //can access all the ints present in this chunk , by incrementing base pointer
        total_number_of_pages = (int**) calloc(total_number_of_shelves, sizeof(int*));


    // for(int i = 0 ; i < total_number_of_shelves; i++){
    //     printf(" here we are %d ", total_number_of_books[i]);
    // }

   // total_number_of_pages = *total_number_of_books;
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        
        if (type_of_query == 1) {
            /*
             * Process the query of first type here.
             */
            int x, y;
            scanf("%d %d", &x, &y);
        
            // printf("%d after ",  total_number_of_books[x] );

            // we must add y number of pages of that book
            if(total_number_of_books[x] == 0){
                 total_number_of_pages[x] = (int*) malloc(1* sizeof(int));
                *(*(total_number_of_pages + x) + 0 )=  y;
            }else{
                 total_number_of_pages[x] = (int*) realloc(total_number_of_pages[x], (total_number_of_books[x] + 1) * sizeof(int));
                *(*(total_number_of_pages + x) + (total_number_of_books[x]+ 1) )=  y;
            }
           

            // go to xth shelf and add a book to it
            // printf("%d before ",  total_number_of_books[x] );
            total_number_of_books[x] = total_number_of_books[x] + 1;
            printf("x = %d , total_number of books %dth shelf, %d ",x, x, total_number_of_books[x]);





            // increase the number of books in the xth shelf by 1
            // *(total_number_of_books + x) += 1;
            //*(total_number_of_books + x) = *(total_number_of_books + x) +1;

            

            //int *ptr = total_number_of_books + x;
            //ptr = (int*)realloc(ptr,sizeof(int));
            // increase the number of pages on the xth shelf by y
            //total_number_of_pages = realloc(void *__ptr, size_t __size)
    
        } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        free(total_number_of_books);
    }
    
    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            free(*(total_number_of_pages + i));
        }
    }
    
    if (total_number_of_pages) {
        free(total_number_of_pages);
    }
    
    return 0;
}