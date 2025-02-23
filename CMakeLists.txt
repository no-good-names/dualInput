cmake_minimum_required(VERSION 3.30)
project(DualInput C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Rewrite this later
file(GLOB_RECURSE SERVER_SOURCE_FILES "server/*.c" "server/*.h")
file(GLOB_RECURSE CLIENT_SOURCE_FILES "client/*.c" "server/*.h")

add_executable(server ${SERVER_SOURCE_FILES})
add_executable(client ${CLIENT_SOURCE_FILES})

target_link_libraries(server pthread)
target_link_libraries(client pthread)

