/* 
 * File:   BinaryTree.h
 * Author: pete
 *
 * Created on 24 April 2013, 17:17
 */

#ifndef BINARYTREE_H
#define	BINARYTREE_H
#include <iostream>

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
    
public:
    BinaryTree();
    BinaryTree(const BinaryTree<T>& orig);
    virtual ~BinaryTree();

    void Insert(T key);

    void TraverseInOrder();
    
private:
    Node* root;

    void DestroyTree(Node* leaf);
    void Insert(T key, Node* leaf);
    void TraverseInOrder(Node* leaf);
};

template <typename T>
BinaryTree<T>::BinaryTree() 
:root(0)
{
}

template <typename T>
BinaryTree<T>::BinaryTree(const BinaryTree<T>& orig) {
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
    if (root == 0)
        root = new Node(key);
    else
        Insert(key, root);
}

template <typename T>
void BinaryTree<T>::Insert(T key, Node* leaf)
{
    if (key < leaf->value)
    {
        if (leaf->left == 0)
            leaf->left = new Node(key);
        else
            Insert(key, leaf->left);
    }
    else // if (key >= leaf->value)
    {
        if (leaf->right == 0)
            leaf->right = new Node(key);
        else
            Insert(key, leaf->right);
    }
}

template <typename T>
void BinaryTree<T>::TraverseInOrder()
{
    TraverseInOrder(root);
    std::cout << std::endl;
}
    
template <typename T>
void BinaryTree<T>::TraverseInOrder(Node* leaf)
{
    if (leaf == 0)
        return;
    TraverseInOrder(leaf->left);
    std::cout << leaf->value << ", ";
    TraverseInOrder(leaf->right);
}

#endif	/* BINARYTREE_H */

