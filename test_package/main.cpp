#include "foobar.h"
#include <vector>
#include <string>

int main() {
    foobar();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    foobar_print_vector(vec);
}
