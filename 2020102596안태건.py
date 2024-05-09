sales = []
menu_prices = {
    '아메리카노':3000,
    '라떼':3500,
    '에스프레소':3250,
    '모카치노':3200,
    '우유':2300,
    '오렌지 쥬스':1800
}
materials_prices = {
    '아메리카노':500,
    '라떼':1100,
    '에스프레소':950,
    '모카치노':980,
    '우유':400,
    '오렌지 쥬스':300
}
def add_to_sales(item,quantity):
    if item in menu_prices:
        sales.append((item,quantity))
        print('{0} 잔의 {1}를 판매했습니다.'.format(quantity,item))
    else:
        print('{0}이 존재하지 않습니다.'.format(item))

def calculate_total(flag=True):
    total = 0
    for item,quantity in sales:
        if flag:
            total += menu_prices[item]*quantity
        else:
            total += materials_prices[item]*quantity
    return total

def display_sales():
    if not sales:
        print('아무것도 팔지 못했습니다.')
    else:
        print('--------------------')
        print('오늘 매출은 다음과 같습니다.')
        for item, quantity in sales:
            print('{0} {1}잔 : {2:,}원 판매했습니다.'.format(item,quantity,menu_prices[item]*quantity))
        tot_sales = calculate_total()
        tot_materials = calculate_total(False)
        print('--------------------')
        print('오늘 하루 전체 매출은 {:,}원 입니다.'.format(tot_sales))
        print('오늘 매출에 대한 재료값은 {:,}원 입니다.'.format(tot_materials))
        print('오늘 수익은 {:,} 원 입니다.'.format(tot_sales-tot_materials))
        print('--------------------')

end = True
print('오늘 하루의 매출을 정리해봅시다.')
while end:
    sales_menu = input('오늘 판매된 메뉴를 입력하세요.')
    sales_count = int(input('이 메뉴의 판매 수량을 입력하세요.'))
    add_to_sales(sales_menu,sales_count)
    if input('입력을 종료할까요? Y/N') == 'Y':
        end = False
display_sales()