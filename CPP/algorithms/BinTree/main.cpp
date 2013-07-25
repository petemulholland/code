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

void TestCopyCtor();
void TestRootInsertion();
void TestIntTree();
void TestFloatTree();
void TestCharTree();

/*
 * 
 */
int main(int argc, char** argv) 
{
    TestCopyCtor();
    //TestRootInsertion();
    //TestIntTree();
    //TestFloatTree();
    //TestCharTree();
    
    return 0;
}

template <typename T>
void outputTree(BinaryTree<T>& tree)
{
    cout << endl;
    cout << "Tree size: " << tree.count() 
         << ", height: " << tree.height() << endl;
    
    cout << "In order traversal:" << endl;
    tree.inOrderPrint();
    cout << endl;
    tree.inOrderGraph();
    cout << endl << "Pre order traversal:" << endl;
    tree.preOrderPrint();
    cout << endl;
    tree.preOrderGraph();
    cout << endl << "Post order traversal:" << endl;
    tree.postOrderPrint();
    cout << endl;
    tree.postOrderGraph();
    cout << endl;
}

void TestCopyCtor()
{
    BinaryTree<int> tree;
    
    cout << "Testing ints, inserting:" << endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        int data = rand() % 100;
        cout << data << ", ";
        tree.Insert(data);
    }
    cout << "Original tree:" << endl;
    tree.inOrderGraph();

    BinaryTree<int> copy(tree);
    cout << "Copied tree:" << endl;
    copy.inOrderGraph();
}

void TestRootInsertion()
{
    BinaryTree<int> tree;
    
    cout << "Testing root insertion with rotation:" << endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        int data = rand() % 100;
        cout << "Inserting: " << data << endl;
        tree.Insert(data);
        tree.inOrderGraph();
    }
}

void TestIntTree()
{
    BinaryTree<int> tree;
    
    cout << "Testing ints, inserting:" << endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        int data = rand() % 100;
        cout << data << ", ";
        tree.Insert(data);
    }
    outputTree(tree);
}

void TestFloatTree()
{
    BinaryTree<float> tree;
    
    cout << "Testing floats, inserting:" << endl;
    srand(time(0));
    for (int i = 0; i < 20; ++i)
    {
        float data = (rand() % 10000) / 100.0; 
        cout << data << ", ";
        tree.Insert(data);
    }
    outputTree(tree);
}

void TestCharTree()
{
    BinaryTree<char> tree;
    
    cout << "Testing chars, inserting:" << endl;
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
        
        cout << data << ", ";
        tree.Insert(data);
    }
    outputTree(tree);
}
