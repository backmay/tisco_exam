def mix_sentence(n, msg):
    for i in range(n):
        print(string[i::n],end =" ")
    print('x')

string = 'Is text important ?'
mix_sentence(3, string)
string = 'Pay_attention_to_space'
mix_sentence(5, string)
string = 'Une chocolatine !'
mix_sentence(1, string)