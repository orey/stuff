#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100 // Maximum number of elements in the map

int size = 0; // Current number of elements in the map
char keys[MAX_SIZE][100]; // Array to store the keys
int values[MAX_SIZE]; // Array to store the values

// Function to get the index of a key in the keys array
int getIndex(char key[])
{
  for (int i = 0; i < size; i++) {
    if (strcmp(keys[i], key) == 0) {
      return i;
    }
  }
  return -1; // Key not found
}

// Function to insert a key-value pair into the map
void insert(char key[], int value)
{
  int index = getIndex(key);
  if (index == -1) { // Key not found
    strcpy(keys[size], key);
    values[size] = value;
    size++;
  }
  else { // Key found
    values[index] = value;
  }
}

// Function to get the value of a key in the map
int get(char key[])
{
  int index = getIndex(key);
  if (index == -1) { // Key not found
    return -1;
  }
  else { // Key found
    return values[index];
  }
}

// Function to print the map
void printMap()
{
  for (int i = 0; i < size; i++) {
    printf("%s: %d\n", keys[i], values[i]);
  }
}

void test(){
  int a = 12;
  int* ptr = &a;
  printf("Length of ptr: %d\n", sizeof(ptr));
}


int main()
{
  insert("Geeks", 5);
  insert("GFG", 3);
  insert("GeeksforGeeks", 7);

  printf("Value of complete Map: \n");
  printMap();
  
  printf("\nValue of apple: %d\n", get("GFG"));
  printf("Index of GeeksforGeeks: %d\n",
         getIndex("GeeksforGeeks"));
  printf("==============================\n");
  test();
    
  
  return 0;
}

