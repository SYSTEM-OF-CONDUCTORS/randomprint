import json
import cgi

form = cgi.FieldStorage()
print_value = form.getvalue('print')

#print(print_value)

def try_to_open_file(filename, mode):
    for i in range(0,50):
        while True:
            try:
                f = open(filename, mode)
            except:
                continue
            break
    return f

if print_value == None:
    f = try_to_open_file('file.json', 'r')
    print("Content-type: application/json")
    print()
    print(f.readline())
    f.close()
    f = try_to_open_file('file.json', 'w')
    f.write(json.dumps({'print':'fales'}))
    f.close()

else:
    f = try_to_open_file('file.json', 'w')
    f.write(json.dumps({'print':print_value}))
    print("Content-type: text/html")
    print()
    print("<body style=\"background-color:PaleGoldenRod;\"></body>")
    print("<img src=\"https://www.emojiall.com/images/240/apple/1faa8.png\" width=\"50%\" style=\"margin: 0; position: absolute; top: 50%; left: 50%; -ms-transform: translate(-50%, -50%); transform: translate(-50%, -50%);\"></img>")
    f.close()