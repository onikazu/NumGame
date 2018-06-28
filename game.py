import random

# determine the number
# https://python.civic-apps.com/random-shuffle-choice-sample/
# range(10)は0~9の配列
answer_num_list = random.sample(range(10), 3)

def is_unique(seq):
    return len(seq) == len(set(seq))


print('数字あてゲームへようこそ')

attack_count = 0
while(True):
    bite = 0
    eat = 0
    input_num = input('三桁の数字を入力してください:')
    attack_count += 1
    
    # 入力された数字をリストに変換する
    input_num_list = []
    try:
        for num in input_num:
            input_num_list.append(int(num))
            
    except:
        print('予期せぬ入力が行われました')

    # double num check
    if not is_unique(input_num_list):
        attack_count -= 1
        print('重複した数字を入力してはいけません')
        continue

    # check eat
    for i in range(3):
        if(answer_num_list[i]==input_num_list[i]):
            eat += 1
        
        #check bite
        for j in range(3):
            if(i != j):
                if(answer_num_list[i] == input_num_list[j]):
                    bite += 1
    
    # 結果表示
    print('{0}eat,{1}bite'.format(eat, bite))
    
    if(eat == 3):
        break
    
print('ゲーム終了です。お疲れ様でした。あなたは{0}回で正解にたどり着きました。'.format(attack_count))