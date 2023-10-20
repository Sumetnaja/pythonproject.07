# ------ Tuple คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ เพิ่ม ลบก็ไม่ได้ ------
        #   0   1   2   3   4       5
my_tuple1 = (10, 20, True, 10, 'SAU', (20, 'IOT'))
            #   6   5   4   3   2       1   ติด -


# การเข้าถึงข้อมูลใน List เพื่อเอาข้อมูลมาใช้ หรือแก้ไขคำข้อมูลให้มันใหม่
# เขาถึงแต่ละข้อมูล
print(my_tuple1[4]) # SAU
print(my_tuple1[-2]) # SAU
print(my_tuple1[5]) # [20, 'IOT']
print(my_tuple1[-1]) #[20, 'IOT']
print(my_tuple1[5][1] ) # IOT
print(my_tuple1[-1][-1] ) # IOT

# เข้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพธ์จะเป็น List
print(my_tuple1[1:4] ) # 20, True, 10
print(my_tuple1[3:] ) # 10, 'SAU', [20, 'IOT']
print(my_tuple1[:3]) # 10, 20, True

# เข้าถึงทุกข้อมูล
for info in my_tuple1 :
    print(info, end=', ')

print()

# หากอยากจะแก้ข้อมูลใน Tuple ก็พอทำได้ แต่ต้องอ้อมๆหน่อย
my_List = list(my_tuple1)
my_List[4] = 'IOT'
my_tuple1 = tuple( my_List)
print(my_tuple1)

# Tuple Method
print(my_tuple1.count(10) ) # 2
print( my_tuple1.index('IOT') )

# Tuple Function
my_tuple3 = (10, 20, 10, 30, True)
print(len(my_tuple3))
print(min(my_tuple3))
print(max(my_tuple3))
