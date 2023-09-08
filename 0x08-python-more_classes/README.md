<centre><h1>0x08. Python - More Classes and Objects</h1></centre>

<hr>

<h2>General</h2>
<ul>
    <li>What is OOP</li>
    <li>"first-class everything"</li>
    <li>What is a class</li>
    <li>What is an object and instance</li>
    <li>What is the difference between a class and an object or instance</li>
    <li>What is an attribute</li>
    <li>What are and how to use public, protected and private attributes</li>
    <li>What is <code>self</code></li>
    <li>Wht is a method</li>
    <li>What is the special <code>__init__</code> method and how to use it</li>
    <li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
    <li>What is a property</li>
    <li>What is the difference between an attribute and a property in Python</li>
    <li>What is the Pythonic way to write getters and setters in Python</li>
    <li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
    <li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
    <li>What is a class attribute</li>
    <li>What is the difference between a object attribute and a class attribute</li>
    <li>What is a class method</li>
    <li>What is a static method</li>
    <li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
    <li>How to bind attributes to object and classes</li>
    <li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
    <li>How does Python find the attributes of an object or class</li>
    <li>How to use the <code>getattr</code> function</li>
</ul>

<hr>

<h2>Test Files :heavy_check_mark:</h2>
<ul>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/0-main.py" target="_blank">0-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/1-main.py" target="_blank">1-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/2-main.py" target="_blank">2-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/3-main.py" target="_blank">3-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/4-main.py" target="_blank">4-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-main.py" target="_blank">5-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/6-main.py" target="_blank">6-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/7-main.py" target="_blank">7-main.py</a></h3></li>
    <li><h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/8-main.py" target="_blank">8-main.py</a></h3></li>
</ul>

<hr>

<h2>Taks :page_with_curl:</h2>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/0-rectangle.py" target="_blank">0-rectangle.py</a></h3>
<ul>
    <li>Write an empty class <code>Rectangle</code> that defines a rectangle:</li>
    <ul>
        <li>You are not allowed to import any module</li>
    </ul>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/1-rectangle.py" target="_blank">1-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>
<ul>
    <li>Private instance attribute <code>width</code>:</li>
    <ul>
        <li>property <code>def width(self):</code> to retrieve it</li>
        <li>property setter <code>def width(self, value):</code> to set it:</li>
        <ul>
            <li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code></li>
            <li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be >= 0</code></li>
        </ul>
    </ul>
    <li>Private instance attribute <code>height</code>:</li>
    <ul>
        <li>property <code>def height(self):</code> to retrieve it</li>
        <li>property setter <code>def height(self, value):</code> to set it:</li>
        <ul>
            <li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code></li>
            <li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be >= 0</code></li>
        </ul>
    </ul>
    <li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/2-rectangle.py" target="_blank">2-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>
<ul>
    <li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
    <li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:</li>
    <ul>
        <li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
    </ul>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/3-rectangle.py" target="_blank">3-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>
<ul>
    <li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>:</li>
        <li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
    </ul>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/4-rectangle.py" target="_blank">4-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>
<ul>
    <li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code></li>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py" target="_blank">5-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>
<ul>
    <li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not  ellipsis) when an instance of <code>Rectangle</code> is deleted.</li>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/6-rectangle.py" target="_blank">6-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>
<ul>
    <li>Public class attribute <code>number_of_instances</code></code></li>
    <ul>
        <li>Initialized to <code>0</code></li>
        <li>Incrememented during each new instance instantiation</li>
        <li>Decremented during each instance deletion</li>
    </ul>
    <li>You are not allowed to import any module</li>
</ul>

<hr>

<h3><a href="https://github.com/LivingDemonness28/alx-higher_level_programming/blob/main/0x08-python-more_classes/7-rectangle.py" target="_blank">7-rectangle.py</a></h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>
<ul>
    <li>Public class attribute <code>print_symbol</code></code></li>
    <ul>
        <li>Initialized to <code>#</code></li>
        <li>Used as symbol for string representation</li>
        <li>Can be any type</li>
    </ul>
    <li>You are not allowed to import any module</li>
</ul>