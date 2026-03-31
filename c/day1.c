#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** read_file(int* count) {
	FILE *file;

	file = fopen("puzzle_input/day1.txt", "rb");
	fseek(file, 0l, SEEK_END);
	size_t file_size = ftell(file);
	printf("size: %zu\n", file_size);
	rewind(file);
	file = fopen("puzzle_input/day1.txt", "r");

	char** str = (char**) malloc(file_size * sizeof(char*));
	char buf[256];

	int i = 0;
	while (fgets(buf, sizeof(buf), file) != NULL) {
		str[i] = malloc(strlen(buf) + 1);
		strcpy(str[i], buf);
		i++;
	}
	fclose(file);
	*count = i;
	return str;
}

long int sum(long int *arr, size_t size) {
	long int s = 0;
	for (int i = 0; i < size; i++) {
		s += arr[i];
	}
	return s;
} 

int main(void) {
	printf("Hello world!\n");
	int len;
	char **str = read_file(&len);
	long int *arr = malloc(len * sizeof(long int));
	int counter = 0;
	char *endptr;
	for (int i = 0; i < len; i++) {
		printf("count: %d, string:%s\n", counter, str[i]);
		if (str[i][0] == '\n') {
			break;
		}
		arr[i] = strtol(str[i], &endptr, 10);
		counter++;
	}
	printf("%ld\n", sum(arr, counter));
 }
