import sympy
def text_to_numbers(text):
    return [ord(char) for char in text]

p = 17
q = 23

n = p * q
phi_n = (p - 1) * (q - 1)

e = 5
assert sympy.gcd(e, phi_n) == 1, "e không hợp lệ"

d = pow(e, -1, phi_n)

# 5. Mã hóa thông điệp
message = "TranVanTuan"
message_numbers = text_to_numbers(message)

# Mã hóa từng ký tự
cipher_numbers = [pow(m, e, n) for m in message_numbers]
print("Bản mã:", cipher_numbers)