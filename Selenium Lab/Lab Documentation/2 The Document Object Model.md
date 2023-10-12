# The Document Object Model (DOM)
The Document Object Model (DOM) is a programming interface that represents the structure of a web page, allowing developers to access and manipulate its elements. 
It serves as a bridge between the content of a web page and the scripts or code running on it. 
The DOM provides a hierarchical representation of the HTML or XML document, with each element represented as a node in the tree-like structure.

By using the DOM, developers can easily interact with HTML elements and modify their properties, such as changing text, colors, or styles dynamically.
The HTML DOM provides a way to interact with and manipulate the elements of an HTML document using JavaScript. 
[It allows you to access, modify, and add elements dynamically, change styles and classes, handle events, and perform other operations on the document.]
(https://www.freecodecamp.org/news/manipulate-html-and-css-using-javascript/)

The DOM also enables the creation of new elements, To create a new element, we can use document.createElement() with the argument of element, which is the element name. 
However, it does not append it to the document. It creates an empty element with no inner HTML.
https://medium.com/@fernnandoptr/dom-manipulation-in-a-nutshell-76c8b7eb3f1c#:~:text=asquerySelector().-,Adding%20Elements,the%20document.%20It%20creates%20an%20empty%20element%20with%20no%20inner%20HTML.,-In%20order%20to

## DOM Tree with Relationships to Other Programs
[![](https://mermaid.ink/img/pako:eNqtU8tu2zAQ_JUFTzJg5wN0KGBbceLEbgO4KApIOaxFSmJCkQJJ1RAs_3v5kA0kSG89WV7Ozs7MYs-kVJSRlCwWi0JabgVLIfuxh52qeQkboU5lg9oWslSy4nVaSADbsNbBjmjY7e8v1ByPgpmAAOg0b1EPayWUTqEgHZfvBSlkmFNdaeFnFuHL3A19Bff6DVbnxrbiEh9WsbbOG4b09UMty4-KDlNtHWqjRwETTpC0I9znwdEchJs-B6XBlJp3duq5jz28ggAbYZOEjysBOM_W_c4-wyOdZgKMHZznhjELKCk0mjkyBXelMVBxz_mQrA-HieEhMpQoY-N1kAnNJ3bssHYtq8_zoupowwT-t0gPJ24bMLr03rxa5NLAG_7B2AJ-uyM8Jk-30iTlMZK3KHnXC7QsbN1RI6UfZbWK8moAv5NrICMsI0sWN7HNp44p2G0kt1hLbF38aK3mx96ysANOR3hKvs74OXkZbKPkbErKyYcOjWHe9gi7fCPQvE9jniOoQ-3ff-93MQ5vZPmyvYlc_YMrvu6mILxLzqJll4EJ0QXgtI59CHH2X3L7fr4Ldb_DS8xwSeakZbpFTt05nj2uIOG0CuIPiLIKe2H9DV0cFHurDoMsSWp1z-ak76gTk3GsNbYkrVAYV2WUW6X38cTDpV_-AgpVSC4?type=png)](https://mermaid.live/edit#pako:eNqtU8tu2zAQ_JUFTzJg5wN0KGBbceLEbgO4KApIOaxFSmJCkQJJ1RAs_3v5kA0kSG89WV7Ozs7MYs-kVJSRlCwWi0JabgVLIfuxh52qeQkboU5lg9oWslSy4nVaSADbsNbBjmjY7e8v1ByPgpmAAOg0b1EPayWUTqEgHZfvBSlkmFNdaeFnFuHL3A19Bff6DVbnxrbiEh9WsbbOG4b09UMty4-KDlNtHWqjRwETTpC0I9znwdEchJs-B6XBlJp3duq5jz28ggAbYZOEjysBOM_W_c4-wyOdZgKMHZznhjELKCk0mjkyBXelMVBxz_mQrA-HieEhMpQoY-N1kAnNJ3bssHYtq8_zoupowwT-t0gPJ24bMLr03rxa5NLAG_7B2AJ-uyM8Jk-30iTlMZK3KHnXC7QsbN1RI6UfZbWK8moAv5NrICMsI0sWN7HNp44p2G0kt1hLbF38aK3mx96ysANOR3hKvs74OXkZbKPkbErKyYcOjWHe9gi7fCPQvE9jniOoQ-3ff-93MQ5vZPmyvYlc_YMrvu6mILxLzqJll4EJ0QXgtI59CHH2X3L7fr4Ldb_DS8xwSeakZbpFTt05nj2uIOG0CuIPiLIKe2H9DV0cFHurDoMsSWp1z-ak76gTk3GsNbYkrVAYV2WUW6X38cTDpV_-AgpVSC4)
DOM works with either HTML or XML files, this diagram is an example formed under the assumption an HTML file is being used. While the tree itself consists of the file elements and spreads from the DOM, do take note that the DOM content can not only contain code such as Javascript, but that the Javascript code can modify the content of the DOM and its associated tree.

## The main advantages of the DOM 
- Data persists in memory
- You can go forwards and backwards in the tree (random access)
- You can make changes directly to the tree in memory
[source](https://docs.progress.com/bundle/openedge-abl-use-xml-117/page/DOM-advantages.html#:~:text=The%20general%20advantages%20of%20DOM,to%20the%20tree%20in%20memory)

It is supported by almost all web browsers and can be accessed using programming languages such as JavaScript, Python, or Java. This makes it a versatile tool for web development, allowing developers to write code that works across different environments.

Overall, the Document Object Model is a powerful tool for web developers, providing a convenient and standardized way to interact with and manipulate web page elements. 
Its flexibility, platform independence, and extensive support make it an essential part of modern web development.
