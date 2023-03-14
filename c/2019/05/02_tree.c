/* tree.c */
#include "template/head.h"

typedef struct tree tree;
struct tree 
{
	char *word;
	int count;
	tree *left, *right;
};
tree *tree_upd(tree *root, const char *word)
{
	int r;

	if (root == NULL)
	{
		root = (tree *) malloc(sizeof(*root));
		if (root == NULL || (root->word = Strdup(word)) == NULL)
			return NULL;
		root->count = 1;
		root->left = root->right = NULL;
	}
	else
	{
		r = Strcmp(word, root->word);
		if (r < 0)
			root->left = tree_upd(root->left, word);
		else if (r > 0)
			root->right = tree_upd(root->right, word);
		else
			++root->count;
	}
	return root;
}
void tree_prn(tree *root)
{
	if (root == NULL)
		return;
	tree_prn(root->left);
	printf("count: %3d, word: %s\n", root->count, root->word);
	tree_prn(root->right);
}
void file_tree(FILE *fp)
{
	char buf[300];
	int size = sizeof(buf);
	tree *root = NULL;

	while (Getword(buf, size, fp) != EOF)
		if (Isalpha(*buf))
			root = tree_upd(root, buf);
	tree_prn(root);
}
typedef struct table table;
struct table 
{
	char *word, *def;
	int count;
	table *next;
};
unsigned Hash(const char *word, int size)
{
	unsigned val;

	for (val = 0; *word != '\0'; ++word)
		val = 31 * val + *word;
	return val % size;
}
table *tab_seek(table *list[], int nlist, const char *word)
{
	unsigned h;
	table *p;

	h = Hash(word, nlist);
	for (p = list[h]; p != NULL; p = p->next)
		if (Strcmp(p->word, word) == 0)
			return p;
	return NULL;
}
table *tab_upd(table *list[], int nlist, const char *word, const char *def)
{
	unsigned h;
	table *p;

	p = tab_seek(list, nlist, word);
	if (p == NULL)
	{
		p = (table *) malloc(sizeof(*p));
		if (p == NULL || (p->word = Strdup(word)) == NULL)
			return NULL;
		h = Hash(word, nlist);
		p->next = list[h];
		list[h] = p;
		p->count = 1;
	}
	else
	{
		free(p->def);
		++p->count;
	}
	if ((p->def = Strdup(def)) == NULL)
		return NULL;
	return p;
}
void tab_prn(table *list[], int nlist)
{
	int i, j;
	table *p;

	for (i = 0; i < nlist; ++i)
		for (p = list[i], j = 1; p != NULL; p = p->next, ++j)
			printf("[%3d-%d] Count: %3d, Word: %-30s, Def: %s\n", i, j, p->count, p->word, p->def);
}
void file_table(FILE *fp)
{
	table *list[199];
	int nlist = sizeof(list) / sizeof(*list);
	char buf[300];
	int bsize = sizeof(buf);
	int i;

	for (i = 0; i < nlist; ++i)
		list[i] = NULL;
	while (Getword(buf, bsize, fp) != EOF)
		if (Isalpha(*buf))
			tab_upd(list, nlist, buf, "001132");
	tab_prn(list, nlist);
}