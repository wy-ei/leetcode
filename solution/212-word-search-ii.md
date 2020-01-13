## 212. Word Search II

- 难度： 困难
- 通过率： 26.9%
- 题目链接：[https://leetcode.com/problems/word-search-ii](https://leetcode.com/problems/word-search-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二维网格&nbsp;<strong>board&nbsp;</strong>和一个字典中的单词列表 <strong>words</strong>，找出所有同时在二维网格和字典中出现的单词。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中&ldquo;相邻&rdquo;单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 
<strong>words</strong> = <code>[&quot;oath&quot;,&quot;pea&quot;,&quot;eat&quot;,&quot;rain&quot;]</code> and <strong>board </strong>=
[
  [&#39;<strong>o</strong>&#39;,&#39;<strong>a</strong>&#39;,&#39;a&#39;,&#39;n&#39;],
  [&#39;e&#39;,&#39;<strong>t</strong>&#39;,&#39;<strong>a</strong>&#39;,&#39;<strong>e</strong>&#39;],
  [&#39;i&#39;,&#39;<strong>h</strong>&#39;,&#39;k&#39;,&#39;r&#39;],
  [&#39;i&#39;,&#39;f&#39;,&#39;l&#39;,&#39;v&#39;]
]

<strong>输出:&nbsp;</strong><code>[&quot;eat&quot;,&quot;oath&quot;]</code></pre>

<p><strong>说明:</strong><br>
你可以假设所有输入都由小写字母 <code>a-z</code>&nbsp;组成。</p>

<p><strong>提示:</strong></p>

<ul>
	<li>你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？</li>
	<li>如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： <a href="/problems/implement-trie-prefix-tree/description/">实现Trie（前缀树）</a>。</li>
</ul>


## 解法：

把待查询的词加入到字典树种，然后从矩阵的各个位置开始深度优先遍历，去和字典树中的单词进行匹配。

```cpp
class Trie {
public:
    struct Node;
    struct Node{
        string word;
        Node* next['z'-'a'+1]{nullptr};
    };

    Trie() {
        root = new Node;
    }

    void insert(const string& word) {
        Node* p = root;
        for(char ch : word){
            int index = ch - 'a';
            if(p->next[index] == nullptr){
                p->next[index] = new Node;
            }
            p = p->next[index];
        }
        p->word = word;
    }
    
    ~Trie() noexcept {
        // free memory
        ;
    }

    Node* root;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        if(board.empty() || board[0].empty()) return matched_words;
        n_rows = board.size();
        n_cols = board[0].size();
        this->board_ = &board;

        for(const string &word: words){
            trie.insert(word);
        }

        for(size_t i=0;i<n_rows;i++){
            for(size_t j=0;j<n_cols;j++){
                dfs(i, j, trie.root);
            }
        }
        return matched_words;
    }

    void dfs(int row, int col, typename Trie::Node *node){
        vector<vector<char>>& board = *board_;
        char ch = board[row][col];
        if(ch == '#') return;

        node = node->next[ch - 'a'];
        if(node == nullptr) return;
        
        if(!node->word.empty()){
            matched_words.push_back(::move(node->word));
            node->word.clear();
        }
        
        board[row][col] = '#';

        if(row > 0) dfs(row-1, col, node);
        if(row+1 < n_rows) dfs(row+1, col, node);
        if(col > 0) dfs(row, col-1, node);
        if(col+1 < n_cols) dfs(row, col+1, node);

        board[row][col] = ch;
    }

private:
    vector<string> matched_words;
    vector<vector<char>>* board_;
    Trie trie;
    int n_cols;
    int n_rows;
};

```