#!/bin/python

import os
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("dirname", help="Dirname to create the project")
    parser.add_argument("path", help="Path to create project")
    args = parser.parse_args()
    
    dir = args.dirname
    path = args.path

    dir = path + "/" + dir
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.makedirs(dir + '/include')
        os.makedirs(dir + '/src')

        file = open(dir + '/CMakeLists.txt', 'w')
        file.write("# Auto generated by Nixsm\n" + 
                   "CMAKE_MINIMUM_REQUIRED(VERSION 2.8.9)\n\n" +
                   "project(" + args.dirname + ")\n\n" +
                   "include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)\n\n" +
                   "file(GLOB_RECURSE sources ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc)\n" +
                   "file(GLOB_RECURSE includes ${CMAKE_CURRENT_SOURCE_DIR}/include/*.h)\n\n" +
                   "add_executable(${PROJECT_NAME} ${sources} ${includes})\n" +
                   "# target_link_libraries(${PROJECT_NAME})\n")
        file.close()

        file = open(dir + '/src/main.cc', 'w')
        file.write("#include <iostream>\n\n" +
                   "int main(int argc, char** argv){\n" +
                   "    std::cout << \"Hello World\" << std::endl;\n"+
                   "}\n")
        print("Done")
    else:
        print('File exists')
