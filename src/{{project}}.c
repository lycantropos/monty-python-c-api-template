#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyModuleDef _{{project}}_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "{{project}}",
    .m_doc = PyDoc_STR("{{description}}"),
    .m_size = -1,
};

PyMODINIT_FUNC PyInit__{{project}}(void) {
  return PyModule_Create(&_{{project}}_module);
}
