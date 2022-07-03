# Testing nested functions from here: https://youtu.be/WOHsHaaJ8VQ
def multi_function(operator): # +, -, *, / or %
  def add(n1, n2):
    return n1 + n2
  def sub(n1, n2):
    return n1 - n2
  def mul(n1, n2):
    return n1 * n2
  def div(n1, n2):
    return n1 / n2
  def mod(n1, n2):
    q1, q2 = divmod(n1, n2)
    return f"Quotient: {q1}, Remainder: {q2}"

  if operator == '+':
    return add # Functions are objects like data types and can be used the same way
  elif operator == '-':
    return sub
  elif operator == '*':
    return mul
  elif operator == '/':
    return div
  elif operator == '%':
    return mod

mod_function = multi_function('%') # The result of the function (which is another function) is saved to a variable
sub_function = multi_function('-')
mul_function = multi_function('*')
print(sub_function) # Prints function object: multi_function.<locals>.sub
print(mod_function(63, 13)) # Adding parameters calls function normally
print(mul_function(13, 4))
