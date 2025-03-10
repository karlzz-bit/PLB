
---

# DataStructures

欢迎来到我的DataStructures项目！这个项目旨在提供从基础到进阶的数据结构的详细实现和解释。无论你是初学者还是有经验的程序员，这个项目都能帮助你深入理解和掌握各种数据结构。
## 目录
asdfasdfhruihfiokasdm,okifjnhuiewrhtgasedfc
sadtgkj89rqeiwjfkpoasd
fwerj98igjpasd
fqwertjg9w8iodkf,cv[sd]a
gvsdfgj9weirajkmvgf[asd
fewrj98itgjaspoedl.fvc
asdg4598whgj09asdop.vc
]
1. [基础数据结构](#基础数据结构)
    - [数组 (Array)](#数组-array)
    - [链表 (Linked List)](#链表-linked-list)
    - [栈 (Stack)](#栈-stack)
    - [队列 (Queue)](#队列-queue)
2. [树和图](#树和图)
    - [二叉树 (Binary Tree)](#二叉树-binary-tree)
    - [二叉搜索树 (Binary Search Tree)](#二叉搜索树-binary-search-tree)
    - [平衡树 (Balanced Tree)](#平衡树-balanced-tree)
    - [图 (Graph)](#图-graph)
3. [高级数据结构](#高级数据结构)
    - [哈希表 (Hash Table)](#哈希表-hash-table)
    - [堆 (Heap)](#堆-heap)
    - [Trie (前缀树)](#trie-前缀树)
    - [后缀树 (Suffix Tree)](#后缀树-suffix-tree)

## 基础数据结构

### 数组 (Array)
数组是一种线性数据结构，用于存储固定大小的元素集合。这些元素可以通过索引快速访问。

```cpp
// 数组的示例代码
#include <iostream>
using namespace std;

int main() {
    int array[5] = {1, 2, 3, 4, 5};
    cout << array[0] << endl;  // 输出 1
    return 0;
}
```

### 链表 (Linked List)
链表是一种线性数据结构，其中每个元素都是一个节点，节点包含数据和指向下一个节点的引用。

```cpp
// 链表的示例代码
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
public:
    Node* head;
    LinkedList() {
        head = nullptr;
    }

    void append(int data) {
        Node* newNode = new Node(data);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* last = head;
        while (last->next != nullptr) {
            last = last->next;
        }
        last->next = newNode;
    }
};
```

### 栈 (Stack)
栈是一种后进先出（LIFO）的数据结构，可以通过`push`和`pop`操作进行元素的添加和移除。

```cpp
// 栈的示例代码
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> stack;
    stack.push(1);
    stack.push(2);
    cout << stack.top() << endl;  // 输出 2
    stack.pop();
    return 0;
}
```

### 队列 (Queue)
队列是一种先进先出（FIFO）的数据结构，可以通过`enqueue`和`dequeue`操作进行元素的添加和移除。

```cpp
// 队列的示例代码
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> queue;
    queue.push(1);
    queue.push(2);
    cout << queue.front() << endl;  // 输出 1
    queue.pop();
    return 0;
}
```

## 树和图

### 二叉树 (Binary Tree)
二叉树是一种每个节点最多有两个子节点的数据结构，通常用于实现更复杂的数据结构。

```cpp
// 二叉树的示例代码
#include <iostream>
using namespace std;

class TreeNode {
public:
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int data) {
        this->data = data;
        this->left = nullptr;
        this->right = nullptr;
    }
};
```

### 二叉搜索树 (Binary Search Tree)
二叉搜索树是一种特殊的二叉树，具有左子节点小于父节点，右子节点大于父节点的性质。

```cpp
// 二叉搜索树的示例代码
#include <iostream>
using namespace std;

class TreeNode {
public:
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int data) {
        this->data = data;
        this->left = nullptr;
        this->right = nullptr;
    }
};

class BST {
public:
    TreeNode* root;
    BST() {
        root = nullptr;
    }

    void insert(int data) {
        root = insertRec(root, data);
    }

private:
    TreeNode* insertRec(TreeNode* root, int data) {
        if (root == nullptr) {
            return new TreeNode(data);
        }
        if (data < root->data) {
            root->left = insertRec(root->left, data);
        } else if (data > root->data) {
            root->right = insertRec(root->right, data);
        }
        return root;
    }
};
```

## 高级数据结构

### 哈希表 (Hash Table)
哈希表是一种用于实现高效查找的数据结构，通过哈希函数将键映射到表中的位置。

```cpp
// 哈希表的示例代码
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> hashTable;
    hashTable["key1"] = 1;
    hashTable["key2"] = 2;
    cout << hashTable["key1"] << endl;  // 输出 1
    return 0;
}
```

### 堆 (Heap)
堆是一种特殊的完全二叉树，分为最大堆和最小堆，通常用于实现优先队列。

```cpp
// 堆的示例代码
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> maxHeap;
    maxHeap.push(1);
    maxHeap.push(2);
    cout << maxHeap.top() << endl;  // 输出 2
    maxHeap.pop();
    return 0;
}
```

### Trie (前缀树)
Trie是一种树形数据结构，主要用于存储字符串集合，以支持快速的字符串查找。

```cpp
// Trie的示例代码
#include <iostream>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() {
        isEndOfWord = false;
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }

    void insert(string key) {
        TrieNode* node = root;
        for (char c : key) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string key) {
        TrieNode* node = root;
        for (char c : key) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};
```

### 后缀树 (Suffix Tree)
后缀树是一种压缩字典树，用于字符串快速查找和模式匹配。

```cpp
// 后缀树的示例代码
// 由于后缀树实现较复杂，这里给出简单的类定义
#include <iostream>
#include <string>
using namespace std;

class SuffixTreeNode {
    // 后缀树节点的定义
};

class SuffixTree {
public:
    SuffixTree(string text) {
        // 构建后缀树
    }

private:
    SuffixTreeNode* root;
};
```

---