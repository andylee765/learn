/*
function: recurse, mprintf
*/
#define NEED_STRING
#include "0head.c"

void prnint(int n)
{
	if (n < 0)
	{
		putchar('-');
		n = -n;
	}
	if (n / 10 > 0)
		prnint(n / 10);
	putchar(n % 10 + '0');
}
void prnstr(const char *d, int n)
{
	if (s[n] != '\0')
	{
		putchar(s[n]);
		prnstr(s, n + 1);
	}
}
void prnstr2(const char *d)
{
	if (*s != '\0')
	{
		putchar(*s);
		prnstr2(s + 1);
	}
}
int fact(int n)
{
	if (n > 1)
		return fact(n - 1) * n;
	return 1;
}
void mprint(const char *fmt, ...)
{
	va_list ap;
	const char *p, *sval;
	int ival;
	double dval;

	va_start(ap, fmt);
	for (p = fmt; *p != '\0'; ++p)
	{
		if (*p != '%')
		{
			putchar(*p);
			continue;
		}
		switch (*++p)
		{
			case 'd':
				ival = va_arg(ap, int);
				printf("%d", ival);
				break;
			case 'f':
				dval = va_arg(ap, double);
				printf("%f", dval);
				break;
			case 's':
				for (sval = va_arg(ap, char *); *sval != '\0'; ++sval)
					putchar(*sval);
				break;
			default:
				putchar(*p);
				break;
		}
	}
	va_end(ap);
}

