#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define FOOBAR_EXPORT __declspec(dllexport)
#else
  #define FOOBAR_EXPORT
#endif

FOOBAR_EXPORT void foobar();
FOOBAR_EXPORT void foobar_print_vector(const std::vector<std::string> &strings);
