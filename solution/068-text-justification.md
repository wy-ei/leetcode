## 68. Text Justification

- 难度： 困难
- 通过率： 21.9%
- 题目链接：[https://leetcode.com/problems/text-justification](https://leetcode.com/problems/text-justification)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个单词数组和一个长度&nbsp;<em>maxWidth</em>，重新排版单词，使其成为每行恰好有&nbsp;<em>maxWidth</em>&nbsp;个字符，且左右两端对齐的文本。</p>

<p>你应该使用&ldquo;贪心算法&rdquo;来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格&nbsp;<code>&#39; &#39;</code>&nbsp;填充，使得每行恰好有 <em>maxWidth</em>&nbsp;个字符。</p>

<p>要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。</p>

<p>文本的最后一行应为左对齐，且单词之间不插入<strong>额外的</strong>空格。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>单词是指由非空格字符组成的字符序列。</li>
	<li>每个单词的长度大于 0，小于等于&nbsp;<em>maxWidth</em>。</li>
	<li>输入单词数组 <code>words</code>&nbsp;至少包含一个单词。</li>
</ul>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>
words = [&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;, &quot;of&quot;, &quot;text&quot;, &quot;justification.&quot;]
maxWidth = 16
<strong>输出:</strong>
[
&nbsp; &nbsp;&quot;This &nbsp; &nbsp;is &nbsp; &nbsp;an&quot;,
&nbsp; &nbsp;&quot;example &nbsp;of text&quot;,
&nbsp; &nbsp;&quot;justification. &nbsp;&quot;
]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong>
words = [&quot;What&quot;,&quot;must&quot;,&quot;be&quot;,&quot;acknowledgment&quot;,&quot;shall&quot;,&quot;be&quot;]
maxWidth = 16
<strong>输出:</strong>
[
&nbsp; &quot;What &nbsp; must &nbsp; be&quot;,
&nbsp; &quot;acknowledgment &nbsp;&quot;,
&nbsp; &quot;shall be &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]
<strong>解释: </strong>注意最后一行的格式应为 &quot;shall be    &quot; 而不是 &quot;shall     be&quot;,
&nbsp;    因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong>
words = [&quot;Science&quot;,&quot;is&quot;,&quot;what&quot;,&quot;we&quot;,&quot;understand&quot;,&quot;well&quot;,&quot;enough&quot;,&quot;to&quot;,&quot;explain&quot;,
&nbsp;        &quot;to&quot;,&quot;a&quot;,&quot;computer.&quot;,&quot;Art&quot;,&quot;is&quot;,&quot;everything&quot;,&quot;else&quot;,&quot;we&quot;,&quot;do&quot;]
maxWidth = 20
<strong>输出:</strong>
[
&nbsp; &quot;Science &nbsp;is &nbsp;what we&quot;,
  &quot;understand &nbsp; &nbsp; &nbsp;well&quot;,
&nbsp; &quot;enough to explain to&quot;,
&nbsp; &quot;a &nbsp;computer. &nbsp;Art is&quot;,
&nbsp; &quot;everything &nbsp;else &nbsp;we&quot;,
&nbsp; &quot;do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]
</pre>


## 解法：

再也不想做 hard 类型的题了。

```python
class Solution:
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        rows = []
        
        row_words = []
        row_length = 0
        row_words_length = 0
        for word in words:
            word_length = len(word)
            
            if row_length + word_length <= max_width:
                row_words_length += word_length
                row_length += word_length + 1
                row_words.append(word)
            else:
                rows.append((row_words, row_words_length))
                row_words = [word]
                row_words_length = word_length
                row_length = word_length + 1
        rows.append((row_words, row_words_length))

        return self.merge(rows, max_width)

    def merge(self, rows, max_width):
        str_rows = []
        for row_count, row in enumerate(rows):
            row_words = row[0]
            row_words_length = row[1]
            words_count = len(row_words)
            space_count = max_width - row_words_length
            
            gap_count = words_count - 1
            if gap_count == 0:
                gap_space_count = 0
                remain_space_count = 0
            else:
                gap_space_count = space_count // gap_count
                remain_space_count = space_count % gap_count
            
            if row_count == len(rows) - 1:
                gap_space_count = 1
                remain_space_count = 0
            
            row_str_list = []
            for i, word in enumerate(row_words):
                row_str_list.append(word)
                if i == len(row_words) - 1:
                    break
                row_str_list.append(' ' * gap_space_count)
                if remain_space_count > 0:
                    row_str_list.append(' ')
                    remain_space_count -= 1
            
            str_row = ''.join(row_str_list)
            
            # 处理一行只有一个单词或最后一行的情况
            if max_width != len(str_row):
                str_row += (' ' * (max_width - len(str_row)))
            
            str_rows.append(str_row)

        return str_rows
```