import hashlib

lorem = "Lorem ipsum, dolor sit amet consectetur adipisicing elit."
lorem += " Praesentium ducimus sint tempora, corrupti culpa suscipit cum?"
lorem += " Illum necessitatibus cupiditate libero culpa perspiciatis deleniti id sapiente eos ipsa natus, eligendi laborum."


h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())
print(h)