/*
 * sort.c 
 */
#include "template/head.h"

void quicksort(int v[], int left, int right)
{
	int last, i;

	if (left >= right)
		return ;
	swap(v, left, (left / 2 + right / 2));
	last = left;
	for (i = left + 1; i <= right; ++i)
		if (v[i] < v[left])
			swap(v, ++last, i);
	swap(v, left, last);
	quicksort(v, left, last - 1);
	quicksort(v, last + 1, right);
}
void qksort(int v[], int n)
{
	quicksort(v, 0, n - 1);
}
void shsort(int v[], int n)
{
	int gap, i, j;

	for (gap = n / 2; gap > 0; gap /= 2)
		for (i = gap; i < n; ++i)
			for (j = i - gap; j >= 0 && v[j] > v[j + gap]; j -= gap)
				swap(v, j, j + gap);
}
void insort(int v[], int n)
{
	int temp, i, j;

	for (i = 1; i < n; ++i)
	{
		temp = v[i];
		for (j = i; j > 0 && temp < v[j - 1]; ++j)
			v[j] = v[j - 1];
		v[j] = temp;
	}
}
