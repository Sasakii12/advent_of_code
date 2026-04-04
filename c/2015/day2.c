#include <ctype.h>
#include <stdio.h>
#include <stddef.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>



char** sv_split(char* str, char* delim, int *count) {
	char* str_copy = malloc((sizeof(str)));
	strcpy(str_copy, str);
	size_t delim_count = 0;
	for (size_t i = 0; i < strlen(str_copy); i++) if (str_copy[i] == *delim) delim_count++;
	char** result = malloc((delim_count * 1) * sizeof(char**));
	char *buf = strtok(str_copy, delim);
	for (size_t i = 0; i < delim_count + 1; i++ ) {
		result[i] = malloc(sizeof(char*) * 2);
		int j = 0;

		// Only need to trim from the left for this problem
		while (isspace(buf[j])) j++;

		result[i] = j + buf;
		buf = strtok(NULL, delim);
	}
	*count = delim_count + 1;
	return result;
}


char** read_input(int *count) {
	FILE *file;
	file = fopen("puzzle_input/day2.txt", "rb");

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

int* str_to_int_arr(char **arr, int len) {
	if (len == 0) {
		return NULL;
	}
	int* new_arr = malloc(len * sizeof(int));
	for (int i = 0; i < len; i++) {
		new_arr[i] = strtol(arr[i], NULL, 10);
	}
	return new_arr;
}



int min_side(int l, int w, int h) {
	// These conversion are fine because the mathmatical formula
	// always returns an integer
	int min_wh = (int) ((1./2.) * (w + h - abs(w - h)));
	int min_awh = (int) ((1./2.) * (l + min_wh - abs(l - min_wh)));
	return min_awh;
}

// Day 1
int calc_rect(char **input, int count) {
	int split_len = 0;
	int factor = 2;
	long int final_sum = 0;
	for (int i = 0; i < count; i++) {
		char **split = sv_split(input[i], "x", &split_len);
		if (split_len < 3) break;
		int *int_split = str_to_int_arr(split, split_len);

		int l = int_split[0];
		int w = int_split[1];
		int h = int_split[2];

		int lw = l * w, wh = w * h, hl = h * l;
		int min_fact = min_side(lw, wh, hl);
		
		long int res = (factor * lw) + (factor * wh) + (factor * hl) + min_fact;
		final_sum += res;

		free(split);
		free(int_split);
	}

	return final_sum;
}

int min(int a, int b) {
	return a < b ? a : b;
}

// Day 2
int calc_rect2(char **input, int count) {
	int split_len = 0;
	int factor = 2;
	long int final_sum = 0;
	for (int i = 0; i < count; i++) {
		char **split = sv_split(input[i], "x", &split_len);
		if (split_len < 3) break;
		int *int_split = str_to_int_arr(split, split_len);

		int l = int_split[0];
		int w = int_split[1];
		int h = int_split[2];
		
		int fst_min = min_side(l,w,h);
		int scd_min = 0;
		if (fst_min == l) scd_min = min(w,h);
		else if (fst_min == w) scd_min = min(l,h);
		else scd_min = min(w, l);

		final_sum += (l * w * h) + (2 * (fst_min + scd_min));


		free(split);
		free(int_split);
	}

	return final_sum;
}

int main(void) {
	int count = 0;
	char **inp = read_input(&count);
	printf("%d\n",calc_rect(inp,count));
	printf("%d\n",calc_rect2(inp,count));

	free(inp);
}


