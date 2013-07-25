/* 
 * File:   BinaryTree.h
 * Author: pete
 *
 * Created on 24 April 2013, 17:17
 */

#ifndef BINARYTREE_H
#define	BINARYTREE_H
#include <iostream>

using namespace std;

template <typename T>
class BinaryTree 
{
private:
    struct Node
    {
        T value;
        Node* left;
        Node* right;
        
        Node(T data)
        : value(data), left(0), right(0)
        { }
    };
    
    enum eOrder { inorder, preorder, postorder };
    
public:
    BinaryTree();
    BinaryTree(const BinaryTree<T>& orig);
    virtual ~BinaryTree();

    void Insert(T key);

    int count() { return count(root); }
    int height() { return height(root); }
    
    void inOrderPrint();
    void preOrderPrint();
    void postOrderPrint();
    
    void inOrderGraph();
    void preOrderGraph();
    void postOrderGraph();
    
private:
    Node* root;

    void DestroyTree(Node* leaf);
    void InsertAtRoot(T key, Node*& leaf);
    void Insert(T key, Node*& leaf);
    void CopyTree(Node* copyFrom, Node*& copyTo);
    
    int count(Node* leaf);
    int height(Node* leaf);
    
    void rotateRight(Node*& leaf);
    void rotateLeft(Node*& leaf);

    void traversePrint(eOrder order, Node* leaf, void (BinaryTree<T>::*visit)(Node* leaf));
    void printNode(Node* leaf);

    void traverseGraph(eOrder order, Node* leaf, int height, 
                       void (BinaryTree<T>::*visit)(Node* leaf, int height));
    void graphNode(Node* leaf, int height);
};

template <typename T>
BinaryTree<T>::BinaryTree() 
:root(0)
{
}

template <typename T>
BinaryTree<T>::BinaryTree(const BinaryTree<T>& orig) 
:root(0)
{
    CopyTree(orig.root, root);
}

template <typename T>
BinaryTree<T>::~BinaryTree() 
{
    DestroyTree(root);
}

template <typename T>
void BinaryTree<T>::DestroyTree(Node* leaf)
{
    if (leaf != 0)
    {
        DestroyTree(leaf->left);
        DestroyTree(leaf->right);
        delete leaf;
    }
}

template <typename T>
void BinaryTree<T>::Insert(T key)
{
    InsertAtRoot(key, root);
}

template <typename T>
void BinaryTree<T>::CopyTree(Node* copyFrom, Node*& copyTo)
{
    if (copyFrom == 0)
        return;
    
    Insert(copyFrom->value, copyTo);
    CopyTree(copyFrom->left, copyTo->left);
    CopyTree(copyFrom->right, copyTo->right);
}

template <typename T>
void BinaryTree<T>::Insert(T key, Node*& leaf)
{
    if (leaf == 0)
    {
        leaf = new Node(key);
        return;
    }
    if (key < leaf->value)
    {
        Insert(key, leaf->left);
    }
    else // if (key >= leaf->value)
    {
        Insert(key, leaf->right);
    }
}

template <typename T>
void BinaryTree<T>::InsertAtRoot(T key, Node*& leaf)
{
    if (leaf == 0)
    {
        leaf = new Node(key);
        return;
    }
    if (key < leaf->value)
    {
        InsertAtRoot(key, leaf->left);
        rotateRight(leaf);
    }
    else // if (key >= leaf->value)
    {
        InsertAtRoot(key, leaf->right);
        rotateLeft(leaf);
    }
}

template <typename T>
void BinaryTree<T>::rotateRight(Node*& leaf)
{
    Node* leafLeft = leaf->left;
    leaf->left = leafLeft->right;
    leafLeft->right = leaf;
    leaf = leafLeft;
}

template <typename T>
void BinaryTree<T>::rotateLeft(Node*& leaf)
{
    Node* leafRight = leaf->right;
    leaf->right = leafRight->left;
    leafRight->left = leaf;
    leaf = leafRight;
}

template <typename T>
void BinaryTree<T>::inOrderPrint()
{ 
    traversePrint(inorder, root, &BinaryTree<T>::printNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::preOrderPrint()
{ 
    traversePrint(preorder, root, &BinaryTree<T>::printNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::postOrderPrint()
{ 
    traversePrint(postorder, root, &BinaryTree<T>::printNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::traversePrint(eOrder order, Node* leaf, 
                                  void (BinaryTree<T>::*visit)(BinaryTree<T>::Node* leaf))
{
    if (leaf == 0)
        return;
    
    if (order == preorder)
        (this->*visit)(leaf);
    
    traversePrint(order, leaf->left, visit);
    
    if (order == inorder)
        (this->*visit)(leaf);

    traversePrint(order, leaf->right, visit);

    if (order == postorder)
        (this->*visit)(leaf);
}

template <typename T>
void BinaryTree<T>::printNode(Node* leaf)
{
    cout << leaf->value << ", ";
}

template <typename T>
int BinaryTree<T>::count(Node* leaf)
{
    if (leaf == 0)
        return 0;
    
    return count(leaf->left) + count(leaf->right) + 1; 
}

template <typename T>
int BinaryTree<T>::height(Node* leaf)
{
    if (leaf == 0)
        return -1;
    
    int l = height(leaf->left);
    int r = height(leaf->right);
    
    return (l > r ? l + 1 : r + 1);
}


template <typename T>
void BinaryTree<T>::inOrderGraph() 
{ 
    traverseGraph(inorder, root, 0, &BinaryTree<T>::graphNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::preOrderGraph() 
{ 
    traverseGraph(preorder, root, 0, &BinaryTree<T>::graphNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::postOrderGraph() 
{ 
    traverseGraph(postorder, root, 0, &BinaryTree<T>::graphNode); 
    cout << endl;
}

template <typename T>
void BinaryTree<T>::traverseGraph(eOrder order, Node* leaf, int height, 
                                  void (BinaryTree<T>::*visit)(Node* leaf, int height))
{
    if (leaf == 0)
        return;
    
    if (order == preorder)
        (this->*visit)(leaf, height);
    
    traverseGraph(order, leaf->left, height + 1, visit);
    
    if (order == inorder)
        (this->*visit)(leaf, height);

    traverseGraph(order, leaf->right, height + 1, visit);

    if (order == postorder)
        (this->*visit)(leaf, height);
}

template <>
void BinaryTree<float>::graphNode(Node* leaf, int height)
{
    for (int i = 0; i < height; ++i)
        cout << "      ";
    if (leaf != 0)
    {
        cout.precision(2);
        cout << std::fixed << right << leaf->value << ' ' << endl;
    }
    else
        cout << "*     " << endl;
}

template <>
void BinaryTree<int>::graphNode(Node* leaf, int height)
{
    for (int i = 0; i < height; ++i)
        cout << "   ";
    if (leaf != 0)
    {
        cout.precision(2);
        cout << std::fixed << right << leaf->value << ' ' << endl;
    }
    else
        cout << "*  " << endl;
}

template <typename T>
void BinaryTree<T>::graphNode(Node* leaf, int height)
{
    for (int i = 0; i < height; ++i)
        cout << "  ";
    cout << (leaf != 0 ? leaf->value : '*') << ' '  << endl;
}

#endif	/* BINARYTREE_H */

