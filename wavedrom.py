import IPython.core.display
import json


def draw_wavedrom(data, width=None):
    """
    A function to provide digital waveform drawing in ipython notebook.
    It utilises the wavedrom java script library, documentation for which can
    be found here: https://code.google.com/p/wavedrom/.
    Please place WaveDrom.js and WaveDromSkin.js in your notebook folder under
    the subdirectory js.

    Note the optional argument width forces the width in pixels

    Example usage:
        import wavedrom
        a = {
        'signal': [
          {'name': 'clk', 'wave': 'p.....|...'},
          {'name': 'dat', 'wave': 'x.345x|=.x', 'data': ['head', 'body', 'tail', 'data']},
          {'name': 'req', 'wave': '0.1..0|1.0'},
          {},
          {'name': 'ack', 'wave': '1.....|01.'}
        ]}
        wavedrom.draw_wavedrom(a)
    """
    style = ""
    if width != None:
	style = ' style="width: ' + str(int(width)) + 'px"'
    htmldata = '<div' + style + '><script type="WaveDrom">' + json.dumps(data) + '</script></div>'
    IPython.core.display.display_html(IPython.core.display.HTML(htmldata))
    jsdata = 'WaveDrom.ProcessAll();'
    IPython.core.display.display_javascript(IPython.core.display.Javascript(
        data=jsdata, lib=['files/js/wavedrom.min.js', 'files/js/wavedromskin.js']))
