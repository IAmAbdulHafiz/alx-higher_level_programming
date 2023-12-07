#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int size, alloc, index;
    PyObject *list_item;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List items = %d\n", size);
    printf("[*] Allocated is = %d\n", alloc);

    for (index = 0; index < size; index++)
    {
        printf("Element %d: ", index);

        list_item = PyList_GetItem(p, index);
        printf("%s\n", Py_TYPE(list_item)->tp_name);
    }
}
