#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** read_input(int *count) {
	FILE *file;
	file = fopen("puzzle_input/day1.txt", "rb");
	fseek(file, 0, SEEK_END);
	size_t size = ftell(file);
	rewind(file);

	char** str = (char**)malloc(size * sizeof(char*));
	char buf[256];
	int i = 0;
	
	while (fgets(buf, 256, file) != NULL) {
		str[i] = malloc(strlen(buf) + 1);
		strcpy(str[i], buf);
		i++;
	}
	*count = i;
	return str;
}

long int sum(long int *arr, int len) {
	int s = 0;
	for (int i = 0; i < len; i++) {
		s += arr[i];
	}
	return s;
}

long int max_of_arr(long int *arr, int len) {
	long int max_of_arr = arr[0];
	for (int i = 1; i < len; i++) {
		if (max_of_arr < arr[i]) {
			max_of_arr = arr[i];
		}
	}
	return max_of_arr;
}

long int* arr_of_max(char** str, int len, int* max_len) {
	char *endptr; 
	long int *arr_buf = malloc(10 * sizeof(long int));
	int sum_counter = 0;
	int counter = 0;
	long int *arr_of_max = malloc(len * sizeof(long int));
	for (int i = 0; i < len; i++) {		
		if (str[i][0] == '\n') {
			arr_of_max[sum_counter] = sum(arr_buf, counter);
			counter = 0;
			sum_counter++;
			continue;
		}
		arr_buf[counter] = strtol(str[i], &endptr, 10);
		if (endptr == str[i]) {
			printf("No diigits found\n");
			return NULL;
		} else if (*endptr == '\0') {
			printf("Invalid character %c\n", *endptr);
			return NULL;
		}
		counter++; }
	*max_len = sum_counter;
	return arr_buf;
}

int main(void) {
	int len;
	int max_len;
	char **str = read_input(&len);
	long int *arr_max = arr_of_max(str, len,&max_len);
	long int max = max_of_arr(arr_max, max_len);
	printf("%ld\n", max);

	free(str);
	free(arr_max);
}
