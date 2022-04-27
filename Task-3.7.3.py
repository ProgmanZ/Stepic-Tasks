set_dict = {input().lower() for _ in range(0, int(input()))}
user_text = [input().split(' ') for _ in range(0, int(input()))]
set_result = {elem.lower() for val in user_text for elem in val}
print(*(set_result - set_dict), sep='\n')