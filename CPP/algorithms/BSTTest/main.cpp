/* 
 * File:   main.cpp
 * Author: pete
 *
 * Created on 24 April 2013, 11:05
 */

#include <cstdlib>
#include <ctime>
#include "BinaryTree.h"

using namespace std;

void TestIntTree();
void TestFloatTree();
void TestCharTree();

/*
 * 
 */
int main(int argc, char** argv) 
{
    TestIntTree();
    TestFloatTree();
    TestCharTree();
    
    return 0;
}

void TestIntTree()
{
    BinaryTree<int> tree;
    
    std::cout << "Testing ints, inserting:" << std::endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        int data = rand() % 100;
        std::cout << data << ", ";
        tree.Insert(data);
    }
    std::cout << std::endl << "In order traversal:" << std::endl;
    tree.TraverseInOrder();
    std::cout << std::endl;
}

void TestFloatTree()
{
    BinaryTree<float> tree;
    
    std::cout << "Testing floats, inserting:" << std::endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        float data = (rand() % 10000) / 100.0; 
        std::cout << data << ", ";
        tree.Insert(data);
    }
    std::cout << std::endl << "In order traversal:"<< std::endl;

    tree.TraverseInOrder();
    std::cout << std::endl;
}

void TestCharTree()
{
    BinaryTree<char> tree;
    
    std::cout << "Testing chars, inserting:" << std::endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        char data = rand() % 62;
        if (data < 10)
            data += 48;
        else if (data < 36)
            data += 55; // 65 - 10
        else 
            data += 61; // 97 - 36
        
        std::cout << data << ", ";
        tree.Insert(data);
    }
    std::cout << std::endl << "In order traversal:" << std::endl;

    tree.TraverseInOrder();
    std::cout << std::endl;
}
