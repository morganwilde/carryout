#include <stdlib.h>
#include <stdio.h>
#include <math.h>

long long powSafe(
	long base,
	long modulo,
	long long total
) {
	// This has complexity of O(1)
	// Regular pow() wouldn't work because of combined complexity O(n^2)
	// base - base number
	// modulo - the divisor, used to keep only the relevant portion of total
	// total - the value of variable^i-1, I.e.
	// 2^3 = 2*2*2 = 8 or
	// 2^3 = 2*2^2 = 8
	return (total * base) % modulo;
}

long long polyF(
	long x,
	long m,
	long coeffs[],
	int n
) {
	// loop through all coefficients, adding them up
	long long total = 0;
	long long totalTemp = 1; // number^0=1
	int i;
	for (i = 0; i <= n; i++) {
		if (i > 0) {
			// Since each term increases its power by one we can
			// carry over the product for the next term
			totalTemp = powSafe(x, m, totalTemp);

			// Output requires only the mod of the result, so to save space
			// mod each intermediate step
			total += (totalTemp * coeffs[i]) % m;
		}
		else
			total += coeffs[i] % m;
	}

	return total % m;
}

int main() {
	FILE *fileI = fopen("poly.in", "r");
	FILE *fileO = fopen("poly.out", "w+");

	// Read the the first line
	// n - degree of the polynomial, range [0, 1000]
	// k - number of argument values to evaluate, range [0, 1000]
	int n, k;
	fscanf(fileI, "%d %d", &n, &k);	
	//printf("n=[%d], k=[%d]\n", n, k);

	// Read the second line
	// Number of arguments to be read - n+1
	// coeff - coefficient of the polynomial, range [0, 10^9]
	int i;
	long coeff, coeffs[n+1];
	for (i = 0; i < (n+1); i++) {
		fscanf(fileI, "%ld", &coeff);
		coeffs[i] = coeff;
	}

	// Read the rest of the document
	// Number of lines to be read - k
	// x - polynomial variable, range [0, 10^9]
	// m - mod value, range [1, 10^9]
	int line;
	long x, m;
	long long polyValue;
	for (line = 0; line < k; line++) {
		fscanf(fileI, "%ld %ld", &x, &m);
		polyValue = polyF(x, m, coeffs, n);
		fprintf(fileO, "%lld\n", polyValue);
		//printf("x=[%ld], m=[%ld], value=[%lld]\n", x, m, polyValue);
	}

	// Close resources
	fclose(fileI);
	fclose(fileO);

	return 0;
}
