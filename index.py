import qrcode
import base64

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Portfolio</title>
</head>
<style>
    body {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        min-height: 100vh;
        min-width: 100vw;
        background-image: linear-gradient(black, white, grey, black, white, grey);
    }
    .container {
        background-color: #eee;
        height: 80vh;
        width: 95%;
        overflow: hidden;
        border-radius: 7.5px;
        align-items: center;
        justify-content: center;
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
    } .container .content {
        font-family: "Ubuntu", serif;
        align-items: center;
        justify-content: center;
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
    } .container h1 {
        font-size: 102px;
    } .container h2 {
        font-size: 46px;
    } .container span {
        font-size: 25px;
        font-family: monospace;
    } .container p {
        font-size: 28px;
    }
</style>
<body>
    <div class="container">
        <div class="content">
            <h1>HELLO</h1>
            <h2>I am Samannoy Bhattacharjee</h2>
            <p>I am a programmer, enthusiast, hobbyist and introvert</p><br><br>
            <span><code>And I turn coffee into bugs....  &#9749; &#9749;</code></span>
        </div>
        <div class="url" style="display: flex; flex-direction: row; gap: 34px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
            <a href="https://github.com/samannoyb">GitHub</a>
            <a href="https://instagram.com/octotastic_samannoyb">Instagram</a>
            <a href="https://youtube.com/@samannoyb">YouTube</a>
        </div>
    </div>
</body>
</html>"""


encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

data_url = f"data:text/html;base64,{encoded_html}"

qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=4,
)

qr.add_data(data_url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("img_name.png")