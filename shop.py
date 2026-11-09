# 미니 프로젝트 - 쇼핑몰 장바구니 & 할인쿠폰

# 판매 상품   번호(번호는 자동생성)   상품명  가격  재고

# 메뉴  1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료
# 1. 상품목록(전체 상품을 번호 · 가격 · 재고(또는 품절)로 출력)
# 2. 담기 (상품 번호와 수량을 받아 장바구니에 추가. 이미 담긴 상품이면 수량을 더함)
# 3. 빼기 (상품 번호를 받아 장바구니에서 제거)
# 4. 장바구니 (담긴 상품, 상품 합계, 할인, 배송비, 결제 금액 출력)
# 5. 쿠폰 (쿠폰 목록을 보여 주고 하나를 골라 적용 (한 번에 1장))
# 6. 결제  (영수증 출력 → 재고 감소 → 장바구니 비우기 → 쿠폰 초기화)
# q. 종료 

# 상품
# 장바구니
class Shopping(): 
    def init(self):
        pass

#        for number in enumerate(self.items, start=1):


items_val = []
items_basket =[]
sl_message = ["선택 : ","상품 번호 : ","수량 : ","쿠폰 번호 : "]

# 삼품 클래스
class Goods():
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.value = [self.name,self.price,self.stock]
    #재고 수량 변경
    def item_stock_set(self,new_stock):
        self.stock = new_stock
    def item_stock_get(self):
        if self.stock == 0:
            return "품절"
        else :
            return self.stock

# 상품 등록
def items_set():
    earphones =  Goods("무선 이어폰",89000,3)
    tumbler =  Goods("텀블러",15000,10)
    sup_battery =  Goods("보조배터리",32000,5)
    mouse_pad =  Goods("마우스패드",9000,0)
    usb_hub =  Goods("USB 허브",18000,4)
    value = [earphones,tumbler,sup_battery,mouse_pad,usb_hub]
    return value

def menu():
    print("-"*60)
    print(f"1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*60)




def delivery_charge_set(stock, price):
    c_num = int(stock) * int(price)
    print(c_num , c_num >= 30000)
    if c_num >= 30000 or stock == 0 :
        return 0
    else :
        return 3000


# 1. 상품 목록 
def goods_list():
    for number, item in enumerate(items_val,start=1) :
        stock_text = "품절" if item.stock == 0 else f"재고 {item.stock} 개"
        print(f"{number}. {item.name:<15}   {item.price:>8,}원       ({stock_text})")
    user_select()

# 2. 담기

def item_add_basket(user_sl):
    user_sl_sec = user_sl_num(2)
    goods = items_val[user_sl]

    if user_sl_sec <= 0:
        print("수량은 1개 이상 입력하세요.")
        user_select()
        return

    # 장바구니에 동일한 상품이 있는지 확인
    for item in items_basket:
        if item["item"].name == goods.name:
            current_quantity = item[goods.name]
            total_quantity = current_quantity + user_sl_sec

            # 기존 수량 + 추가 수량이 재고를 초과하는지 확인
            if total_quantity > goods.stock:
                print(f"재고가 부족합니다. (현재 재고: {goods.stock}개, 장바구니: {current_quantity}개)")
                user_select()
                return

            # 기존 장바구니 수량 증가
            item[goods.name] = total_quantity

            # 배송비 다시 계산
            item["delivery_charge"] = delivery_charge_set(total_quantity, goods.price)

            print(f"{goods.name} {user_sl_sec}개를 추가했습니다. (총 {total_quantity}개)")
            user_select()
            return

    # 장바구니에 없는 상품이라면 새로 추가
    if user_sl_sec > goods.stock:
        print(f"재고가 부족합니다. (현재 재고: {goods.stock}개)")
        user_select()
        return

    items_basket.append({
        goods.name: user_sl_sec,
        "item": goods,
        "delivery_charge": delivery_charge_set(user_sl_sec, goods.price)
    })

    print(f"{goods.name} {user_sl_sec}개를 담았습니다.")
    user_select()

def goods_add_basket():
    user_sl = user_sl_num(1) - 1
    if items_val[user_sl].stock != 0:
        item_add_basket(user_sl)
        
    else :
        print("품절된 상품입니다.")
        goods_add_basket()


# 3. 빼기


def goods_remove_basket():
    user_sl = user_sl_num(1)
    user_sl2 = user_sl_num(2)
    for number, item in enumerate(items_basket,start=1) :
        key_name = list(item.keys())
        if number == user_sl :
            if item[key_name[0]] == user_sl2 :
                items_basket.pop(number-1)
                user_select()    
            elif item[key_name[0]] > user_sl2 :
                item[key_name[0]] = item[key_name[0]] - user_sl2
                item["delivery_charge"] = delivery_charge_set(item[key_name[0]],item[key_name[1]].price)
                user_select()
            else :
                print("장바구니의 수량을 초과했습니다. 다시 입력하세요")
                goods_remove_basket()


def goods_remove_basket_main():
    show_result = show_basket()
    if not show_result :
        user_select()
    else :
      goods_remove_basket()





# 4. 장바구니
def show_basket():
    if len(items_basket) > 0 :
        for number, item in enumerate(items_basket,start=1) :
            key_name = list(item.keys())
            goods = item[key_name[1]]
            quantity = item[key_name[0]]
            delivery_charge = item["delivery_charge"]

            print(f"{number}. {goods.name:<15}   {goods.price:>8,}원 {delivery_charge:>8}   재고 {goods.stock}개 장바구니수량 {quantity}개")
        return True
    else :
        print("장바구니가 비어있습니다.")
        return False 
    

def show_basket_main():
    show_basket()
    user_select()

#5 쿠폰
def coupon_ck():
    pass


def coupon_ck_main():
    print("1. 쿠폰 없음\n")
    print("2. 10% 할인 (최대 5,000원)\n")
    print("3. 3,000원 할안 (20,000원 이상 구매시)\n")
    user_sl = user_sl_num(3)







# 메뉴 선택 input
def user_sl_num(slm_num):
    user_input = input(sl_message[slm_num])
    return int(user_input) if user_input.lstrip("-").isdigit() else user_input
# 상품 선택 input



# 선택에 따른 메뉴 옵션 선택
def user_select():
    menu()
    user_sl = user_sl_num(0)
    if user_sl == 1:
        goods_list()
    if user_sl == 2:
        goods_add_basket()
    if user_sl == 3:
        goods_remove_basket_main()
    if user_sl == 4:
        show_basket_main()
    if user_sl == 5:
        coupon_ck_main()
    if user_sl == "q":
        pass


    
    else :
        pass





def main() :
    global items_val
    items_val =  items_set()
    user_select()
    # print(user_sl)

    



    # items_val[0].stock = 0
    



main()