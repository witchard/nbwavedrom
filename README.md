nbwavedrom
==========

A simple package to add wavedrom (http://wavedrom.com) timing diagrams into a jupyter notebook.

To get started simply clone this repository, cd to the folder and run ```jupyter notebook```.
Then take a look at the example notebook.

Note, there are two wavedrom rendering engines built in. The default is to use the
wavedrom-cli (https://github.com/wavedrom/cli). This requires phantomjs. This is the
best option as it embeds the SVG into the notebook. If phantomjs is not found then a
browser based render will be used, this means that the notebook can't be converted to
PDF or displayed on github.

Phantomjs can be installed from here: http://phantomjs.org/download.html.

Wavedrom source code can be found here:

* https://github.com/wavedrom/wavedrom.github.io
* https://github.com/wavedrom/cli/
