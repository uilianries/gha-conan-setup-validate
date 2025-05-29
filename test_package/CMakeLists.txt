cmake_minimum_required(VERSION 3.10)
project(test_package LANGUAGES CXX)

find_package(foobar REQUIRED CONFIG)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE foobar::foobar)
