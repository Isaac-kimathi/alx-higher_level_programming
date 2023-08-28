#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, x;
	PyObject *lmnt;
	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);
		for (x = 0; x < size; x++)
		{
			lmnt = PyList_GetItem(p, x);
			printf("Element %zd: ", x);
			if (PyBytes_Check(lmnt))
			{
				printf("bytes\n");
			}
			else if (PyFloat_Check(lmnt))
			{
				printf("float\n");
			}
			else if (PyLong_Check(lmnt))
			{
				printf("int\n");
			}
			else
			{
			printf("%s\n", Py_TYPE(lmnt)->tp_name);
			}
		}
	}
	else
	{
		printf("[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, x;
	const char *dt;

	if (PyBytes_Check(p))
	{
		size = PyBytes_GET_SIZE(p);
		dt = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", dt);
		rintf("  first %d bytes: ", size > 10 ? 10 : (int)size);
		for (x = 0; x < (size > 10 ? 10 : size); x++)
		{
			printf("%02x", (unsigned char)data[x]);
			if (x != (size > 10 ? 9 : size - 1))
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	double val;
	if (PyFloat_Check(p))
	{
		double val = PyFloat_AS_DOUBLE(p);
		printf("[.] float object info\n");
		printf("  value: %f\n", val);
	}
	else
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
	}
}
