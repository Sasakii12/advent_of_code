#include <stddef.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	char key;
	int value;
} hash_table;

int linear_search(hash_table *table, char key, size_t size) {
	for (size_t i = 0; i < size; i++) {
		if (table[i].key == key) return table[i].value;
	}
	return 0;
}

char** read_input(int *count) {
	FILE *file;
	file = fopen("puzzle_input/day1.txt", "rb");

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

int calc_stairs(char** str, int str_count) {
	int floor = 0;
	int char_counter = 0;

	hash_table direction[] = {{'(', 1}, {')', -1}};
	size_t table_size = sizeof(direction) / sizeof(direction[0]);
	for (int i = 0; i < str_count; i++) {
		while (str[i][char_counter] != '\0') {
			floor += linear_search(direction, str[i][char_counter],table_size);
			char_counter += 1;
		}
		char_counter = 0;
	}
	return floor;
}

int main(void) {
	int input_count;
	char** str = read_input(&input_count);
	printf("%d\n", calc_stairs(str, input_count));

	free(str);
}
