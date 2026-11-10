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

# 삼품 클래스
class Goods():
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    #재고 수량 리턴
    def get_stock(self) :
        return self.stock if self.stock > 0 else "품절"
    def set_stock(self,buy_stock) :
        self.stock -= buy_stock


class Shopping():      
    def __init__(self):
        self.basket = []
        self.message = ["선택 : ","상품 번호 : ","수량 : ","쿠폰 번호 : "]
        self.items_set() # 상품등록
        # 상품 등록
    def items_set(self):
        earphones =  Goods("무선 이어폰",89000,3)
        tumbler =  Goods("텀블러",15000,10)
        sup_battery =  Goods("보조배터리",32000,5)
        mouse_pad =  Goods("마우스패드",9000,0)
        usb_hub =  Goods("USB 허브",18000,4)
        self.items = [earphones,tumbler,sup_battery,mouse_pad,usb_hub]

    def print_menu():
        print("-"*60)
        print(f"1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
        print("-"*60)



        

def main() :
    shopping = Shopping()
    print(shopping.items)



main()