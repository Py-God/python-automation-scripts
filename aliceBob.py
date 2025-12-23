import re

matchRegex = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.', re.IGNORECASE)
text = 'Alice eats apples. Bob pets cats. Carol throws baseballs. BOB EATS CATS. Robocop eats apples. ALICE THROWS FOOTBALLS'
matches = matchRegex.findall(text)
print(matches)
