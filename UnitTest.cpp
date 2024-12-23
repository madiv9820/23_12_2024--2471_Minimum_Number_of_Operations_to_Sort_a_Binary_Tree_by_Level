#include "Solution.hpp"
#include <iostream>
#include <string>

struct TestCase {
    vector<string> input;
    int output;
};

class UnitTest {
private:
    Solution sol;
    vector<TestCase> testcases;

    TreeNode* createBinaryTree(vector<string> array) {
        TreeNode* root = nullptr;
        if(array[0] != "null") root = new TreeNode(stoi(array[0]))

        queue<TreeNode*> q;
        q.push(root);

        for(int index = 1; index < array.size(); ) {
            TreeNode* node = q.front(); q.pop();
            if(array[index] != "null") { 
                node->left = new TreeNode(stoi(array[index])); 
                q.push(node->left); 
                ++index;
            }
            if(index < array.size() && array[index] != "null") { 
                node->right = new TreeNode(stoi(array[index])); 
                q.push(node->right); 
                ++index; 
            }
        }

        return root;
    }

public:
    UnitTest() {
        testcases = {{{"1","4","3","7","6","8","5","null","null","null","null","9","null","10"}, 3}, 
                     {{"1","3","2","7","6","5","4"}, 3}, 
                     {{"1","2","3","4","5","6"}, 0}}
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            TreeNode* root = createBinaryTree(testcases[i].input);
            int result = sol.minimumOperations(root);
            cout << "TestCase " << i+1 << ": " << ((result == testcases[i].output) ? "passed":"failed") << endl;
        }
    }
};