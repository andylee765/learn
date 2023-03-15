/* kmp search */
#include "template/head.h"

void getlps(const char *s, int lps[])
{
	int len = Strlen(s);
	int i, j;

	lps[0] = 0;
	for (i = 1, j = 0; i < len; )
	{
		if (s[i] == s[j])
		{
			++j;
			lps[i] = j;
			++i;
		}
		else if (j != 0)
			j = lps[j - 1];
		else
		{
			lps[i] = 0;
			++i;
		}
	}
}
int kmp_search(const char *dest, const char *sub)
{
	int d, s;
	int d_len = Strlen(dest), s_len = Strlen(sub);
	int *lps;

	lps = (int *) malloc(s_len * sizeof(int));
	if (lps == NULL)
		return -1;
	getlps(sub, lps);
	for (d = s = 0; d < d_len && s < s_len;  )
	{
		if (dest[d] == sub[s])
		{
			++d;
			++s;
		}
		else if (s != 0)
			s = lps[s - 1];
		else
			++d;
	}
	free(lps);
	if (s == s_len)
		return d - s;
	return -1;
}