#include <ctype.h>
#include <stdio.h>
#include <stddef.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>



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

typedef struct {
	int x;
	int y;
} grid;

int is_visisted(grid *visited ,grid* pos, int len) {
	if (len == 0) {
		return 0;
	}

	for (int i = 0; i < len; i++) {
		if (visited[i].x == pos->x && visited[i].y == pos->y) return 1;
	}
	return 0;
}

void update_pos(grid *pos, char dire) {
	if (dire == '>') {
		pos->x += 1;
	} else if (dire == '<') {
		pos->x -= 1;
	} else if (dire == '^') {
		pos->y += 1;
	} else if (dire == 'v') {
		pos->y -= 1;
	}
}

int navigate_grid(char** inp, int len) {
	int presents = 1;
	grid curr_pos = {0,0};	
	grid *nav_grid = malloc(len * (strlen(inp[0]) + 1) * sizeof(curr_pos));
	int grid_len = 1;

	nav_grid[0] = curr_pos;

	for (int i = 0; i < len; i++) {
		for (int k = 0; k < strlen(inp[i]); k++) {
			update_pos(&curr_pos, inp[i][k]);

			if (is_visisted(nav_grid, &curr_pos, grid_len)) {
				continue;
			}
			nav_grid[grid_len] = curr_pos;
			grid_len++;
			presents++;
			
		}
	}
	return presents;

}

int navigate_grid2(char** inp, int len) {
	int presents = 1;
	grid curr_pos1 = {0,0};	
	grid curr_pos2 = {0,0};
	grid *nav_grid = malloc(len * (strlen(inp[0]) + 1)* sizeof(curr_pos1));
	int grid_len = 1;

	nav_grid[0] = curr_pos1;
	

	for (int i = 0; i < len; i++) {
		for (int k = 0; k < strlen(inp[i]); k++) {
			if (k % 2 == 0) {
				update_pos(&curr_pos1, inp[i][k]); 
 
				if (is_visisted(nav_grid, &curr_pos1, grid_len)) { 
					continue; 
				} 
				nav_grid[grid_len] = curr_pos1; 
				grid_len++; 
				presents++; 
			}	
			else {
				update_pos(&curr_pos2, inp[i][k]); 
 
				if (is_visisted(nav_grid, &curr_pos2, grid_len)) { 
					continue; 
				} 
				nav_grid[grid_len] = curr_pos2; 
				grid_len++; 
				presents++; 

			}
		}
	}
	return presents;
}


int main(void) {
	printf("Hello, World!\n");
	int count;
	int count2;
	char** inp = read_input(&count);
	char ** inp2 = read_input(&count2);
	printf("Presents: %d\n", navigate_grid(inp, count));	
	printf("Presents: %d\n", navigate_grid2(inp2, count2));	
}
