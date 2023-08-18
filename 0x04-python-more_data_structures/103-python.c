#include <stdio.h>
#include <python.h>

/**
 * print_python_bytes - prints python bytes information
 *
 * @p: python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int sz, x, thr;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", sz);
	printf("  trying string: %s\n", str);

	if (sz >= 10)
		thr = 10;
	else
		thr = sz + 1;
	printf("  first %ld bytes:", thr);
	x = 0;
	for (; x < thr; x++)
		if (str[x] >= 0)
			printf(" %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);
	printf("\n");
}

/**
 * print_python_list - Prints python list information
 *
 * @p: python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *xp;
	long int sz, x;
	PyListObject *lt;

	sz = ((PyVarObject *)(p))->ob_size;
	lt = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", lt->allocated);
	x = 0;
	for (x < sz; x++){
		xp = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((xp)->ob_type)->tp_name);
		if (PyBytes_Check(xp))
			print_python_bytes(xp);
	}
}

