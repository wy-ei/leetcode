---
title: 动物收容所
qid: 03.06
tags: [设计]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/animal-shelter-lcci/](https://leetcode-cn.com/problems/animal-shelter-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>动物收容所。有家动物收容所只收容狗与猫，且严格遵守&ldquo;先进先出&rdquo;的原则。在收养该收容所的动物时，收养人只能收养所有动物中&ldquo;最老&rdquo;（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中&ldquo;最老&rdquo;的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如<code>enqueue</code>、<code>dequeueAny</code>、<code>dequeueDog</code>和<code>dequeueCat</code>。允许使用Java内置的LinkedList数据结构。</p>

<p><code>enqueue</code>方法有一个<code>animal</code>参数，<code>animal[0]</code>代表动物编号，<code>animal[1]</code>代表动物种类，其中 0 代表猫，1 代表狗。</p>

<p><code>dequeue*</code>方法返回一个列表<code>[动物编号, 动物种类]</code>，若没有可以收养的动物，则返回<code>[-1,-1]</code>。</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>：
[&quot;AnimalShelf&quot;, &quot;enqueue&quot;, &quot;enqueue&quot;, &quot;dequeueCat&quot;, &quot;dequeueDog&quot;, &quot;dequeueAny&quot;]
[[], [[0, 0]], [[1, 0]], [], [], []]
<strong> 输出</strong>：
[null,null,null,[0,0],[-1,-1],[1,0]]
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>：
[&quot;AnimalShelf&quot;, &quot;enqueue&quot;, &quot;enqueue&quot;, &quot;enqueue&quot;, &quot;dequeueDog&quot;, &quot;dequeueCat&quot;, &quot;dequeueAny&quot;]
[[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
<strong> 输出</strong>：
[null,null,null,null,[2,1],[0,0],[1,0]]
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>收纳所的最大容量为20000</li>
</ol>


## 解法：

使用两个队列来存放两种动物，每个动物关联一个序列号，序列号越小，说明越早到来。

```c++
struct Animal{
    int id;
    int series_num;
    Animal() = default;
    Animal(int id, int num): id(id), series_num(num){}
};

class AnimalShelf {
public:
    AnimalShelf():num(0) {

    }

    void enqueue(vector<int> animal) {
        if(animal[1] == 0){
            cat_queue.emplace(animal[0], num++);
        }else{
            dog_queue.emplace(animal[0], num++);
        }
    }

    vector<int> dequeueAny() {
        if(cat_queue.empty() && dog_queue.empty()){
            return {-1, -1};
        }
        if(cat_queue.empty()){
            return dequeueDog();            
        }else if(dog_queue.empty()){
            return dequeueCat();
        }

        if(dog_queue.front().series_num < cat_queue.front().series_num){
            return dequeueDog();
        }else{
            return dequeueCat();
        }
    }

    vector<int> dequeueDog() {
        if(dog_queue.empty()){
            return {-1, -1};
        }
        Animal dog = dog_queue.front();
        dog_queue.pop();
        return {dog.id, 1};
    }

    vector<int> dequeueCat() {
        if(cat_queue.empty()){
            return {-1, -1};
        }
        Animal cat = cat_queue.front();
        cat_queue.pop();
        return {cat.id, 0};
    }

private:
    queue<Animal> dog_queue;
    queue<Animal> cat_queue;
    int num;
};
```