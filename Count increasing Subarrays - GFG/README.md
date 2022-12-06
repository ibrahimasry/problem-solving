# Count increasing Subarrays
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of <strong>N</strong> integers <strong>Arr<sub>1</sub>, Arr<sub>2</sub>, ….Arr<sub>N</sub></strong>, count number of subarrays of <strong>Arr</strong> which are strictly increasing.&nbsp;<br>
A subarray <strong>Arr<sub>[i, j]</sub></strong> is the array where <strong>1 &lt;= i &lt;&nbsp;j &lt;= N</strong> is a sequence of integers of <strong>Arr<sub>i</sub>, Arr<sub>i+1</sub>, ….Arr<sub>j</sub></strong>. A subarray <strong>Arr<sub>[i, j]</sub></strong> is strictly increasing if <strong>Arr<sub>i</sub> &lt; Arr<sub>i+1</sub> &lt; Arr<sub>i+2</sub> &lt; ……. &lt; Arr<sub>j</sub>.</strong></span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: 
</strong>N = 6
Arr[] = {1, 3, 3, 2, 3, 5}
<strong>Output:</strong> 4
<strong>Explanation:</strong>
(1,3), (2, 3), (3, 5) and (2, 3, 5)
are the only increasing subarrays.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>
N = 2
Arr[] = {1 5} 
<strong>Output:</strong> 1
<strong>Explanation:</strong>(1, 5) is the only increasing
subarray.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countIncreasing()</strong>&nbsp;which takes the array of integers&nbsp;<strong>arr[]</strong><strong>&nbsp;</strong>and<strong>&nbsp;n&nbsp;</strong>as parameters and returns a integer denoting&nbsp;the answer.<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>7</sup><br>
1 &lt;= Arr<sub>i</sub> &lt;= 10<sup>7</sup></span></p>

<p>&nbsp;</p>
</div>