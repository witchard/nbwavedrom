nbwavedrom
==========

A simple package to add wavedrom (http://wavedrom.com) timing diagrams into a jupyter notebook.

Example: https://github.com/witchard/nbwavedrom/blob/master/examples/example.ipynb

To get started simply `pip install nbwavedrom` or `pip install git+git://github.com/witchard/nbwavedrom.git`
for the development version. Then take a look at the example notebook within jupyter notebook.

Note, there are two wavedrom rendering engines built in. The default is to use the
wavedrom-cli (https://github.com/wavedrom/cli). This requires phantomjs. This is the
best option as it embeds the SVG into the notebook. If phantomjs is not found then a
browser based render will be used, this means that the notebook can't be converted to
PDF or displayed on github.

Phantomjs can be installed from here: http://phantomjs.org/download.html.

Wavedrom source code can be found here:

* https://github.com/wavedrom/wavedrom.github.io
* https://github.com/wavedrom/cli/
