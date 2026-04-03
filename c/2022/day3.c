#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
	char key;
	int value;
} Alphabet;


Alphabet* linear_search(Alphabet *letters, size_t size, char key) {
	for (size_t i = 0; i < size; i++) {
		if (letters[i].key == key) {
			return &letters[i];
		}
	}
	return NULL;
}

char** read_input(int *count) {
	FILE *file;
	file = fopen("puzzle_input/day3.txt", "rb");

	// Check if the file opening succeded, if so crash the program
	if (file == NULL) {
		fprintf(stderr, "Error opening file: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	fseek(file, 0, SEEK_END);
	long size = ftell(file);
	rewind(file);
	char** str = (char**)malloc(size * sizeof(char*));
	char buf[256];
	int i = 0;
	
	while (fgets(buf, sizeof(buf), file) != NULL) {
		str[i] = malloc(strlen(buf) + 1);
		strcpy(str[i], buf);
		i++;
	}
	*count = i;
	fclose(file);
	return str;
}

char rucksack(char* str, int len) {
	char arr;
	int counter = 0;
	for (int i = 0; i < len / 2; i++) {
		for (int j = len / 2; j < len; j++) {
			if (str[i] == str[j]) {
				arr = str[i];
			}
		}
	}
	return arr;
}



int main(void) {
	int len;
	char** str = read_input(&len);
	char* alphs= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char* common_chars = malloc(len * sizeof(char*));
	for (int i = 0; i < len; i++) {
		common_chars[i] = rucksack(str[i], strlen(str[i]));	
	}
	printf("%c\n", common_chars[1]);

	Alphabet alph[] = {
	    {'a', 1}, {'b', 2}, {'c', 3}, {'d', 4}, {'e', 5}, {'f', 6}, {'g', 7}, 
	    {'h', 8}, {'i', 9}, {'j', 10}, {'k', 11}, {'l', 12}, {'m', 13}, 
	    {'n', 14}, {'o', 15}, {'p', 16}, {'q', 17}, {'r', 18}, {'s', 19}, 
	    {'t', 20}, {'u', 21}, {'v', 22}, {'w', 23}, {'x', 24}, {'y', 25}, 
	    {'z', 26},
	    {'A', 27}, {'B', 28}, {'C', 29}, {'D', 30}, {'E', 31}, {'F', 32}, 
	    {'G', 33}, {'H', 34}, {'I', 35}, {'J', 36}, {'K', 37}, {'L', 38}, 
	    {'M', 39}, {'N', 40}, {'O', 41}, {'P', 42}, {'Q', 43}, {'R', 44}, 
	    {'S', 45}, {'T', 46}, {'U', 47}, {'V', 48}, {'W', 49}, {'X', 50}, 
	    {'Y', 51}, {'Z', 52}
	};
	size_t alph_size = sizeof(alph) / sizeof(Alphabet);
	int s = 0;
	for (int k = 0; k < len; k++) {
		s += linear_search(alph, alph_size, common_chars[k])->value;
	}
	printf("%d\n", s);

}
