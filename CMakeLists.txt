cmake_minimum_required(VERSION 3.28.1)

project(C_Lambdas)

add_executable(
    ${PROJECT_NAME}
    ${PROJECT_SOURCE_DIR}/Main.c
    ${PROJECT_SOURCE_DIR}/Lambda.h
)

target_compile_options(${PROJECT_NAME} PRIVATE -fms-extensions)
set_property(TARGET ${PROJECT_NAME} PROPERTY C_STANDARD 23)