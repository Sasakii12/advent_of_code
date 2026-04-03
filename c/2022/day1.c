#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <errno.h>

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

long int* max_of_three(long int *arr, int len) {

	if (len < 3) {
		return NULL;
	}

	long int fst = LONG_MIN, sec = LONG_MIN, thd = LONG_MIN;
	long int *max_arr = malloc(3 * sizeof(long int));

	for (int i = 0; i < len; i++) {
		if (fst < arr[i]) {
			fst = arr[i];
		}
	}

	for (int j = 0; j < len; j++) {
		if (sec < arr[j] && arr[j] != fst) {
			sec = arr[j];
		}
	}
	
	for (int k = 0; k < len; k++) {
		if (thd < arr[k] && arr[k] != sec && arr[k] != fst) {
			thd = arr[k];
		}
	}
	max_arr[0] = fst;
	max_arr[1] = sec;
	max_arr[2] = thd;
	return max_arr;
}

long int* arr_of_max(char** str, int len, int* max_len) {
	char *endptr; 
	long int *arr_buf = malloc(len * sizeof(long int));
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

		// Handle cases where the input is not a number
		if (endptr == str[i]) {
			printf("No diigits found\n");
			return NULL;
		} else if (*endptr == '\0') {
			printf("Invalid character %c\n", *endptr);
			return NULL;
		}

		counter++; }
	*max_len = sum_counter;
	return arr_of_max;
}

int main(void) {
	int len;
	int max_len;
	char **str = read_input(&len);
	long int *arr_max = arr_of_max(str, len,&max_len);
	if (arr_max == NULL) {
		exit(EXIT_FAILURE);
	}
	long int max = max_of_arr(arr_max, max_len);
	printf("max: %ld\n", max);
	long int *max_three = max_of_three(arr_max, max_len);
	printf("max of three: %ld, %ld, %ld\n",max_three[0], max_three[1], max_three[2]);
	printf("Sum of max threes: %ld\n", sum(max_three, 3));
	
	free(max_three);
	free(str);
	free(arr_max);
}
