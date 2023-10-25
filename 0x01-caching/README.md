<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">0x01. Caching</h1>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(219, 62, 62);font-size: 14px;">Back-end</span></strong></div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <ul style="font-size: 11px;">
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">By: Guillaume, CTO at Holberton School</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Weight: 1</li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Project will start <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Oct 24, 2023 6:00 AM</span></span>, must end by <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Oct 26, 2023 6:00 AM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">Checker was released at <span title=""><span style="border-bottom: 0.5px dashed currentcolor;">Oct 24, 2023 6:00 PM</span></span></li>
        <li style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">An auto review will be launched at the deadline</li>
    </ul>
</div>
<div style="text-align: start;color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);font-size: 14px;border: 1px solid rgb(221, 221, 221);">
    <div>
        <h2 style="color: inherit;font-size: 30px;">Background Context</h2>
        <p>In this project, you learn different caching algorithms.</p>
        <h2 style="color: inherit;font-size: 30px;">Resources</h2>
        <p><strong><strong>Read or watch</strong></strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/fjhr6EvFeF3mWwsPQXUKdQ" title="Cache replacement policies - FIFO" target="_blank" style="color: transparent;">Cache replacement policies - FIFO</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/U44RQjXp8xBtsbNIyhHIyw" title="Cache replacement policies - LIFO" target="_blank" style="color: transparent;">Cache replacement policies - LIFO</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/gKerxvR4dnXQYkBX2ujZiQ" title="Cache replacement policies - LRU" target="_blank" style="color: transparent;">Cache replacement policies - LRU</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Tmk4qEBZ7QTknvbpKabWfQ" title="Cache replacement policies - MRU" target="_blank" style="color: transparent;">Cache replacement policies - MRU</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/8PEJ8L34bxhL2y--BW5zGQ" title="Cache replacement policies - LFU" target="_blank" style="color: transparent;">Cache replacement policies - LFU</a></li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/-gpAdRQTx1Rb-amaz9JZhQ" title="explain to anyone" target="_blank" style="color: transparent;">explain to anyone</a>, <strong><strong>without the help of Google</strong></strong>:</p>
        <h3 style="color: inherit;font-size: 24px;">General</h3>
        <ul>
            <li>What a caching system is</li>
            <li>What FIFO means</li>
            <li>What LIFO means</li>
            <li>What LRU means</li>
            <li>What MRU means</li>
            <li>What LFU means</li>
            <li>What the purpose of a caching system</li>
            <li>What limits a caching system have</li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">Requirements</h2>
        <h3 style="color: inherit;font-size: 24px;">Python Scripts</h3>
        <ul>
            <li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3</code> (version 3.7)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">#!/usr/bin/env python3</code></li>
            <li>A <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">pycodestyle</code> style (version 2.5)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wc</code></li>
            <li>All your modules should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have a documentation (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
        </ul>
        <h2 style="color: inherit;font-size: 30px;">More Info</h2>
        <h3 style="color: inherit;font-size: 24px;">Parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 21.6px;">BaseCaching</code></h3>
        <p>All your classes must inherit from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> defined below:</p>
        <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">$ cat base_caching.py
#!/usr/bin/python3
&quot;&quot;&quot; BaseCaching module
&quot;&quot;&quot;

class BaseCaching():
    &quot;&quot;&quot; BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    &quot;&quot;&quot;
    MAX_ITEMS = 4

    def __init__(self):
        &quot;&quot;&quot; Initiliaze
        &quot;&quot;&quot;
        self.cache_data = {}

    def print_cache(self):
        &quot;&quot;&quot; Print the cache
        &quot;&quot;&quot;
        print(&quot;Current cache:&quot;)
        for key in sorted(self.cache_data.keys()):
            print(&quot;{}: {}&quot;.format(key, self.cache_data.get(key)))

    def put(self, key, item):
        &quot;&quot;&quot; Add an item in the cache
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;put must be implemented in your cache class&quot;)

    def get(self, key):
        &quot;&quot;&quot; Get an item by key
        &quot;&quot;&quot;
        raise NotImplementedError(&quot;get must be implemented in your cache class&quot;)
</code></pre>
    </div>
