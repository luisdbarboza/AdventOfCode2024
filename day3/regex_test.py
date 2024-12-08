import re

time_re = r'(?:\b([2][0-3]|0?\d|1[0-9]):([0-5][0-9])(?::([0-5][0-9]))?)(?:\n|$)'
test_str = "23:50:32"

result = re.search(time_re, test_str)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))

mul_re = r'mul\(\d{1,3},\d{1,3}\)'
computers_mem = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

result = re.findall(mul_re, computers_mem)
print(result)