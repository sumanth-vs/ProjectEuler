//Shorest Distance Program


#include <bits/stdc++.h> 
using namespace std; 

// Fixing Values of N and M
#define N 4 
#define M 4 


// new class
class Item {
public: 
	int r; 
	int c; 
	int dist; 
	Item(int x, int y, int w) 
		: r(x), c(y), dist(w) 
	{ 
	} 
}; 

int Final_destination(char grid[N][M]) 
{ 
    //returns -1, finds shortest path in grid
	Item sor(0, 0, 0); 
 
	bool visited[N][M]; 
	for (int i = 0; i < N; i++) { 
		for (int j = 0; j < M; j++) 
		{ 
			if (grid[i][j] == '0') 
				visited[i][j] = true; 
			else
				visited[i][j] = false; 

			if (grid[i][j] == 's') 
			{ 
			sor.r = i; 
			sor.c = j; 
			} 
		} 
	} 

	queue<Item> q; 
	q.push(sor); 
	visited[sor.r][sor.c] = true; 
	while (!q.empty()) { 
		Item p = q.front(); 
		q.pop(); 

		// IF destination found; 
		if (grid[p.r][p.c] == 'd') 
			return p.dist; 

		// Going up 
		if (p.r - 1 >= 0 && 
			visited[p.r - 1][p.c] == false) { 
			q.push(Item(p.r - 1, p.c, p.dist + 1)); 
			visited[p.r - 1][p.c] = true; 
		} 

		// Going down
		if (p.r + 1 < N && 
			visited[p.r + 1][p.c] == false) { 
			q.push(Item(p.r + 1, p.c, p.dist + 1)); 
			visited[p.r + 1][p.c] = true; 
		} 

		// Going to the left
		if (p.c - 1 >= 0 && 
			visited[p.r][p.c - 1] == false) { 
			q.push(Item(p.r, p.c - 1, p.dist + 1)); 
			visited[p.r][p.c - 1] = true; 
		} 

		// Going to the right
		if (p.c + 1 < M && 
			visited[p.r][p.c + 1] == false) { 
			q.push(Item(p.r, p.c + 1, p.dist + 1)); 
			visited[p.r][p.c + 1] = true; 
		} 
	} 
	return -1; 
} 

int main() 
{ 
	char doubleDimArray[N][M] = { { '0', '*', '0', 's' }, 
                        { '', '0', '', '*' }, 
                        { '0', '', '', '*' }, 
                        { 'd', '', '', '*' } };

	cout << Final_destination(doubleDimArray); 
	return 0; 
}