</div>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. Basic dictionary</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BasicCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>This caching system doesn&rsquo;t have limit</li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 0-main &quot;&quot;&quot;
BasicCache = __import__(&apos;0-basic_cache&apos;).BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
print(my_cache.get(&quot;D&quot;))
my_cache.print_cache()
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.put(&quot;A&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0-basic_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">1. FIFO caching</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">FIFOCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>You can overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super().__init__()</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                        <li>If the number of items in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> is higher that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching.MAX_ITEMS</code>:<ul>
                                <li>you must discard the first item put in cache (FIFO algorithm)</li>
                                <li>you must print <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DISCARD:</code> with the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> discarded and following by a new line</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 1-main &quot;&quot;&quot;
FIFOCache = __import__(&apos;1-fifo_cache&apos;).FIFOCache

my_cache = FIFOCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">1-fifo_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">2. LIFO Caching</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">LIFOCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>You can overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super().__init__()</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                        <li>If the number of items in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> is higher that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching.MAX_ITEMS</code>:<ul>
                                <li>you must discard the last item put in cache (LIFO algorithm)</li>
                                <li>you must print <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DISCARD:</code> with the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> discarded and following by a new line</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 2-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 2-main &quot;&quot;&quot;
LIFOCache = __import__(&apos;2-lifo_cache&apos;).LIFOCache

my_cache = LIFOCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">2-lifo_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">3. LRU Caching</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">LRUCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>You can overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super().__init__()</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                        <li>If the number of items in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> is higher that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching.MAX_ITEMS</code>:<ul>
                                <li>you must discard the least recently used item (LRU algorithm)</li>
                                <li>you must print <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DISCARD:</code> with the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> discarded and following by a new line</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 3-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 3-main &quot;&quot;&quot;
LRUCache = __import__(&apos;3-lru_cache&apos;).LRUCache

my_cache = LRUCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;B&quot;))
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()
my_cache.put(&quot;H&quot;, &quot;H&quot;)
my_cache.print_cache()
my_cache.put(&quot;I&quot;, &quot;I&quot;)
my_cache.print_cache()
my_cache.put(&quot;J&quot;, &quot;J&quot;)
my_cache.print_cache()
my_cache.put(&quot;K&quot;, &quot;K&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">3-lru_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">4. MRU Caching</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">MRUCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>You can overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super().__init__()</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                        <li>If the number of items in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> is higher that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching.MAX_ITEMS</code>:<ul>
                                <li>you must discard the most recently used item (MRU algorithm)</li>
                                <li>you must print <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DISCARD:</code> with the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> discarded and following by a new line</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 4-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 4-main &quot;&quot;&quot;
MRUCache = __import__(&apos;4-mru_cache&apos;).MRUCache

my_cache = MRUCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;B&quot;))
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()
my_cache.put(&quot;H&quot;, &quot;H&quot;)
my_cache.print_cache()
my_cache.put(&quot;I&quot;, &quot;I&quot;)
my_cache.print_cache()
my_cache.put(&quot;J&quot;, &quot;J&quot;)
my_cache.print_cache()
my_cache.put(&quot;K&quot;, &quot;K&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">4-mru_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">5. LFU Caching</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">#advanced</span></strong></div>
        </div>
        <div>
            <p>Create a class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">LFUCache</code> that inherits from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code> and is a caching system:</p>
            <ul>
                <li>You must use <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> - dictionary from the parent class <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching</code></li>
                <li>You can overload <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def __init__(self):</code> but don&rsquo;t forget to call the parent init: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">super().__init__()</code></li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def put(self, key, item):</code>
                    <ul>
                        <li>Must assign to the dictionary <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> value for the key <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> or <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">item</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>, this method should not do anything.</li>
                        <li>If the number of items in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> is higher that <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">BaseCaching.MAX_ITEMS</code>:<ul>
                                <li>you must discard the least frequency used item (LFU algorithm)</li>
                                <li>if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used</li>
                                <li>you must print <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">DISCARD:</code> with the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> discarded and following by a new line</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">def get(self, key):</code>
                    <ul>
                        <li>Must return the value in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code> linked to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code>.</li>
                        <li>If <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> is <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code> or if the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">key</code> doesn&rsquo;t exist in <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">self.cache_data</code>, return <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">None</code>.</li>
                    </ul>
                </li>
            </ul>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">guillaume@ubuntu:~/0x01$ cat 100-main.py
#!/usr/bin/python3
&quot;&quot;&quot; 100-main &quot;&quot;&quot;
LFUCache = __import__(&apos;100-lfu_cache&apos;).LFUCache

my_cache = LFUCache()
my_cache.put(&quot;A&quot;, &quot;Hello&quot;)
my_cache.put(&quot;B&quot;, &quot;World&quot;)
my_cache.put(&quot;C&quot;, &quot;Holberton&quot;)
my_cache.put(&quot;D&quot;, &quot;School&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;B&quot;))
my_cache.put(&quot;E&quot;, &quot;Battery&quot;)
my_cache.print_cache()
my_cache.put(&quot;C&quot;, &quot;Street&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;A&quot;))
print(my_cache.get(&quot;B&quot;))
print(my_cache.get(&quot;C&quot;))
my_cache.put(&quot;F&quot;, &quot;Mission&quot;)
my_cache.print_cache()
my_cache.put(&quot;G&quot;, &quot;San Francisco&quot;)
my_cache.print_cache()
my_cache.put(&quot;H&quot;, &quot;H&quot;)
my_cache.print_cache()
my_cache.put(&quot;I&quot;, &quot;I&quot;)
my_cache.print_cache()
print(my_cache.get(&quot;I&quot;))
print(my_cache.get(&quot;H&quot;))
print(my_cache.get(&quot;I&quot;))
print(my_cache.get(&quot;H&quot;))
print(my_cache.get(&quot;I&quot;))
print(my_cache.get(&quot;H&quot;))
my_cache.put(&quot;J&quot;, &quot;J&quot;)
my_cache.print_cache()
my_cache.put(&quot;K&quot;, &quot;K&quot;)
my_cache.print_cache()
my_cache.put(&quot;L&quot;, &quot;L&quot;)
my_cache.print_cache()
my_cache.put(&quot;M&quot;, &quot;M&quot;)
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/0x01$ 
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-caching</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">100-lfu_cache.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Help</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Check your code</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
