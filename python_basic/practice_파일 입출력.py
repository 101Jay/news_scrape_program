score_file = open("score.txt", "w", encoding="utf8")
score_file.write("hi!\n")
score_file.write("helloow\n")
score_file.close()

#w로 열면 덮어쓰기 됨 -> 이어서 쓸라면 a로 열어주면 됨

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("i am back\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()#닫아주는 거 잊지말자!

#몇 줄인지 모를 때 읽어오기

# while True : 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# lines = score_file.readlines()
# for line in lines : 
#     print(line,end="")

# score_file.close()

#pickle

# import pickle   ///피클 형태로 파일 쓰기
# profile_pickle = open("profile.pickle","wb")
# profile = {"이름": "you"}
# pickle.dump(profile, profile_pickle)
# profile_pickle.close

# import pickle
# profile_pickle = open("profile.pickle", "rb")
# profile = pickle.load(profile_pickle)
# print(profile)

#with의 사용 -> with를 사용하면 close할 필요가 없기 때문에 코드가 간결해진다.

with open("score.txt", "a", encoding="utf8") as my_score:
    my_score.write("파이썬을 열심히 공부하고 있습니다.")

with open("score.txt","r",encoding="utf8") as my_score_read:
    print(my_score_read.read())

