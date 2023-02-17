from pyscript import Element

text = Element("text1")
to_link = Element('to_link1')
to_img = Element('to_img1')
to_waring = Element('to_waring1')


def get_link(*args,**kwargs):
    if text.element.value != '':
        url = "https://chart.googleapis.com/chart?chs=400x400&cht=qr&choe=UTF-8&chl=" + str(text.element.value)
        a = '<a href="' + url + '" target="_blank">TO QR Code</a>'
        b = '<img src="' + url + '" >'
        to_img.element.innerHTML = b
    else:
        c = 'กรุณาใส่ตัวหนังสือหรือลิ้งก์ในช่องว่างก่อน!'
        c = '<p class="danger">'+c+'</p>'
        to_waring.element.innerHTML = c


def clear(*args,**kwargs):
    to_img.element.innerHTML = "<div></div>"
    text.clear()