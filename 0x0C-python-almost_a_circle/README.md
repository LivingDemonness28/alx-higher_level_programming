<h1>0x0C. Python - Almost a circle</h1>

<h2>Resources</h2>
<ul>
    <li><a href="https://intranet.alxswe.com/rltoken/7gc6UzxSL81HcuAwklUbuQ" target="_blank">args/kwargs</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/rGVU9mt57rVURGnjK6n4_Q" target="_blank">JSON encoder and decoder</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/soictNXCPE18ASL3INoeew" target="_blank">unittest module</a></li>
    <li><a href="https://intranet.alxswe.com/rltoken/uI9iskBCcNo5pc7j9Vy86A" target="_blank">Python test cheatsheet</a></li>
</ul>

<hr>

<h2>General</h2>
<ul>
    <li>What is Unit testing and how to implement it in a large project</li>
    <li>How to serialize and deserialize a Class</li>
    <li>How to write and read a JSON file</li>
    <li>What is *args and how to use it</li>
    <li>What is **kwargs and how to use it</li>
    <li>How to handle named arguments in a function</li>
</ul>

<hr>

<h2>Tasks :page_with_curl:</h2>

<h3>0. If it's not tested it doesn't work</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/tests" target="_blank">tests</a>

<p>All your files, classes and methods must be unit tested and be PEP 8 validated.</p>

<hr>

<h3>1. Base class</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/base.py" target="_blank">models/base.py</a>
<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/__init__.py" target="_blank">models/__init__.py</a>

<p>Write the first class <code>Base</code>:</p>
<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python package</p>
<p>Create a file named <code>models/base.py</code>:</p>
<ul>
    <li>Class <code>Base</code>:</li>
    <ul>
        <li>private class attribute <code>__nb_objects = 0</code></li>
        <li>class constructor: <code>def __init__(self, id=None):</code>:</li>
        <ul>
            <li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> with this argument value - you can assume <code>id</code> is an integer and you don't need to test the type of it</li>
            <li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
        </ul>
    </ul>
</ul>
<p>This class will be the “base” of all other classes in this project. The goal of it is to manage <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</p>

<hr>

<h3>2. First Rectangle</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/rectangle.py" target="_blank">models/rectangle.py</a>

<p>Write the class <code>Rectangle</code> that inherits from <code>Base</code>:</p>

<ul>
    <li>In the file <code>model/rectangle.py</code></li>
    <li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
    <li>Private instance attributes, each with its own public getter and setter:
        <ul>
            <li><code>__width</code> -> <code>width</code></li>
            <li><code>__height</code> -> <code>height</code></li>
            <li><code>__x</code> -> <code>x</code></li>
            <li><code>__y</code> -> <code>y</code></li>
        </ul>
    </li>
    <li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None)</code>:
        <ul>
            <li>Call the super class with <code>id</code> - this super call with use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
            <li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code>to the right attribute?</li>
        </ul>
    </li>
</ul>

<p>Why private attributes with getter/setter? Why not directly public attribute?</p>

<p>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.</p>

<hr>

<h3>3. Validate attributes</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/rectangle.py" target="_blank">models/rectangle.py</a>

<p>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded):</p>

<ul>
    <li>f the input is not an integer, raise the <code>TypeError</code> exception with the message: <code>name of the attribute must be an integer</code>. Example: <code>width must be an integer</code></li>
    <li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code>name of the attribute must be > 0</code>. Example: <code>width must be > 0</code></li>
    <li>If <code>x</code>or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code>name of the attribute must be >= 0</code>. Example: <code>x must be >= 0</code></li>
</ul>

<hr>

<h3>4. Area first</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/rectangle.py" target="_blank">models/rectangle.py</a>

<p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>

<hr>

<h3>5. Display #0</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/rectangle.py" target="_blank">models/rectangle.py</a>

<p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don't need to handle <code>x</code> and <code>y</code> here.</p>

<hr>

<h3>6. __str__</h3>

<a href="https://github.com/LivingDemonness28/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle/models/rectangle.py" target="_blank">models/rectangle.py</a>

<p>Update the class <code>Rectangle</code> by overriding the <code>__str__</code> the method so that it returns <code>[Rectangle] (\<id\>) \<x\>/\<y\> - \<width\>/\<height\></code></p>

<hr>
