import utils as u

print("Number Check:", u.is_num("123"))
print("Formatted:", u.cap("   ayaan ahmed "))
print("Addition:", u.add(10, 5))
print("Subtraction:", u.sub(10, 5))
print("Multiplication:", u.mul(10, 5))
print("Division:", u.div(10, 5))
print("Today's Date:", u.today())

u.write("sample.txt", "Hello World")
print("File Exists:", u.exists("sample.txt"))
print("File Content:", u.read("sample.txt"))
