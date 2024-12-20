# 과제 2
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
juice = input("마시고 싶은 음료? ")
if juice in vending_machine :
    print(f"{juice} 드릴게요")
else :
    print(f"{juice}는 지금 없네요")

# 과제 3
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print("남은 음료수:",vending_machine,"\n")

user = input("사용자 종류를 입력하세요:\n 1.소비자\n 2.주인\n")

# 소비자일 경우,
if user == '1' or user == '소비자' :
    juice = input("마시고 싶은 음료? ")
    if juice in vending_machine : # 음료 제공 후 리스트에서 삭제
        print(f"{juice} 드릴게요")
        vending_machine.remove(juice)
        print("남은 음료수:",vending_machine,"\n")
    else :
        print(f"{juice}는 지금 없네요") # 없음

# 주인일 경우,
elif user == '2' or user == '주인'  : 
    work = input("할 일 선택(문자 입력):\n 1. 추가\n 2. 삭제\n")
    # 추가할 경우,
    if work == '1' or work == '추가'  :
        print("남은 음료수:",vending_machine,"\n")
        juice = input("추가할 음료수? ")
        # if vending_machine.count(juice) != 0 : # 중복O => 위치에 값 추가
        #     vending_machine.insert(vending_machine.index(juice),juice)
        # else : # 중복X => 새로 추가 후 정렬
        # 굳이 이렇게 할 필요없고 그냥 sort 만 사용하면 됨!
        vending_machine.append(juice)
        vending_machine.sort()
        print("추가 완료")
        print("남은 음료수:",vending_machine,"\n")
    
    # 삭제할 경우,
    elif work == '2' or work == '삭제'  :
        print("남은 음료수:",vending_machine,"\n")
        juice = input("삭제할 음료수? ")
        if juice in vending_machine :
            vending_machine.remove(juice)
            print("삭제 완료")
            print("남은 음료수:",vending_machine,"\n")
        else :
            print(f"{juice}는 지금 없네요")

    # 입력한 값이 1, 2, 추가, 삭제가 아닐 경우
    else :
        print("입력을 잘못 하셨습니다.")

# 입력한 값이 1, 2, 소비자, 주인이 아닐 경우
else :
    print("입력을 잘못 하셨습니다.")

# 실습 3
# 남은 음료수 확인 함수
def check_machine(list) :
    print(f'남은 음료수 : {list} \n')

# 음료수가 있는 지 확인하는 함수
def is_drink(juice,list) :
    if juice in list : # 음료 제공 후 리스트에서 삭제
        print(f"{juice} 드릴게요")
        list.remove(juice)
        check_machine(list)
    else :
        print(f"{juice}는 지금 없네요") # 없음

# 음료수를 추가하는 함수
def add_drink(juice, list) :
    list.append(juice)
    list.sort()
    print("추가 완료")
    check_machine(list)

# 음료수를 삭제하는 함수
def remove_drink(juice, list) :
    if juice in list :
            list.remove(juice)
            print("삭제 완료")
            check_machine(list)
    else :
        print(f"{juice}는 지금 없네요")

# 자판기 프로그램
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
check_machine(vending_machine)

user = input("사용자 종류를 입력하세요:\n 1.소비자\n 2.주인\n")

# 소비자일 경우,
if user == '1' or user == '소비자' :
    juice = input("마시고 싶은 음료? ")
    is_drink(juice, vending_machine) # 음료 있는지 확인

# 주인일 경우,
elif user == '2' or user == '주인'  : 
    work = input("할 일 선택(문자 입력):\n 1. 추가\n 2. 삭제\n")
    # 추가할 경우,
    if work == '1' or work == '추가'  :
        check_machine(vending_machine)
        juice = input("추가할 음료수? ")
        add_drink(juice,vending_machine)
    
    # 삭제할 경우,
    elif work == '2' or work == '삭제'  :
        print("남은 음료수:",vending_machine,"\n")
        juice = input("삭제할 음료수? ")
        remove_drink(juice, vending_machine)

    # 입력한 값이 1, 2, 추가, 삭제가 아닐 경우
    else :
        print("입력을 잘못 하셨습니다.")

# 입력한 값이 1, 2, 소비자, 주인이 아닐 경우
else :
    print("입력을 잘못 하셨습니다.")
